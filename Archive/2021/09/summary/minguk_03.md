# Lipschitz Generative Adversarial Nets
### Zhiming Zhou, Jiadong Liang, Yuxuan Song, Lantao Yu, Hongwei Wang, Weinan Zhang, Yong Yu, Zhihua Zhang, ICML 2019
#### Summarized by Minguk Kang
---
 

총평: 


	
Auxiliary Discriminative Classifier GAN과 함께 올해 읽은 GAN 논문 가장 재미있게 읽었던 논문 중에 하나임.
	
기존에 WGAN이 다뤘던 Gradient Vanishing 문제와는 다른 Gradient uninformative 문제를 다루고 있음. 
	
Gradient uninformative 관점으로, 기존 unrestricted GAN과 IPM 기반의 GAN들이 가지고 있는 문제점을 이론적으로 실험적으로 잘 지적하였고, 이를 해결한 Lipschitz constrain을 가정한 discriminator의 좋은 특징 1) 학습된 discriminator가 generator에게 어떤 real image direction으로 학습하도록 가이드를 해줌 (fake image가 어떤 real image에 coupling되어 있음), 2), real 과 fake distribution이 겹칠 때 density가 다르면 fake x가 어떤 real y로 update되도록 함, 3) Unique Nash equilibrium일 때 f*_{\deriv x} =0이기에 oscillation이 없음 (저자의 수학실력이 감탄스러움)을 이론적으로 실험적으로 잘 보인 논문이라고 생각함.
	
Writing이 clear하게 적혀있음. 저자의 이전 논문에서도 느꼈지만, writing을 정말 잘하시는 것 같음.

 
Method:
-저자는 먼저 gradient informative problem이 무엇인지 gradient vanishing이랑 무엇이 다른지에 대해서 확실하게 설명함. Gradient vanishing은 discriminator function f와 non-saturation, hinge, least square loss의 차이를 만드는 꼭지 함수 \phi, \pi, \psi 사이의 관계이며, gradient informative는 gradient \deriv{f(x)_{x}}의 방향에 대한 문제라는 것을 확실히 함.
-Unrestricted GAN은 gradient vanishing 뿐만아니라, gradient informative 문제에도 시달린다는 것을 보였음.
-IPM 기반 GAN은 gradient vanishing에서는 자유로울 수 있으나, gradient uninformative문제는 여전이 존재한 다는 것을 Fisher GAN을 통해 설명하였음.
-WGAN은 Fisher GAN과는 다른게 IPM기반 GAN이지만 gradient informative 문제에서 자유로움을 보여주었고, 왜 그런지에 대한 물음을 던짐.
-하지만, WGAN은 optimal critic f*가 unique하지 않고, 1-Lipschitz constrain만을 걸어주기에 Nash equilibrium에 도달하여도 gradient가 있어 oscillation할 수 있음을 지적함.
-이러한 문제를 모두 해결할 수 있는 새로운 GAN의 family인 Lipschitz GANs (LGAN)을 제안함.
-LGAN은 꼭지 함수가 특정 조건을 만족한다는 가정하에 Lipschitz constant를 0으로 줄이는 regularization과 함께 구성될 수 있음.
-Lipschitz regularization은 WGAN-GP와 같이 real과 fake image사이의 interpolation 이미지 x_t의 batch 내에서 largest norm을 0으로 줄이는 방식으로 구성됨. 이를 Max Gradient Penalty라고 명명하였음.
 
실험:
-우선 기존 GAN들이 Gradient uninformative 문제를 격고 있다는 것을 보여주기 위해 2 gaussian mixture model과 10개의 CIFAR10 이미지를 real distribution으로 가정하고, least square loss과 LGAN loss로 gradient의 방향을 확인해봤음.
-CIFAR10, Tiny-ImageNet데이터를 사용하여 unconditional image generation 실험을 수행하였음. 실험 결과는 당연히 LGAN이 기존 hinge loss GAN과 LSGAN의 성능을 뛰어넘었음.
-하지만 Large scale image generation 실험을 수행하지 않았고, x_t를 구하는 과정으로 인해 계산 복잡도가 상당히 올라간다는 것은 단점이라고 생각함. 또한, Tiny-ImageNet실험에서 IS과 FID값이 StudioGAN의 결과와는 너무 다르게 나와서 어떤 차이가 있는지 의아하며, extensive한 이론 결과와는 반대로 real image generation 실험 부분이 많이 빈약하다고 생각됨.
