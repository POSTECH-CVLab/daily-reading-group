# LOGAN: Latent Optimisation For Generative Adversarial Networks
### Yan Wu, Jeff Donahue, David Balduzzi, Karen Simonyan, Timothy Lillicrap
#### Summarized by Minguk Kang
---
 
총평:
	
1. 2020년 ICLR에 제출된 논문으로 약 2년이 지난 현재를 기준으로도 ImageNet 생성 실험에서 SOTA를 지키고 있는 논문임(Diffusion model 제외).
	
2. Game theory, Optimisation, Compressed sensing에서 차용되고 있는 이론들을 활용해 비싼 Hessian 계산없이 adversarial training을  안정화 시키는데 성공하였음.
	
3. 높은 성능에 비해서, 아직 구현에 성공한 사람이 없음. 실제로 잘 동작하는 방법일지에 대한 의문이 있음.
	 

Task: Image Generation using GANs
 
Motivation: 적대적 목적함수의 parameters에 대한 gradient는 정확한 form으로 표시할 수 없는데, 이는 cyclic한 gradient update를 야기할 수 있다 (Balduzzi et al.는 이를 simultaneous gradient 라고 명명하였음). 이러한 cyclic gradient를 목적함수의 curvature를 고려하여 업데이트하는 Symplectic  Gradient Adjustment (SGA)를 통해 해결해보자.
 
Method: SGA를 통해 gradient update를 하기위해서는 헤시안 행렬을 구할 필요가 있는데, Neural Network 학습을 할 때 헤시안을 each stage마다 계산하는 것은 계산 부담을 야기함. 이를 해결하기 위해 Wu et al.이 latent optimisation을 제안하였는데, 이는 poor한 latent update로 인해 원하는 효과를 얻지 못함. 따라서, 더욱 좋은 latent optimizer인 Natural Gradient Decent (NGD)를 사용하자는게 포인트. Natural Gradient Descent를 수행하기 위해서는 Fisher Information matrix F를 구할 필요가 있는데, F를 근사하기 위해 Tikhonov damping을 사용하였고, 이를 통해 성공적으로 이미지 생성을 할 수 있음을 실험결과로 보여주었음.
 
Experimental Results: 
CIFAR10 using DCGAN 실험과 ImageNet using BIgGAN-deep 실험을 수행하였음. CIFAR10 실험에서는 이전의 Wu et al.의 Compressed Sensing GAN (CS-GAN)과 비교하였고 unconditional Image generation 실험에서 17.7의 FID로 기존 모델 대비 높은 성능 향상을 보여주었음. BigGAN-deep에 대한 실험은 3가지 아키텍처 변화를 통해 baseline 성능을 끌어올린 상태에서 수행하였으며, LOGAN (GD) = 4.86, LOGAN (NGD) = 3.36의 FID를 보여주며 최초로 이미지넷 생성 실험에서 4미만의 FID 값을 달성하였음. 이미지넷 생성 실험에서 latent optimisation step은 큰 regularization coefficient로 restriction해주는데, 이는 큰 모델일 수록 Lipschitz constant가 크기 때문이라고 서술되어 있음.
