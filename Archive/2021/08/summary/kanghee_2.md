# CORAL - Colored structural representation for bi-modal place recognition
### Author information - arxiv
#### Summarized by Kanghee Lee
---

**Task** : Place recognition with two modalities (RGB image, point cloud) 

**Motivation** : seasons, weather, illumination, viewpoints에 취약한 image와 structure features가 별로 없는 경우 discriminative한 feature를 추출하기 힘든 Lidar data 두 개를 fusion해서 이용하여 place recognition을 하려 함.
Contribution)

1) local dense elevation map representation을 제안하여 LIDAR로 부터 structural information을 encoding함

2) 다양한 environmental changes에 robust한 semantic representation with corresponding geometry (CORAL)을 제안

**Method**) \
Input은 front-view RGB image와 만elevation image generated from pcd이다. \
a) Elevation map generation
PCD의 point에 Global frame G(=velo2cam maybe) 을 곱하고 projection matrix [0, 0, 1] 을 곱하여 elevation e_p를 계산한다. 그리고 x, y 좌표는 grid map의 index로 활용된다. \
b) Network architecture
ResNet18과 FPN을 통해 feature를 뽑고 RGB image의 extracted feature에서 projection layer를 통해 BEW frame을 만든다. 이 frame feature를 feature extracted from elevation map에 더하여 다시 ResNet, FPN을 통해 feature를 만든다.
이렇게 만들어진 feature는 NetVLAD를 통해 Global descriptor로 만들어진다. 

**Datasets**)

Oxford, KITTI(only 00 - visit same places repeatedly)