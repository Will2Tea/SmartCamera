#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

TRAIN_DATA_ROOT=/home/will/CaffeSmartCamera/lfw_dataset/train
VAL_DATA_ROOT=/home/will/CaffeSmartCamera/lfw_dataset/val

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 /usr/bin/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    /home/will/CaffeSmartCamera/lfw_dataset/train/ \
    /home/will/CaffeSmartCamera/lfw_dataset/train.txt \
    /home/will/CaffeSmartCamera/lfw_dataset/train_lmdb

echo "Creating test lmdb..."

GLOG_logtostderr=1 /usr/bin/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    /home/will/CaffeSmartCamera/lfw_dataset/val/ \
    /home/will/CaffeSmartCamera/lfw_dataset/val.txt \
    /home/will/CaffeSmartCamera/lfw_dataset/val_lmdb

echo "Done."
