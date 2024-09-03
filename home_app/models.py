from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.utils import timezone


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

VISIBILITY = (
    ("Only Me", "Only Me"),
    ("Everyone", "Everyone")
)

FRIEND_REQUEST = (
    ("pending", "pending"),
    ("accept", "accept"),
    ("reject", "reject")
)

NOTIFICATION_TYPE = (
    ("Friend Request", "Friend Request"),
    ("Friend Request Accepted", "Friend Request Accepted"),
    ("New Friend", "New Friend"),
    ("New Comment", "New Comment"),
    ("Comment Liked", "Comment Liked"),
    ("Comment Replied", "Comment Replied")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    cover_image = models.ImageField(
        "featured image", upload_to='images', height_field=None,
        width_field=None, max_length=None)
    country = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(
        "profile image", upload_to='images', height_field=None,
        width_field=None, max_length=None, blank=True,
        default='images/default/profile.png',)
    phone = models.CharField(max_length=15, blank=True)
    """ A special method that is used to define the user-friendly
    string representation of an object """
    def __user__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_profile_url(self):
        return self.profile_img.url


class Post(models.Model):
    """ models.UUIDField is a field type that used for uniquely
    identifying objects or records in a database """
    id_post = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=200, unique=True)
    featured_image = models.ImageField(
        "featured image", upload_to='images', height_field=None,
        width_field=None, blank=True, max_length=None)
    visibility = models.CharField(
        max_length=100, choices=VISIBILITY, default='Everyone', blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    admin_approved = models.BooleanField(default=True)

    class Meta:
        """ class Meta Allow you to specify various options for the model,
        ordering is used to specify the default ordering for the model's
        database queries """
        ordering = ['-created_on']

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username

    def get_count_liked(self):
        return self.likes.count()

    @classmethod
    def get_list_approve(self):
        return Post.objects.filter(admin_approved=True)

    def get_all_comments(self):
        return self.comment_set.all().order_by('-date')

    def get_users_liked(self):
        return self.likes.all()

    def remove_user_liked(self, user):
        return self.likes.remove(user)

    def add_user_liked(self, user):
        return self.likes.add(user)

    def total_shares(self):
        return self.shared_posts.count()


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="comment_likes")
    id_post_comment = models.UUIDField(primary_key=True, default=uuid.uuid4)

    #ReplyComment

    def __str__(self):
        return str(self.post)

    def get_all_replycomments(self):
        return self.replycomment_set.all().order_by('date')

    def get_date_string(self):
        return self.date.strftime('%Y-%m-%d %H:%M:%S')

    def get_owner(self):
        return self.user.profile.get_full_name()


    class Meta:
        verbose_name_plural = 'comment'


class Gallery(models.Model):
    """ This Gallery class use to store multiple images in class Post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(
        "image", upload_to='images', height_field=None,
        width_field=None, max_length=None, default=uuid.uuid4)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        """ To stop Django automatically create a plural
        verbose name from your object by adding "s" """
        verbose_name_plural = 'Gallery'


class FriendRequest(models.Model):
    id_friend_request = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="FriendRequest_user")
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="FriendRequest_friend")
    status = models.CharField(
        max_length=100, default="pending", choices=FRIEND_REQUEST)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Friend Request'


class Friend(models.Model):
    id_friend = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Friend_user")
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Friend_friend")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

    @classmethod
    def unfriend(cls, user, friend):
        cls.objects.filter(user=user, friend=friend).delete()
        cls.objects.filter(user=friend, friend=user).delete()

    class Meta:
        verbose_name_plural = 'Friend'


class ReplyComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ReplyComment_user")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, blank=True, related_name="ReplyComment_likes")
    id_reply_comment = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.comment)

    class Meta:
        verbose_name_plural = 'Reply Comment'


class Notification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reply_user")
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notification_user")
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True)
    notification_type = models.CharField(
        max_length=500, choices=NOTIFICATION_TYPE)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    id_notification = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Notification'


class Popular(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares', verbose_name="User", help_text="The user who shared this content")
    content = models.TextField(help_text="Content of the share")
    created_at = models.DateTimeField(default=timezone.now, help_text="Date and time the content was shared")
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time the content was last updated")
    likes = models.ManyToManyField(User, related_name='liked_shares', blank=True, help_text="Users who liked the share")
    share_count = models.PositiveIntegerField(default=0, help_text="Number of times this content has been shared")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="shared_posts", null=True)
    id_share = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.post)

    def __str__(self):
        return f"Share by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = "Share"
        verbose_name_plural = "Shares"
