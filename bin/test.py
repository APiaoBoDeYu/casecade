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
    argparser.add_argument('-m', type=str, default='/home/igi/media/yhy/casecade/model_output')
    argparser.add_argument('-t', type=str, default='/home/igi/media/yhy/jinjuxiushi/test_dataset')
    args = argparser.parse_args() 

    model_path = args.m
    test_path  = os.path.join(args.t, 'photo')#photo 路径
    rst_path =   os.path.join(args.t, 'results')

    # if test_step == '1':
    #     useful_tag=['JJXS_yybw','XCXJ_BY3','XCXJ_BY2','NZXJ_yjh','XCXJ_XS']
    #     tag_dir={7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}
    # else:
    #     useful_tag = ['XCXJ_JJC', '44_NZXJ_YYX', '41_NZXJ']
    #     tag_dir={7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}
    useful_tag=['JJXS_yybw','XCXJ_BY3','XCXJ_BY2','NZXJ_yjh','XCXJ_XS']
    tag_dir={0:'XCXJ_JJC', 1:'44_NZXJ_YYX', 2:'41_NZXJ',7:'JJXS_yybw',8:'XCXJ_BY3',9:'XCXJ_BY2',10:'NZXJ_yjh',11:'XCXJ_XS'}

    #if not os.path.exists(test_path):
        #os.makedirs(test_path)
    # if not os.path.exists(rst_path):
    #     os.makedirs(rst_path)

    ckpt_step1 = os.path.join(model_path,'region', 'epoch_50.pth')
    ckpt_step2 = os.path.join(model_path,'screw', 'epoch_50.pth')
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
        rst = BKXQS_detector(model_step1, model_step2, img_path, thres=0.48, min_size=250)
        pkl_rst.append(rst)
        with open(os.path.join(rst_path, rst['fname']+'.txt'), 'w') as f:
            for (x0, y0, x1, y1, conf,cla) in rst['detections']:
                # print('{} {} {} {} {} {}\n'.format(tag_dir[int(cla)],conf, int(float(x0)), int(float(y0)), int(float(x1)), int(float(y1))))
                f.write('{} {} {} {} {} {}\n'.format(tag_dir[int(cla)],conf, int(float(x0)), int(float(y0)), int(float(x1)), int(float(y1))))
    with open('test_20210812.pkl', 'wb') as f:
        pickle.dump(pkl_rst , f)

    sys.stdout.write('Process end with exit code 0\n')
