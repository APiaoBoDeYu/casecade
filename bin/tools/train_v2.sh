#!/usr/bin/env bash

PYTHON=${PYTHON:-"python"}

CONFIG='configs/region.py'
GPUS=4

$PYTHON -m torch.distributed.launch --nproc_per_node=$GPUS \
    $(dirname "$0")/train.py $CONFIG --launcher pytorch --validate
