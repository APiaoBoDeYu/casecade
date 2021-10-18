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
import cv2,codecs
from tqdm import tqdm
classes = ['ZX_wbj', 'ZX_tl', 'YP_qs', 'YP_tk', 'YP_zc', 'ZX_zc']
region_classes = ['JYZ_czzz','JYZ_fhzs', 'JYZ_blps', 'JYZ_czzs', 'JYZ_chd', 'JYZ_czps']

new_image_id = 0

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

def crop(image_id,detection_dir, raw_path, path, train_txt):
    global new_image_id
    in_file = open('%s/Annotations/%s.xml'%(raw_path,image_id))
    #print('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
    img = cv2.imread('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    #[xmin, xmax, ymin, ymax]
    luosi = []
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        xmlbox = obj.find('bndbox')
        xmin = int(xmlbox.find('xmin').text)
        xmax = int(xmlbox.find('xmax').text)
        ymin = int(xmlbox.find('ymin').text)
        ymax = int(xmlbox.find('ymax').text)
        cls_id = classes.index(cls)
        #print(cls)
        luosi.append([ymin, ymax, xmin, xmax, cls_id])
    #print("luosi is {}!!!!!!!!!".format(len(luosi)))
    region_txt = codecs.open(os.path.join(detection_dir,image_id+'.txt'),'r',encoding='utf-8')
    lines = region_txt.readlines()
    for line in lines:
        line = line.strip()


        xmin = int(line.split(' ')[2])
        xmax = int(line.split(' ')[4])
        ymin = int(line.split(' ')[3])
        ymax = int(line.split(' ')[5])
        w = xmax - xmin
        h = ymax - ymin
        ################add code ######################
        iscontain = False
        for item in luosi:
            if item[0]>=ymin and item[1]<=ymax and item[2]>=xmin and item[3]<=xmax:
                iscontain = True
        if iscontain == False:
            continue
        ################add code ######################
        cropped = img[ymin:ymax, xmin:xmax]
        cv2.imwrite("%s/step2_JPEGImages/%06d.jpg"%(path,new_image_id), cropped)
        train_txt.write(os.path.join(path, 'step2_JPEGImages/%06d.jpg\n'%(new_image_id)))
        out_file = open(os.path.join(path, 'step2_labels/%06d.txt'%(new_image_id)), 'w')
        out_file.write("{} {}\n".format(w, h))
        new_image_id += 1
        for item in luosi:
            if item[0]>=ymin and item[1]<=ymax and item[2]>=xmin and item[3]<=xmax:
                b = (item[2]-xmin, item[3]-xmin, item[0]-ymin, item[1]-ymin)
                out_file.write("{} {} {} {} {}\n".format(item[4],b[0],b[1],b[2],b[3]))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='train')
    argparser.add_argument('-trdata', type=str,
                           default='/media/igi/d49ac859-1afb-45ad-be53-44d8c3ae6489/训练数据/韶关数据/绑扎线')
    args = argparser.parse_args()
    pwd = os.path.abspath(os.path.dirname(__file__))
    pwd = os.path.abspath(os.path.dirname(pwd))
    train_dir = '%s/train_data'%pwd
    print(train_dir)
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists('%s/step2_JPEGImages'%train_dir):
        os.makedirs('%s/step2_JPEGImages'%train_dir)
    if not os.path.exists('%s/step2_labels'%train_dir):
        os.makedirs('%s/step2_labels'%train_dir)
        
    imgs = []
    #os.removedirs()
    if not os.path.exists('%s/JPEGImages'%train_dir):
        os.symlink('%s/photo'%args.trdata, '%s/JPEGImages'%train_dir)
    if not os.path.exists('%s/Annotations'%train_dir):
        #os.makedirs('%s/step2_labels'%train_dir)
        os.symlink('%s/xml' % args.trdata, '%s/Annotations' % train_dir)
    detection_dir = '%s/results' % (args.trdata)
    if not os.path.isdir(detection_dir):
        print("Oh, it is not a dir !")
    else:

        #os.symlink('%s/photo'%args.trdata, '%s/JPEGImages'%train_dir)
        #os.symlink('%s/xml'%args.trdata, '%s/Annotations'%train_dir)

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
            crop(image_id,detection_dir,raw_path=train_dir,path=train_dir, train_txt=f)
        f.close()


        sys.stdout.write('Process end with exit code 0')
