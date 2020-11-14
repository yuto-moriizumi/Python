from datetime import datetime
import json
lines = ""
while True:
    i = input()
    if i[:3] == "end":
        break
    lines += i
json_object = json.loads(lines)
output = []
for user_id in json_object["users"]:
    tweetDatetime = json_object["users"][user_id]["tweetDate"]
    tweetDatetime = datetime.fromtimestamp(
        tweetDatetime).strftime('%Y-%m-%d %H:%M:%S')
    output.append(
        "(" + ",".join([f"'{user_id}'", f"'ID_NONE_{tweetDatetime}_{user_id}'", "'CONTENT_NONE'", f"'{tweetDatetime}'"]) + ")")

f = open('TJ2S_output.txt', 'w')
f.write(",\n".join(output) + ";")
f.close()
