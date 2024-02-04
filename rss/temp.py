class Feed:
    def __init__(self, title):
        self.title = title

# Sample feeds list with Feed objects
feeds = [
    Feed("Title 1"),
    Feed("Title 2"),
    Feed("Title 3"),
    Feed("Title 2"),  # Duplicate title
    Feed("Title 4"),
    Feed("Title 5"),
    Feed("Title 1"),  # Duplicate title
    Feed("Title 6"),
    Feed("Title 14"),
    Feed("Title 7"),
    Feed("Title 8"),
    Feed("Title 9"),
    Feed("Title 10"),
    Feed("Title 11"),
    Feed("Title 12"),
    Feed("Title 13"),
    Feed("Title 14"),
]

# Keep only the first 10 unique feeds based on feed.title
unique_feeds = []
seen_titles = set()

for feed in feeds:
    if feed.title not in seen_titles:
        unique_feeds.append(feed)
        seen_titles.add(feed.title)

# Keep only the first 10 feeds if the list is longer
unique_feeds = unique_feeds[:10]

# Print the unique feeds
for feed in unique_feeds:
    print(feed.title)
