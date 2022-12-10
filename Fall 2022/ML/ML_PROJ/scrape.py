# import snscrape.modules.twitter as sntwitter
# import pandas as pd

# tweets_list2 = []
# i = 0
# for j,tweet in enumerate(sntwitter.TwitterSearchScraper('$TSLA since:2021-10-28 until:2022-11-05').get_items()):
#     if i>1000 or j > 1000000:
#         break
#     if tweet.likeCount > 1000 or tweet.retweetCount > 1000:
#         tweets_list2.append([tweet.date, tweet.rawContent, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.user.followersCount, tweet.user.verified])
#         i+=1
#         if i % 100 == 0:
#             print("Tweet accepted: "+str(i))
#     if j % 30000 == 0:
#         print("Tweets seen: "+str(j))
    
    
# tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Text', 'Username', "Likes", "ReTweet", "Followers", "Verified"])
# tweets_df2.to_csv("/Users/abhinav/Desktop/output.csv")

# import twint
# import nest_asyncio
# nest_asyncio.apply()
# # Set up TWINT configuration function

# def get_tweets(start_date, end_date, company_name):
#     c = twint.Config()
#     c.Search = company_name
#     c.Since = start_date
#     c.Until = end_date
#     c.Store_csv = True
#     c.Lang = 'en'
#     c.Count = True
#     c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Twecd ..et: {tweet}"
#     c.Custom['tweet'] = ['id', 'date', 'time', 'tweet']
#     twint.run.Search(c)     
#     c.Output = 'tesla_tweets'

# # Get tweets for Tesla

# get_tweets('2021-10-28', '2021-11-05', 'tesla')

import twint

# Configure
c = twint.Config()
c.Search = "tesla"
c.Lang = "en"
c.Limit = 300
c.Output = "./tweets.csv"
c.Since = '2021-10-28'
c.Until = '2021-11-05'
c.Store_csv = True
c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet}"
c.Custom['tweet'] = ['id', 'date', 'time', 'tweet']
# Run
twint.run.Search(c)