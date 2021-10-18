# coding=utf-8
# --------------------------------------------------------
# Written by LeiZhang
# @2020.11
# 预处理step1和step2数据
# --------------------------------------------------------
import xml.etree.ElementTree as ET
import os, xml.dom.minidom
import argparse
import sys
import cv2
from tqdm import tqdm

classes =['ZX_wbj', 'ZX_tl', 'YP_qs', 'YP_tk', 'YP_zc', 'ZX_zc']
region_classes = ["JYZ_czzs", "JYZ_fhzs", "JYZ_chd", "JYZ_czzz", "JYZ_blps", "JYZ_czps"]

new_image_id = 0


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def crop(image_id, raw_path, path, train_txt):
    global new_image_id
    in_file = '%s/Annotations/%s.xml' % (raw_path, image_id)
    # print('%s/JPEGImages/%s.jpg'%(raw_path, image_id))
    img = cv2.imread('%s/JPEGImages/%s.jpg' % (raw_path, image_id))

    try:
        dom = xml.dom.minidom.parse(in_file)
        root = dom.documentElement
    except Exception as e:
        print("%s : %s" % (in_file, e))
        # print(roots + '/' + file)
    # tree = ET.parse(in_file)
    # root = tree.getroot()
    # size = root.find('size')
    # [xmin, xmax, ymin, ymax]
    luosi = []
    for label in root.getElementsByTagName('object'):
        cls = str(label.getElementsByTagName('name')[0].firstChild.data)
        if cls not in classes:
            continue
        # xmlbox = obj.find('bndbox')
        xmin = int(label.getElementsByTagName('xmin')[0].firstChild.data)
        xmax = int(label.getElementsByTagName('xmax')[0].firstChild.data)
        ymin = int(label.getElementsByTagName('ymin')[0].firstChild.data)
        ymax = int(label.getElementsByTagName('ymax')[0].firstChild.data)
        cls_id = classes.index(cls)
        #luosi.append([ymin, ymax, xmin, xmax, cls_id])
        interal = 50
        cropped = img[ymin-interal:ymax+interal, xmin-interal:xmax+interal]
        w = ymax+interal -(ymin-interal)
        h = xmax+interal - (xmin-interal)
        cv2.imwrite("%s/step2_JPEGImages/%06d.jpg" % (path, new_image_id), cropped)
        train_txt.write(os.path.join(path, 'step2_JPEGImages/%06d.jpg\n' % (new_image_id)))
        out_file = open(os.path.join(path, 'step2_labels/%06d.txt' % (new_image_id)), 'w')
        out_file.write("{} {}\n".format(w, h))
        new_image_id += 1
        b = (interal, w -60 +interal, interal, h -60  + interal)
        if b[1] - b[0] > 10 or b[3] - b[2] > 10:
            # out_file.write("{} {} {} {} {}\n".format(item[4],b[0],b[1],b[2],b[3]))
            out_file.write("{} {} {} {} {}\n".format(cls_id , b[0], b[1], b[2], b[3]))
        # print(cls)
        #luosi.append([ymin, ymax, xmin, xmax, cls_id])

    # for label in root.getElementsByTagName('object'):
    #     cls = str(label.getElementsByTagName('name')[0].firstChild.data)
    #     if cls not in region_classes:
    #         continue
    #     # xmlbox = obj.find('bndbox')
    #     xmin = int(label.getElementsByTagName('xmin')[0].firstChild.data)
    #     xmax = int(label.getElementsByTagName('xmax')[0].firstChild.data)
    #     ymin = int(label.getElementsByTagName('ymin')[0].firstChild.data)
    #     ymax = int(label.getElementsByTagName('ymax')[0].firstChild.data)
    #     w = xmax - xmin
    #     h = ymax - ymin
    #     ################add code ######################
    #     iscontain = False
    #     for item in luosi:
    #         if item[0] >= ymin and item[1] <= ymax and item[2] >= xmin and item[3] <= xmax:
    #             iscontain = True
    #     if iscontain == False:
    #         continue
    #     ################add code ######################
    #     cropped = img[ymin:ymax, xmin:xmax]
    #     cv2.imwrite("%s/step2_JPEGImages/%06d.jpg" % (path, new_image_id), cropped)
    #     train_txt.write(os.path.join(path, 'step2_JPEGImages/%06d.jpg\n' % (new_image_id)))
    #     out_file = open(os.path.join(path, 'step2_labels/%06d.txt' % (new_image_id)), 'w')
    #     out_file.write("{} {}\n".format(w, h))
    #     new_image_id += 1
    #     for item in luosi:
    #         if item[0] >= ymin and item[1] <= ymax and item[2] >= xmin and item[3] <= xmax:
    #             b = (item[2] - xmin, item[3] - xmin, item[0] - ymin, item[1] - ymin)
    #             if b[1] - b[0] > 10 or b[3] - b[2] > 10:
    #                 # out_file.write("{} {} {} {} {}\n".format(item[4],b[0],b[1],b[2],b[3]))
    #                 out_file.write("{} {} {} {} {}\n".format(cls + "_dhss", b[0], b[1], b[2], b[3]))



if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description='train')
    argparser.add_argument('-trdata', type=str, default='./')
    args = argparser.parse_args()
    pwd = os.path.abspath(os.path.dirname(__file__))
    pwd = os.path.abspath(os.path.dirname(pwd))
    train_dir = args.trdata  # '%s/train_data'%pwd
    # if not os.path.exists(train_dir):
    #     os.makedirs(train_dir)
    if not os.path.exists('%s/step2_JPEGImages'%train_dir):
        os.makedirs('%s/step2_JPEGImages'%train_dir)
    if not os.path.exists('%s/step2_labels'%train_dir):
        os.makedirs('%s/step2_labels'%train_dir)

    imgs = []
    # os.removedirs()
    # os.symlink('%s/photo'%args.trdata, '%s/JPEGImages'%train_dir)
    # os.symlink('%s/xml'%args.trdata, '%s/Annotations'%train_dir)

    with open(os.path.join(train_dir, 'train.txt'), 'w') as f:
        dir_ = '%s/JPEGImages' % train_dir
        img_list = os.listdir(dir_)
        # pbar = tqdm(range(len(img_list)))
        for img in img_list:
            if not img.split('.')[-1] == 'jpg':
                os.rename(os.path.join(dir_, img), os.path.join(dir_, img.split('.')[0] + '.jpg'))
            img = img.split('.')[0] + '.jpg'
            imgs.append(img.split('.')[0])
            f.write(os.path.join(dir_, img) + '\n')
            # pbar.update(1)

    f = open(os.path.join(train_dir, 'step2_train.txt'), 'w')
    pbar = tqdm(range(len(imgs)))
    for image_id in imgs:
        pbar.update(1)
        crop(image_id, raw_path=train_dir, path=train_dir, train_txt=f)
    f.close()

    sys.stdout.write('Process end with exit code 0')
