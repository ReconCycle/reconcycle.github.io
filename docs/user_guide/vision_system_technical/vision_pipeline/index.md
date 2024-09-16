# Vision Pipeline

Vision pipeline utilizes information obtained through camera sensors to select the appropriate action during the disassembly process.

Docker container that offers GPU support and a configured python environment for [vision-pipeline](https://github.com/ReconCycle/vision-pipeline) and [action-predictor](https://github.com/ReconCycle/action_predictor).

![RViz](./readme_rviz.png)

<!-- TODO add user guides, method overviews etc.-->

## Usage

Set the parameters you want in `config.yaml`.

Run example:
```
python ros_pipeline.py
```

To enable the pipeline for realsense or basler use:
```
rosservice call /vision/realsense/enable True
```
or
```
rosservice call /vision/basler/enable True
```

**Publishes**:

Basler:

- `/vision/basler/colour`, Image
- `/vision/basler/detections`, ROSDetections
- `/vision/basler/markers`, MarkerArray
- `/vision/basler/poses`, PoseArray

Realsense:

- `/vision/realsense/colour`, Image
- `/vision/realsense/detections`, ROSDetections
- `/vision/realsense/markers`, MarkerArray
- `/vision/realsense/poses`, PoseArray
- `/vision/realsense/gaps`, ROSGaps
- `/vision/realsense/cluster`, Image
- `/vision/realsense/mask`, Image
- `/vision/realsense/depth`, Image
- `/vision/realsense/lever`, PoseStamped

**Services**:

- `/vision/basler/enable` True/False
- `/vision/realsense/enable` True/False
- `/vision/vision_get_detection` VisionDetection.srv (from [context_action_framework](https://github.com/ReconCycle/context_action_framework))

The `/vision/vision_get_detection` service provides a single stable detection result from the requested camera.

For example, to get one Basler detection, run:

```
rosservice call /vision/vision_get_detection 0 False
```
To get a Realsense detection, run:
```
rosservice call /vision/vision_get_detection 1 True
```
where True provides the gaps as well.

** Camera Services:**

- `rosservice call /basler/set_sleeping` True/False
- `rosservice call /realsense/enable` True/False

**config**

The configuration file is in `config.yaml`. It should have the following format:


```yaml
node_name: "vision"
reid: False

basler:
  target_fps: 2
  max_allowed_acquisition_delay: 1.0 # in seconds
  rotate_img: 180 # specify in degrees
  topic: "basler" # topic that we publish to: /node_name/topic
  camera_node: "/basler" # camera topic
  image_topic: "image_rect_color"
  sleep_camera_on_exit: False #! debug, usually set to True
  publish_labelled_img: True
  publish_graph_img: False
  has_depth: False
  run_continuous: False
  wait_for_services: True # only disable for rosbag
  detect_arucos: False
  table_name: "table_vision"
  parent_frame: "vision_table_zero" # When publishing transforms, this is the base/parent frame from which they are published.
  create_parent_frame: False # GOE only
  marker_lifetime: 1 # in seconds
  work_surface_ignore_border_width: 100
  show_work_surface_detection: True
  use_worksurface_detection: True
  debug_work_surface_detection: False # debug worksurface detection

realsense:
  target_fps: 2
  max_allowed_acquisition_delay: 1.0 # in seconds
  rotate_img: 0 # specify in degrees
  topic: "realsense" # topic that we publish to: /node_name/topic
  camera_node: "/realsense" # camera node
  image_topic: "color/image_raw"
  info_topic: "color/camera_info"
  depth_topic: "aligned_depth_to_color/image_raw"
  sleep_camera_on_exit: False #! debug, usually set to True
  publish_labelled_img: True
  publish_depth_img: True
  publish_cluster_img: True
  publish_graph_img: False
  has_depth: True
  compute_gaps: True
  run_continuous: False
  wait_for_services: True # only disable for rosbag
  detect_arucos: False # GOE only
  camera_height: 0.20 # height in meters
  parent_frame: 'panda_2/realsense' # When publishing TFs, this will be the parent frame.
  create_parent_frame: False # GOE only
  marker_lifetime: 1 # in seconds
  calibration_file: '/root/vision-pipeline/realsense_calib/realsense_calib.yaml'
  debug_clustering: False

obj_detection:
  debug: True # shows error messages
  model: yolov8 # yolov8/yolact

  # yolact config
  yolact_dataset_file: ~/vision_pipeline/data_limited/yolact/2023-07-18_firealarms_hcas/dataset.json
  yolact_score_threshold: 0.5
  

  # yolov8 config
  yolov8_model_file: ~/vision_pipeline/data_limited/yolov8/output_2024-07-17_20000_incl_new_jsi_imgs/epoch80.pt
  yolov8_score_threshold: 0.5

  superglue_templates: ~/datasets2/reconcycle/2023-12-04_hcas_fire_alarms_sorted_cropped
  superglue_model_file: "~/superglue_training/output/train/2023-11-18_superglue_model/weights/best.pt"
  superglue_match_threshold: 0.5
  rotation_median_filter: True
  superglue_visualise_to_file: False #! saves images... don't run all the time

  classifier_model_file: "~/vision_pipeline/data_limited/classifier/2024-07-03__08-33_classify/lightning_logs/version_0/checkpoints/epoch=319-step=319.ckpt"
  classifier_threshold: 0.5
  allow_list_classes: ["kalo", "hekatron", "fumonic"]
```




