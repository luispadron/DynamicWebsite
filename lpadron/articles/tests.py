from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Article

# Test the model
class ArticleModelTests(TestCase):

    def test_article_creation_date(self):
        article = Article.objects.create(
            title = " A title for a test article",
            subtitle = "A subtitle for a test article",
            body = "A body for a test article",
            img_link = "http://www.ejobvacancy.com/wp-content/uploads/2016/07/Transformer-Open-and-Short-Circuit-Tests.png",
            slug = "a-title-for-a-test-article",
            created_at = timezone.now(),
        )
        now = timezone.now()
        self.assertLess(article.created_at, now)

# Test the views
class ArticleViewsTests(TestCase):
    def setUp(self):
        self.article1 = Article.objects.create(
            title = " A title for a test article",
            subtitle = "A subtitle for a test article",
            body = "A body for a test article",
            img_link = "http://www.ejobvacancy.com/wp-content/uploads/2016/07/Transformer-Open-and-Short-Circuit-Tests.png",
            slug = "a-title-for-a-test-article1",
            created_at = timezone.now(),
        )
        self.article2 = Article.objects.create(
            title = " A title2 for a test article",
            subtitle = "A subtitle2 for a test article",
            body = "A body for a test2 article",
            img_link = "http://www.ejobvacancy.com/wp-content/uploads/2016/07/Transformer-Open-and-Short-Circuit-Tests.png",
            slug = "a-title-for-a-test-article2",
            created_at = timezone.now(),
            )

    def test_article_list_view(self):
        resp = self.client.get('/articles/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.article1, resp.context['articles'])
        self.assertIn(self.article2, resp.context['articles'])
