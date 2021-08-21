# Unsupervised Learning of Probably Symmetric Deformable 3D objects from Images in the Wild. 
 
## Shangzhe Wu, Christian Rupprecht, Andrea Vedaldi - CVPR 2020 (best paper)

#### Summarized by Minguk Kang
---

**Task**: learning 3D deformable object categories from raw single-view images.
 
**Motivation**: While many deep networks appear to understand images as 2D textures, 3D modelling can explain away much of the variability of natural images and potentially improve image understanding in general. 
 
Training condition: 
(1) The algorithm should not require 2D or 3D ground truth information.
(2) The algorithm should only use a single shot of instances. 
 
**Method**:

- Utilize an auto-encoder that can decomposes the images into albedo, depth, illumination, and view point without any supervision. 
- They explicitly model asymmetric illumination let the model estimate a confidence score for symmetricness. 
- They try to reconstruct the original image with lighting function of a (albede), d (depth), and l (light direction) and a reprojection funtion of d (depth) and view point (w).
	
**Experiments**:  Use CelebA, 3DFAW, and BFW to evaluate the depth reconstruction quality of the proposed model with scale-invariant depth error (SIDE).
 
총평: 논문이 굉장히 잘 조직화되어있고, 넓은 범위의 ablation study를 담고 있다. 싱글샷의 얼굴 이미지를 가지고 3D 복원을 할 수 있다는 것이 정말 흥미로웠고, CVPR 베스트페이퍼 답게 결과가 convincing 한 것 같다. 하지만, 3D vision을 잘 모르는 학생이라면 method 중간 부분부터는 이해하기 어렵기에 해당 분야를 공부하고 다시 읽어봐야 할 것 같다.
