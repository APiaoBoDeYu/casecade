# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-09-20 22:35:57
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-09-26 22:11:41

import glob
import json
import os
import shutil
import operator
import sys
import argparse
import math
import numpy as np
from collections import defaultdict
from detection_api import bbox_iou_numpy
import pickle
from tqdm import tqdm
MINOVERLAP = 0.5# default value (defined in the PASCAL VOC2012 challenge)

if __name__ == "__main__":
    with open('gt.pkl', 'rb') as f:
        gts = pickle.load(f)
    with open('test_20191215.pkl', 'rb') as f:
        dts = pickle.load(f)
    assert len(dts) == len(gts), 'size not match!'
    dt_num, gt_num, tp_num = 0, 0, 0
    for gt, dt in tqdm(zip(gts, dts)):
        assert gt['fname'] == dt['fname'],  '%s don\'t match %s!'%(gt['fname'], dt['fname'])
        dt_bboxes = dt['detections']
        gt_bboxes = gt['detections']
        if len(gt_bboxes) == 0:
            dt_num += len(dt_bboxes)
            continue
        if len(dt_bboxes) == 0:
            gt_num += len(gt_bboxes)
            continue
        dt_num += len(dt_bboxes)
        gt_num += len(gt_bboxes)
        dt_bboxes = np.array(dt_bboxes)
        gt_bboxes = np.array(gt_bboxes)

        ious = bbox_iou_numpy(gt_bboxes, dt_bboxes)
        for iou in ious:
            if np.any(iou>0.5):
                tp_num += 1
    print("tp:{} gt:{} dt:{}\n".format(tp_num, gt_num, dt_num))
    print("recall: {} | prec: {}\n".format(1.0*tp_num/gt_num, 1.0*tp_num/dt_num))

