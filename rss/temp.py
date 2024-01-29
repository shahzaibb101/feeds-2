import feedparser
import re
from html import unescape

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    
    if feed.entries:
        for entry in feed.entries:
            entry.summary = re.sub('<.*?>', '', entry.summary)
            entry.summary = unescape(entry.summary)
            print("Title:", entry.title)
            print("Summary:", entry.summary)
            print('\n')
    else:
        print("incorrect")

if __name__ == "__main__":
    rss_feed_url = "https://www.reutersagency.com/feed/?best-sectors=economy&post_type=best"
    fetch_rss_feed(rss_feed_url)

