from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid
from datetime import datetime



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

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    cover_image = CloudinaryField('image', default='placeholder')
    country = models.CharField(max_length=100, blank=True)
    """ A special method that is used to define the user-friendly
    string representation of an object """
    def __user__(self):
        return self.user.username

class Post(models.Model):
    """ models.UUIDField is a field type that used for uniquely
    identifying objects or records in a database """
    id_post = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    visibility = models.CharField(
        max_length=100, choices=VISIBILITY, default='Everyone')
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

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

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(
        max_length=1000)
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, blank=True, related_name="comment_likes")
    id_post_comment = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name_plural = 'comment'


class Gallery(models.Model):
    """ This Gallery class use to store multiple images in class Post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = CloudinaryField(
        'image', null=True, blank=True, default='placeholder')
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
        verbose_name_plural = 'FriendRequest'


class Friend(models.Model):
    id_friend = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Friend_user")
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Friend_friend")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)

    class Meta:
        verbose_name_plural = 'Friend'
    
    
class ReplyComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ReplyComment_user")
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
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

