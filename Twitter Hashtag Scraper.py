import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:COVID, OR from:Health) until:2022-04-16 since:2021-01-01"
limit = 100
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount])

df = pd.DataFrame(tweets, columns=["Date", "Username", "Tweet", "LikeCount"])
print(df)

df.to_csv('tweet100.csv')