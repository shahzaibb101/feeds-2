from django.shortcuts import render, redirect
from rss.parser import *
from rss.prediction import *

# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        data = request.POST
        url = data['url']
        feeds = fetch_rss_feed(url)

        if data['sentiment']:
            selected = data['sentiment']
            print("Selected:",selected)
        
        if feeds != "Not found":
            found = 'true'

            unique_feeds = []
            seen_titles = set()

            for feed in feeds:
                if feed.title not in seen_titles:
                    unique_feeds.append(feed)
                    seen_titles.add(feed.title)

            feeds = unique_feeds[:10]
                                        
            for feed in feeds:
                feed['summary'] = feed.summary
                feed['sentiment'] = get_prediction(feed['summary'])
                if feed['sentiment'] == 'Happy':
                    feed['secondary_text'] = 'This feed brings cheerful and uplifting content, spreading positivity and good vibes.'
                elif feed['sentiment'] == 'Sad':
                    feed['secondary_text'] = 'The tone of this feed is more somber, sharing stories that may evoke feelings of empathy or reflection.'
                else:
                    feed['secondary_text'] = 'This feed provides news and updates without a specific emotional tone, offering a balanced view of various topics.'
                if 'authors' in feed:
                    feeds_author = feed.authors
                    feed['author_name'] = feeds_author[0].get('name')
                    feed['author_email'] = feeds_author[0].get('email')
                else:
                    feed['author_name'] = None
                    feed['author_email'] = None
                if 'links' in feed:
                    feed['link'] = feed.links[0]['href']
                else:
                    feed['link'] = None

            selected_sentiment = data.get('sentiment', 'All')
            if selected_sentiment != 'All':
                feeds = [feed for feed in feeds if feed['sentiment'] == selected_sentiment]

            return render(request, "dash.html", {'feeds': feeds, 'found': found, 'selected': selected, 'url': url})

        else:
            found = 'false'
            return render(request, "dash.html", {'feeds': None, 'found': found, 'selected': selected})
        
    else:
        return render(request, "dash.html")