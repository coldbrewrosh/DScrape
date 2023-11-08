import requests
import pandas as pd
import time

url = "https://www.daraz.com.np/womens-clothing/"


# Initialize a list to store DataFrames
data_frames = []

for x in range(1, 11):
    querystring = {"ajax": "true", "page": f"{x}", "sort": "order"}

    # headers = {
    #     "cookie": "JSESSIONID=FFDEAAD8301069FD105AB179001F890B; lzd_sid=1d5b30d2840f78c0cde378773dc5ef5a; _tb_token_=33eee15e8b88f",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    #     "Accept": "*/*",
    #     "Accept-Language": "en-US,en;q=0.5",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Referer": "https://www.daraz.com.np/mens-casual-tops/?page=2&sort=order&spm=a2a0e.searchlistcategory.pagination.5.7359210faQbjtn",
    #     "Content-Type": "application/json",
    #     "Connection": "keep-alive",
    #     "Cookie": "lzd_cid=1de92dbc-0bef-47cf-c401-01c7140d3aaa; t_uid=1de92dbc-0bef-47cf-c401-01c7140d3aaa; hng=NP^|en-NP^|NPR^|524; userLanguageML=en-NP; t_fv=1698232869182; cna=JOi/HeiVO2UCARsiMAeZLDiv; _m_h5_tk=182b68df90edf04ae0cfff45de29fbba_1699435279322; _m_h5_tk_enc=575afb26545b8355ca0655d651f6c882; _bl_uid=74lp8o2t5O3otF01U4yOv4s5s2Lm; _gcl_au=1.1.1657259476.1698232870; isg=BEJCKWTEk1Zppo95Ru3JPX6skEikE0YtoLDHF4xaXrXA3-dZdKAtPE9Zj0OjlL7F; l=fBao5kBRPMPUENIWBO5Churza77OyIOVCkPzaNbMiIEGa61cgahT9NCTsfSpzdtfQT5m9etrVskUfdFJ7oaU-x6QVdrGpIK55tJ68etzRyMc.; _ga_GEHLHHEXPG=GS1.1.1699430663.14.1.1699430668.0.0.0; _ga=GA1.1.1689701666.1698232871; tfstk=dNeWmy6wsUYSQgcFgTs4lonMFZHEPy6a9HiLjkpyvYHJJeEtuJSoT_fLGyUmaXEELrwQ7rJrwafoJpUUkbpEUvuLlY24apuPrvZL7A_N7OWaquDmpN7NfSQ9rOHHYsISfuqoKvQN7OWaqpw8dgsa6H_NFnrClKv2Q1dXpCYYetyxVbgQaq9_f-vZMVKSkp9CYlBN0du6HQABcfvKcQjfcBA3p_pLJ; _fbp=fb.2.1698232872518.545560773; cto_bundle=Nc7VQV9HJTJGZVJTa29STnIyd200MHhvNkJlb3NSYmZ2Q0dkTDg5U0RKY2RXUndWSG9kRUdORWloNmZPYWNib3pmYzFHJTJGdnJXY2ZXYmo4QUx2QVZGcDRrTUNoNDhXamVZbmMlMkJ0bCUyRk9ieXZHTTRybDBndGQ4VU52SWx6RmViJTJCcUNJUjR3SXd1TlRYcyUyRmkxdm1CcFNwMDRJcDhLTFElM0QlM0Q; daraz_smart_banner=hide; lwrid=AQGLe6Y8ocQDoA4b8kH4zBu75CW0; epssw=1*NpC_11gYY5USMdXMCm7z7liGKJtIf4yYzrySCDUEJyLzJ7GSuzUm_ZKdYerEIB13aOZTXQ9Ajhj9oJtVdD1OF9_nZrFSH_srm-pC3hxGsCnPE91GQRIoqb6ANK6C3TMl6LtoToMNPnATRGEFcjWW4HGDJdt59UOWe_eQ0qsnh-onxbxtyULRyTB4yaKUvTB4pL3RyaQRhXLJ4TOlYUaTyUQRpLHR3kmndC..; xlly_s=1; lzd_sid=1a88dfa64cd05eb585a5c0db3c660c68; _tb_token_=e31110710eea5; _gid=GA1.3.518495196.1699427363; JSESSIONID=F60F43F17B58A459E90FBC9A3FCE31C3",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "TE": "trailers"
    # }
    # r = requests.request("GET", url, headers=headers, params=querystring)
    
    r = requests.request("GET", url, params=querystring)
    print(f"Currently on page : {x}")

    # Check if the request was successful
    if r.status_code == 200:
        data = r.json()
        res = []
        for p in data['mods']['listItems']:
            element = data['mods']['listItems'][0]['name']
            res.append(p)
        print(element)
        df = pd.json_normalize(res)

        # Save the data to a separate CSV file for each request
        csv_file_name = f'pd_list_req/csv/mens-casual-tops-page-{x}.csv'
        df.to_csv(csv_file_name, index=False)
        print(f"Saved data to {csv_file_name}")

        # Clear the res list for the next iteration
        res.clear()

    # Delay for 10 seconds between requests to avoid overloading the server
    print("")
    time.sleep(5)

# # Concatenate all the DataFrames into one
# merged_data = pd.concat(data_frames, ignore_index=True)

# # Save the merged DataFrame to a CSV file
# merged_data.to_csv('merged_data.csv', index=False)
