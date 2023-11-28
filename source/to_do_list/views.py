from django.shortcuts import render
from to_do_list.models import Article
from django.http import HttpResponseRedirect


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        Article.objects.create(
            description=request.POST.get('description'),
            created_at=request.POST.get('created_at')
        )
        return HttpResponseRedirect('/')

