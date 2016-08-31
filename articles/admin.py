from django.contrib import admin
from django.db import models
from .models import Article

from pagedown.widgets import AdminPagedownWidget

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Article, ArticleAdmin)
