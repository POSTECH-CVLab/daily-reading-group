# PointNet: Deep Learning on Point Sets for 3D classification and segmentation
### Charles R. Qi, Hao Su, Kaichun Mo, Leonidas J. Guibas - CVPR 2017
#### Summarized by Jiye Kim

---

### **Task** : 
Point cloud architecture


### **Main Idea** : 
-  point cloud data를 permutation invariant하게 학습할 수 있도록 MLP, max-pooling을 쌓아서 network를 구성하고 여러가지 task에서 잘 되는 것을 확인했다.


### **Summary** :  
- point clouds 전체를 input으로 받고 MLP와 max-pooling을 통해서 permutation invariant한 representation을 학습할 수 있다.
- 중간 feature와 마지막 global feature를 concat해서 사용해서 local 정보를 활용하는 segmentation network를 구성할 수도 있다.
- T-Net을 사용해서 feature alignment를 맞춰준다. T-Net은 point cloud를 canonical space로 보내기 위해 적용되어야 하는 transformation matrix를 계산한다. 중간 feature transformation matrix는 64*64 차원인데 이 matrix는 너무 커서 optimize시키기 어렵기 때문에 matrix가 orthogonal matrix가 되게 regularization term을 추가한다.
- Task로 Classification, part segmentation, semantic segmentation in scenes를 수행하고 잘되는 것을 확인했다.




### **총평**:
- 3D 비전 발표의 일환으로 읽었다. pointcloud를 다루는 초기 architecture를 제안했다는 점이 contribution인 것 같다.
