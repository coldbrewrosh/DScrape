import requests
import pandas as pd

url = "https://www.daraz.com.np/mens-casual-tops"

res = []
for x in range(1,11):
    querystring = {"ajax":"true","page":f"{x}","sort":"order"}

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.daraz.com.np/mens-casual-tops/?page=1&sort=order",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    r = requests.request("GET", url, headers=headers, params=querystring)
    print(f"Currently on page : {x}")
    data = r.json()
    for p in data['mods']['listItems']:
        res.append(p)

df = pd.json_normalize(res)
df.to_csv('pd_list_req/mens-casual-tops-10-pages.csv', index=False)