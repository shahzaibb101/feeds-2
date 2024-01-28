import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    
    if feed.entries:
        for entry in feed.entries:
            print(entry.title)
            print(entry.summary)
            print('\n')
    else:
        print("incorrect")

if __name__ == "__main__":
    rss_feed_url = "https://feeds.bbci.co.uk/news/rss.xml"
    fetch_rss_feed(rss_feed_url)
