# Activation Maximization Generative Adversarial Nets
### Zhiming Zhou, Han Cai, Shu Rong, Yuxuan Song, Kan Ren, Weinan Zhang, Yong Yu, Jun Wang, ICLR 2018
#### Summarized by Minguk Kang
---

총평: 
	
LableGAN generator objective function을 logit에 대해 미분하여 overlaid-gradient problem을 해석적으로 발견하고, 이를 새로운 AMGAN loss를 통해 해결하였음.
	
LabelGAN의 내용을 숙지하고 논문을 읽는게 중요한데, LabelGAN에 대한 설명이 부족하여 이해하는데 어려움이 있었음.
	
AMGAN과 ACGAN의 차이점을 잘 설명하였고, ACGAN의 문제점 (classifier가 adversarial training을 하지않음)을 activation maximization 관점에서 잘 지적하였음.
	
2018년 논문이고, CIFAR10 Tiny ImageNet에서만 성능 확인을 했기에 실제 large-scale image generation에서 효과적일지에 대한 의문이 있음. 

Task: Conditional Generative Adversarial Networks
 
Method:
AMGAN 학습 방법은 정말 간단합니다. cGAN이 adversarial learning과 classification learning을 같이 하도록 하기위해 discriminator 학습시 real image는 classification을 잘 하도록, fake dataset은 k+1 class를 예측하도록 학습합니다. 다음으로, generator를 학습할 때는 fake image의 dynamic label (activation이 가장 높은 값)을 예측하도록 강제하는데, 이를 통해 non-hierarchical하게 conditioning을 하는 GAN이 되게 됩니다. 이때 프레임워크의 이름이 Activation Maximization GAN인 이유는 fake 이미지에 대해서 conditional adversarial training (해당하는 logit의 값을 minimization and maximization 하는 activation maximization process)을 수행하기 때문입니다. 
 
Results:
baseline 비교는 ACGAN, LabelGAN, vanillaGAN을 사용하여 CIFAR10, TinyImageNet 생성 실험을 통해 수행하였습니다. IS과 AM Score를 기준으로 outperform하는 것을 보였으며, Improved GAN, ACGAN, WGAN-GP, SGAN등의 당시 최신 모델과 비교를 통해 CIFAR10에서 가장 높은 IS값을 보여주는 SOTA모델임을 증명하였습니다. 하지만, 평가에 사용한 AM score는 IS가 real dataset에 비해서 많이 부족한 상황에서 0.08의 아주 낮은 값을 보여주었기 때문에 실제로 image의 diversity를 잘 잡아낼 수 있을지에 대한 우려가 있을 것으로 예상됩니다.
