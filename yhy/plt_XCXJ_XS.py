# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-10-09 15:16:54
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-10-09 22:04:00
import xml.etree.ElementTree as ET
import os
import argparse
import sys
from tqdm import tqdm
import cv2
from tqdm import tqdm
import numpy as np

# 小，5个

# classes = ['JJXS_yybw', 'XCXJ_BY3', 'XCXJ_BY2', 'NZXJ_yjh', 'XCXJ_XS']
classes = ['XCXJ_XS']

# 大，7个

# region_classes = ['XCXJ_JJC','XCXJ','44_NZXJ_YYX','38_XXXJ','41_NZXJ','45_NZXJ_ZDX','37_NZXJ_YJSX ']
# 将38_XXXJ :1462,45_NZXJ_ZDX :45,37_NZXJ_YJSX :325类别定义为41_NZXJ :4257
# region_classes = ['XCXJ_JJC', '44_NZXJ_YYX', '41_NZXJ']
new_image_id = 0


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def crop(image_id, raw_path, path, train_txt):
    global new_image_id
    in_file = open('%s/Annotations/%s.xml' % (raw_path, image_id))

    img = cv2.imdecode(np.fromfile('%s/JPEGImages/%s.jpg' % (raw_path, image_id), dtype=np.uint8), -1)
    tree = ET.parse(in_file)
    root = tree.getroot()


    luosi = []
    #一张图片
    new_image_id=0
    for obj in root.iter('object'):
        cls = obj.find('name').text
        print(cls)
        if cls != 'JJXS_yybw':
            continue
        xmlbox = obj.find('bndbox')
        xmin = int(xmlbox.find('xmin').text)
        xmax = int(xmlbox.find('xmax').text)
        ymin = int(xmlbox.find('ymin').text)
        ymax = int(xmlbox.find('ymax').text)
        # cls_id = classes.index(cls)

        cropped = img[ymin:ymax, xmin:xmax]
        # cv2.imwrite("%s/step2_JPEGImages/%06d.jpg"%(path,new_image_id), cropped)
        cv2.imencode('.jpg', cropped)[1].tofile("/home/igi/media/yhy/jinjuxiushi/test_dataset/JJXS_yybw/%s_%s.jpg" % (image_id,new_image_id))
        # train_txt.write(os.path.join(path, 'step2_JPEGImages/%06d.jpg\n' % (new_image_id)))
        # out_file = open(os.path.join(path, 'step2_labels/%06d.txt' % (new_image_id)), 'w')
        # out_file.write("{} {}\n".format(w, h))
        new_image_id += 1



if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='train')
    argparser.add_argument('-trdata', type=str, default='/media/zkzx/9f8c0111-3713-4aa2-ae7d-fd35f3300098/BKXQS')
    args = argparser.parse_args()
    pwd = os.path.abspath(os.path.dirname(__file__))
    pwd = os.path.abspath(os.path.dirname(pwd))
    train_dir='../train_data'
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists('%s/step2_JPEGImages' % train_dir):
        os.makedirs('%s/step2_JPEGImages' % train_dir)
    if not os.path.exists('%s/step2_labels' % train_dir):
        os.makedirs('%s/step2_labels' % train_dir)

    imgs = []

    with open(os.path.join(train_dir, 'train.txt'), 'w') as f:
        dir_ = '%s/JPEGImages' % train_dir
        img_list = os.listdir(dir_)
        # pbar = tqdm(range(len(img_list)))
        for img in img_list:
            if not img.split('.')[-1] == 'jpg':
                os.rename(os.path.join(dir_, img), os.path.join(dir_, img.split('.')[0] + '.jpg'))
            img = img.split('.')[0] + '.jpg'
            imgs.append(img.split('.')[0])
            f.write(os.path.join(dir_, img) + '\n')
            # pbar.update(1)

    f = open(os.path.join(train_dir, 'step2_train.txt'), 'w')
    pbar = tqdm(range(len(imgs)))
    for image_id in imgs:
        pbar.update(1)
        crop(image_id, raw_path=train_dir, path=train_dir, train_txt=f)
    f.close()

    sys.stdout.write('Process end with exit code 0')
