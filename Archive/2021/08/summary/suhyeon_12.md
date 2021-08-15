# Wasserstein gan
### Martin Arjovsky et al. (Courant Institute of Mathematical Sciences, Facebook AI Resarch) 
#### Summarized by Suhyeon Jeong
---

**Overview** : EM distance 를 이용해 data distribuiton 을 학습하는 generative model, Wasserstein-GAN 을 제안함

 

**task** : 2d image generation

 

**Method** :


**Earth Mover distance (Wasserstein-1)** : 두 distribution 간의 distance 를 측정할 때, 기존의 TV distance / KL divergence / JS divergence 의 경우 두 distribution 이 서로 겹치지 않으면 두 distribution 이 가까워 지더라도 항상 고정된 값을 가진다.  논문의 Example 1 에서 간단한 예시를 통해 확인할 수 있다. 특히 학습 초반에는 두 distribution 간 겹치는 부분이 많지 않은 데다 distribution 내 가능한 모든 sample 들을 보는 것이 아닌 batch 로 그 중 일부만 보기 때문에 두 확률 분포가 겹치는 부분 없이 서로 다른 영역에서 측정될 가능성이 높다. 이럴 경우 서로 겹치는 부분이 생기기 전까지 distance 는 수렴하지 않고 고정된 값을 가지게 되며, GAN 에서 이러한 현상은 학습이 되지 않는 중요한 원인이 되기도 한다. 그리하여 두 확률분포의 차이를 덜 strict 하게 계산하여 언제든 useful gradient 를 제공하는 EM distance 를 도입한다. 
EM distance 는 distribuiton 이 겹치는 정도에 의존해 distance 를 계산하는 기존의 세 방식들과는 달리, 두 distribution 내 sample 들의 거리를 base로 계산한다. 뽑힌 sample 들에 따라 distance 는 다르게 측정될 수 있는데, EM distance 는 그 중 가장 작은 distance 기댓값이며, 해당 기댓값을 가지는 sample 들을 뽑는 joint distribution 을 학습한다.

 

**WGAN** : 
discriminator 대신 EM distance 를 사용해 이를 최소화하는 것을 loss로 하여 학습한다.
EM distance 를 구하기 위한 joint distribution 을 구하기 위해서는 ground truth data distribution 을 알아야 하나, 이는 우리가 모르는 것이기 때문에 직접적으로 EM distance 를 구하긴 힘들다. 대신 Kantorovich-Rubinstein duality 를 이용하여 식을 바꾸고, 1-Lipschitz function 을 k-Lipschits 를 만족하는 parameterized family of function , F_w 로 치환하면 문제를 w 에 대한 optimization problem 으로 바꿀 수 있다. 이를 이용하여 iteration 마다 function F_w (critic)를 먼저 어느 정도 학습하고, 학습된 critic 으로 EM distance 를 계산하여 본 모델을 학습시킨다. 

 

**총평** : GAN 분야의 기본적이고 고전적인 논문이지만 수학적인 base 가 잘 다져져 있지 않으면 이해하기가 어려운 논문이었다. 덕분에 여러 distance metric (+KL divergence) 들에 대한 이해도를 높이고 여러 재미있는 theorem 들을 공부하는 좋은 기회가 되었다.
