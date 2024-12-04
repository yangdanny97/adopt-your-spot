import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Run VADER sentiment analysis on the reasons

data = None
with open("data/adopt_your_spot_geocoded.json", "r") as f:
    data = json.load(f)

sentimentAnalyzer = SentimentIntensityAnalyzer()


def calculate_sentiment(text):
    scores = sentimentAnalyzer.polarity_scores(text)
    compound_score = scores['compound']
    return compound_score


sentiments = []
pos, neg, neu = 0, 0, 0

for entry in data:
    reason = entry["Can you tell us why you have selected this spot?"]
    # block is classified as strongly negative sentiment
    reason = reason.replace("block", "")
    sentiment = calculate_sentiment(reason)
    entry["sentiment"] = sentiment
    sentiments.append(sentiment)
    if sentiment < 0.05 and sentiment > -0.05:
        neu += 1
    elif sentiment > 0:
        pos += 1
    elif sentiment < 0:
        neg += 1
with open("data/adopt_your_spot_geocoded.json", "w") as f:
    json.dump(data, f, indent=4)
print(pos, neu, neg)
