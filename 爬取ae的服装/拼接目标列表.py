import json
import os


def get_json_list(path):
    json_file = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('new.json'):
                file_path = os.path.join(root,file)
                json_file.append(file_path)
    return json_file

file=get_json_list('women')
# print(file)
all_url=[]
for f1 in file:
    with open(f1,'r',) as f:
        data = json.load(f)
        all_url.extend(data)
print(all_url)
with open('all_women.json','w',) as f:
    json.dump(all_url,f)