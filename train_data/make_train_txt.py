#coding=utf-8
# --------------------------------------------------------
# Written by LeiZhang
# @2020.11
#转换step2需要的文件统计
# --------------------------------------------------------
import math,os,codecs
path_ori="./step2_JPEGImages/"
f=codecs.open('./step2_train.txt','w',encoding='utf-8')
import xml.dom.minidom,codecs
for file in os.listdir(path_ori):
    f.write("/home/igi/LeiZHang/cascade_jyz_sg/train_data/step2_JPEGImages/%s\n"%(file))
f.close()


