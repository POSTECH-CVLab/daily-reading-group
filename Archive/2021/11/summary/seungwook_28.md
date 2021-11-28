# Revealing Scenes by Inverting Structure from Motion Reconstruction
## Francesco Pittalugo et al., University of Florida - CVPR 2019
#### Summarized by Seungwook Kim
---

**총평**:
* GSAI QE 의 일환으로 읽게 됨
* SfM pipeline이 어떻게 privacy 를 위협하는 데 악용될 수 있을지에 대한 주제를 다룸
* 그 가능성을 처음 다룸으로서 Oral paper로서 인정받았다고 생각됨

**Task**: Reconstructing images used for SfM pipeline using ouptut point clouds

**Motivation**:
* SfM-generated point clouds may be used on their own (images are usually discarded for security reasons) to be applied for other tasks (ex. robot nagivation)
* However, the point clouds and the point-wise descriptors (SIFT?) alone may suffice to reconstruct the images, which may threat the image-wise security as well.

**Dataset**: MegaDepth, NYU datasets

**Method**: VisibNet - CoarseNet - RefineNet

Preliminary: given a camera pose, so that we know "which part" of the point cloud to reconstruct

Visibnet: Given a point cloud, determine the visibility of points
* Occluded points should not be used for reconstruction
* NN supervised using point-wise GT depth

CoarseNet: From results of VisibNet, reconstruct "rough" image
* L1 pixel loss, L2 perceptual loss

RefineNet: Refines output of CoarseNet
* L1 pixel loss, L2 perceptual loss, adversarial loss

**Results**
* Using SIFT descriptors and point cloud alone, can reconstruct the scene image with low MAE and high SSIM
* Using a sparse pcd (~20% of original SfM pcd) still yields high-quality images
* Using more information (Descriptors -> orientation -> scale -> colour -> depth...) gives better results.
