from __future__ import unicode_literals
from django.db import models
import json
import requests

class Project(models.Model):
    name = models.CharField(max_length=100)
    #stars = models.IntegerField()
    #description = models.CharField(max_length=100)
    #link = models.CharField(max_length=200)

# Populate Project DB
"""
projects = requests.get("https://api.github.com/users/theshteves/repos")
projects = projects.text.encode("ascii", "ignore")
projects = json.loads(projects)

popular = [proj["full_name"] for proj in projects if int(proj["stargazers_count"]) > 1]
for x in popular:
    try:
        Project.objects.get(name=x)
    except Project.DoesNotExist:
        Project.objects.create(name=x)
"""

#[Project.objects.create(name=x) for x in popular if x not in Project.objects.all()]
