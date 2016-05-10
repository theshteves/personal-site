from app_home.models import Project
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests


def home(request):
    projects = requests.get("https://api.github.com/users/theshteves/repos")
    projects = json.dumps(projects.json())
    projects = json.loads(projects)
    
    popular = [proj["full_name"] for proj in projects if int(proj["stargazers_count"]) > 0]
    [Project.objects.create(name=x) for x in popular]
    """
    for proj in projects:
        if int(proj["stargazers_count"]) > 1:
            Project.objects.create(name=proj["full_name"])
    """
    return render(request, "home/index.html", {"projects": Project.objects.all()})
