#coding: UTF-8

import twitter
import pprint

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key="hhYBDvLE2ka5j0a4mEnxasi69",
                     consumer_secret="OHW2h9nMEFbtmsnXUsZudfYDIfWT2bE7JK2ts5CmBdNiOCLzkx",
                     token="2993483719-zTGnAgAB7gI3JlDrfC68cXZ7fB1m214BIZptEzq",
                     token_secret="xTh1jqDNsIYdvegAMZsgWUZodOlCIhyB4ZldDmVxJRoFg")

t = twitter.Twitter(auth=auth)

# twitterへメッセージを投稿する
# t.statuses.update(status="私は神です")

# result = t.search.tweets(q="#春から静大")["statuses"]
# for tweet in result:
# pprint.pprint(tweet["text"])
