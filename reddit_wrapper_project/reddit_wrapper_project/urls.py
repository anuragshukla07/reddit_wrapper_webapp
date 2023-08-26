from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('articles.urls')),        #this url basically re-routes the server to the url file of the app
]
