# CircleGAN: Generative Adversarial Learning across Spherical Circles
### Woohyeon Shim and Minsu Cho, POSTECH, Neurips 2020
#### Summarized by Minguk
---
 
총평:

1. Generative Adversarial Network 프레임워크가 가지고 있는 low diversity generation 문제를 tackle 하였음. low diversity 문제는 real images와 fake images를 한 방향으로 모으는 기존의 adversarial loss가 문제였다고 주장하고 있는데, 상당히 재미있었음.
	
2. Low diversity 문제를 해결하기 위해 pivot이 무한개인 great circle로 real image를 밀어주는 circle training을 제안함. 이를 위해 realness score와 diversifiability score를 정의하였고 relativistic averaged loss를 적용하였는데 아이디어가 정말 참신하다고 생각됨.
	
3. Multi pivot으로 real images를 밀어주는 학습을 할 때 diversity가 확보되는 이유에 대한 이론적 실험적 설명이 부족한 것 같음. 논문에서는 multiple discriminator를 예로 설명했는데, 실험 파트에 multiple discriminator를 사용하는 모델과 비교한 결과가 없어서 아쉬웠음.
	
4. 또한, AMGAN, TACGAN을 예로 들며 diverse 한 이미지를 생성할 수 있는 모델을 제안한다고 했는데, 실험 파트에서 AMGAN만 비교한 점이 아쉬움.
	
5. 추가적인 3가지 loss terms (center estimation loss, radius equalization loss, and classification loss), 2개의 추가 learnable embeddings (center embedding, unit-pivotal embedding), 1개의 hyperparameter \tau 로 인해 프레임워크가 복잡해보임.
	
6. 그럼에도 불구하고, spectral normalization을 사용하지 않고 기존 baseline들을 이긴 점과 novel한 idea로 인해 정말 재미있게 읽은 논문이었음.

Task: Image Generation, Conditional Image Generation, Generative Adversarial Networks
 
Method:

Center estimation loss를 통해 learnable center embedding c를 업데이트 한다.
	
이미지 (X)를 discriminator에 인가하여 embedding v_{i}^{emd}를 추출해준다.
	
v_{i}^{emd}를 learnable embedding c를 사용하여 c를 중심으로 하는 unit-hyper sphere에 projection 시킨다 (v_i).
	
s_real 과 s_diverse 점수를 계산하고, 이를 통해 relativistic averaged loss를 계산한다.
	
radius equalization loss를 통해 image embedding의 center로부터 거리가 평균거리 R에 얼마나 가까운지 계산한다.
	
Discriminator는 relative averaged loss + equalization loss로 Generator는 relative averaged loss를 통해 업데이트 한다.
	 

Class conditional CircleGAN의 경우, c와 p를 class 갯수만큼 생성한 다음 위와 똑같은 방식으로 class conditional 하게 loss를 계산한다. 이때 ACGAN의 classification loss를 추가하여 class conditioning 성능을 향상시킨다.
 
Experimental Results:
실험은 주로 WGAN-GP, SNGAN, SphereGAN를 기준으로 이루어졌으며, unconditional의 경우 CIFAR100, STL10을 conditional의 경우 CIFAR10, CIFAR100, Tiny_ImageNet, ImageNet데이터를 사용하여 광범위하게 이루어졌음. 평가를 위해 IS, FID 뿐만 아니라 Fidelity and Diversity를 측정할 수 있는 GAN-train (recall), GAN-test metrics을 사용했였는데, 다양한 측도를 통해 제안하는 알고리즘의 우수성을 잘 증명하였음. 다만 ablation study를 CIFAR10에서만 수행한 것과 실험을 1번만 수행했다는 것이 정말 아쉬움.
