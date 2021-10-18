#*-*coding=utf-8-*

import cv2
import os
import  xml.dom.minidom
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
path ='/home/igi/media/yhy/jinjuxiushi/test_dataset/misinformation/'#"./misinformation/"# "./photo/"
resultpath = '/home/igi/media/yhy/jinjuxiushi/test_dataset/results/'
savepath = "/home/igi/media/yhy/jinjuxiushi/test_dataset/misinformation/"#"./draw_only_xml/"
if not os.path.isdir(savepath):
    os.makedirs(savepath)
# useful_tag = ['BLQ']
useful_tag = ['JJXS_yybw', 'XCXJ_BY3', 'XCXJ_BY2', 'NZXJ_yjh', 'XCXJ_XS']
tag_dir = {7: 'JJXS_yybw', 8: 'XCXJ_BY3', 9: 'XCXJ_BY2', 10: 'NZXJ_yjh', 11: 'XCXJ_XS'}
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    return cv_img
# cv2.namedWindow("ss")
# cv2.resizeWindow("ss",width=500,height=500)
for roots,dirs,files in os.walk(path):
    print("root is {}".format(roots))
    #print("dirs is {}".format(dirs))
    #print(files)
    for file in files:
        #file = file.decode("utf-8").encode("gbk")
        #print(file)
        if file[-3:] == "jpg" or file[-3:] == "JPG" :
            #xmlfile = roots +"_XML/"+ file[0:-3] + "xml"
            xmlfile =resultpath+ file[0:-3] + "txt"

            if os.path.isfile(roots +"/"+ file):
                img = cv_imread(roots +"/"+ file)  # 打开当前路径图像
                iscontain = True
                print("read image")
                labellist=open(xmlfile).readlines()
                for label in labellist:
                    elememts =label.strip().split(' ')
                    #str_name = str(label.getElementsByTagName('name')[0].firstChild.data)
                    str_name = elememts[0] + ' ' + elememts[1]
                    if float(elememts[2]) < 0.7:
                        continue

                    # tag_dir[int(elememts[1])]
                    if not elememts[0] in useful_tag:
                        #iscontain = True
                        continue
                    print(str_name)
                    xmin = int(elememts[2])
                    ymin = int(elememts[3])
                    xmax = int(elememts[4])
                    ymax = int(elememts[5])
                    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),2)
                    print("draw")
                    cv2.putText(img, str_name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),2)
                if iscontain == True:
                    #shutil.copy(path +'/' + file , savepath + '/' + file)
                    #shutil.copy(xmlfile ,savepath + '/' + file[0:-3] +'xml')
                    cv2.imencode(file[-4:], img)[1].tofile(savepath +file)



