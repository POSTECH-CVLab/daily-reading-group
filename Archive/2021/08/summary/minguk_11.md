# Dual Projection Generative Adversarial Networks for Conditional Image Generation
### Ligong Han, Martin Renqiang Min, Anastasis Stathopoulos, Yu Tian, Ruijiang Gao, Asim Kadav, Dimitris Metaxas
#### Summarized by Minguk Kang

총평:

1. Conditional GAN을 두가지로 나누었음. 첫번째는 label matching (p(y|x), q(y|x))이고, 두번재는 data matching (p(x|y|, q(x|y))임. ACGAN은 label matching에 PD는 data matching을 하는 모델임.
	
2. 하지만, ACGAN의 생성 성능이 왜 안좋은지에 대한 분석은 없는 것 같음.
	
3. 제안된 Dual Projection GAN의 경우 PD와 마찬가지로 Vanilla Adversarial Loss를 가정하고 있으므로, Hinge loss에도 그 이론적인 가정이 유효할지는 모르겠음.
	
4. 논문에 생략된 내용이 많아 이해하는데 어려움이 있었음.
	 

Task: Develop a new projection-based GAN for conditional Image generation.
 

Motivation: PD는 data matching을 기본으로 하기에 생성된 이미지의 embedding을 뽑아보면 제대로 disentangle되어 있지 않음. 따라서, label matching을 할 수 있는 추가적인 loss를 Projection discriminator에 도입하면 성능향상을 도모할 수 있지 않을까라는 동기가 있음.

 

Method: Projection discriminator는  두개의 proxy가 tie되어 있는데, 본 논문에서는 label matching을 위해 하나로 tied된 V를 V_true와 V_fake로 untie하였음. untie된 proxy를 바탕으로 cross-entropy losses를 추가하는데, 이는 위에서 언급했듯 data matching만 할 수 있는 PD의 단점을 해결하기 위한 방법임.  위와 같은 방식으로 projection discriminator에 classification losses들이 coupling 된 모델을 dual projection GAN이라고 명명하였음. Dual projection GAN은 data matching과 label matching을 동시에 수행할 수 있다는 장점을 가지고 있고, Imagenet 생성과 같은 label matching이 어려운 학습을 할 때는 자연스럽게 data matching만 하도록 reduce되어 데이터셋 무관하게 원하는 분포를 잘 학습할 수 있다는 특징을 가지고 있다고 주장하고 있음 (본인은 아니라고 생각).


Experimental Results: 실험은 StudioGAN을 사용하여 수행되었으며, CIFAR10 dataset에서 PD대비 std안에 들어올 정도로 마이너한 성능 향상을 보여주었음. 하지만, ImageNet 256 배치 실험의 경우 FID값이 16.86으로 기존 baseline (BigGAN 23.07) 대비 상당한 성능 향상을 보여주는 것을 확인 할 수 있었음. Imagenet을 학습할 때는 Dual projection GAN이 PD로 reduce 된다고 했는데 생성 성능이 더 좋아지는 이유에 대해서는 규명할 필요가 있다고 생각함.
