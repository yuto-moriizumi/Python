# ハイパー道楽から銃の性能をとってきます

import requests
import pprint
from bs4 import BeautifulSoup
#response = requests.get("https://review-of-my-life.blogspot.com/")
# print(response.text)
html_doc = requests.get(
    "http://www.hyperdouraku.com/airgun/index.html")
html_doc.encoding = html_doc.apparent_encoding
html_doc = html_doc.text
soup = BeautifulSoup(html_doc, 'html.parser')
urls = []
for i in soup.find_all("a"):
    urls.append("http://www.hyperdouraku.com/airgun/"+i.get("href"))
# print(urls)

f = open("result.csv", "w")
f.write("name,length,heavy,inner,magazine,cost,date,maxSpeed,avgSpeed,minSpeed,energy,rpm\n")
for j in range(0, len(urls)):
    print(j+1+"番目を取得中、残り"+len(urls)-j-1+"個", end="")
    html_doc = requests.get(urls[j])
    html_doc.encoding = html_doc.apparent_encoding
    html_doc = html_doc.text
    soup = BeautifulSoup(html_doc, 'html.parser')  # BeautifulSoupの初期化
    # print(soup.prettify())

    # TODO1 このページのaタグをすべて抜き出してください。(HTMLの内容)
    title = soup.title.text
    # print("タイトル："+title)
    tags = soup.find_all("td", bgcolor="#4B6957")

    data = [""]*12
    data[0] = title
    for i in range(0, len(tags), 2):
        #print(tags[i].text+"："+tags[i+1].text.split(" ")[0])
        text = ""
        try:
            text = "".join(tags[i+1].text.split(" ")
                           [0].split("\n")[0].split(","))
            if(tags[i].text == "全長"):
                data[1] = text
            if(tags[i].text == "重量"):
                data[2] = text
            if(tags[i].text == "銃身長"):
                data[3] = text
            if(tags[i].text == "装弾数"):
                data[4] = text
            if(tags[i].text == "定価"):
                data[5] = text
            if(tags[i].text == "発売日"):
                data[6] = text
            if(tags[i].text == "最高"):
                data[7] = text
            if(tags[i].text == "平均"):
                data[8] = text
            if(tags[i].text == "最低"):
                data[9] = text
            if(tags[i].text == "ジュール"):
                data[10] = text
            if(tags[i].text == "回転数"):
                data[11] = text
        except IndexError:
            break
    print(data)
    f.write(",".join(data)+"\n")
