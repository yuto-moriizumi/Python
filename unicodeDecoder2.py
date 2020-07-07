

import sys
import re


class Tweet:
    def __init__(self):
        self.createdAt = ''
        self.text = ''
        self.source = ''
        self.screenName = ''
        self.location = ''
        self.description = ''
        #self.count = None

    def __str__(self):
        s = ''
        try:
            s = self.createdAt+','+self.text+self.source+','+self.screenName +\
                ','+self.location+',"'+self.description  # +','+self.count
            return s
        except:
            return 'Error'


for iii in sys.argv[1:]:
    #    print(sys.argv[1:])
    #    print('Open:'+iii)
    #f = None
    try:
        f = open('1komaResult424221398.json', 'r')
    except:
        print('Cant open:'+iii)
        continue
    f2 = open('result.csv', 'a')
    ans = []
    tweet = None
    tweet = Tweet()

    lines = f.readlines()
    print('行数：'+str(len(lines)))
    for i in lines:
        found = re.findall('"created_at".*"', i)
        if len(found) > 0:
            if tweet.description != '':
                try:
                    f2.write(str(tweet))
                    f2.write('\n')
                    print(str(tweet))
                except:
                    pass
                tweet = Tweet()
            tweet.createdAt = found[0][14:]
            # print(found[0][14:])
            continue
        found = re.findall('"text".*"', i)
        if len(found) > 0:
            try:
                ans.append(found[0].encode().decode('unicode-escape'))
                text_mod = re.sub(
                    '"text".*"', found[0].encode().decode('unicode-escape').replace('\n', ''), i)
                # print(text_mod[20:-2])
                # f2.write(text_mod)
                tweet.text = text_mod[20:-1]
            except:
                #print(i, end='')
                # f2.write(i)
                pass
        found = re.findall('"source".*"', i)
        if len(found) > 0:
            tweet.source = '"'+found[0][79:-6]+'#'
            # print(found[0][79:-6])
            continue
        found = re.findall('"screen_name".*"', i)
        if len(found) > 0:
            tweet.screenName = found[0][14:]
            # print(found[0][14:])
            continue
        found = re.findall('"location".*"', i)
        if len(found) > 0:
            try:
                s = i[29:-3].encode().decode('unicode-escape')
                # print('Location:'+s)
                tweet.location = '"'+s+'"'
            except:
                tweet.location = ''
            continue
        found = re.findall('"description".*"', i)
        if len(found) > 0:
            # print('YAAAAAAAa'+i[32:-2])
            try:
                s = i[32:-2].encode().decode('unicode-escape')
                # print('Desc:'+s)
                tweet.description = s
            except:
                tweet.description = 'None'
            continue
        #found = re.findall('"statuses_count".*"', i)
        # if len(found) > 0:
        #    #tweet.screenName = found[0][14:]
        #    print('YAAAAAAAAA'+found[0])
        #    continue
    f.close()
    f2.close()
# print(ans)
# input()
input('Press Enter to exit')
