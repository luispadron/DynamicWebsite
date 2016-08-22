from django.conf.urls import include, url
from django.contrib import admin

# Import views
from . import views

urlpatterns = [
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
]
