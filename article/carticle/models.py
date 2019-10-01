from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField




#####################  creating college model   ######################

class College(models.Model):
    name = models.CharField(max_length=800, unique=True)
    description = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

#####################  creating article model   ######################

class Article(models.Model):
    subject = models.CharField(max_length=30, unique=True)
    message = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField( auto_now=True, null=True)
    author = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='article_images', default="")
    # likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def snippet(self):
        return self.message[:30]+ '........'
    
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('article_edit', kwargs={'pk': self.pk})
    
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

#####################  creating comment model   ######################


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    reply = models.ForeignKey('Comment', null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(max_length = 160, default="")
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}-{}'.format(self.article.subject, str(self.user.username))

#####################  creating image model   ######################
  
class Image(models.Model):
    name = models.CharField(max_length=20, unique=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

#####################  creating videos model   ######################

class Video(models.Model):
    name = models.CharField(max_length=20, unique=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)











