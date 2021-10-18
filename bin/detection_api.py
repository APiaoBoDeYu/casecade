from mmdet.apis import init_detector, inference_detector
import numpy as np
import cv2
import os 
import shutil
def bbox_iou_numpy(box1, box2):
    area = (box2[:,2] - box2[:,0]) * (box2[:,3] - box2[:,1])
    iw = np.minimum(np.expand_dims(box1[:,2],axis=1), box2[:,2]) - np.maximum(np.expand_dims(box1[:,0], 1), box2[:,0])
    ih = np.minimum(np.expand_dims(box1[:,3],axis=1), box2[:,3]) - np.maximum(np.expand_dims(box1[:,1], 1), box2[:,1])

    iw = np.maximum(iw, 0)
    ih = np.maximum(ih, 0)

    ua = np.expand_dims((box1[:,2] - box1[:,0]) * (box1[:,3] - box1[:, 1]), axis=1) + area - iw * ih
    ua = np.maximum(ua, np.finfo(float).eps)

    intersection = iw * ih
    return intersection / ua

    
def BKXQS_detector(model_step1, model_step2, imgPath, thres=0.48, min_size=250):
    
    img = cv2.imread(imgPath)
    fname = os.path.basename(imgPath).split('.')[0]
    step1_rst_list = inference_detector(model_step1, img)
    final_rst = []
    print("大区域有%s种类型"%len(step1_rst_list))
    for i in range(len(step1_rst_list)):
        step1_rst=step1_rst_list[i]
        if len(step1_rst)<1:
            continue
        #遍历一个类型的所有结果
        for k, det in enumerate(step1_rst):
            x1, y1, x2, y2, conf = det
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = y2 - y1, x2 - x1

            if x1>=x2 or y1>=y2:
                continue
            #将第一步检测的结果也加进去
            if det[4] > thres and (det[3] - det[1]) * (det[2] - det[0]) > min_size:
                tmp = []
                for element in det:
                    tmp.append(element)
                tmp.append(i)
                final_rst.append(tmp)

            region = img[y1:y2, x1:x2]
            cv2.imwrite('../test_data/%s_%s.jpg'%(fname,k), region)
            # print(os.path.abspath(os.path.dirname(__file__)))
            tmp_file = '../test_data/%s_%s.jpg'%(fname,k)
            offset_x, offset_y = x1, y1
            step2_rst_list = inference_detector(model_step2, tmp_file)  #每张图都返回一个list，5个元祖，但是有很多空的
            os.remove(tmp_file)
            for j in range(len(step2_rst_list)):
                step2_rst=np.array(step2_rst_list[j])
                if len(step2_rst)<1:
                    continue
                step2_rst[:,0] = step2_rst[:,0] + offset_x
                step2_rst[:,1] = step2_rst[:,1] + offset_y
                step2_rst[:,2] = step2_rst[:,2] + offset_x
                step2_rst[:,3] = step2_rst[:,3] + offset_y
                for rst in step2_rst:
                    if rst[4] > thres and (rst[3]-rst[1])*(rst[2]-rst[0]) > min_size:
                        tmp = []
                        for element in rst:
                            tmp.append(element)
                        tmp.append(j + 7)
                        final_rst.append(tmp)

    locations = np.array(final_rst)
    if locations.shape[0] == 0:
        return {'fname':fname, 'detections':[]}

    # postpreprocess
    indices = np.argsort(-locations[:,-1])
    sorted_loc = locations[indices]
    loc = sorted_loc[0][np.newaxis,:]
    for bnd in sorted_loc[1:]:
        bbox2 = bnd[np.newaxis, :4]
        #print(loc)
        bbox1 = loc[:, :4]
        ious = bbox_iou_numpy(bbox1, bbox2)
        if not np.any(ious>0.5):
            loc = np.concatenate((loc, bnd[np.newaxis, :]), axis=0)

    loc = loc.tolist()
    return {'fname':fname, 'detections':loc}

def BKXQS_detector_step2(model_step2, imgPath, thres=0.48, min_size=250):
    #读取小图片，并预测
    fname = os.path.basename(imgPath).split('.')[0]
    step2_rst_list = inference_detector(model_step2, imgPath)





    #处理检测结果
    final_rst = []
    for j in range(len(step2_rst_list)):
        step2_rst = np.array(step2_rst_list[j])
        if len(step2_rst) < 1:
            continue
        for rst in step2_rst:
            if rst[4] > thres and (rst[3] - rst[1]) * (rst[2] - rst[0]) > min_size:
                tmp = []
                for element in rst:
                    tmp.append(element)
                tmp.append(j)
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
    #
    #
    # img = cv2.imread(imgPath)
    # fname = os.path.basename(imgPath).split('.')[0]
    # #第一步检测
    # step1_rst_list = inference_detector(model_step1, img)
    # final_rst = []
    #
    # for i in range(len(step1_rst_list)):
    #     step1_rst = step1_rst_list[i]
    #     if len(step1_rst) < 1:
    #         continue
    #     # 遍历一个类型的所有结果
    #     for k, det in enumerate(step1_rst):
    #         x1, y1, x2, y2, conf = det
    #         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    #         w, h = y2 - y1, x2 - x1
    #
    #         if x1 >= x2 or y1 >= y2:
    #             continue
    #         # 将第一步检测的结果也加进去
    #         if det[4] > thres and (det[3] - det[1]) * (det[2] - det[0]) > min_size:
    #             tmp = []
    #             for element in det:
    #                 tmp.append(element)
    #             tmp.append(i)
    #             final_rst.append(tmp)
    #
    #         region = img[y1:y2, x1:x2]
    #         cv2.imwrite('../test_data/%s_%s.jpg' % (fname, k), region)
    #         # print(os.path.abspath(os.path.dirname(__file__)))
    #         tmp_file = '../test_data/%s_%s.jpg' % (fname, k)
    #         offset_x, offset_y = x1, y1
    #
    #         step2_rst_list = inference_detector(model_step2, tmp_file)  # 每张图都返回一个list，5个元祖，但是有很多空的
    #
    #         for j in range(len(step2_rst_list)):
    #             step2_rst = np.array(step2_rst_list[j])
    #             if len(step2_rst) < 1:
    #                 continue
    #             step2_rst[:, 0] = step2_rst[:, 0] + offset_x
    #             step2_rst[:, 1] = step2_rst[:, 1] + offset_y
    #             step2_rst[:, 2] = step2_rst[:, 2] + offset_x
    #             step2_rst[:, 3] = step2_rst[:, 3] + offset_y
    #             for rst in step2_rst:
    #                 if rst[4] > thres and (rst[3] - rst[1]) * (rst[2] - rst[0]) > min_size:
    #                     tmp = []
    #                     for element in rst:
    #                         tmp.append(element)
    #                     tmp.append(j + 7)
    #                     final_rst.append(tmp)
    #
    # locations = np.array(final_rst)
    # if locations.shape[0] == 0:
    #     return {'fname': fname, 'detections': []}
    #
    # # postpreprocess
    # indices = np.argsort(-locations[:, -1])
    # sorted_loc = locations[indices]
    # loc = sorted_loc[0][np.newaxis, :]
    # for bnd in sorted_loc[1:]:
    #     bbox2 = bnd[np.newaxis, :4]
    #     # print(loc)
    #     bbox1 = loc[:, :4]
    #     ious = bbox_iou_numpy(bbox1, bbox2)
    #     if not np.any(ious > 0.5):
    #         loc = np.concatenate((loc, bnd[np.newaxis, :]), axis=0)
    #
    # loc = loc.tolist()
    # return {'fname': fname, 'detections': loc}