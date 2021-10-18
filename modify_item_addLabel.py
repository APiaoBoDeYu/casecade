#coding=utf-8
from xml.etree.ElementTree import parse, Element
import os
classname=[]
classnamenum=[]
import shutil
badlist=[]
path2='./test/xml/'
change_name = {"JYZ_C_BL_BL" :"JYZ_C_BL" ,
"JYZ_WDSQZB":"JYZ_WDSQZB",
"JYZ_C_DTC_DTC" :"JYZ_C_DTC",
"JYZ_SQZB" :"JYZ_SQZB",
"JYZ_C_FH_FH" :"JYZ_C_FH",
"JYZ_C_CZ_CZ" :"JYZ_C_CZ" ,
"JYZ_C_unknown_unknown" :"JYZ_C_unknown" }
def modifyXMLName(folderPath, fileName):
    tree = parse(folderPath+'/'+fileName)
    root=tree.getroot()
    labels=tree.findall('./object')
    index = 0
    for label in tree.findall('./object'):# labels:
        
        name = label.find('name').text
        #if name == 'BLQ':
        #    label.find('name').text='JYZ_C_FH'
        #if name == 'JYZ_C_unknown':
            #print(folderPath+'/'+fileName)
        if not label.find('LX') is None:
            name = name + "_" + label.find('LX').text
        

           #print(name)
        label.find('name').text = name #change_name[name]
        if name in badlist:
            print(index)
            #labels.pop(index)
            root.remove(label)
        index += 1

        if not name in classname:
            classname.append(name)
            classnamenum.append(1)
        else:
            for i in range(len(classname)):
                if name == classname[i]:
                    classnamenum[i] += 1
        # if name in ['JYZ_DHSS_FH', 'JYZ_C_unknown', 'JYZ_GMDHSS_CZ','JYZ_C_DTC',]:
        #     print(path2+'/'+fileName)
    #objects = doc.findall('./object/name')
    #for subObj in objects:
        #subObj.text = className
    tree.write(path2+'/'+fileName, encoding='utf-8')   #此处应保存为Annotations的路径
    


fileList = os.listdir(path2)
for fileName in fileList:
    if not fileName.split('.')[-1]=='xml':
        continue
    modifyXMLName(path2, fileName)
print(classname,classnamenum)
