# Your GAN is secretly an Energy-based Model and You Should Use Discriminator Driven Latent Sampling

### Tong Che, Ruixiang Zhang, Jascha Sohl-Dickstein, Hugo Larochelle, Liam Paull, Yuan Cao, Yoshua Bengio, Neurips 2020

#### Summarized by Minguk Kang
---
 
총평:
	
Vanilla loss를 사용하는 GAN이 Energy-based Model로 정의될 수 있음을 보이고, Continuous state space에서 Markov Chain Monte Carlo (MCMC)를 하는 방법 중 하나인 Langevin dynamics를 사용하여 이미지의 질을 높히는 방법을 제안.
	
Wasserstein GAN의 경우 특정한 시나리오에서 Energy based model를 학습시키는 것과 같다는 것을 보임.
	
Langevin sampling을 하면 mode-dropping 문제를 해결할 수 있다는 것을 보였음. 하지만, 이에대한 이론적 설명이 부족한게 아쉬웠음.
	
제가 부족한 것일 수 있지만, 논문을 읽으며 Langevin sampling이 학습을 하면서 이루어지는 것인지 evaluation을 하면서 이루어지는 것인지에 대해서 헷깔렸음.
	 

Task: Unconditional Image Enhancement and Generation.
 
Method:
 
-Vanilla GAN의 optimal discriminator가 e^{d(x)} = p_{d}/p_{g}임을 보였음.

-optimal 하지 않은 경우를 고려하기 위해, p_{d}* = p_{g}e^{d(x)}/Z_0인 Boltzmann distribution을 정의하였음. 이때 Boltzmann distribution은 물리학에서 사용하는 분포가 그 분포가 맞으며, p = e^{-E(x)}/Z 라고 정의됨. 따라서, 위의 경우 Energy function은 E(x) = -log(p_g) - d(x)임.

-위의 Boltzmann distribution은 2가지 특징을 가지고 있는데, (1) optimal discriminator일 때 p_{d}* = p_{d}임, (2)  Boltzmann distribution은 implicit generator분포의 bias를 올바른 방향으로 수정해 줌.

-따라서 위에서 정의한 Boltzmann distribution에서 이미지를 생성해주면 real distribution에 가까울 것인데, 문제는 Boltzmann distribution이 implicit distribution p_{g}와 intractable한 값인 Z_0와 연관되어 있어 샘플링을 하기가 힘들다는 문제가 있음.

-하지만, data distribution에서 MCMC를 진행하는 것은 비싸기에, rejection sampling에 관한 lemma1을 사용하여 Boltzmann 분포를 induce할 수 있는 새로운 p_{t}(z)를 정의함.

-이제 재료가 다 모였으니, Langevin sampling을 통해 data generation을 하자!

-WGAN의 경우 EBM인데 K-Lipschitz regularization이 적용되고, p_{d}*대신 p_{g}로 minimax게임을 수행한 EBM의 approximation이라고 간주하였음.  또한, WGAN에 가정된 EBM을 KL minimax 관점에서 Kantorovich dual과 수식적 결과가 일치함을 보였음.
 
실험:

토이데이터 세트와, CIFAR10, ImageNet 데이터세트를 사용해서 실험이 수행되었으며, pre-trained된 모델에 논문에서 제안한 DDLS을 수행하여 성능향상을 IS, FID를 통해 측정하였음. 당연 결과는 더 좋다고 나왔겠지만, 2020년에 나온 논문이고, 당시에 SOTA모델인 BigGAN, StyleGAN2에 대한 실험이 없다는 것이 너무 아쉬웠음. 또한, Conditional GAN에 DDLS를 적용하는 방법에 대한 이론적 증명과 설명이 없어 실제 GAN에 사용할 때는 주의가 요구되는 것 같음. 마지막으로 pixel space에서하는 MCMC와 latent space하는 MCMC의 속도차이에 대한 분석도 있었으면 좋지 않았을까 생각됨.
