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
classes = ["JYZ_SQZB","JYZ_WDSQZB"]
region_classes =['JYZ_C_DTC','JYZ_C_BL','JYZ_C_CZ','JYZ_C_FH']#["JYZ_C_unknown"]

savedir='/media/igi/2dc91e84-4382-41e7-9940-a171405bac53/LeiZhang/cascade_jyz_zb_smallbox_20200601/train_data/save/'
new_image_id = 0

def crop(image_id, raw_path, path, train_txt):
    global new_image_id
    in_file = open('%s/Annotations/%s.xml'%(raw_path,image_id))
    #print('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
    img = cv2.imread('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in region_classes:
            continue
        #img = cv2.imread('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
        xmlbox = obj.find('bndbox')
        xmin = int(xmlbox.find('xmin').text)
        xmax = int(xmlbox.find('xmax').text)
        ymin = int(xmlbox.find('ymin').text)
        ymax = int(xmlbox.find('ymax').text)
        w = xmax - xmin
        h = ymax - ymin

        cropped = img[ymin:ymax, xmin:xmax]
        if not os.path.isdir("%s/step2_JPEGImages/%s"%(path,cls)):
            os.makedirs("%s/step2_JPEGImages/%s"%(path,cls))
        #if not cls == "JYZ_C_unknown":
        #   continue
        cv2.imwrite("%s/step2_JPEGImages/%s/%s_%06d.jpg"%(path,cls,image_id,new_image_id), cropped)
        train_txt.write(os.path.join(path, 'step2_JPEGImages/%06d.jpg\n'%(new_image_id)))
        out_file = open(os.path.join(path, 'step2_labels/%06d.txt'%(new_image_id)), 'w')
        out_file.write("{} {}\n".format(w, h))
        new_image_id += 1



if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='train')
    argparser.add_argument('-trdata', type=str, default='/media/zkzx/9f8c0111-3713-4aa2-ae7d-fd35f3300098/BKXQS')
    args = argparser.parse_args()
    pwd = os.path.abspath(os.path.dirname(__file__))
    pwd = os.path.abspath(os.path.dirname(pwd))
    train_dir = '%s/train_data'%pwd
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists('%s/step2_JPEGImages'%train_dir):
        os.makedirs('%s/step2_JPEGImages'%train_dir)
    if not os.path.exists('%s/step2_labels'%train_dir):
        os.makedirs('%s/step2_labels'%train_dir)
        
    imgs = []
    #os.removedirs()
    os.symlink('%s/photo'%args.trdata, '%s/JPEGImages'%train_dir)
    os.symlink('%s/xml'%args.trdata, '%s/Annotations'%train_dir)

    with open(os.path.join(train_dir, 'train.txt'), 'w') as f:
        dir_ = '%s/JPEGImages'%train_dir
        img_list = os.listdir(dir_)
        #pbar = tqdm(range(len(img_list)))
        for img in img_list:
            if not img.split('.')[-1] == 'jpg':
                os.rename(os.path.join(dir_, img),os.path.join(dir_, img.split('.')[0] + '.jpg'))
            img=img.split('.')[0] + '.jpg'
            imgs.append(img.split('.')[0])
            f.write(os.path.join(dir_, img)+'\n')
            #pbar.update(1)
    
    f = open(os.path.join(train_dir, 'step2_train.txt'),'w')
    pbar = tqdm(range(len(imgs)))
    for image_id in imgs:
        pbar.update(1)
        crop(image_id,raw_path=train_dir,path=train_dir, train_txt=f)
    f.close()
    

    sys.stdout.write('Process end with exit code 0')
