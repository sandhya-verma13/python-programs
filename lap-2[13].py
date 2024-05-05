# Sample comments data
comments = [
    ("Great product, love the features!", 50),
    ("The customer service was terrible, won't recommend.", 20),
    ("Best purchase ever, highly recommended.", 100),
    ("The delivery was delayed, very disappointed.", 10),
    ("Amazing quality, exceeded my expectations.", 80)
]

# List of keywords to track
keywords = ["product", "customer service", "recommend", "delivery", "quality"]

# Dictionary to store keyword frequencies
keyword_freq = {keyword: 0 for keyword in keywords}

# Count keyword frequencies in comments
for comment, likes in comments:
    for keyword in keywords:
        if keyword in comment.lower():
            keyword_freq[keyword] += 1

# Sort keywords by frequency in descending order
sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)

# Extract sorted keywords from sorted list of tuples
top_trending_topics = [keyword for keyword, freq in sorted_keywords]

# Display the top trending topics
print("Top Trending Topics:")
for topic in top_trending_topics:
    print(topic)
