from django.urls import path                                                    #Imports the path function from the django.urls module
from .views import GetArticlesView                                              #Imports the GetArticlesView class from the views module of the current package (app).

urlpatterns = [
    path('get_articles/', GetArticlesView.as_view(), name='get_articles'),
]
