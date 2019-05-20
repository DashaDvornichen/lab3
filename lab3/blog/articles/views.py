from django.shortcuts import render
from blog.articles.models import Article
from django import template


def archive(request):
    return render(request, "archive.html", {"posts": Article.objects.all()})
