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


def BKXQS_detector(model_step1, model_step2, imgPath, thres=0.48, min_size=250):
    img = cv2.imread(imgPath)
    fname = os.path.basename(imgPath).split('.')[0]

    step1_rst_list = inference_detector(model_step1, img)
    final_rst = []
    #num =0
    height,width,_=img.shape
    for i in range(len(step1_rst_list)):
        step1_rst = step1_rst_list[i]
        # if i == 3:
        #     continue
        for k, det in enumerate(step1_rst):
            x1, y1, x2, y2, conf = det
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = y2 - y1, x2 - x1

            if  x1 >= x2 or y1 >= y2 or float(conf)<0.3:#x1 >= x2 or y1 >= y2 :
                continue
            tmp_region = []
            tmp_region.append(x1)
            tmp_region.append(y1)
            tmp_region.append(x2)
            tmp_region.append(y2)
            tmp_region.append(conf)
            tmp_region.append(i)
            if i == 3:
                continue
            final_rst.append(tmp_region)
            stretch_length =
            region = img[max(0,y1-20):min(height,y2+20), max(0,x1-20):min(width,x2+20)]
            cv2.imwrite('.%s.jpg' % (fname), region)
            tmp_file = '.%s.jpg' % (fname)
            offset_x, offset_y = x1, y1
            step2_rst_list = inference_detector(model_step2, tmp_file)
            os.remove(tmp_file)
            for  j in range(len(step2_rst_list)):
                # if i >3:
                #     continue
                step2_rst= np.array(step2_rst_list[j])
                step2_rst[:, 0] = step2_rst[:, 0] + offset_x
                step2_rst[:, 1] = step2_rst[:, 1] + offset_y
                step2_rst[:, 2] = step2_rst[:, 2] + offset_x
                step2_rst[:, 3] = step2_rst[:, 3] + offset_y
                for rst in step2_rst:

                    if rst[4] > thres and (rst[3] - rst[1]) * (rst[2] - rst[0]) > min_size:
                        #rst.append(i)
                        tmp =[]
                        for element in rst:
                            tmp.append(element)
                        tmp.append(j+4)
                        #final_rst.append(rst)
                        final_rst.append(tmp)
            # step2_rst = np.array(step2_rst_list[0])
            # os.remove(tmp_file)
            # step2_rst[:, 0] = step2_rst[:, 0] + offset_x
            # step2_rst[:, 1] = step2_rst[:, 1] + offset_y
            # step2_rst[:, 2] = step2_rst[:, 2] + offset_x
            # step2_rst[:, 3] = step2_rst[:, 3] + offset_y
            # for rst in step2_rst:
            #     if rst[4] > thres and (rst[3] - rst[1]) * (rst[2] - rst[0]) > min_size:
            #         final_rst.append(rst)
            # step2_rst2 = np.array(step2_rst_list[1])
            #
            # step2_rst2[:, 0] = step2_rst2[:, 0] + offset_x
            # step2_rst2[:, 1] = step2_rst2[:, 1] + offset_y
            # step2_rst2[:, 2] = step2_rst2[:, 2] + offset_x
            # step2_rst2[:, 3] = step2_rst2[:, 3] + offset_y
            # for rst in step2_rst2:
            #     if rst[4] > thres and (rst[3] - rst[1]) * (rst[2] - rst[0]) > min_size:
            #         final_rst.append(rst)
        #num += 1


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
