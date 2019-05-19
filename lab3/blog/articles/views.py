from django.shortcuts import render
from articles.models import Article
from django import template


def archive(request):
    return render(request, "templates/archive.html", {"posts": Article.objects.all()})
