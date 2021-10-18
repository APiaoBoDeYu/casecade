import pickle
from collections import Counter
f = open('./bin/test_20210805.pkl','rb')
objects=[]
info = pickle.load(f)
for file in info:
    for dec in file['detections']:
        objects.append(dec[5])

result=Counter(objects)
tag_dir={7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}
print(result)
for i in result:
    print('%s:'%tag_dir[i]+'%s'%result[i])
print(f)