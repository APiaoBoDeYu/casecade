# -*- coding: utf-8 -*-
# @Author: Lu Shaohao(Bravo)
# @Date:   2019-09-12 09:08:45
# @Last Modified by:   Lu Shaohao(Bravo)
# @Last Modified time: 2019-09-12 09:27:14

from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import mmcv

config = 'configs/cascade_rcnn_x101_64x4d_fpn_1x.py'
checkpoint_file = 'work_dirs/cascade_rcnn_x101_64x4d_fpn_1x/latest.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')

test_file = open('data/test.txt', 'r')
test_imgs = [l.strip() for l in test_file.readlines]
for img in test_imgs[0]:
    result = inference_detector(model, img)
    show_result_pyplot(img, result, model.CLASSES)

