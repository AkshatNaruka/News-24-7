from unicodedata import category
from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    newsApi = NewsApiClient(api_key='819ae34f4578407cb6a3e7038512f551')
    headLines = newsApi.get_top_headlines(sources='google-news-in,the-hindu,crypto-coins-news,fox-news,recode')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    
    mylist = zip(news,desc,img)

    return render(request, "main/index.html",context={"mylist":mylist})
