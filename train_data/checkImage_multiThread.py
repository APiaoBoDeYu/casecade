import os
import shutil
from random import shuffle
import cv2
import xml.dom.minidom
from tqdm import tqdm
path = './photo/'
xmlPath = './xml/'
import time
from queue import Queue
#movePath = '/home/zy/Desktop/nc_fzc_zsj_wrj/data/dwv_ori/20190410/'
# jpgList = []
# pbar=tqdm(range(len(os.listdir(path))))
filelist = os.listdir(path)
Q = Queue(maxsize=len(filelist))
for file in filelist:
    Q.put(os.path.join(path, file))
pbar = tqdm(range(len(os.listdir(path))))
from threading import Thread
def check_image():

    while True:
        if Q.qsize() == 0:
            break
        try:
            file = Q.get()
            img = cv2.imread(file)
            o_h = img.shape[0]
            pbar.update(1)
            # if img.shape[0] <1500 or img.shape[1] <2000:
            # print(file)
            if img is None:
                print(file_path)
            dom = xml.dom.minidom.parse(xmlPath + file.split('/')[-1].split('.')[0] + '.xml')
            root = dom.documentElement
            # labellist = root.getElementsByTagName('object')
            # width = int(root.getElementsByTagName('width')[0].firstChild.data)
            height = int(root.getElementsByTagName('height')[0].firstChild.data)
            assert o_h <= height
        except:
            print("image is broken {} ".format(path + file))

if __name__=="__main__":



    for i in range(30):
        thread1 = Thread(target=check_image, args=())
        thread1.daemon = True
        thread1.start()
    while True:
        if Q.qsize() == 0:
            break
        time.sleep(1)
        #thread1.join()
    # for i in range(len(filelist)):
    #     # file1 = filelist[i]
    #     # file2 = filelist[i+1]
    #     # file3 = filelist[i+2]
    #     # file4 = filelist[i+3]
    #     # file5 = filelist[i+4]
    #     if file.__contains__("jpg") or file.__contains__("JPG"):
    #         thread1 = Thread(target=check_image, args=(path,file))
    #         thread1.daemon = True
    #         pbar.update(1)
    #         thread2 = Thread(target=check_image, args=(path,file))
    #         thread2.daemon = True
    #         pbar.update(1)
    #         thread3 = Thread(target=check_image, args=(path,file))
    #         thread3.daemon = True
    #         pbar.update(1)
    #         thread4 = Thread(target=check_image, args=(path,file))
    #         thread4.daemon = True
    #         pbar.update(1)
    #         thread5 = Thread(target=check_image, args=(path,file))
    #         thread5.daemon = True
    #         pbar.update(1)
    #         thread1.start()
    #         #thread1.join()
    #         thread2.start()
    #         #thread2.join()
    #         thread3.start()
    #         #thread3.join()
    #         thread4.start()
    #         #thread4.join()
    #         thread5.start()
    #         #thread5.join()


            #if not os.path.isfile(path + "train_xml/" + file[0:-3]+ "xml"):
                #print(file)

            #img = cv2.imread(path +"train/"+ file )
            #print(img.shape)
            # if not float(img.shape[0])/float(img.shape[1]) == 0.75:
            #     print(file)
            #     shutil.move(path +"train/"+ file,path +"move/"+ file)
            #     shutil.move(path + "train_xml/" + file[0:-3]+ "xml", path + "move/" + file[0:-3]+ "xml")
            #jpgList.append(file)
    # print(jpgList)
    # jpglist2 = shuffle(jpgList)
    # print(jpgList)
    # for i in range(0,len(jpgList)):
    #     if not i%9==0:
    #         shutil.copy(path + "JPEGImages/" + jpgList[i],path + "train/" + jpgList[i])
    #         shutil.copy(path + "Annotations/" + jpgList[i][0:-3] + "xml",path + "train_xml/" + jpgList[i][0:-3]+ "xml")
    #     else:
    #         shutil.copy(path + "JPEGImages/" + jpgList[i],path + "test/" + jpgList[i])
    #         shutil.copy(path + "Annotations/" + jpgList[i][0:-3] + "xml",path + "test_xml/" + jpgList[i][0:-3]+ "xml")
