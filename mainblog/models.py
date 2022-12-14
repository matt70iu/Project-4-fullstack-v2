'''required imports'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# pylint: disable-all


class Category(models.Model):

    '''Category model'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        '''Redirect back to home'''
        return reverse('home')


class Profile(models.Model):
    '''Profile model'''
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to='media/images/profile/')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        '''Redirects back to homepage'''
        return reverse('home')


class Post(models.Model):
    '''Post model'''
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='media/images')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='Please enter post here')
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(
        max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        '''Returns no of likes'''
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        '''Adds like no to post'''
        return reverse('article-detail', kwargs={'pk': self.id})


class Comment(models.Model):
    '''Comment model'''
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
