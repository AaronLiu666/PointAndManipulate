# PointAndMnipulate
## Manipulate robot arm with pointing gesture. 

Similar idea as ICRA2022: Augmenteted Pointing Gesture Estimation for Human-Robot Interaction 

LINK: https://ieeexplore.ieee.org/abstract/document/9811617

## Ideas
the paper above use the direction of forearm as the poiting direction, but a pointing happens when we look at something and finger tip at it. It means the direction of forearm may not be the most ituitive way to represent a pointing action especially when the arm is not fully stretched out. Out sight should be the reference which is a line going through our eyes and finger tip. 

## Problem
~~?eye recognition~~

hard to locate the hand when arm is not fully streched out because there may be a lot of obstruction.

precision is also a problem since 2 points(eye and fingertip) stays not far enough in this situation for a distance from camera to people(under 2m) which means a small difference in coordinate brings a big difference in angle change.


## Steps
### Pose estimation
  - [x]human pose estimation: arm and eyes center(midpoint of two eyes)
  
    on going:
    
      AlphaPose: https://github.com/MVIG-SJTU/AlphaPose
      
      Model: 
      
  - [ ]hand pose estimation: considering which to be the end point of the sight line
  
### Pointing estimation
transform keypoints in image frame(in camera) to world frame
  - [ ]coordinates transform
    - [ ]hand-eye calibration
    - [ ]jittering optimization(depends on performance)
    - [ ]compensation(optional)
    
### Interacton design
after getting the pointing position/line of sight, how do we interact with the arm? 
- projection on X-Y plane and see what is there and how can we interact/manipulate
- collision checking: line of sight and object in the workspace then interact

## Updates

2022.3.22

running :
```bash
python scripts/demo_inference.py --cfg configs/halpe_coco_wholebody_136/resnet/256x192_res50_lr1e-3_2x-dcn-combined.yaml --checkpoint pretrained_models/multi_domain_fast50_dcn_combined_256x192.pth --vis --webcam 6
```

model here is [Fast Pose (DCN)](https://github.com/MVIG-SJTU/AlphaPose/blob/master/docs/MODEL_ZOO.md#multi-domain-models-strongly-recommended), expecting around 10 fps. Other models available at [here](https://github.com/MVIG-SJTU/AlphaPose/blob/master/docs/MODEL_ZOO.md)

in `--webcam` parameter, 

|id|camera|
|:---:|:----:|
|0|webcam on laptop|
|5|depth or stereo of D435i|
|6|color of D435i|
||| 
test
