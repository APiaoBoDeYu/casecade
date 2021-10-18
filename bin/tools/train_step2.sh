#!/usr/bin/env bash

PYTHON=${PYTHON:-"python3"}

CONFIG='configs/rcnn_screw.py'
GPUS=2
$PYTHON -m torch.distributed.launch --nproc_per_node=$GPUS \
    $(dirname "$0")/train.py $(dirname "$0")/../$CONFIG --launcher pytorch 
