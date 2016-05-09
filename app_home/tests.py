from django.test import Client, TestCase
from django.contrib.staticfiles import finders

client = Client()

class ViewTestCase(TestCase):
    def setUp(self):
        self.response = client.get("#")
        self.found_css = finders.find("css/home_index.css")
        self.found_img = finders.find("img/steven.jpeg")
        self.found_js = finders.find("js/home_index.js")

    def test_home_index(self):
        """ Verify home's index assests are linked """
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(not self.found_css, False)
        self.assertEqual(not self.found_img, False)
        self.assertEqual(not self.found_js, False)
