from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm

# Create your tests here.
class TestAboutViews(TestCase):

    def setUp(self):
        """
        Creates about me content
        """
        self.about = About(title="About title",
                         content="About content")
        self.about.save()


    def test_render_about_page_with_collaboration_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
