import requests
import time

old = 0
while True:
    time.sleep(1)
    x = requests.get("https://api.scratch.mit.edu/studios/5842709/comments")
    if x.status_code != 200:
        raise SystemExit("Did not get a 200, halting")
    x = x.json()
    if old == x:
        continue
    res = []
    for i in x:
        found = 0
        if old == 0:
            break
        for j in old:
            if i["id"] == j["id"]:
                found = 1
        if found:
            continue
        else:
            res.append(i)
    res.reverse()
    for i in res:
        i["content"] = i["content"].replace("\n", " ")
        print(f"{i['author']['username']}: {i['content']} ({i['reply_count']} replies)")
    old = x
