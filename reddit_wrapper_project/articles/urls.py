from django.urls import path
from .views import GetArticlesView

urlpatterns = [
    path('', GetArticlesView.as_view(), name='articles'), #this is basically the url used for accessing the data from the server
]
