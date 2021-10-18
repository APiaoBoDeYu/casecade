#!/usr/bin/env bash

PYTHON=${PYTHON:-"python3"}

CONFIG='/configs/rcnn_region.py'
GPUS=2

#使用shell脚本的方式启动另一个python文件
$PYTHON -m torch.distributed.launch --nproc_per_node=$GPUS \
    $(dirname "$0")/train.py $(dirname "$0")/../$CONFIG --launcher pytorch

#$PYTHON $(dirname "$0")/train.py $(dirname "$0")/../$CONFIG --launcher pytorch \
#      -m torch.distributed.launch --nproc_per_node=$GPUS
