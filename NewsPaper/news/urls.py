from django.urls import path
from .views import NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail')
]