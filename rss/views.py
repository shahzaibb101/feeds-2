from django.shortcuts import render, redirect
from rss.parser import *
from rss.prediction import *

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "sign-up.html")

def login(request):
    return render(request, "login.html")

def dashboard(request):
    if request.method == 'POST':
        data = request.POST
        url = data['url']
        feed = fetch_rss_feed(url)
        
        if feed:
            summary = feed.summary
            sentiment = get_prediction(summary)
            if sentiment == 'Happy':
                secondary_text = 'This feed brings cheerful and uplifting content, spreading positivity and good vibes.'
            elif sentiment == 'Sad':
                secondary_text = 'The tone of this feed is more somber, sharing stories that may evoke feelings of empathy or reflection.'
            else:
                secondary_text = 'This feed provides news and updates without a specific emotional tone, offering a balanced view of various topics.'
            feeds_author = feed.authors
            author_name = feeds_author[0].get('name')
            author_email = feeds_author[0].get('email')
            print(url)
            print(summary)
            print(sentiment)
            # print(feed)

            return render(request, "dashboard.html", {'sentiment': sentiment, 'secondary_text': secondary_text, 'feed': feed, 'author_name': author_name, 'author_email': author_email, 'summary': summary, 'found': 'true'})
        else:
            return render(request, "dashboard.html", {'found': 'false'})
    else:
        return render(request, "dashboard.html")