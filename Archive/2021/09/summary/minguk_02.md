# Top-k Training of GANs: Improving GAN Performance by Throwing Away Bad Samples
### Samarth Sinha, Zhengli Zhao, Anirudh Goyal, Colin Raffel, Augustus Odena, Neurips 2020
#### Summarized by Minguk Kang
---
총평:
	
Generator 업데이트를 할 때 discriminator output기준 top-k 샘플들로 (일반적으로 k는 training이 됨에따라 줄어듬) 업데이트를 하는 것이 GAN의 생성 성능을 올려줄 수 있다는 실험적으로 밝힌 논문.
	
원 코드에 단 1줄만 추가하면 되기 때문에 implementation이 간단하고, 또한 추가 overhead가 없다는 장점이 있음.
	
Augustus Odena가 교신저자로 있어 기대하고 읽었지만, top-k training이 GAN학습에 효과적인 이유를 실험적으로만 설명하여 아쉬웠던 논문.
	
또한, discriminator output이 낮은 값 (true data manifold에서 멀리 떨어짐)을 가지는 샘플을 더 잘 업데이트 하는게 GAN 학습에 도움이 될 것이라고 생각했는데, 실제 현상은 그 반대여서 의아했던 논문. 

Task: Generative Adversarial Networks, Sampling rejection
Method: Method는 정말 간단하며 아래와 같은 방식으로 동작함


	
Discriminator를 학습한다.
	
Generator의 discriminator output score를 구한다.
	
torch.topk 함수를 통해 Generator가 생성한 이미지 중 on-manifold에 있는 top-k를 골라 gradient descent를 수행한다.
	
이 때, 학습 초반에는 k=num_batch_size로 모든 샘플을 다 학습에 사용하고, 학습 중후반에는 gamma=0.75~0.999사이의 값으로 k값을 scaling해주어 gradient update를 한다. 또한, k 값의 하한은 배치 크기의 50~75%사이의 값으로 한다.

Experiments: Mixture of gaussian 실험을 통해 Top-k training이 GAN 생성 성능에 미치는 영향을 조사했고, Bottom-(B-K) 실험은 통해 off-manifold data가 generator update를 off-manifold 방향으로 하도록 방해한다는 것을 실험적으로 보였다. 또한, CIFAR10, ImageNet conditional Image Generation 실험을 통해 Top-k training이 실제 GAN 학습에도 적용되어 성공적인 분포학습을 할 수 있음을 보였다.
