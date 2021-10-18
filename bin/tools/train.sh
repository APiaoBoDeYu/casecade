#!/usr/bin/env bash

PYTHON=${PYTHON:-"python"}

CONFIG='configs/rcnn_region.py'
GPUS=4
RESUME='work_dirs/region919/epoch_12.pth'

$PYTHON -m torch.distributed.launch --nproc_per_node=$GPUS \
    $(dirname "$0")/train.py $CONFIG --launcher pytorch --validate --resume_from $RESUME
