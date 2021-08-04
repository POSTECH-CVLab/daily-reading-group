# Closed-From Factorization of Latent Semantics in GANs
### Yujun Shen et al., The Chinese University of Hong Kong) - CVPR 2021
#### Summarized by Jinoh Cho
---

**Task**: Finding interpretable directions of the latent space in GANs via unsupervised way
	
	
	
**Motivation**:
		
* Previous works usually performed in supervised fashion, which requires sampling a collection of images and labeling them to train a classfifer. => They heavily rely on the attribute predictors or human annotators to get the label.
		
* GANspace paper also propose the way to find interpretable directions in latent space, but it still needs some sampling data step to apply PCA operation.
	
	
	
**Method**:

		
* GAN이 랜덤 노이스 벡터로 부터 생성하는 것을 우리는 affine transformation이라고 볼 수 있음.
		
* 이에 우리는 GAN을 G(z) = Az + b 라는 식 하나로 표현할 수 있게 된다. (z는 랜덤 노이스 백터)
		
* 여기서 우리가 latent space에 manipulation을 가하는 것을 함수로 표현하게 된다면 다음과 같이 쉽게 표현할 수 있다. edit(G(z)) = G(z') = G(z+alpha*n)
		
* G(z')을 우리는 풀어서 쓰게 되면 G(z') = G(z+alph\*n) = Az+b+alpha\*A\*n + b= G(z) + alpha\*A\*n + b으로 표현할 수 있게 된다.
		
* 우리는 G(z')-G(z)가 변화가 큰 방향으로 manipulation을 하길 원하기 때문에 결국 n\* = argmax||An||^2을 푸는 문제로 바뀌게 되고 이는 라그랑지안 멀티플라이어를 사용해서 쉽게 n\*을 구할 수 있게 된다.
		
* 라그랑지안 멀티플라이어를 도입하여 n에 대해서 편미분을 하게 되면 n\*은 A^T\*A의 eigenvector가 된다는 것을 쉽게 유도할 수 있다.
		
* 결국 pretrained된 갠 네트워크 파라미터를 이용해서 eigenvector를 찾는 문제로 바뀌게 되는 것이다.
		
* 이 가정을 이용해서 이논문에서는 PGGAN, StyleGAN, BigGAN 모델에서 meaningful한 direction으로 latent vector를 manipulation해보면서 실험 결과를 보여준다. 이 외에도 Supervised way로(InterFaceGAN) 찾아낸 latent space direction과 비교하는 실험을 보여주는데 이 실험에서도 거의 comparable한 결과를 보여준다. 뿐만아니라 GANSpace에서 mainpulation을 가한 결과보다 FID스코어도 좋으며 2k개의 mainpulation 이미지결과를 User들에게 보여주면서 control한 attirbute와 바뀐 이미지가 correspoing한지를 물어봤을때 SeFA(논문에서 제안한 방법)이 더 좋은 결과를 보였다. 
	
z**총평**: 간단한 수식 gan을 affine transformation으로 표현할 수 있다는 것에서 부터 간단하게 수식부터 시작해서 수학적으로 결론을 이끌어낸 이후에 이를 실험적으로도 잘 보인 것 같다. 다만 G(z')-G(z)가 변화가 큰 방향이 meaningful한 direction인가에 대한 의문은 아직 있다. (변화가 크게 되면 아예 이미지 컨텐츠가 바뀌면 되는 것이니깐...그래도 실험적으로 잘 보여서 잘 되는 것 같기두?? 하다..내가 잘못 생각한 것일까?, 그렇다면 컨텐츠를 유지하기 위한 Regularization 도입은 별로인가???)