#*-*coding=utf-8-*

import cv2
import os
import  xml.dom.minidom
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
path ='./photo/'#"./misinformation/"# "./photo/"
xmlpath = './xml/'
savepath = "./bz_img/"#"./draw_only_xml/"
attr_name_list =[]#['GD','LD','GDS','LDS']
if not os.path.isdir(savepath):
    os.makedirs(savepath)
useful_tag = ['JYZ_C_CZ','JYZ_C_BSJYZ_cz','JYZ_YP_QS','JYZ_YP_TK','JYZ_YP_normal','JYZ_C_BL']
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    return cv_img
# cv2.namedWindow("ss")
# cv2.resizeWindow("ss",width=500,height=500)
for roots,dirs,files in os.walk(path):
    print("root is {}".format(roots))
    print("dirs is {}".format(dirs))
    #print(files)
    for file in files:
        #file = file.decode("utf-8").encode("gbk")
        #print(file)
        if file[-3:] == "jpg" or file[-3:] == "JPG" :
            #xmlfile = roots +"_XML/"+ file[0:-3] + "xml"
            xmlfile =xmlpath+ file[0:-3] + "xml"

            if os.path.isfile(roots +"/"+ file):
                img = cv_imread(roots +"/"+ file)  # 打开当前路径图像
                iscontain = False
                print("read image")
                try:
                    dom = xml.dom.minidom.parse(xmlfile)
                    print(roots+"/" + file)
                    root = dom.documentElement
                    labelList = root.getElementsByTagName('object')
                except:
                    continue
                for label in labelList:
                    #str_name = str(label.getElementsByTagName('name')[0].firstChild.data)
                    str_name = str(label.getElementsByTagName('name')[0].firstChild.data)
                    for attr_name in attr_name_list:
                        if len(label.getElementsByTagName(attr_name)) >0:
                            attr_value =str(label.getElementsByTagName(attr_name)[0].firstChild.data)
                            str_name += '_'+ attr_value
                    print(str_name)
                    #if not str_name in useful_tag:
                    #    #iscontain = True
                    #    continue
                    iscontain = True
                    xmin = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('xmin')[0].firstChild.data)
                    ymin = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('ymin')[0].firstChild.data)
                    xmax = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('xmax')[0].firstChild.data)
                    ymax = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('ymax')[0].firstChild.data)
                    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,255),2)
                    print("draw")
                    cv2.putText(img, str_name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),2)
                if iscontain == True:
                    #shutil.copy(path +'/' + file , savepath + '/' + file)
                    #shutil.copy(xmlfile ,savepath + '/' + file[0:-3] +'xml')
                    cv2.imencode(file[-4:], img)[1].tofile(savepath +file)



