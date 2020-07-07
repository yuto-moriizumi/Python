import json
import glob


def toTuple(*args):
    return tuple(args)


files = glob.glob('./データ\*.json')

output = open('result.csv', 'a')

for file in files:
    tweets = json.load(open(file))
    for tweet in tweets['statuses']:
        user = tweet["user"]
        t = toTuple(tweet["created_at"], tweet["text"].replace('\n', '').replace(',', '、'),
                    tweet["source"], user["screen_name"], user["location"].replace(',', '、'), user["description"].replace('\n', '').replace(',', '、'), str(user["statuses_count"]))
        w = str(','.join(t))
        try:
            output.write(w+'\n')
            print('Success:', end='')
            print(w)
        except:
            print('Error:', end='')
            print(w)
