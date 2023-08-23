from django.urls import path
from .views import GetArticlesView

urlpatterns = [
    path('get_articles/', GetArticlesView.as_view(), name='get_articles'),
]
