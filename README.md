# ZAIC2025_AeroEyes

| Drone Object Localization for Search and Rescue


## Overview

This repository contains our solution for the **Drone-based Object Localization Challenge**, focusing on emergency and disaster response scenarios.  
The mission: build a perception system capable of identifying and localizing a specific target object in drone-captured videos, based on a few reference images.

In real-world search-and-rescue missions, this system helps drones automatically locate missing persons or critical items (e.g., backpacks, bicycles, or laptops) under difficult conditions such as floods, forests, or post-storm environments.


## Task Description

Given:
- **3 reference images** of the target object.
- **1 drone video** scanning a large area.

The model must:
- Detect and **localize** the target object in the video.
- Output **bounding boxes** with frame indices.
- Handle **scale, rotation, occlusion,** and **viewpoint variation**.
- Operate **efficiently** for real-time deployment on **Jetson-based drones**.

## Technical Approach

Our approach combines:
- **Visual Similarity Modeling:** feature extraction and matching between reference images and video frames using pretrained vision encoders (e.g., CLIP, ViT, or SAM-based backbones).
- **Spatio-Temporal Tracking:** motion consistency and frame linking using optical flow or transformer-based tracking.
- **Object Refinement:** bounding box refinement via lightweight detection head (YOLO-style or DETR-style).


Focus areas:

- Robustness to environmental noise (lighting, motion blur)
- Jetson-optimized inference (TensorRT / ONNX Runtime)
- Real-time frame processing pipeline

## Pipeline Overview

1. **Reference Encoding:** Extract embeddings from reference images.
2. **Frame Sampling:** Read drone video frames efficiently.
3. **Frame Matching:** Compute similarity between reference embeddings and frame patches.
4. **Detection & Tracking:** Generate bounding boxes and track object across frames.
5. **Output:** Save predictions as JSON or CSV.


## Future Work

- Integrate multi-modal CLIP-like embeddings for few-shot generalization.
- Add attention-based temporal smoothing for long video sequences.
- Test on **Jetson Xavier / Orin** for real-time performance.


## License

Apache License. See [LICENSE](LICENSE) for details.