#!/bin/bash
PYTHON=${PYTHON:-"python3"}
echo $PYTHON
CONFIG='/configs/rcnn_region.py'
GPUS=2
echo $(dirname "$0")
