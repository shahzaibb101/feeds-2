import feedparser
import re
from html import unescape

def fetch_rss_feed(url):
    print("Url:",url)
    feed = feedparser.parse(url)
    print("Feed",feed)
    
    if feed.entries:
        for entry in feed.entries:
            entry.summary = re.sub('<.*?>', '', entry.summary)
            entry.summary = unescape(entry.summary)
            
        return(feed.entries)
    else:
        return "Not found"

if __name__ == "__main__":
    rss_feed_url = "https://podcastfeeds.nbcnews.com/RPWEjhKq"
    print(fetch_rss_feed(rss_feed_url))
