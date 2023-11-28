from django.urls import path
from to_do_list.views import index_view, article_create_view

urlpatterns = [
    path('', index_view),
    path('articles/add/', article_create_view),
]