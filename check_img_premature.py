#coding=utf-8

import os
from skimage import io
from PIL import Image
from tqdm import tqdm
import shutil
def is_valid(img):
    bValid = True
    with open(img,'rb') as f:
        #standardstr = f.seek(-2,2)
        try:

            buf = f.read()
            if not buf.startswith(b"\xff\xd8"):
                bValid =False
                print('{} is not start with \xff\xd8'.format(img))
            elif buf[6:10] in (b'JFIF',b'Exif'):
                if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                    bValid = False
                    print('{} is not end with \xff\xd9'.format(img))
            else:
                try:
                    Image.open(img).verify()
                except Exception as e:
                    bValid =False
                    print('{} is not correct'.format(img))
                    print(e)

        except Exception as e:
            print(e)
            print('{} is not correct2'.format(img))
    #if  bValid==False:
        #print(img)
        #shutil.move(img,'./premature_pic/'+img.split('/')[-1])
        #if not f.read()=='\xff\xd9':
            #print(img)
    #try:
    #    io.imread(img)
    #except Exception as e:
    #    print(e)
    #    print(img)
    #try:
        #Image.open(img).load()
    #except Exception as e:
        #print(e)
        #print(img)


path='./train_data/JPEGImages'#'./JPEGImages'#'./premature_pic'#'./JPEGImages'
filelist=os.listdir(path)
pbar=tqdm(range(len(filelist)))
for file in filelist:
    pbar.update(1)
    picPath=os.path.join(path,file)
    is_valid(picPath)
    #shutil.move('./Annotations/' + file.split('.')[0] + '.xml', './premature_pic/' + file.split('.')[0] + '.xml')
    
