# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-10-10 20:40:22
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-10-10 21:26:46

import argparse
import os
from mmdet.apis import init_detector
from detection_api_ei_canshu import BKXQS_detector
from tqdm import tqdm
import pickle
import sys,cv2
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

    ckpt_step1 = os.path.join(model_path,'model_output/region', 'epoch_29.pth')
    ckpt_step2 = os.path.join(model_path,'model_output/screw', 'epoch_20.pth')
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
            print(file)
            if file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'JPG':
                test_imgs.append(os.path.join(roots, file))
    # test_imgs = os.listdir(test_path)
    #print(test_imgs)
    pbar=tqdm(range(len(test_imgs)))
    pkl_rst = []
    labellist= ['JYZ_C_DTC','JYZ_C_BL','JYZ_C_CZ','JYZ_C_FH',"JYZ_SQZB","JYZ_WDSQZB"]
    colorSelect={'JYZ_C_DTC': (0, 255, 255), 'JYZ_C_BL': (0, 255, 255), 'JYZ_C_CZ': (0, 255, 255), 'JYZ_C_FH': (0, 255, 255),
     "JYZ_SQZB": (0, 0, 255), "JYZ_WDSQZB": (0, 0, 255)}
    basedir = os.path.abspath(os.path.dirname(__file__))
    for img_path in test_imgs:
        pbar.update(1)
        try:

            pbar.update(1)
            #img_path = img#os.path.join(test_path, img)
            rst = BKXQS_detector(model_step1, model_step2, img_path, thres=0.48, min_size=250)
            img = Image.open(img_path)  # cv2.imread(img_path)
            img_Draw = ImageDraw.Draw(img)
            img_font = ImageFont.truetype(os.path.join(basedir, "simhei.ttf"), 30, encoding='utf-8')
            red = (255, 0, 0)  # (0,0,255)
            #with open(os.path.join(rst_path, rst['fname'] + '.txt'), 'w') as f:
            f_text_dir=img_path.replace(img_path.split('/')[-1], '').replace('jpg','txt').replace('photo','results')
            if not os.path.isdir(f_text_dir):
                os.makedirs(f_text_dir)
            with open(img_path.replace('jpg','txt').replace('photo','results'), 'w') as f:
                for (x0, y0, x1, y1, conf,labelnum) in rst['detections']:
                    if conf < 0.76:
                        continue
                    x0 = int(float(x0))
                    y0 = int(float(y0))
                    x1 = int(float(x1))
                    y1 = int(float(y1))
                    f.write('{} {} {} {} {} {}\n'.format(labellist[int(labelnum)],conf, x0, y0, x1, y1))
                    #cv2.rectangle(img,(x0,y0),(x1,y1),(0,0,255),2)
                    #cv2.putText(img,'BKXQS',(x0,y0-30),os.path.join(basedir,"simhei.ttf"),(0,0,255),2)
                    strTxt = labellist[int(labelnum)] + " %s"%conf
                    img_Draw.text((x0, y0 - 30), strTxt, colorSelect[labellist[int(labelnum)]], font=img_font)
                    img_Draw.rectangle((x0, y0, x1, y1), outline=colorSelect[labellist[int(labelnum)]], width=2)
            f.close()
            savedir = img_path.replace(img_path.split('/')[-1], '').replace('photo', 'predicted_jyz_zb')
            savepath = img_path.replace('photo', 'predicted_jyz_zb')
            #print(savepath)
            if not os.path.isdir(savedir):
                os.makedirs(savedir)
            img.save(savepath, quality=95, subsampling=0)
        except Exception as e:
            print("%s is broken %s !!!\n"%(test_path,e))
            continue
        # #img_path = os.path.join(test_path, img)
        # rst = BKXQS_detector(model_step1, model_step2, img, thres=0.48, min_size=250)
        # pkl_rst.append(rst)
        # with open(os.path.join(rst_path, rst['fname']+'.txt'), 'w') as f:
        #     for (x0, y0, x1, y1, conf,labelnum) in rst['detections']:
        #         f.write('{} {} {} {} {} {}\n'.format(labellist[int(labelnum)], conf, int(float(x0)), int(float(y0)),
        #                                              int(float(x1)), int(float(y1))))
        #          #f.write('JYZ_ZW {} {} {} {} {}\n'.format(conf, int(float(x0)), int(float(y0)), int(float(x1)), int(float(y1))))
    with open('test_20191017.pkl', 'wb') as f:
        pickle.dump(pkl_rst , f)

    sys.stdout.write('Process end with exit code 0\n')
