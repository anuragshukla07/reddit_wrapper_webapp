from django.urls import path
from .views import GetArticlesView

urlpatterns = [
    path('articles/', GetArticlesView.as_view(), name='articles'),
]
