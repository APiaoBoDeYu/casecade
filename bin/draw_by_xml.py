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
xmlpath = '/home/igi/media/yhy/jinjuxiushi/test_dataset/xml/'
savepath = "/home/igi/media/yhy/jinjuxiushi/test_dataset/reigion_class/"#"./draw_only_xml/"

# useful_tag = ['BLQ']
# useful_tag = ['JJXS_yybw', 'XCXJ_BY3', 'XCXJ_BY2', 'NZXJ_yjh', 'XCXJ_XS']
# tag_dir = {7: 'JJXS_yybw', 8: 'XCXJ_BY3', 9: 'XCXJ_BY2', 10: 'NZXJ_yjh', 11: 'XCXJ_XS'}
useful_tag = ['XCXJ_JJC','XCXJ','44_NZXJ_YYX','41_NZXJ','XCXJ_XS']
tag_color={'XCXJ_JJC':(255,0,0),'XCXJ':(0,255,0),'44_NZXJ_YYX':(160,32,240),'41_NZXJ':(255,255,0),'XCXJ_XS':(0,255,255)}
#蓝(255,0,0)，绿（0,255,0),红(0,0,255)，青(255,255,0)
def cv_imread(filePath):
    cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    return cv_img
# cv2.namedWindow("ss")
# cv2.resizeWindow("ss",width=500,height=500)
for roots,dirs,files in os.walk(path):
    print("root is {}".format(roots))
    #print("dirs is {}".format(dirs))
    #print(files)
    file_i=0
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
                NZXJ=[]
                for label in labelList:
                    #str_name = str(label.getElementsByTagName('name')[0].firstChild.data)
                    str_name = str(label.getElementsByTagName('name')[0].firstChild.data)

                    #临时
                    if '44_NZXJ_YYX' ==  str_name:
                        NZXJ.append(str_name)
                    else:
                        continue

                    if not str_name in useful_tag:
                        #iscontain = True
                        continue
                    print(str_name)
                    iscontain = True
                    xmin = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('xmin')[0].firstChild.data)
                    ymin = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('ymin')[0].firstChild.data)
                    xmax = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('xmax')[0].firstChild.data)
                    ymax = int(label.getElementsByTagName('bndbox')[0].getElementsByTagName('ymax')[0].firstChild.data)
                    color=tag_color[str_name]
                    cv2.rectangle(img,(xmin,ymin),(xmax,ymax),color,2)
                    cv2.putText(img, str_name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 2, color, 2)
                    print("draw")
                    #cv2.putText(img, str_name, (xmin, ymin), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255),2)

                # #用以保存特殊图片
                if len(NZXJ):
                    file_i+=1
                    cv2.imencode(file[-4:], img)[1].tofile('/home/igi/media/yhy/jinjuxiushi/test_dataset/change_color/' + file)
                    print(file_i)

                # if iscontain == True:
                #     #shutil.copy(path +'/' + file , savepath + '/' + file)
                #     #shutil.copy(xmlfile ,savepath + '/' + file[0:-3] +'xml')
                #     cv2.imencode(file[-4:], img)[1].tofile(savepath +file)



