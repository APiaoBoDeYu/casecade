#coding=utf-8

import os
import cv2
path ='./train_data/step2_labels'
savepth='./train_data/save/'
pic='./train_data/step2_JPEGImages/'
num =[0,0,0,0]
from tqdm import tqdm
pbar = tqdm(range(len(os.listdir(path))))
for file in os.listdir(path):
    pbar.update(1)
    f=open(os.path.join(path,file),'r')
    lines=f.readlines()
    img=cv2.imread(pic+ file.split('.')[0] + '.jpg')
    print(pic+ file.split('.')[0] + '.jpg')
    for line in lines:
        print(line)
        fields=line.split(' ')
        if len(fields)==5 and fields[0]=='0':
            num[int(fields[0])] += 1
            x0=int(fields[1])
            x1=int(fields[2])
            y0=int(fields[3])
            y1=int(fields[4])
            cv2.rectangle(img, (x0, y0), (x1, y1), (0, 0, 255), 2)
            # cv2.rectangle(img,(),(),(255),2)
    cv2.imwrite(savepth + file.split('.')[0] + '.JPG', img)
    print(savepth + file.split('.')[0] + '.JPG')
    print(file)
print('LST :{}'.format(num))
