import json
import os
import sys

import requests
from bs4 import BeautifulSoup
import multiprocessing
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'X-Access-Token':'eyJlcGsiOnsia3R5IjoiRUMiLCJjcnYiOiJQLTI1NiIsIngiOiItUU5jVDRyX05LM2Yxb0dTYzF1a0w5RlI2ak9BWWNoR3FOcGppWE01U2xNIiwieSI6ImZERWlCUmp3OFJDeU82ZXBYS2pxS1I4QktaM2NHa01OZmVyeGgzeE9PUDgifSwia2lkIjoiS0VZMSIsImN0eSI6IkpXVCIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJFQ0RILUVTK0EyNTZLVyJ9.IZZeyFuXASIoMvZGsjb0wr6o0XybBZ-pd3mz82Jg8djghOhSHuNWtw.irGd_QjE-0Y9lqhImmCEKg.lHBI2pw6NW8Hvuj2j7T2jerdy48Rt5JlbE6ntB0qlQqstsyYRn2hpgxPu5tVTF-Sc2L9q9OPJc18CMHssTNYN5LA1g3PUMIC-tVcfUuh0EY8eitJGq-QPi05DcUsXHmyHdnbeha6eNs9rCzFz8Jq4OxTks47l9pPXbXduafa9tQBzX1UUvDJ-dLGTnmZk5ovvHBFiyMrMMl0pv9-WUkh-d6hfQFjvQAoLAuk80jBsDFV3XcAX9WH5-0iO4ACQ-MlIzmJdKfyFZ3Oo5DyUx8RHe5H47r8aFxJErTn8XJM1VrZXQGOYmA96sAU5RkIWJPdI44W3YF-Cu9BAoenKVt9Rinnn-qX4aT-ORvTKpHgfL6D5KyABBeGCmKkzv0nJM-RR3dTr4rVXgOxmZFeqN4jKBpfo1TEcpmUrtUfYxSsYeMD9EP4-P5yKU_cetziyWssRCdm97obvLp-I0rMERa-vhBOpL95sMeuUQrPdU_NMTaQB8pwqgpx6H0EBsD-l0_07C_pAwqqdQTyCOHsW7e4T9JNh9G9AG1AiADI-U5l7kdWjddrPP_8DMgsw8sQl7jSL9wBc4j1HOw3jZrhSWqio6cGBpLhknESDSfSbiBuHVNgU27NYAVW7WkB5-2M4S5jaQ39-RS3jsgLaO9G2yTKi2ZqpU8mLhPcTMWxkXaCLv6NigiKfBxZJm-Ycgadxg9H.oKm9tSCdffaTiiFxI78aWA'
}



def get_res(url):
    retry=0
    while retry<5:
        try:
            bs=BeautifulSoup(requests.get(url,headers=header,timeout=30).text,'html.parser')
            return bs
        except requests.exceptions.Timeout:
            print('Timeout:')
            retry=retry+1
    return None



def getallcolor(url):
    all_url=[]
    base_url='https://www.ae.com/us/en/p/men/pants/cargo-pants/ae-flex-lived-in-cargo-pant/'
    res=get_res(url)
    # print(res)
    try:
        all_color=res.find_all('div',{'class':'swatch _swatch_1e4pqf _swatch_1brgyx'})
        # print(all_color)
        for color in all_color:
            # print(color)
            c_url=color.find('img',{'class':'img-responsive _swatch-img_1e4pqf'}).get('src')
            id_num=c_url.split('/')[-1].split('?')[0].split('_')[:-1]
            id_num=id_num[0]+'_'+id_num[1]+'_'+id_num[2]
            ful_url=base_url+id_num
            all_url.append(ful_url)
            print(ful_url)
        return all_url
    except Exception as e:
        print('未找到其他颜色衣服：'+e)

def main(path):
    newpath=path.split('.json')[0]+'_new.json'
    all_url=[]
    with open(path,'r') as f:
        data=json.load(f)
    for d in data:
        all_url.append(d)
        print(f'正在搜集有关{d}的相关链接！')
        other=getallcolor(d)
        all_url=all_url+other
    with open(newpath,'w') as f:
        json.dump(all_url,f)


def get_all_file_paths(folder_path):

    file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    return file_paths
if __name__ =="__main__":

    men_path_list=get_all_file_paths('men')
    women_path_list=get_all_file_paths('women')
    # print(men_path_list)
    args=men_path_list+women_path_list
    pool=multiprocessing.Pool(processes=6)
    results=pool.map(main,args)
    pool.close()
    pool.join()

