# HRegNet : A Hierarchical Network for Large-scale Outdoor LiDAR Point Cloud Registration
### Fan Lu et al., Tongji University - ICCV 2021
#### Summarized by Kanghee Lee
---

**Task**) \
Point cloud registration
	
**Motivation**) \
Outdoor LiDAR pcd는 높은 sparsity와 large spatial range때문에 기존 method들로 registration을 할 경우 unreliable or time-consuming한 경우가 대다수이다.

**Contribution**)
1) 정확하고 robust한 registration을 위해서 shallower하고 deeper layer에서의 keypoints와 descriptors들의 강점을 결합한 hierarchical paradigm을 propose했다. \
2) bilateral consensus와 neighborhood consensus를 효율적으로 통합한 새로운 similarity features를 design했다.

	
**Method**) \
point cloud의 small sets of keypoints들과 descriptor들을 hierarchically downsampling한다. Layer가 깊어질 수록 single keypoint의 information은 증가하지만 sparsity가 증가함에 따라 corresponding keypoints에 대한 error가 커진다.
따라서 bottom layer에서 global하게 keypoints들을 matching하여 coarse하게 registration을 수행한다. 그리고나서 upper layer에서 local matching을 통해 fine registration을 수행한다.
다음으로, robustness와 accuracy를 위해서 두 가지 중요한 concepts인 bilateral consensus와 neighborhood consesnsus를 이용하여 similarity features를 만든다.

1) Feature extraction : 먼저 WFPS를 통해 candidate keypoints들을 선정한다. 그 후 shared MLP를 통해 feature extraction을 수행한다. \
2) Correspondence network : geometric features, descriptor features, similarity features에 shared MLP를 통해 feature를 가공한 후 Maxpooling과 softmax를 통해 attentive weight를 만든다. \
3) Similarity features : Source point cloud와 Target point cloud 각각에서의 keypoint가 서로서로 가장 가깝게 매칭되도록 하는 bilateral consensus를 계산한다. Source point cloud의 Keypoints neighborhood들이 Target point cloud의 keypoints neighborhood들과 매칭되도록 하는 Neighborhood consensus를 계산한다.

