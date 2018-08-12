# Description
Twitter Official API has the bother limitation of time constraints, you can't get older tweets than a week. The project is to get the old tweets. The project is modified from https://github.com/Jefferson-Henrique/GetOldTweets-python.git. I fixed the code bug for "GetOldTweets-python" which will loose some tweets and customed it for my current purpose. And also I fixed the time different problem. The final time should be date - 3 hours.

## Prerequisites
This package assumes using Python 2.x.
```
pip install -r requirements.txt
```

## Components
- **Tweet:** Model class to give some informations about a specific tweet.
  - id (str)
  - permalink (str)
  - username (str)
  - text (str)
  - date (date)
  - retweets (int)
  - favorites (int)
  - retweetornot (int): whether the current twitter text retweets other user's tweet.
  - hashtags (str)

- **Exporter.py:** Export tweets to a csv file.
- **top.py:** Export special purpose top tweets to the csv files based on the date in folder top.
- **all.py:** Export special purpose latest tweets to the csv file based on the date in folder lastest.
- **top:** Include all top tweets.
- **lastest:** Include all lastest tweets.
- **final:** Include the final result.
- **final.csv:** Include all the tweets details.
- **extract_twitter_num.py** Generate the twitter.csv.
- **merge_csv.py**Merge different csv files to one file, final.csv.
- **twitter.csv** Show the number of twitters for each day including #walkaway.
- **result:** Include the twitter username and date for each tweet. 
