from django.shortcuts import render, get_object_or_404, reverse
from to_do_list.models import Article, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html',  {'status_choice': status_choices})
    elif request.method == "POST":
        Article.objects.create(
            description=request.POST.get('description'),
            created_at=request.POST.get('created_at'),
            detailed_description=request.POST.get('detailed_description'),
            status=request.POST.get('status')
        )
        return HttpResponseRedirect('/')

