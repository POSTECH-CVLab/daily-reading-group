# Learning to Orient Surfaces by self-supervised Spherical CNNs
## Riccardo Spezialetti et al., University of Bologna - Nuerips2020
### Summarized by Seungwook Kim
---

**총평**:
* PCA와 같은 prior 없이, point cloud의 canonical pose를 바로 예측하도록 (regression) 하는 work.
* 현재 진행중인 연구주제와 비슷해서 읽게 됨.
* 아직 canonical pose를 엄청 잘 estimate한다고 하긴 어려움.
* large-scale point cloud에서의 evaluation이 미약함 (GT transformation이 주어졌을 때, point repeatability 확인), 새로운 contribution의 방향성이 될듯.

**Task**: 3D Canonical orientation prediction
* Hypothesis/assumption: 3D objects have a canonical pose 
* If point clouds are aligned, downstream tasks on point clouds will improve in performance.

**Method**: Self-supervised pipeline
* Siamese network, taking pointcloud and a rotated pointcloud as input
* Each network is trained to output "canonical rotation"
  * self-supervised by the augmented rotation
  * Loss between GT rotation and predicted rotation between the two point clouds

Augment missing parts to handle occlusion:
* randomly select a point, remove points around the selected point to "mimic" occlusion

Results show: 
* better LRF repeatability (but only up to ~0.4, which is still very low)
* better classification accurafy when trained without rotation augmentation, but tested with varying rotation
* but significantly worse results when trained&tested both without rotation augmentation
  * canonical pose estimation may actually deteriorate the performance
  * which is obvious from the first observation, since LRF repeatability is as low as 0.4 as well.

Test time adaptation: use the test set to train the network without data snooping
* since there is no label involved
* Not sure if this is really fair
