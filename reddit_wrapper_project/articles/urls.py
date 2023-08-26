from django.urls import path
from .views import GetArticlesView

urlpatterns = [
    path('', GetArticlesView.as_view()),
]
