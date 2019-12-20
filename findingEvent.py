import requests
import json
def getEvent():
    ACCESS_TOKEN = "CDbpXyjBeKv_-58SLLZcLXRsC_jkaTNBE-Cr2gat"
    response = requests.get(
        url="https://api.predicthq.com/v1/events",
        headers={
            "Authorization": "Bearer CDbpXyjBeKv_-58SLLZcLXRsC_jkaTNBE-Cr2gat",
            "Accept": "application/json"},
        params={
            "within": "100mi@33.9395909,-84.1952443",
            "start.gt": "2019-12-19",
            "end.ite": "2020-02-19",
        }
    )
    a = response.json()
    b = a.get("results")
    inner = []
    outer = []
    for i in range(1):
        for ii in range(10):
            try:
                inner.append(b[ii].get("title"))
                inner.append(b[ii].get("category"))
                inner.append(b[ii].get("start"))
                inner.append(b[ii].get("end"))
                outer.append(inner)
            except IndexError:
                break   
    # print(len(inner), len(inner[0]))
    return outer[0]

res = getEvent()
for i in range (len(res)):
    try:
        print(res[i*4+1])
    except IndexError:
        break

