# cGANs with Auxiliary Discriminative Classifier
### Liang Hou, Qi Cao, Huawei Shen, Xueqi Cheng, Neurips 2021 submission
#### Summarized by Minguk Kang
---
 
총평: 
	
1. 최근 읽은 논문 중 가장 재미있게 읽은 논문. 실험 결과가 아쉬운 것만 빼면, ACGAN의 mode-dropping에 대한 이론적 설명은 정말 흥미롭게 읽었음.
	
2. 논문 라이팅이 명료하고, Projection Discriminator의 단점 및 이론적 한계를 설명하는 부분은 본인이 Projection discriminator 논문을 읽을 때 생각했던 바와 정확히 일치하여 정말 재미있었음.
	
3. ContraGAN이나 ReACGAN과 잘 조화되면, 생성모델 소타인 ADM (Ablated Diffusion Model) 을 이길수도 있을 것이라고 예상됨.
	 

Task: Conditional Image generation using a classifier-based GAN.
 
Motivation: "ACGAN이 생성한 이미지의 recall이 낮은 이유가 있을까?"에 대한 질문에서 논지가 시작됨. Conditional GAN의 목적은 데이터와 레이블의 joint distribution (p(x,y))를 학습하는 것인데, ACGAN의 경우 Joint distribution을 학습하는 것과 marginal distribution matching하는 것 사이의 conflict가 생김. 또한, 조건부 엔트로피 H(Y|X)를 줄이는 방향으로 일어나는 학습은 데이터셋의conditional distribution가 겹치는 경우 mode-dropping을 야기할 수 있음.  따라서, 이런 두가지 term을 제거하고 ACGAN 학습을 성공적으로 할 수 있는 방법이 없을까에 대한 고민에서 시작된 논문임.
 
Method: 저자는 Projection discriminator가 위의 2가지 문제 없이 데이터의 joint distribution을 학습할 수 있는 이유를 optimal discriminator의 수식에 생성된 이미지의 분포에 대한 정보가 들어가기 때문이라고 생각하였음. 따라서, optimal classifier 수식에 생성된 이미지 분포에 대한 정보를 추가하려고 시도하였고, 결과적으로 adversarial learning 과 classification을 같이 수행하는 Auxiliary Discriminator Classifier (ADC)를 제안하였음. 저자는 제안하는 ADC기 이론적으로 위에서 언급한 두가지 문제에서 자유로울 수 있다는 것을 보였으며, MOG 데이터를 사용하여 실험적으로도 보여주었음. 또한, Projection discriminator의 단점에 대해서도 지적하는데, (1) Partition function에 대한 고려를 하지않고 \psi(x)로 퉁처버렸기 때문에 더이상 probabilistic model이 아니라는 점과 (2) PD는 adv loss가 vanilla loss라는 가정하에 유도된 식이므로 실제 구현 방식에서 사용하는 hinge loss를 쓰게되면 이론적 당위성을 잃어버린 다는 것임. 하지만, ADC는 이러한 가정에서 자유로우며, 따라서 어떠한 adversarial loss에도 잘 조화될 수 있음을 MOG 실험을 통해 보여주었음. 
 
Experimental results: MOG 데이터세트를 사용하여 overlapped distribution 학습을 ADCGAN이 더 잘할 수 있음을 보였음. 또한, CIFAR10, CIFAR100, Tiny-ImageNet 데이터세트를 사용하여 이미지 생성 결과를 평가하였으며 CIFAR10, CIFAR100에서는 ADCGAN이 Tiny-Imagenet에서는 PDGAN의 성능이 좋음을 IS, FID 점수를 사용하여 확인하였음.
