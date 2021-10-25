# RandLA-Net: Efficient Semantic Segmentation of Large-Scale Point Clouds
### Qingyong Hu, Bo Yang, Linhai Xie, Stefano Rosa, Yulan Guo, Zhihua Wang, Niki Trigoni, Andrew Markham - CVPR 2020 Oral
#### Summarized by Jiye Kim

---

### **Task** : 
Semantic Segmentation of point clouds



### **Main Idea** : 
-  large scale point cloud에 대해 segmentation을 수행하기 위해서 computational cost가 적은 random sampling을 사용한다. random sampling으로 인해 중요한 feature를 담은 point가 없어질 수 있기 때문에 sampling전 k-nearest neighbor에 있는 points의 feature를 aggregate하고 sampling하는 과정을 반복함으로서 receptive field size를 키운다. 이렇게 정보는 유지하면서 sampling은 효율적으로 할 수 있다고 주장한다.



- 전체적으로 gnn의 message passing을 수행하고 노드를 random sampling해서 줄이고 다시 message passing을 수행하고 줄이는 과정을 반복했다고 생각하면 되는데 graph를 explicit하게 만들지는 않음.


### **Method** :  
1. random sampling의 장점



- 기존에 많이 사용되는 heuristic sampling (Farthest point sampling, inverse density importance sampling), learning-based sampling (generator-based sampling, continuous relazation bsed sampling, policy gradient based sampling) 은 large-scale point cloud에 적용되기엔 너무 computationally heavy 하거나, 메모리가 많이 들거나, 학습이 힘든 문제가 있었다. 따라서, O(1)가 드는 random sampling을 사용한다고 한다.



2. Local feature aggregation

   1) local spatial encoding

     - 먼저 각 point i에 대해 k-nearest neighbor를 구한다.
     - point p_i의 position 정보와 그 neighbor p_ik의 position 정보를 합쳐서 p_ik의 relative point position r_ik을 구한다.
     - r_ik와 해당 point의 feature f_ik를 concat해서 새로운 feature vector f_ik^hat 을 만든다.
   2) attentive pooling

     - local spatial encoding에서 나온 feature을 shared mlp를 태우고 softmax를 씌워 각 weight를 구한다.
     - 이것으로 weighted sum해서 point i에 k nearest neighbor들을 고려한 aggregated feature를 만든다.
   3) dilated residual block

     - locse, attentive pooling을 두번 쌓아서 dilated residual block을 만든다.


 - 전체구조는 u-net구조로 dilated residual block을 몇개 쌓아 encoding하고 upsampling을 통해 decoding한 후 FC layer를 몇번 돌린 구조.



### **Experiment** :
- Random sampling이 다른 sampling 방법들보다 얼마나 efficient 한지 실험적으로 보임.
- semantic3d, semantickitti, S3DIS dataset에서 잘 되는 것을 보임.

### **총평**:
- 3d 비전 과목의 일환으로 읽었다. 전체적으로 간단한 방법으로 좋은 성능을 낸 논문인 것 같다.
