Denoising Diffusion Probabilistic Models
 
**Task**: Image generation using a new probabilistic model
 
**Motivation**: Generative Adversarial Networks have two shortcomings: (1) training GANs is extremely hard and (2) generated images are not diverse. So, the authors of this paper propose a new sort of generative model named denoising diffusion probabilistic model (DDPM) whose theoretical ground stems from diffusion and denoising processes of non-equilibrium thermodynamics.
 
**Method**: DDPM consists of two processes: forward (denoising) process and reverse process. In the case of forward process, they assume that each forward process follows a conditional gaussian distribution with pre-defined mean and variance. In addition to this, the each forward process should follow Markov property. This two constraints are applied to each reverse process too, but the mean and variance are not known. Thus, the objective of DDPM is estimating means and variances of each reverse process and sampling clean images using conditional gaussian distributions and Markov property. To do so, the authors of this paper simplify maximizing likelihood of observed dataset to minimizing one of its variational upper bound under conditional gaussian and Markov assumption. Using the fact that a neural network is an universal function approximator, the authors train a neural network to estimate unknown mean and variance of conditional gaussians in the reverse process.  
 
**총평**: Diffusion model의 본격적인 유행을 알린 논문이라고 생각함. Diffusion model 학습을 위해서는 몇 가지 디자인 초이스들이 있는데, 이를 score-based model 및 langevin dynamics와 잘 연관지어 선택해 나갔다고 생각됩니다. 어려운 수학내용에 비해서 라이팅은 정말 깔끔하게 적혀있으며, CIFAR10을 기준으로 unconditional image generation에서 SOTA를 찍었기 때문에 향후 conditioning 방법이 개발되어 Imagenet과 같은 더 복잡한 데이터세트에서도 좋은 성능을 보여줄 것이라 기대됩니다.
