import json
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Access-Token':'eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiJfdWxITVNkeWpnN1FSak90Q0s1WlJ5RW0yRjZaM3R4UVA0OVdGejVESDdZIiwieSI6Ik5QUFNLdXcyWk83clBIcmNOWVFNTU80REdIOTd0RWx3S1ZzbHZ1Z2JpTm8ifSwia2lkIjoiS0VZMSIsImN0eSI6IkpXVCIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJFQ0RILUVTK0EyNTZLVyJ9.quVE6p65QfrZQg8jj_JhQFZa63vLBhxHQASfNA1ic8k7Vey2NWMPBA.sG_YTZg4orqICzMg67lIWw.Ipafv8gIM2HW2HhoR3EHUXVfWPcOWdAStXimDehubQ2EwyBsfK2F8zBviuiBKpj_siZyt8r-hQthXfTrOzZLiZFESQnlpHVNKxQ1qJmORN9K6VNOK2hYwiFbWjcoCVXeu_s2FVzCXRphCWzJIAdNuCr2-Z8oxN14sWLxohZ9dNsJsm5sQDEFVf4aQchu2RrTPz5aMgtt6A4PREvaYhonCyYHu08ZKrg0vCUdQJGj9ISe2C8Nu5b0T0nbufT9ekNI-oZRTkFgcW0rAtWI7-M2pV5xy2g0S8667vq5czdb2v7WnHNuUfPGYSkOR1YsU5rkuYJdUF3W8md__huORnm1DA-G7Yv5oAvGwyO4MEU6RPjdKFWWps5jdwBOEoTUxGHsQ6bS8oYEs3EdSRbpyRZEqr1pN1W3cQ8mLCkBGfL5TcjBg-Td6fSMgp-8I2bozF6g20yMgIB7OJ1aUEACDiULbabZccl30vMjUNHLsibWi1_UIJ2v7OubdKS0G27zezJXapVtLkjlF5scp472XTWkUJHKLBUqB5o5L6djiMEMWP6pcWil5f2ZTgEbcnfR9vN983Di8Dv5bkqQ5Stg5uCRUM0QmECATcUQfmer6i-zB1XhqDJu_s1scLaBmb9z7Faf2mUMM-QOcoMg2WIJ6Iz8VMKMShixpkvWuz6WAyL-pXRlPYtIMsXvo6hX4JeFxNaR.fV3J5LLMseN8-AR6u4z9bQ'
}


#获取请求返回值
def get_res(url):
    bs=BeautifulSoup(requests.get(url,headers=header).text,'html.parser')
    return bs


#获取页面的主要图片
def get_main_pic(url):
    try:
        main_pic=[]
        imgs=get_res(url).find_all('img',{'class':'_image_2vfqsz _media-item_2vfqsz'})
        for img in imgs:
            pic_url=img.get('src')
            ful_url='https:'+pic_url.split('?')[0]+'?$pdp-mz-opt$&fmt=webp'
            main_pic.append(ful_url)
            # print(ful_url)
        return main_pic
    except:
        print('找不到目标链接的图片返回空！')
        return []

# url='https://www.ae.com/us/en/p/men/polos/sweater-polos/ae-weekend-tipped-sweater-polo-shirt/0112_5464_455'#测试错误链接
# main_pic=get_main_pic(url)
# print(main_pic)

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
        res=requests.get(url,headers=header).json()#这边需要修改一下tooken的判定
        # print(res)
        data_set=res['data']
        if data_set !={}:
            include=res['included']
            for dic in include:
                data=dic['relationships']['product']['data']['id']
                ful_data=base_url+data
                all.append(ful_data)
            # print(res)
            return all
        else:
            print('tooken过期')
            header['X-Access-Token']=input('请输入新tooken：')
    except:
        return []


# url='https://www.ae.com/ugp-api/outfitter/v1/product/1165_3733_615?include=similar-products'#含无效链接
# url='https://www.ae.com/ugp-api/outfitter/v1/product/0123_4882_219?include=similar-products'#没有搭配的链接
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
    print(allpic)
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

    with open('all_men_pic.txt','w') as f:
        json.dump(all_dic,f,indent=4)


    # print(allpic)

