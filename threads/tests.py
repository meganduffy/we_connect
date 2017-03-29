from django.test import TestCase
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import resolve
from .models import Subject
from .views import forum, threads


class ForumPageTest(TestCase):

    # Model Tests

    def test_check_content_is_correct(self):
        forum_page = self.client.get('/forum/')
        self.assertTemplateUsed(forum_page, "forum.html")
        forum_page_template_output = render_to_response("forum.html",
                                                          {'subjects': Subject.objects.all()}).content
        self.assertEqual(forum_page.content, forum_page_template_output)

    # URL Tests

    def test_forum_page_resolvers(self):
        forum_page = resolve('/forum/')
        self.assertEqual(forum_page.func, forum)

    def test_forum_page_status_is_ok(self):
        forum_page = self.client.get('/forum/')
        self.assertEqual(forum_page.status_code, 200)
