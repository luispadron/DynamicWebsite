from django.db import models

# Create your models here.
class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=140)
    body = models.TextField()

    def __str__(self):
        return self.title
