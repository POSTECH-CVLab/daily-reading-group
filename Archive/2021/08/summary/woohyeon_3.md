# Scene Representation Networks: Continuous 3D-Structure-Aware Neural Scene Representations
### Vincent Sitzmann et al., Stanford University) - NeurIPS 2019 (Oral, Honorable Mention "Outstanding New Directions")
#### Summarized by Woohyeon Shim
---

**Task**: distillation of a sequence of posed images into a neural scene representations
	
**Motivation**:
		
* vs. classic 3D representation (e.g., voxel grids, point cloud, or meshes): these are discrete, limiting achievable spatial resolution, only sparsly sampling the underlying smooth surfaces of a scene.
		
* vs. function-space based representation (e.g., decision boundary of a learned binary classifier or a continuous signed distance field): these often require explicit 3D supervision and are unclear how to efficiently infer and represent appearance.
	
	
	
**Idea**: Representing a scene as a continuous, differentiable and implicit function that maps a 3D world coordinate to a feature representation and training with renderer which uses a differentiable ray marcher and then transforms the feature-based representation into the same 2D image.
	
**Key features**: sampling with arbitrary resolution, applicable to high-resolution synthesis, encapsulating both scene geometry and appearance, multi-view consistency of the rendered images, working in limited data regime, interpretable, controllable under multi-view and projective geometry and with appearance, generalizable to unseen camera intrinsic matrices and transformations, weaker supervision using just a set of posed 2D images, end-to-end trainable.
	
**Method**:
	

		
		
* **Representing scenes** with MLP (Φ): 3D coordinates x ⇒ feature representation v
		
* **Neural rendering** with two stages approach: (v, E, K) ⇒ v ⇒ I \
v: feature, E: extrinsic, K: intrinsic, I: image
    * 1st stage: Differentiable ray marching algorithm
    	* start at a depth d_init close to the camera.
    	* step along the ray toward surface of the scene.
    	* use LSTM to compute step length: (v, h_i, c_i) ⇒ (Δ, h_i+1, c_i+1) h: hidden state, c: cell state
    	* increase depth accordingly and extract the feature vector at corresponding point.
    	* iterate this process for a constant number of steps.
    	* final estimates yield depth maps, which visualizes every step of the ray marcher. This makes the ray marcher interpretable, as failures in geometry estimation show as inconsistencies in the depth map.
			
			
			
    * 2nd stage: per-pixel generation by 1x1 conv given feature vector.
		
		
		
		
* **Generalizing across scene** given a set of instance datasets of a single class.
			
    * learning shape and appearance priors at a low-dimensional embedding manifold.
			
    * mapping priors into weight of MLP of representing scenes by an additional MLP which resembles HyperNetwork.
		
		
* **Training: image reconstruction loss** + regularization terms for positivity constraint of depth + term that enforces Gaussian prior to a latent vector.
		
	
	
	
**Experiments**: novel view synthesis, shape and appearance interpolation, and few-shot reconstruction.
	
**총평**: NeRF의 시초가 된 이쪽 계열의 초기 논문인듯 함. ray marching algorithm으로 3D Geometry를 조작하고 latent sampling으로 shape과 appearance를 변화를 주는 것이 핵심인듯 함. ray marching algorithm을 제대로 이해할 수 있어 좋았음. 실험 결과는 작은 셋에서 예상 가능한 범위 내에서만 해서 크게 새로운 것은 없었음.