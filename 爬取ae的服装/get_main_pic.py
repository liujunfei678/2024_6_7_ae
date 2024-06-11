import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Access-Token':'eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJGTHVndWIyVWxhYldzeHQxZ2REVnZzcl9tRXNEQWdpcnFxeHNaRVBiQ2VjIiwieSI6IlBzMmZPbnlFTjhPUDJjUmlrSkJDOXJ5VlZCM3RIYlhaMWs0bzRvQ2ZiLUEifSwia2lkIjoiS0VZMSIsImN0eSI6IkpXVCIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJFQ0RILUVTK0EyNTZLVyJ9.QX8gtRxPMiqQ5mHMM5YpILFkkzcBqf2fK_ZhGIB78wWhJX_pcJIR7A.41UMqDjJetg0eKdLbFjnTg.oPJTnLkAK6iK3Mcl8bLyw_bySjI0whC141XTYVfUEk2tfw74FGxrNkV3wiF9P--FpGgAgY9o6M4cvftJLkCnpXKEsT7w-W58iaFGtsNvwxpfh7EH0KDR808Qi8lpZNWM9Av50SCN41vKfeFIA3IpmYPHoQDoE8yDkSkm-M3EwCm9K6--WOg0GtVBhgfjP3tFvHEZqWYQNXBIeXvJOQOaeDgU9AnfkfV4n7TybR9kZFIkgJYLKOn2O-PFc4R6_E5309BJN5oai074ACxSmRoHwHfZihUxc7NAO4fED37efK4DuzzeH0WxUjv4dGQvpO65jKQv7q0OrRdal5a0au2gYMV2oeoAFf5CaxenpWFdaRygSp68I2esjpDrNz9jcfBUCXu44FI4-BGQoMz-gEwhie96XXySuVVKuc_9S51drfNDCplfF7XnenK3WWtzleRLUk9ngEKHS_xl6X9fZ8s5j-QPWJRN5Qltab1ZXeDv-a2CP_YITHUkNES3RvO4TDqDRvct9mU1RxEhzaqCyvMeseejYZCJk6fg3wNQgDpUAr99ynwfpvgYF-OO_P8GIgiPozd8sOfl343VUWEiVrq5X3PSQ1JYFZsfXZRzvloKK1JMqzUD6Q_-FilQv5iB3xmZQDI9CqMKi-0XmYaOyJSiyYlLYLo1FXiOa4AFQmMMz0x1E8Zxshqzo9yhZ8NqWbk6.qM7gyFJmdiG_6fzi3BHrLw'
}


#获取请求返回值
def get_res(url):
    bs=BeautifulSoup(requests.get(url,headers=header).text,'html.parser')
    return bs


#获取页面的主要图片
def get_main_pic(url):
    main_pic=[]
    imgs=get_res(url).find_all('img',{'class':'_image_2vfqsz _media-item_2vfqsz'})
    for img in imgs:
        pic_url=img.get('src')
        ful_url='https:'+pic_url.split('?')[0]+'?$pdp-mz-opt$&fmt=webp'
        main_pic.append(ful_url)
        # print(ful_url)
    return main_pic

#获取该页面下的所有颜色的服装链接
# def getallcolor(url):
#     all_url=[]
#     base_url='https://www.ae.com/us/en/p/men/pants/cargo-pants/ae-flex-lived-in-cargo-pant/'
#     res=get_res(url)
#     # print(res)
#     try:
#         all_color=res.find_all('div',{'class':'swatch _swatch_1e4pqf _swatch_1brgyx'})
#         # print(all_color)
#         for color in all_color:
#             # print(color)
#             c_url=color.find('img',{'class':'img-responsive _swatch-img_1e4pqf'}).get('src')
#             id_num=c_url.split('/')[-1].split('?')[0].split('_')[:-1]
#             id_num=id_num[0]+'_'+id_num[1]+'_'+id_num[2]
#             ful_url=base_url+id_num
#             all_url.append(ful_url)
#             print(ful_url)
#         return all_url
#     except Exception as e:
#         print('未找到其他颜色衣服：'+e)
url='https://www.ae.com/us/en/p/men/pants/cargo-pants/ae-flex-lived-in-cargo-pant/0123_4882_219?nvid=pdp%3A0123_4882_219&menu=cat4840004'
# getallcolor(url)

# url='https://www.ae.com/us/en/p/men/pants/cargo-pants/ae-flex-lived-in-cargo-pant/0123_4882_219?menu=cat4840004'
# get_main_pic(url)

#获取相关的其他服装链接
def getother(url):
    try:
        all=[]
        base_url='https://www.ae.com/us/en/p/men/polos/sweater-polos/ae-weekend-tipped-sweater-polo-shirt/'
        res=requests.get(url,headers=header).json()
        include=res['included']
        for dic in include:
            data=dic['relationships']['product']['data']['id']
            ful_data=base_url+data
            all.append(ful_data)
        # print(res)
        return all
    except:
        return []


# url='https://www.ae.com/ugp-api/outfitter/v1/product/1149_1839_141?include=similar-products'
# print(getother(url))

def get_allpic(url):
    all_pic=[]
    main_pic=get_main_pic(url)
    all_pic.extend(main_pic)
    name=url.split('/')[-1].split('?')[0]
    similar_url=f'https://www.ae.com/ugp-api/outfitter/v1/product/{name}?include=similar-products'
    otherurl=getother(similar_url)
    for other in otherurl:
        otherpic=get_main_pic(other)
        all_pic.extend(otherpic)
    return all_pic,otherurl

def main(l):
    print(f'正在下载{l}中的图片！')
    allpic, other = get_allpic(l)
    if other != []:
        id = l.split('/')[-1].replace('?', '')
        return {id:allpic}
    else:
        return {}


if __name__=='__main__':
    # url='https://www.ae.com/us/en/p/men/tops/sweaters/ae-striped-sweater-polo-shirt/1149_1839_141?nvid=pdp%3A1149_1839_211&menu=cat4840004'
    all_dic={}
    with open('all_men.json','r') as f:
        data=json.load(f)

    with Pool(6) as p:
        result=p.map(main,data)
    for i in result:
        all_dic.update(i)

    with open('all_men_pic.json','w') as f:
        json.dump(all_dic,f,indent=4)


    # print(allpic)

