import requests
import pandas as pd
import time

url = "https://www.daraz.com.np/mens-casual-tops"

res = []
for x in range(1,11):
    querystring = {"ajax":"true","page":f"{x}","sort":"order"}

    headers = {
        "cookie": "JSESSIONID=B58B2BC51CA77C01438644DE9353F76E; lzd_sid=1d5b30d2840f78c0cde378773dc5ef5a; _tb_token_=33eee15e8b88f",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.daraz.com.np/mens-casual-tops/?page=1&sort=order",
        "Connection": "keep-alive",
        "Cookie": "lzd_cid=1de92dbc-0bef-47cf-c401-01c7140d3aaa; t_uid=1de92dbc-0bef-47cf-c401-01c7140d3aaa; hng=NP^|en-NP^|NPR^|524; userLanguageML=en-NP; t_fv=1698232869182; cna=JOi/HeiVO2UCARsiMAeZLDiv; _m_h5_tk=90a29061bd6e347a926292cb26374a3e_1699269945342; _m_h5_tk_enc=51f77fd71db8b8528cce51d3978be754; _bl_uid=74lp8o2t5O3otF01U4yOv4s5s2Lm; _gcl_au=1.1.1657259476.1698232870; isg=BDU14gqAvLycP9hw3Sw2RIXdR7HvsunE68EwXrdavKzxjleAfwDQlWxI2Mq41QF8; l=fBao5kBRPMPUEkSXBOfZPurza77OtIO4YuPzaNbMi9fPOafHb2V1W1F9rgLMCn6NEsvkR3o5gvr6B88_1y4Eh9ZWQlXpM3__vd8HR3zQR; _ga_GEHLHHEXPG=GS1.1.1699262030.9.1.1699266336.0.0.0; _ga=GA1.3.1689701666.1698232871; tfstk=dw3wmz1dVFLZEM4scl4484mcYiZTuPvSiqwbijc01R2G5N6mYYH4GCIji-kqdJZbhPc1uml0LVOTC5a2gJGuC-w_S1nKFbbs5hUfuNUYoL9WPUOt6rU0LwoHFYrt_BoG4UTS6fUYoL9WPCCKER6P0AODwNqyEbenW9HJneLxPJ7czvFaxA88pZYtJ5W7wOr1HW03gqnNniqGlWyWTBRTSTlN.; _fbp=fb.2.1698232872518.545560773; cto_bundle=et_T9V9HJTJGZVJTa29STnIyd200MHhvNkJlb3VJS2d4JTJGVzVRNVlZZ09mMlJ1VXczZVJNZ1NFc1VpYVBpJTJGaEFtTFpKeTdMWFlJUnhXNEMzcmJPT3lnT2V0TFVSakVqOFA0dXQwQ0xPJTJGZVRtWWZTRXNJb1FTZmhTV3VGTTVBREZiM0NYJTJGVTF4JTJCOWowSjlRM0p6elFpTkdaNEFTNmclM0QlM0Q; daraz_smart_banner=hide; lwrid=AQGLe6Y8ocQDoA4b8kH4zBu75CW0; epssw=1*MQc_11gPF13GMOvMJJWNIB1Qt1IIfviaCbMSCVFGpUP0Cqz4JSBV5NPu2M84O6D9Cpy4NKIMji1JzKrqHQ9AdtQN3b9vK6SMjQ9vVKqPE1Cp5KyBF992jhROFLMl6LtasoMNPnxiifD0cjWW4d4Kl9LAOhNWyiW6vWe-uZ-nxYZKdTHBeDmndLedbMmnpL3RyaQRWoQJ49CX15XTLLB4pLHBev9-y1..; t_sid=v0MfojNw1WsvNL95BvaO6zTZ3v448N2i; utm_channel=NA; lzd_sid=1bee82a05b005a1a664ba5f42d9e3c4a; _tb_token_=fe3d93e357797; xlly_s=1; _gid=GA1.3.1806514366.1699262033; JSESSIONID=CDAE5E4FE5C1562F12DC811F04A60560; XSRF-TOKEN=5b189dca-0881-47ac-b773-9c4822e0c141; daraz-marketing-tracker=hide",
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
    df.to_csv(f'pd_list_req/csv/mens-casual-tops-page-{x}.csv', index=False)

    time.sleep(10)

# df = pd.json_normalize(res)
df.to_csv('pd_list_req/csv/mens-casual-tops-10-pages.csv', index=False)