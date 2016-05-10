from django.test import Client, TestCase
from django.contrib.staticfiles import finders
import requests

client = Client()

class TestCase1(TestCase):
    """ Verify home's index assests are linked """

    def setUp(self):
        self.response = client.get("#")
        self.found_css = finders.find("css/home_index.css")
        self.found_img = finders.find("img/steven.jpeg")
        self.found_js = finders.find("js/home_index.js")

    def test_home_index(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(not self.found_css, False)
        self.assertEqual(not self.found_img, False)
        self.assertEqual(not self.found_js, False)

class TestCase2(TestCase):
    """ Verify GitHub API call for projects """

    def setUp(self):
        self.response = requests.get("https://api.github.com/users/theshteves/repos")

    def test_github_request(self):
        self.assertEqual(self.response.status_code, 200)
