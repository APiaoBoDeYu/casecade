#coding=utf-8
from xml.etree.ElementTree import parse, Element
import os
classname=[]
classnamenum=[]
import shutil
import os.path as osp
folderPath='./train_data/Annotations/'
PIC='./train_data/JPEGImages'
move='./train_data/move'
base='/media/zkzx/9f8c0111-3713-4aa2-ae7d-fd35f3300098/cascade_two_pw_jyzzb/train_data/JPEGImages/'
#save_anno='./train_dataset/save_anno'
#save_pic='./train_dataset/save_pic'
import shutil
no_match_filelist=[]
import xml.dom.minidom
need_list=["JYZ_SQPS","JYZ_SQZB"]
def modifyXMLName(fileName,num,kak):
    #print("Original Filename is :{}".format(fileName))

    ori_xml_file=osp.join(folderPath,fileName.split('.')[0] + '.xml')

    ori_pic_file=osp.join(PIC,fileName)
    # if not os.path.isfile(ori_xml_file):
    #     no_match_filelist.append(fileName)
    if not os.path.isfile(ori_pic_file):
        no_match_filelist.append(fileName)
    try:
        #pbar.update(1)
        #xml_path_abs = os.path.join(roots, file)
        dom = xml.dom.minidom.parse(ori_xml_file)
        root = dom.documentElement
    except:
        print(ori_xml_file)
    contain_s = False

    labellist = root.getElementsByTagName('object')
    # img = cv2.imread(respond_pic)
    for label in labellist:
        strname = str(label.getElementsByTagName('name')[0].firstChild.data)
        if strname in need_list:
            print("!!!!!!!!!")
            contain_s = True


    #
    return contain_s#num,kak



    #shutil.copy(ori_xml_file,mod_xml_file)
    #shutil.copy(ori_pic_file,mod_pic_file)
fileList = os.listdir(PIC)
num = 0
kak = [0,0]
#f= open('./train_data/train.txt','w')
num = 0
for fileName in fileList:
    if fileName.split('.')[-1]=='jpg' or fileName.split('.')[-1]=='JPG':
        #f.write(base + fileName)
        #f.write('\n')
        iscontain = modifyXMLName( fileName,num,kak)
        if iscontain == False:
            ori_xml_file = osp.join(folderPath, fileName.split('.')[0] + '.xml')

            ori_pic_file = osp.join(PIC, fileName)
            shutil.move(ori_xml_file, move + '/xml/' + fileName.split('.')[0] + '.xml')
            shutil.move(ori_pic_file, move + '/photo/' + fileName)
            num+= 1
print(no_match_filelist)
print(num)


