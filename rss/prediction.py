import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_prediction(summary):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(summary)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return 'Happy'
    elif compound_score <= -0.05:
        return 'Sad'
    else:
        return 'Neutral'

summary = "Andrea Canning reports on the case that made national headlines in December 2019, when a Texas mother was found murdered after she and her newborn daughter disappeared. Originally aired on NBC on January 31, 2020."
print(get_prediction(summary))
