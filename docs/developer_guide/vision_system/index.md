# Vision System

This guide explains briefly how to create a dataset and train the different models.


## YOLOv8 Segmentation Model for Devices and Components

1. Label a dataset using [Labelme](https://github.com/wkentaro/labelme). 
2. Train on the dataset using [YOLOv8](git@github.com:ultralytics/ultralytics.git).
3. In `vision_pipeline/config.yaml` set the paths correctly:
```yaml
model: yolov8

yolov8_model_file: ~/vision_pipeline/data_limited/yolov8/output_2024-07-17_20000_incl_new_jsi_imgs_p2/epoch60.pt
yolov8_score_threshold: 0.5
```

## Classification Model

1. Train the classifier in [https://github.com/ReconCycle/device_reid](https://github.com/ReconCycle/superglue_training)
2. In `vision_pipeline/config.yaml` set the paths correctly:
```yaml
classifier_model_file: "~/vision_pipeline/data_limited/classifier/2024-07-19__14-32_classify/lightning_logs/version_0/checkpoints/epoch=339-step=339.ckpt"
classifier_threshold: 0.2
classifier_allow_list: ["kalo", "hekatron", "fumonic"]
```

## Rotation Estimation Model (SuperGlue)

1. Train the SuperGlue model in [https://github.com/ReconCycle/superglue_training](https://github.com/ReconCycle/superglue_training).
2. In `vision_pipeline/config.yaml` set the paths correctly:
```yaml
superglue_templates: ~/datasets2/reconcycle/2023-12-04_hcas_fire_alarms_sorted_cropped
superglue_model_file: "~/superglue_training/output/train/2024-06-26_superglue_model_evens_finished/weights/best.pt"

superglue_match_threshold: 0.5
rotation_median_filter: False
superglue_visualise_to_file: False #! saves images... don't run all the time
```


<!-- ## Labelling Images with Segmentation for use with Yolact

```bash
git clone https://github.com/wkentaro/labelme
cd labelme
conda create --name=labelme python=3.6
conda activate labelme
pip install --editable .
cd labelme
labelme
```

### How to Generate COCO dataset from labelme labelled data

1. Create `labels.txt` file in the same directory as the labelled data with contents of your labels:
```
__ignore__
_background_
hca_front
hca_back
hca_side1
hca_side2
battery
pcb
internals_back
internals_front
internals
```
2. Run command:
```bash
cd labelme/examples/instance_segmentation
./labelme2coco.py data_annotated data_dataset_coco --labels labels.txt
```
For example:
```bash
./labelme2coco.py /Users/sebastian/datasets/labelme/kalo_v2_imgs_20-11-2020-selected /Users/sebastian/datasets/labelme/kalo_v2_imgs_20-11-2020-selected-coco --labels /Users/sebastian/datasets/labelme/kalo_v2_imgs_20-11-2020-selected/labels.txt
```

### Create Train Test Split from COCO .json file

Use the script in `tools/coco-train-test-split/cocosplit.py` to split the COCO .json file into a train.json and test.json. -->

<!-- ## How to Train Yolact

In this project this [Yolact API](https://github.com/sebastian-ruiz/yolact) is used.

**These instructions are no longer valid.**

1. Create dataset with NDDS. Make sure instance segmentations and class segmentations are produced.
2. Generate COCO format using the **ndds-to-coco** tool. First test wether it's producing what you want by setting `TESTING_STAGE=True`.
To check whether it worked properly, use the **coco-viewer** tool. Using `TESTING_STAGE=True` set `CATEGORIES` correctly.
3. Open `yolact/data/config.py` and set the following correctly: `NDDS_COCO_CLASSES`, `NDDS_COCO_LABEL_MAP` and the paths in `coco_ndds_dataset`.
4. To start training, replace num_gpus and run:
```
$ export CUDA_VISIBLE_DEVICES=0,1,2 (or whichever GPUs to use, then)
$ python -m yolact.train --config=coco_ndds_config --save_interval=2000 --batch_size=8*num_gpus
```
To resume:
```
$ python -m yolact.train --config=coco_ndds_config --resume=weights/****_interrupt.pth --start_iter=-1 --save_interval=2000 --batch_size=8*num_gpus
```
For training on less data, reduce the save_interval. On few real images use `--save_interval=200` instead.

5. To view logs run: `tensorboard --logdir=yolact/runs`. -->

<!-- First we train on synthetic data.

1. Create dataset with NDDS. Make sure instance segmentations and class segmentations are produced.
2. Generate COCO format using the **ndds-to-coco** tool. First test wether it's producing what you want by setting `TESTING_STAGE=True`.
To check whether it worked properly, use the **coco-viewer** tool. Using `TESTING_STAGE=True` set `CATEGORIES` correctly.
3. Open `yolact/data/config.py` and set the following correctly: `NDDS_COCO_CLASSES`, `NDDS_COCO_LABEL_MAP` and the paths in `coco_ndds_dataset`.
4. To start training, replace num_gpus and run:
```
$ export CUDA_VISIBLE_DEVICES=0,1,2 (or whichever GPUs to use, then)
$ python -m yolact.train --config=coco_ndds_config --save_interval=2000 --batch_size=8*num_gpus
```
To resume:
```
$ python -m yolact.train --config=coco_ndds_config --resume=weights/****_interrupt.pth --start_iter=-1 --save_interval=2000 --batch_size=8*num_gpus
```
For training on less data, reduce the save_interval. On few real images use `--save_interval=200` instead.

6. After training on synthetic data, train using the synthetic weights, but on real data.

Make sure that the class labels of the real data match those of the synthetic data. Use Cocoviewer to get the order of the class labels for the real data.
Example:
```
NDDS_COCO_CLASSES = ('background', 'back', 'battery', 'front', 'internals', 'pcb', 'side2', 'side1')
#                     1             2       3          4        5            6       7       8      # let these always be the corresponding class labels
# for YOLACT the labels need to start at 1
NDDS_COCO_LABEL_MAP = {1:  1,  2:  2,  3:  3,  4:  4,  5:  5,  6:  6,  7:  7,  8:  8,}

# From looking at COCOViewer, we get the following order of the real class labels (with the corresponding label IDs on the next line):
# REAL_CLASSES = ('background', 'front', 'back', 'side1', 'side2', 'battery', 'pcb', 'internals')
#                0             1        2       3        4        5          6      7
# Actually what we want is for the class labels to be in the same order as in NDDS_COCO_CLASSES. To do this we create the REAL_LABEL_MAP as follows:
REAL_LABEL_MAP = {0: 1, 1: 4, 2: 2, 3: 8, 4: 7, 5: 3, 6: 6, 7: 5}
# we set the labels so that they correspond to the NDDS_COCO_CLASSES. We therefore also use the  NDDS_COCO_CLASSES in the config for the real data.
```

Train on real data:
```
python train.py --config=real_config --resume=weights/training_15-01-2021-segmented-battery/coco_ndds_57_36000.pth --start_iter=0
```

7. Done! -->