import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv
header={
    # 'Accept':'application/vnd.oracle.resource+json',
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'Aelang':'en_US',
    # 'Aesite':'AEO_US',
    # 'Content-Type':'application/json',
    # 'Requestedurl':'plp',
    # # 'Requestedurl':'https://www.ae.com/ugp-api/catalog/v1/category/womens?No=180&Nrpp=30&prevPageGroupId=cat10049',
    # 'Sec-Ch-Ua':'"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':"Windows",
    # 'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-origin',
    # 'Traceparent':'00-ef55b9093296efcde93d76583a0122d2-4e73c23c87ebd2db-01',
    # 'Tracestate':'204348@nr=0-1-2498998-1120168438-4e73c23c87ebd2db----1717748757908',
    'Referer':'https://www.ae.com/us/en/c/women/tops/cat10049?pagetype=plp',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Access-Token':'eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJXdlpvX296YUtpTnRhMkJHUEd1ZkIzV21LcFhTaXlHTnZQWGk4ZUQwTDZBIiwieSI6Ik9wSnJDS0hmTkk5bm9yQ1RfRllkOC03WkdYSU4tNFg0cW5XTHg0SlJ1dWMifSwia2lkIjoiS0VZMSIsImN0eSI6IkpXVCIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJFQ0RILUVTK0EyNTZLVyJ9.OBfYUpuZUHGEqOLSiJne3bkj6louZ7uZuXML1iph8taMYhB_6MfvnQ.IMNuSk4k2uO3QdjlPCBzOw.0D4_oSGqnwPWV7QVL2IgqdLSN_91k_ZEFlIWgK8RhmHdvf0Noj2cbqr6GMq1v0IVFNVN7OvNx37d9V5BkV8zKdpt_rCtppjFSXmA_Gcu6OKPIQK43cvcDiE2xRy4FBOoqQw4hDOpMSJrPNEW_kz29YqpdVH1fNU9DvGj7PwRULFVAncFS9DR9fchBBvjmJxuS641bwS3wrMkXsPNeP41yviWpZZ4nsv9gtaQINyYUFUJQJ5DcGnRFzv9aygPIM845OIGmL3PB5V_OtJArq_TZZ9ubqn2mefl-ZwrQskk-2kRmv7bzz-Q71tUG1ybN_WHO6hcHMCrxYITDRycIYFiCLAFysoxxqIQ_0kMkeeV3UslX9RxUs_X7Llt4diUbmED4pzg60Iyc4qxvy4IcxEjAtVL6ZQS6TwZNHQ-2T93d1vI-P536R46S3dQdG-Xhac9OquKtHTRZX7bxOdTnwlOh7pFcEylVu-Dfj2nH_tWmzYcZkt6-STPX6sBLHAnyI-w2ugujzyegO2IxoLEczIaeo-nN_Cl9Fkxf8iqTuBirFvTN7bgA_0r75GJRncciSFRl7tCwOw1QkjhGsRJFeXmwMkfo2MRrPdDekVR6TIK2F6-c5WdIbi7qTMeCjdWSw3J1LA4Iq1ASgL34vvCLETl1Fr0zTRwQwEmP0Cb8jRtMxc0hjLK8VH6mVJuh7KKV2a2.lehyP-pofdVXHwz8CjWjrw'

}
def getfirst(url):
    # url='https://www.ae.com/us/en/c/women/womens?pagetype=clp'
    url_list=[]
    first_header={}
    first_header['User-Agent']=header['User-Agent']
    baseurl='https://www.ae.com'
    res=requests.get(url,headers=first_header).text
    # print(res)
    bs=BeautifulSoup(res,'html.parser')
    datalinks=bs.find_all('a',{'class':'xm-link-to qa-xm-link-to _tile-link_1d4brf _tile-link_1d4brf'})
    for link in datalinks:
        url=baseurl+link.get('href')
        url_list.append(url)
        print(url)
    return url_list
# print(res)





def getlater(n,id):
    url_list=[]
    # url='https://www.ae.com/ugp-api/catalog/v1/category/cat10049?No=236&Nrpp=30&prevPageGroupId=cat7670003'
    # url=f'https://www.ae.com/ugp-api/catalog/v1/category/womens?No={n}&Nrpp=30&prevPageGroupId={id}'

    url=f'https://www.ae.com/ugp-api/catalog/v1/category/mens?No={n}&Nrpp=30&prevPageGroupId={id}'
    res=requests.get(url=url,headers=header).json()
    # pprint(res)
    # bs=BeautifulSoup(res,'html.parser')
    clothing=res['data']['contents'][0]['productContent'][0]['records']
    for l in clothing:
        try:

            base_url='https://www.ae.com/us/en'
            producturl=l['detailsAction']['recordState']
            producturl=base_url+producturl
            url_list.append(producturl)
            print(producturl)
        except Exception as e:
            print("可能不包含该属性：",e)
            continue
    return url_list
# res.encoding='utf-8'
# data=res.text
# res.encoding = res.apparent_encoding
# print(res)
def producturl(firstpage,lastpage,id):
    firstpage=int(firstpage)
    lastpage=int(lastpage)+1
    url_list=[]
    for page in range(firstpage,lastpage,30):
        print(page)
        pageurl=getlater(page,id)
        url_list.extend(pageurl)

    return url_list

if __name__=='__main__':
    with open('men记录.csv', 'r', encoding='utf-8', newline='') as f:
        read=csv.reader(f)
        for i,row in enumerate(read):
            if i<4:
                print(row)
                firstpage=row[0]
                lastpage=row[1]
                id=row[2]
                name=row[3]
                url_list=producturl(firstpage,lastpage,id)
                with open(f'men/{name}.json','w') as f:
                    json.dump(url_list,f)


# producturl(firstpage='30',lastpage='450',id='asd',name='das')

# getlater('30','cat10049')