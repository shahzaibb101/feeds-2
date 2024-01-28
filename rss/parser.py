import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    
    if feed.entries:
        for entry in feed.entries:
            return(entry)
    else:
        return None

if __name__ == "__main__":
    rss_feed_url = "https://podcastfeeds.nbcnews.com/RPWEjhKq"
    print(fetch_rss_feed(rss_feed_url))
