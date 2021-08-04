# NeRD: Neural 3D Reflection Symmetry Detector
### Yichao Zhou et al., UC Berkeley) - CVPR 2021
#### Summarized by Woohyeon Shim
---

**Task**: detecting 3D symmetry from an image
	
	
	
**Motivation**
		
* vs. instance-level 3D pose estimation: CAD model is required beforehand, thus rather limited in practice.
		
* vs. category-level 3D pose estimation: the formulation is ill-posed since the pose is estimated solely by interpolating the training data.
	

	
⇒ identify the reflection symmetry, which commonly exists in man-made objects, as geometric connection between the object poses and the image. (the canonical space of objects is mostly determined by aligning the Y-Z plane to the symmetry planes of objects)
	
	
	
**Method:**

* formulation of 3D symmetry

    * associating two-pixels with coordinate transformation (image(x) → camera → world → camera → image(x')) using camera intrinsic extrinsic matrix and depth.
			
    * integrating symmetry relation into association by the normal vector of symmetry plane.	
		
* coarse-to-fine symmetry sampler
			
    * uniformly sample a list of candidate normal directions ⊂ R3 from Fibonacci lattice.
			
    * find the best normal vector showing the photo-consistency of matched pairs. (elaborated in next stage)
			
    * confine the sampling regions nearby the optimal normal from the previous round.
		
* photo-consistency check with black-box deep network
			
    * construct 3D volume grid by discretizing depth by certain interval given minimal and maximal depth value.
			
    * warp 2D feature map into 3D volume grid and concatenate the original and its associated feature volumes into channel dimensions.
			
    * extract confidence value of single scalar from the cost volume by multiple 3D convolution layers, max-pool operators and sigmoid function. the confidence value indicates whether the current normal is close to the ground truth and is trained with BCE loss.
			
    * the final output can be altered for pose or depth estimation. For training, additional supervision is required.
		
	
**총평**: intra-image (implicit) correlation을 통해 대칭을 찾아낸 논문. gt와 3D 정보(camera intrinsic, extrinsic, symmetry plane)를 쓴 게 한계로 작용할 수 있다고 보지만, 논문에서는 그것을 최대한 활용한 것이 인상적이었음. 하지만 ResNet50으로 직접적으로 regress한 것과 비교한 결과를 보면 결과적으로 거의 차이가 없는데 적용한 dataset이 너무 쉬운게 아닌가 하는 생각이 듦. gt가 필요하지만 pose와 depth estimation도 동시에 가능하게 하다는 것도 장점임.