import json
import pandas as pd
import re
t = "transition.json"
d = "data.csv"
def token_append(data1):
    data1 = data1.lower()
    data = list(set(re.split(r"[ ,]+", data1))) 
    cm = ((pd.read_csv("data.csv")["token"]).max())
    df = list(pd.read_csv("data.csv")["word"])
    with open("data.csv","a") as f:
        for i in data:
            if i not in df:
                cm += 1
                f.write(f"{cm},{i}\n")
                continue
    return data
w2t = dict(zip(pd.read_csv(d)["word"],pd.read_csv(d)["token"]))
t2w = dict(zip(pd.read_csv(d)["token"],pd.read_csv(d)["word"]))
def transistor(data1):
    data1 = data1.lower()
    w2t = dict(zip(pd.read_csv(d)["word"],pd.read_csv(d)["token"]))
    t2w = dict(zip(pd.read_csv(d)["token"],pd.read_csv(d)["word"]))
    al = lambda data,k:[i for i,x in enumerate(data) if x == k]
    data = (re.split(r"[ ,]+", data1))
    with open("transition.json",'r') as m:
            main = json.load(m)
            for i in data:
                nexters1 = [data[k+1] for k in (al(data,i)) if k+1 < len(data)]
                nexters = [w2t[j] for j in nexters1]
                before_nexters = [data[z] for z in (al(data,i))]
                before_nexters = before_nexters[0]
                if before_nexters not in main:
                    main[before_nexters]=nexters
                elif before_nexters in main:
                    main[before_nexters].extend(nexters)
                else:
                    pass
    with open("transition.json",'w') as yogurt:
        json.dump(main,yogurt,indent=4)
"""try:
    ask = []
    for i in range(470000):
        axe = (input(":"))
        ask.append(axe)
    token_append(" ".join(ask))
except KeyboardInterrupt:
    token_append(" ".join(ask))"""

"""data = input("Enter Data pls:")
token_append(data)
pass
pass
transistor(data)"""