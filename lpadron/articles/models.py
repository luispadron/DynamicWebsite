from django.db import models
from django.template.defaultfilters import slugify
import misaka as m

class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=140)
    body = models.TextField()
    img_link = models.CharField(max_length=2000)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_markdown(self):
        return m.html(self.body)

    class Meta:
        ordering = ['-created_at']
