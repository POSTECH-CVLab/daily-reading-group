# Closed-Form Factorization of Latent Semantics in GANs

### Yujun Shen, Bolei Zhou, CVPR 2021

#### Summarized by Minguk Kang
 
---
총평:
	
논문에서 제안하는 SeFa (Semantic Factorization)은 pre-trained generator만 있으면 추가적인 semantic labeling 또는 Feature extraction이 필요없다는 장점을 가지고 있다. 
	
경쟁 논문인 GANSpace에 비해 연산 부담이 적으며, latent navigation을 하는 방법에 대한 justification이 명확하다. 
	
하지만, SeFa를 통해 얻어진 navigation vector가 image semantic상에서 어떤 역할을 하는지에 대한 분석이 부족하다.
	
또한, z를 살짝 바꿨을 때 생성되는 이미지의 variation이 큰 방향이 이미지의 유의미한 semantic을 바꿔줄꺼라는 가정에 대한 분석이 부족한 것 같다.
	 

Method:

-저자는 먼저 GAN Generator의 latent variable z에서 이미지 X로 가는 non-linear mapping을 consecutive mapping들의 composition이라고 생각하였다.

-consecutive mapping의 가장 앞부분 linear layer를 보면, y = G_{1}(z)라고 볼 수 있고, 이는 y = Az + b로 나타낼 수 있다.

-만약, Z space상에서 semantic을 바꾸는 direction n을 찾을 수 있다하면, G_1(z+\alpha*n) = y + \alpha*A*n으로 표시할 수 있다. 

-이때 manipulation process는 sample independent한 것을 확인할 수 있다 (한번 계산해놓고 여러 샘플에도 적용가능!).

-G_1(z+\alpha*n)는 \alpha*A*n이 클 수록 많이 변함으로, 이를 최대화하는 n을 라그랑지안 multiplier를 사용하여 구한다. 

-구한 결과는 놀랍게도, A\topA의 the largest eigen vector이다. 
 
실험:

실험은 Progressive GAN, StyleGAN, BigGAN을 통해 진행되며, FFHQ, anime faces, scenes and objects (LSUN, streetscapes, ImageNet)데이터 세트를 사용해서 진행되었다. Quantitative하게는 GANspace와 비교하여 FID, Re-scoring, User-study를 기준으로 더 좋은 결과를 보여주었다. 또한, Supervised Image editing 방법과 비교를 했는데, 레이블링이 되지 않은 attribute까지 SeFa가 잘 캐치하여 바꾸는 보습을 보여주며 SeFa가 레이블링이 필요하지 않고, 효율적인 알고리즘임을 증명하였다.
