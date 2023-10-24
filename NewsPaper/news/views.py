from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-pub_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pub_date')

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'
