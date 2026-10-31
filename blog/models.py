from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    banner = models.ImageField(default='fallback.png', blank=True)


    def publish(self):
        self.published_date = timezone.now()
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    # Связываем комментарий с конкретным постом
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text