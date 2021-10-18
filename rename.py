#coding=utf-8
from xml.etree.ElementTree import parse, Element
import os
classname=[]
classnamenum=[]
import shutil
import os.path as osp
folderPath='./test/xml/'
PIC='./test/photo'

no_match_filelist=[]
def modifyXMLName(fileName,num):
    #print("Original Filename is :{}".format(fileName))
    ori_xml_file=osp.join(folderPath,fileName.split('.')[0] + '.xml')
    mod_xml_file=osp.join(folderPath,str(num)+'.xml')
    ori_pic_file=osp.join(PIC,fileName)
    if not os.path.isfile(ori_pic_file):
        no_match_filelist.append(fileName)
    mod_pic_file=osp.join(PIC,str(num)+ '.jpg')
    #if not os.path.isfile(ori_xml_file):
        #no_match_filelist.append(fileName)
    os.renames(ori_xml_file,mod_xml_file)
    os.renames(ori_pic_file,mod_pic_file)
    #shutil.copy(ori_xml_file,mod_xml_file)
    #shutil.copy(ori_pic_file,mod_pic_file)
fileList = os.listdir(PIC)
num =0
for fileName in fileList:
    if fileName.split('.')[-1]=='jpg' or fileName.split('.')[-1]=='JPG':

        modifyXMLName( fileName,num)
        num+= 1
print(classname,classnamenum)
print('no match pic{}'.format(len(no_match_filelist)))

