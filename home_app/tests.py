from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Post, Comment


class ProfileModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        Profile.objects.create(user=user, id_user=1)

    def test_get_full_name(self):
        profile = Profile.objects.get(id_user=1)
        full_name = profile.get_full_name()
        self.assertEqual(full_name, ' ')

    def test_get_profile_url(self):
        profile = Profile.objects.get(id_user=1)
        profile_url = profile.get_profile_url()
        self.assertEqual(profile_url, '/media/images/default/profile.png')


class PostModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        Post.objects.create(user=user, title='Test Post', slug='test-post')

    def test_get_count_liked(self):
        post = Post.objects.get(slug='test-post')
        count_liked = post.get_count_liked()
        self.assertEqual(count_liked, 0)

    def test_get_list_approve(self):
        # Assuming admin_approved is False by default
        post = Post.objects.get(slug='test-post')
        list_approve = Post.get_list_approve()
        self.assertNotIn(post, list_approve)


class CommentModelTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        Profile.objects.create(user=user, id_user=1)
        post = Post.objects.create(
            user=user, title='Test Post', slug='test-post')
        Comment.objects.create(user=user, post=post, comment='Test Comment')

    def test_get_owner(self):
        comment = Comment.objects.get(comment='Test Comment')
        owner = comment.get_owner()
        self.assertEqual(owner, ' ')
        