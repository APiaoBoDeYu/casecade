# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-10-10 20:40:22
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-10-10 21:26:46

import argparse
import os
from mmdet.apis import init_detector
from detection_api import BKXQS_detector
from tqdm import tqdm
import pickle
import sys
if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='test phase')
    argparser.add_argument('-m', type=str, default='/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/detection/model_output')
    argparser.add_argument('-t', type=str, default='/media/zkzx/2dc91e84-4382-41e7-9940-a171405bac53/czf/unused/test')
    args = argparser.parse_args() 

    model_path = args.m
    test_path  = os.path.join(args.t, 'photo')
    rst_path =   os.path.join(args.t, 'results')
    #if not os.path.exists(test_path):
        #os.makedirs(test_path)
    if not os.path.exists(rst_path):
        os.makedirs(rst_path)

    ckpt_step1 = os.path.join(model_path,'region', 'epoch_18.pth')
    ckpt_step2 = os.path.join(model_path,'screw', 'epoch_18.pth')
    #ckpt_step1 = os.path.join(model_path, 'step1.pth')
    #ckpt_step2 = os.path.join(model_path, 'step2.pth')
    pwd = os.path.abspath(os.path.dirname(__file__))
    config_step1 = '%s/configs/rcnn_region.py'%pwd
    config_step2 = '%s/configs/rcnn_screw.py'%pwd
    model_step1 = init_detector(config_step1, ckpt_step1, device='cuda:0')
    model_step2 = init_detector(config_step2, ckpt_step2, device='cuda:0')
    test_imgs = []
    for roots, dirs, files in os.walk(test_path):
        for file in files:
            if file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'JPG':
                test_imgs.append(os.path.join(roots, file))
    # test_imgs = os.listdir(test_path)
    pbar=tqdm(range(len(test_imgs)))
    pkl_rst = []
    for img in test_imgs:
        pbar.update(1)
        img_path = os.path.join(test_path, img)
        rst = BKXQS_detector(model_step1, model_step2, img_path, thres=0.48, min_size=750)
        pkl_rst.append(rst)
        with open(os.path.join(rst_path, rst['fname']+'.txt'), 'w') as f:
            for (x0, y0, x1, y1, conf) in rst['detections']:
                 f.write('BKXQS {} {} {} {} {}\n'.format(conf, int(float(x0)), int(float(y0)), int(float(x1)), int(float(y1))))
    with open('test_20191215.pkl', 'wb') as f:
        pickle.dump(pkl_rst , f)

    sys.stdout.write('Process end with exit code 0\n')
