from .registry import DATASETS
from .xml_style import XMLDataset


@DATASETS.register_module
class RegionDataset(XMLDataset):
    '''
    CLASSES = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
               'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
               'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train',
               'tvmonitor')
    '''

    CLASSES = ('XCXJ_JJC',  '44_NZXJ_YYX', '41_NZXJ',)

    def __init__(self, **kwargs):
        super(RegionDataset, self).__init__(**kwargs)
        self.cat2label = {cat:i+1 for i, cat in enumerate(self.CLASSES)}
