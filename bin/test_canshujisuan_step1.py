# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-10-10 20:40:22
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-10-10 21:26:46

import argparse
import os
from mmdet.apis import init_detector
from detection_api_ei_canshu_step1 import BKXQS_detector
from tqdm import tqdm
import pickle
import sys
from PIL import Image,ImageFont,ImageDraw
if __name__ == "__main__":
    os.environ['CUDA_VISIBLE_DEVICES']='0'
    argparser = argparse.ArgumentParser(description='test phase')
    argparser.add_argument('-m', type=str, default='/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/model_output')
    argparser.add_argument('-t', type=str, default='/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection')
    args = argparser.parse_args()

    model_path = args.m
    test_path  = os.path.join(args.t, 'photo')
    rst_path =   os.path.join(args.t, 'results')
    #if not os.path.exists(test_path):
        #os.makedirs(test_path)
    if not os.path.exists(rst_path):
        os.makedirs(rst_path)

    ckpt_step1 = os.path.join(model_path,'model_output/region', 'epoch_35.pth')

    pwd = os.path.abspath(os.path.dirname(__file__))
    config_step1 = '%s/configs/rcnn_region.py'%pwd
    config_step2 = '%s/configs/rcnn_screw.py'%pwd
    model_step1 = init_detector(config_step1, ckpt_step1, device='cuda:0')

    test_imgs = []
    for roots, dirs, files in os.walk(test_path):
        for file in files:
            print(file)
            if file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'JPG':
                test_imgs.append(os.path.join(roots, file))

    pbar=tqdm(range(len(test_imgs)))
    pkl_rst = []
    labellist=['JYZ_czzz','JYZ_fhzs', 'JYZ_blps', 'JYZ_czzs', 'JYZ_chd', 'JYZ_czps']
    basedir = os.path.abspath(os.path.dirname(__file__))
    for img in test_imgs:
        pbar.update(1)
        #try:

        pbar.update(1)
        img_path = img#os.path.join(test_path, img)
        rst = BKXQS_detector(model_step1, img, thres=0.48, min_size=250)
        img = Image.open(img_path)  # cv2.imread(img_path)
        img_Draw = ImageDraw.Draw(img)
        img_font = ImageFont.truetype(os.path.join(basedir, "simhei.ttf"), 30, encoding='utf-8')
        red = (255, 0, 0)  # (0,0,255)
        with open(os.path.join(rst_path, rst['fname'] + '.txt'), 'w') as f:
            for (index,conf,x0, y0, x1, y1) in rst['detections']:
                if conf < 0.1:
                    continue
                x0 = int(float(x0))
                y0 = int(float(y0))
                x1 = int(float(x1))
                y1 = int(float(y1))
                f.write('{} {} {} {} {} {}\n'.format(labellist[int(index)],conf, x0, y0, x1, y1))
                # cv2.rectangle(img,(x0,y0),(x1,y1),(0,0,255),2)
                # cv2.putText(img,'BKXQS',(x0,y0-30),os.path.join(basedir,"simhei.ttf"),(0,0,255),2)
                #img_Draw.text((x0, y0 - 30), labellist[int(labelnum)], red, font=img_font)
                #img_Draw.rectangle((x0, y0, x1, y1), outline=red, width=2)
        f.close()

    sys.stdout.write('Process end with exit code 0\n')
