Conditional Image Synthesis with Auxiliary Classifier GANs - ICML 2017


Overview : 

1. They introduce new specialized cost function which utilize cross entropy loss to train cGAN.
2. They provide two new analyses for assessing the discriminability and diversity of generated images.

Task : Conditional Image Generation


Motivation : New methods for the improved training of generative adversarial networks for image synthesis.

Method & Exp: 

	0. Loss Function : 
  <img src='Archive/2021/08/image/jinoh_210826.png'>
	D is trained to maximize Ls + Lc while G is trained to maximize -Ls + Lc.

	1. Generating High Resolution Images Improves Discriminability.

Pretrained Inception Network를 사용해서 네트워크가 얼마나 알맞게 class를 맞췄는지 비율을 통해서 비교.
Accuracy가 높으면 이미지에 class information을 많이 담고 있다는 것을 의미.
64 by 64 과 128 by 128 resolution을 생성하는 두 ACGAN 모델을 준비.
두 모델에서 생성된 이미지를 16 by 16, 32 by 32, 64 by 64, 128 by 128, 그리고 256 by 256 이미지로 resizing을 해서 resolution - inception accuracy 그래프를 그려보면 128 by 128 ACGAN 모델에서 생성된 이미지를 통해서 resizing한 이미지들이 훨씬 inception accuracy가 높은 것을 볼 수 있었다. 이를 통해서 고해상도 이미지를 생성하는 ACGAN을 통해서 생성해낸 이미지들이 단순히 저해상도 이미지를 resizing하는 것보다 훨씬 더 content를 표현하는데 중요한 정보들을 담고 있다는 것을 보여주었다. 

	2. Measuring the Diversity of Generated Images

생성 모델이 다양한 이미지를 생성 했는가에 대한 척도로 위의 실험에서 사용했던 방법을 사용하기에는 적절치 않다. 왜냐하면 각 클래스 당 좋은 품질의 이미지 한 개만 생성하도록 네트워크가 외우게 되더라도 inception accuracy가 높게 나올 수 있기 때문이다. (Partially mode collapse) 이에 논문에서는 기존의 이미지 간의 similarity metric으로 사용했던 MS-SSIM 방법을 이용하여 Diversity를 측정하는 방법을 제안한다. 한 클래스에 대해서 여러 개의 이미지를 생성을 해서 생성된 이미지들간에 similarity를 측정하여 similarity가 낮으면 Diversity가 높다고 주장을 한다. 

이 외에도 training이 collapse가 됬는지 MS-SSIM - iteration 그래프를 통해서 알아볼 수 있는데, training이 잘 진행되고 있으면 MS-SSIM이 점점 낮아지는 것을 볼 수 있지만, MS-SSIM이 갑자기 증가하기 시작하면 training collapse를 판단 할 수 있게 된다.

	3. Generated Images are both Diverse and Discriminable

이 부분에서는 앞에서 제안한 두가지 metric이 어떤 관계가 있는지 알아보기 위한 실험이다.

MS-SSIM - Inception Acc 커브를 보여주는데, 여기서 살펴보면 MS-SSIM > 0.25(Diversity가 낮은 경우)에서 74퍼센트의 class들에서 모두 Inception Acc가 1% 아래로 나왔다. 게다가, MS-SSIM < 0.25 (Diversity가 높은 경우)에서 78%의 class들에서 모두 Inception Acc가 1%를 초과하였다.  이러한 결과는 GAN의 Drop Modes가 low quality image를 생성하는 것을 보여준다. 

	4. Comparison to Previous Results

CIFAR-10을 사용한 Inception Score를 당시 SOTA인 8.09(Improved Techniques for Training GANs)와 유사한 8.25의 결과를 report함.

	5. Searching for Signature of Overfitting

이 부분에서는 AC-GAN이 training data에 overfitting이 일어나지 않는지를 확인한다.
제일 먼저 시도 할 수 있는 부분이, generated sample에 대해서 k - Nearest Neighbor Search로 training data에서 top-k 개를 sampling을 하여 유사한 이미지가 있는지 살펴본다. 이를 살펴 보았을 때 ACGAN은 training data를 거의 외우지 않는 것을 확인 할 수 있었다.

또한 overfit된 모델이서 우리가 관찰 할 수 있는 특징으로는 latent space interpolation에서 discrete transition이 일어난다는 것인데, AC-GAN에서는 이러한 모습을 거의 찾아 볼 수 없었다. Semantically Meaningful하게 interpolation이 되는 것을 확인 할 수 있었다.

	6. Measuring the Effect of Class Splits on Image Sample Quality

이 부분에서는 ImageNet으로 AC-GAN을 학습 할 때 100개의 모델을 만들어서 각 모델당 10개의 class를 학습 시키는 것이 10개의 모델을 만들어서 100개의 class를 학습시키는 것보다 훨씬 Diversity가 높은 image를 생성할 수 있다는 것을 보여준다. 한 모델에 많은 클래스를 학습을 시키면 mode collapse가 일어난다는 것을 보여준다. 이 외에도 모델을 diverse set of classes로 학습시킬 것인가 similar set으로 학습시키는 것이 좋은가에 대해서도 살펴보려고 했지만 확연한 차이를 발견하지 못했다고 말을 한다.

총평:
     새로운 Conditional GAN training 로스를 제안했다는데에 의의가 있음.
     생성된 이미지를 평가하는 여러가지 지표(MS-SSIM, Inception Acc를 활용)를 제안했다는 의의가 있음.
     논문의 Discussion Part에서 볼 수 있듯이, 앞으로의 GAN이 나아갈 방향에 대해서 잘 정리해 두었음. 
	
