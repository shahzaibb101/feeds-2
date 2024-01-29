import feedparser
import re
from html import unescape

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    
    if feed.entries:
        for entry in feed.entries:
            entry.summary = re.sub('<.*?>', '', entry.summary)
            entry.summary = unescape(entry.summary)
            return(entry)
    else:
        return None

if __name__ == "__main__":
    rss_feed_url = "https://podcastfeeds.nbcnews.com/RPWEjhKq"
    print(fetch_rss_feed(rss_feed_url))
