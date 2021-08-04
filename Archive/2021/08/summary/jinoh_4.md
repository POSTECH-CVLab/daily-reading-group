# GANSpace: Discovering Interpretable GAN Controls
### (Erik Harkonen et al.) - NeurIPS 2020
#### Summarized by Jinoh Cho
---

**Task**: To find meaningful direction in the latent space of GAN, so that they can make interpretable controls for image synthesis
	 
	
**Motivation**:
	

		
Prior works are based on the direct supervision, which is very expensive and time consuming.
		 
	
	
	
Idea:
	
	1. Principal Component Analysis(PCA) in latent space for StyleGAN, and feature space for BigGAN.
	
	2. How BigGAN can be modified to allow StyleGAN-like layer-wise style mixing and control, without retraining


 


	
Method:
	 
	

		
* StyleGAN의 경우 isotropic gaussian에서 latent vector를 추출하여 MLP레이어를 통과 시키기 때문에 MLP의 output space(W)가 isotropic하지 않게 transformation이 된다. 이에 바로 W space에서 PCA를 돌려 meaningful한 direction으로 editing을 가할 수 있다.
		 
		
* BigGAN의 경우에는 좀 더 복잡하게 되는데 왜냐하면 latent vector sampling distribution을 학습하지 않고 단순히 isotropic gaussian에서 추출하여 이를 바로 사용하기 때문이다. 이에 BigGAN의 경우에는 intermediate network layer의 output을 이용해서 PCA를 돌려서 meaningful한 Direction을 찾고 해당 Direction을 다시 isotropic gaussian space에서 corresponding한 Direction으로 다시 찾는 과정이 있다.
		 
	
	
	
Strong Point :
	
	1. We do not need additional training procedure to find meaningful direction in the latent space.
	
	2. We don’t need any annotated attribute(unsupervised)like prior works, no labeling need.
	 
	
Weak Point :
	
	1. PCA를 통해서 방향을 찾았더라도, 해당 방향이 이미지를 생성할 때 어떤 attribute를 바꾸는지에 대해서는 직접 확인 전에는 모른다.
	
	2. Need to sampling procedure and need forward computation for those sampled data. However, it is much more cheap than the prior works.
	 
	
**Experiments**: pre-trained된 BigGAN과 StyleGAN에서 PCA를 통한 latent vector editing을 통해서 어느 attribute를 바꿨는지 실험적으로도 보여주고 있다.
	 
	
**총평**: 굉장히 간단한 기법(PCA를 어디에 적용할 것인가에 대한 고민)을 통해서 GAN의 latent space에서 meaningful한 Direction을 잘 찾아낼 수 있었다. 다만 해당 Direction이 어떤 attribute를 바꾸는지는 직접 찾아내야된다. This paper demonstrates simple but powerful ways to create images with existing GANs.