from django.http import JsonResponse                                    #is used to return JSON-encoded responses from a view.
from django.views import View                                           #base class for creating class-based views in Django.
import praw                                                             #Python Reddit API Wrapper used to interact with the Reddit API
from django.conf import settings   
from django.shortcuts import render                                     #Imports the settings module, which provides access to Django's project settings

class GetArticlesView(View):                                            #GetArticlesView inherits from View
    def get(self,request,*args, **kwargs):
        reddit = praw.Reddit(                                           #initializes the connection with reddit api using praw library
            client_id=settings.REDDIT_API_CONFIG['client_id'],
            client_secret=settings.REDDIT_API_CONFIG['client_secret'],
            user_agent=settings.REDDIT_API_CONFIG['user_agent']         #a useragent tells the server what you are doing for a scrapper app it is not very imp
        )

        subredditname = 'soccer'
        subreddit = reddit.subreddit(subredditname)                     #fetches subreddit threads
        threads = subreddit.new(limit=10)

        articles = []                                                   #the thread fetches all the data from each thread and stores them in articles 
        for thread in threads:
            articles.append({
                'title': thread.title,
                'author': thread.author.name if thread.author else '[not available]',
                'creation_date': thread.created_utc,
                'link': thread.url
            })

        return render(request, 'articles.html', {'articles': articles , 'subredditname': subredditname })       #returns the rendered form of the incoming json data in the html page
        
