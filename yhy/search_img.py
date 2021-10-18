import xml.etree.ElementTree as ET
import os
import argparse
import sys
from tqdm import tqdm
import cv2
from tqdm import tqdm
import numpy as np

#循环打开文件读取文件名
#处理文件名
#cp到指定目录
import shutil
if __name__ == "__main__":
    train_dir='../model_output/XCXJ_XS/'
    all_dir='../train_data/'
    XS_types=['red','black','rough_red','rough_black']


    for XS_type in XS_types:
        imgs=[]
        with open(os.path.join(train_dir, '%s.txt'%XS_type), 'w',encoding='utf-8') as f:
            dir_= os.listdir(train_dir+XS_type)
            for img_name in dir_:
                img_name_o= img_name.split('.')[0][:-2]+'.jpg'
                imgs.append(img_name_o)
                f.write(os.path.join(train_dir,XS_type+img_name_o)+'\n')
                # f.write(train_dir + XS_type + '/' + img_name_o)
                shutil.copy(os.path.join(all_dir + 'JPEGImages/', img_name_o), os.path.join(train_dir, XS_type))
            f.close()
            imgs=list(set(imgs))
            #拷贝图片
            # for img in imgs:
            #     shutil.copyfile(os.path.join(all_dir+'JPEGImages/',img_name_o),os.path.join(train_dir,XS_type))


#
# with open(os.path.join(train_dir, 'train.txt'), 'w') as f:
#     dir_ = '%s/JPEGImages' % train_dir
#     img_list = os.listdir(dir_)
#     # pbar = tqdm(range(len(img_list)))
#     for img in img_list:
#         if not img.split('.')[-1] == 'jpg':
#             os.rename(os.path.join(dir_, img), os.path.join(dir_, img.split('.')[0] + '.jpg'))
#         img = img.split('.')[0] + '.jpg'
#         imgs.append(img.split('.')[0])
#         f.write(os.path.join(dir_, img) + '\n')
#
#     f = open(os.path.join(train_dir, 'step2_train.txt'), 'w')
#     pbar = tqdm(range(len(imgs)))
#     for image_id in imgs:
#         pbar.update(1)
#         crop(image_id, raw_path=train_dir, path=train_dir, train_txt=f)
#     f.close()
#
#     sys.stdout.write('Process end with exit code 0')