#coding=utf-8
# --------------------------------------------------------
# Written by LeiZhang
# @2020.11
#转换step2需要的文件统计
# --------------------------------------------------------
import math,os,codecs,shutil
path_ori='./step2_labels/'#"./step2_JPEGImages/"
import xml.dom.minidom,codecs
for file in os.listdir(path_ori):
    pic="./step2_JPEGImages/" + file.split('.')[0] + '.jpg'
    if not os.path.isfile(pic):
        shutil.move('./step2_labels/'+file ,'./x/'+file )



