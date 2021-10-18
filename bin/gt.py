import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import cv2
import pickle
import argparse 

sets = ['test']
#sets = ['train', 'test']
classes =  ['BKXQS', 'screw', 'nolack','JYZ_DBJJXS']#['BKXQS', 'screw', 'nolack']

region_classes = ['XCXJ_BY2',
                  'XCXJ_BY3',
                  'XCXJ3',
                  'XCXJ_BY1',
                  'XCXJ1',
                  'XCXJ2',
                  ]

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

new_image_id = 0

data_list = []

def crop(image_id, image_set):
    global new_image_id
    tmp = []
    in_file = open('test/xml/%s.xml'%(image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    #[xmin, xmax, ymin, ymax]
    luosi = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls = classes.index(cls)
        xmlbox = obj.find('bndbox')
        xmin = int(xmlbox.find('xmin').text)
        xmax = int(xmlbox.find('xmax').text)
        ymin = int(xmlbox.find('ymin').text)
        ymax = int(xmlbox.find('ymax').text)
        luosi.append([ymin, ymax, xmin, xmax, cls])

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in region_classes:
            continue
        xmlbox = obj.find('bndbox')
        xmin = int(xmlbox.find('xmin').text)
        xmax = int(xmlbox.find('xmax').text)
        ymin = int(xmlbox.find('ymin').text)
        ymax = int(xmlbox.find('ymax').text)
        w = xmax - xmin
        h = ymax - ymin
        for i,item in enumerate(luosi):
            if item[0]>=ymin and item[1]<=ymax and item[2]>=xmin and item[3]<=xmax and item[4]==0:
                #f.write('{} {} {} {} {}\n'.format(item[4], item[2], item[0], item[3], item[1]))
                tmp.append([item[2], item[0], item[3], item[1]])

    data_list.append({'fname':image_id, 'detections':tmp})
wd = getcwd()

for image_set in sets:
    #image_ids = open('imageSets/%s.txt'%(image_set)).read().strip().split()
    with open('test_20191215.pkl','rb') as f:
        image_ids = pickle.load(f)
    image_ids = [p['fname'] for p in image_ids]
    print(len(image_ids))
    for image_id in image_ids:
        crop(image_id, image_set)

argparser = argparse.ArgumentParser('')
argparser.add_argument('--out', type=str)
args = argparser.parse_args()

print(len(data_list))
with open(args.out, 'wb') as f:
    pickle.dump(data_list, f)
from mmcv.runner import get_dist_info
