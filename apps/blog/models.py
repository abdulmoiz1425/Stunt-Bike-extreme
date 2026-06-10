import math
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    excerpt = models.TextField(max_length=300, help_text='Short summary shown on the blog listing page')
    content = models.TextField(help_text='HTML content is supported')
    publish_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    @property
    def reading_time(self):
        word_count = len(self.content.split())
        return max(1, math.ceil(word_count / 200))

    @property
    def effective_meta_title(self):
        return self.meta_title or self.title

    @property
    def effective_meta_description(self):
        return self.meta_description or self.excerpt

    def get_approved_comments(self):
        return self.comment_set.filter(approved=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.name} on "{self.article.title}"'
