from .registry import DATASETS
from .custom import CustomDataset
import os
import numpy as np

@DATASETS.register_module
class ScrewDataset(CustomDataset):

    #CLASSES = ('0','1','2','3','4','5')#['ZX_zc','ZX_wbj','ZX_tl','PWJYZ_zxxd', 'PWJYZ_byjyzzxqs', 'PWJYZ_zxsd']
    # CLASSES = ('0','1','2')
    # CLASSES = ('XCXJ_BY3','XCXJ_BY2','NZXJ_yjh','XCXJ_XS',)
    CLASSES = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15')
    def __init__(self, **kwargs):
        super(ScrewDataset, self).__init__(**kwargs)
        self.cat2label = {cat: i + 1 for i, cat in enumerate(self.CLASSES)}
    def load_annotations(self, ann_file):
        img_infos = []
        with open(ann_file, 'r') as f:
            lines = f.readlines()
        self.img_ids = [line.strip().split('/')[-1].split('.')[0] for line in lines]
        for img_id in self.img_ids:
            filename = 'step2_JPEGImages/{}.jpg'.format(img_id)
            label_path = os.path.join(self.img_prefix, 'step2_labels/{}.txt'.format(img_id))

            with open(label_path, 'r') as f:
                lines = f.readlines()

            width, height = lines[0].strip().split(' ')
            width, height = int(width), int(height)

            img_infos.append(dict(id=img_id, filename=filename, width=width, height=height))

        return img_infos

    def get_ann_info(self, idx):
        img_id = self.img_infos[idx]['id']
        label_path = os.path.join(self.img_prefix, 'step2_labels', '{}.txt'.format(img_id))

        bboxes = []
        labels = []
        with open(label_path, 'r') as f:
            lines = f.readlines()

        for line in lines[1:]:
            line = line.strip()
            data_list = line.split(' ')
            label, xmin, xmax, ymin, ymax = data_list
            bbox = [int(xmin), int(ymin), int(xmax), int(ymax)]
            label = int(label) + 1

            bboxes.append(bbox)
            labels.append(label)

        if not bboxes:
            bboxes = np.zeros((0, 4))
            labels = np.zeros((0, ))
        else:
            bboxes = np.array(bboxes, ndmin=2) - 1 
            labels = np.array(labels)

        bboxes_ignore = np.zeros((0, 4))
        labels_ignore = np.zeros((0,))
        ann = dict(
            bboxes = bboxes.astype(np.float32),
            labels = labels.astype(np.int64),
            bboxes_ignore=bboxes_ignore.astype(np.float32),
            labels_ignore=labels_ignore.astype(np.int64),
        )
        return ann

