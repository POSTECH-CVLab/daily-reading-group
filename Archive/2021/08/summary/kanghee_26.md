# KeypointDeformer: Unsupervised 3D Keypoint Discovery for Shape Control
### Tomas Jakab et al., Google Research - CVPR 2021 oral
#### Summarized by Kanghee Lee
---

**Task**) \
Shape control through 3D keypoints
	
**Motivation**) \
Keypoints는 Shape editing에 좋은 역할을 하지만 keypoint에 대해 explicit한 supervision을 주는 것은 expensive하고 ill-defined하다. 
Unsupervised manner로 keypoint prediction을 해서 keypoint를 이용한 shape deformer model을 제안한다.

**Contribution**)
1) Propose intuitive and simple way to control object shapes
2) keypoint prediction and deformation model are unsupervised
3) keypoints discovered by our methods are better for shape control than manually annotated ones
4) Ours unsupervised 3D keypoints are semantically consistent across object instances of the same category giving us sparse correspondences
	
**Method**) \
전체적인 process는 source shape x가 주어졌을때 keypoint p를 prediction하고 keypoint p를 p’으로 deformation을 가했을때 source shape x가 target shape x’으로 되는 것이다.
1) Shape deformation with keypoints
Shared encoder를 통해 source와 target shape에서 각각 keypoint p, p’을 만든다. 
Keypoint를 통한 전체적인 shape deformation을 위해 Cage-based deformation algorithm을 사용한다. 
Initial Cage는 source shape x를 아우를 수 있는 spherical shape이고 object centre를 향해 cage vertices들을 당겨서 object surface와 가까운 cage model을 만든다. 
이러한 cage를 이용한 deformation은 reliable한 shape-preserving deformation이지만 cage vertices들이 surface위에 있지 않고 coarse structure도 아니며 동일 category, but different shape에 대해 semantically consistent하지 않기 때문에 충분하지 않다. 
따라서 keypoint를 함께 이용하는데 cage와 keypoint를 연관시키기 위해 둘 사이의 influence matrix W(cxk, k=number of keypoints) 를 정의하고 p’-p에 이 influence matrix를 곱한 값을 cage vertices에 더하여 cage를 변형시킨다. 
2) Losses and Regularizers
위 process를 통해 변형된 source shape과 target shape x’사이의 Chamfer distance를 계산하여 similarity loss를 계산한다.
그 후 keypoint regularizer를 위해 input shape에서 farthest sampling을 통해 sampled points q를 구하고 keypoint p와 chamfer distance를 통해 keypoint loss를 계산한다.

**Experiments**) \
Inference때 user가 원하는 keypoint를 특정 direction으로 당김으로써 전체 shape을 변형시킬 수 있다. 
Unsupervised로 구해진 keypoint는 semantically stable하다. 동일 category내에서 consistent하게 존재하는 point들이 keypoint로 설정된다.
