# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-12-06 17:21:09
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-12-06 17:29:08
import cv2 as cv  
import os

def fn(str):
	if str.endswith('.JPG') or str.endswith('.txt') or str.endswith('.jpg'):
		return True 

jpgs = sorted(filter(fn,os.listdir('/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/LST_error')))
txts = sorted(filter(fn,os.listdir('/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/LST_results')))
print(jpgs)
print(txts)
for txt,jpg in zip(txts, jpgs):
    assert txt.split('.')[0] == jpg.split('.')[0] 
    with open('/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/LST_results/%s'%txt, 'r') as f:
        BKXQS = f.readlines()
    if len(BKXQS) == 0:
        continue
    img = cv.imread('/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/LST_error/%s'%jpg)
    for bndbox in BKXQS:
        _, conf, x1, y1, x2, y2 = bndbox.split(' ')
        x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
        cv.rectangle(img, (x1,y1),(x2,y2),(0,0,255),2)

    cv.imwrite('/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/LST_results/init/%s'%jpg, img)

