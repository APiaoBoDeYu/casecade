from mmdet.apis import init_detector, inference_detector
import numpy as np
import cv2
import os
import shutil


def bbox_iou_numpy(box1, box2):
    area = (box2[:, 2] - box2[:, 0]) * (box2[:, 3] - box2[:, 1])
    iw = np.minimum(np.expand_dims(box1[:, 2], axis=1), box2[:, 2]) - np.maximum(np.expand_dims(box1[:, 0], 1),
                                                                                 box2[:, 0])
    ih = np.minimum(np.expand_dims(box1[:, 3], axis=1), box2[:, 3]) - np.maximum(np.expand_dims(box1[:, 1], 1),
                                                                                 box2[:, 1])

    iw = np.maximum(iw, 0)
    ih = np.maximum(ih, 0)

    ua = np.expand_dims((box1[:, 2] - box1[:, 0]) * (box1[:, 3] - box1[:, 1]), axis=1) + area - iw * ih
    ua = np.maximum(ua, np.finfo(float).eps)

    intersection = iw * ih
    return intersection / ua


def BKXQS_detector(model_step1,  imgPath, thres=0.48, min_size=250):
    img = cv2.imread(imgPath)
    fname = os.path.basename(imgPath).split('.')[0]

    step1_rst_list = inference_detector(model_step1, img)
    final_rst = []
    #num =0
    for i in range(len(step1_rst_list)):
        step1_rst = step1_rst_list[i]
        # if i == 3:
        #     continue
        for k, det in enumerate(step1_rst):
            x1, y1, x2, y2, conf = det
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = y2 - y1, x2 - x1

            if  x1 >= x2 or y1 >= y2 or float(conf)<0.1:#x1 >= x2 or y1 >= y2 :
                continue
            if conf > thres and (y2 - y1) * (x2 - x1) > min_size:
                #final_rst.append(rst)
                tmp=[]
                tmp.append(i)
                tmp.append(conf)
                tmp.append(x1)
                tmp.append(y1)
                tmp.append(x2)
                tmp.append(y2)
                final_rst.append(tmp)
    locations = np.array(final_rst)
    if locations.shape[0] == 0:
        return {'fname': fname, 'detections': []}

    # postpreprocess
    indices = np.argsort(-locations[:, -1])
    sorted_loc = locations[indices]
    loc = sorted_loc[0][np.newaxis, :]
    for bnd in sorted_loc[1:]:
        bbox2 = bnd[np.newaxis, :4]
        # print(loc)
        bbox1 = loc[:, :4]
        ious = bbox_iou_numpy(bbox1, bbox2)
        if not np.any(ious > 0.5):
            loc = np.concatenate((loc, bnd[np.newaxis, :]), axis=0)

    loc = loc.tolist()
    return {'fname': fname, 'detections': loc}
