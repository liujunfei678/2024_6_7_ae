import json
with open('all_men_pic.txt','r',encoding='utf-8') as f:
    # data = f.read()
    data=json.load(f)
# print(data)
prefixs=set()

new_data={}

for key,value in data.items():
    prefix=key.split('nvid')[0]
    if prefix in prefixs:
        print('发现重复')
        continue
    prefixs.add(prefix)
    new_data[key]=value
with open('all_men_pic_new.txt','w',encoding='utf-8') as f:
    json.dump(new_data,f,indent=4)