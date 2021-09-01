# cGANs with projection discriminator
### Takeru Miyato and Masanori Koyoma
####Summarized by Minguk Kang
---
총평: 
	
Conditional Image Generation 분야에서 널리 쓰이고 있는 방법으로, BigGAN과 StyleGAN (약간 수정된 방식으로)이 해당 방법을 차용하고 있음. 

기존 Classifier-based GAN의 early training collapse (논문 5 page 5.1)와 unstable training 문제에서 비교적으로 자유로운 새로운 프레임워크인 projection discriminator를 제안한 breakthrough 논문이라고 생각함.
	
몇가지 가정과 수식전개가 정확하지는 않지만, Conditional GAN을 하는 사람은 반드시 정독해야하는 논문이라고 생각함.

Task: Conditional Image Generation using GAN
 
Motivation: 기존 Classifier-based GAN들은 ImageNet과 같은 복잡한 데이터를 생성하기 위해서 multiple generator and discriminator가 필요하다. 따라서, single generator and discriminator pair만 가지고 large-scale image generation을 할 수 있는 모델을 개발하면 어떨까?
 
Method: 해당 논문은 Ian Goodfellow의 GAN 논문에서 소개된 p(x), q(x)에 대한 Adversarial training object를 joint distribution p(x,y), q(x,y)로 확장하면서 시작한다. 해당 adversarial training object는 "vanilla gan objective"를 쓴다는 가정하에 두가지 likelihood ratio들의 합으로 decomposition이 가능한데, 첫 번째는 조건부 분포 p(y|x) 와 q(y|x)의 likelihood ratio 두번째는 p(x)와 q(x) 사이의 likelihood ratio이다. 해당 논문에서 Miyato and Koyoma는 conditional likelihood ratio에 대해서는 우리가 일반적으로 알고 있는 logistic regression model로 디자인을 하고 marginal likelihood ratio에 대해서는 따로 모델 가정을 하지 않는다. 또한, logistic regression model로 디자인 된 conditional likelihood는 분모와 분자를 분리하여 class embedding과 feature embedding 사이의 내적값과 분자의 partition constant로 나눌 수 있는데 partition constant는 class label과는 무관하기 때문에 두의 marginal likelihood를 예측하는 모델과 합하여 새로운 projection discriminator loss를 디자인 하였다. 
 
실험: IS, FID 측도를 사용해서 Imagenet 생성 실험을 수행하였으며, ACGAN 대비 높은 Inception score와 낮은 Intra-class FID를 달성하였다. 또한, CIFAR10 and CIFAR100을 사용해서도 조건부 이미지 생성 실험을 하였는데 결과는 Appendix의 Table3에 있고 역시 Projection discriminator가 ACGAN 보다 더욱 좋을 생성 성능을 보여줌을 확인할 수 있다.
 
한계:
	
논지 전개 시작을 vanilla gan loss에서 유도되는 likelihood ratio에서 시작하는데, 정작 학습은 hinge loss에서 수행하였기에 이론과 실제 구현이 전혀 맞지 않음
	
또한, partition function이 class와는 관계없는 함수라고 생각해서 marginal likelihood 텀과 합치는데, partition function을 계산하기 위해서는 각 class embedding에 대한 정보가 필요하고 이는 특히 주어진 이미지의 corresponding label과 커플링 되어있으므로 이론적으로 해당 부분을 좀 더 보완할 필요가 있어보인다. 
