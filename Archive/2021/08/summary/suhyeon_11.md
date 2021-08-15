# Sampling Matters in Deep Embedding Learning
### Chao-Yuan Wu et al. (UT Austin , Amazon) - ICCV 2017
#### Summarized by Suhyeon Jeong
---

**Overview** : triplet/contrastive loss 등으로 embedding learning 을 할 때, loss 의 형태보다 sample selection 이 훨씬 중요한 역할을 함을 보이고, distance weighted sampling 이라는 sampling strategy 를 제시하였음(outperforms current SOTA). 추가로, simple margin based loss 가 다른 loss 를 outperform 함을 보였음.

**task** : metric learning 
 

**Motivation** : contrastive loss 에서 hard negative 는 빠른 convergence 에 도움을 주지만, triplet loss 에서는 오히려 collapsed model 을 유발한다. FaceNet 에서는 semi-hard negative mining 으로 적절한 난이도의 sample 을 뽑아 이를 피해 갔다. 이와 같이 sampling 은 학습에 매우 큰 영향을 미치기 때문에 좋은 sampling strategy 를 찾는 것은 중요하다. 

 

**Method** : 

**Other sampling strategy** : embedding 을 normalize 하므로, embedding space 를 n 차원의 unit sphere 로 생각할 수 있다. sample 들이 embedding space 상에 uniform하게 분포한다고 가정하면, random sampling 의 경우 n 이 커질수록 pairwise distance 들이 2^(1/2) 을 평균으로 하는 normal distribution 에 가까워진다. dimension 이 높을수록 variance 는 작아진다. 이렇게 될 시, distance 가 큰 너무 쉬운 sample 들로 가득해서 학습이 잘 이루어지지 않는다. 반면 너무 어려운 negative example 들을 sampling 할 경우, distance 가 작아 gradient 의 variance 가 커지게 되어 학습을 방해한다 (noise sensitive). semi-hard negative mining 은 training 이 어느 정도 진행되면 구간 내의 sample 들이 사라져 학습이 더 이상 진전되지 않거나 local minima 에 빠지게 된다. 위의 문제들은 sampling 된 example이 각각 특정 distance 구간에만 몰려 있어서 발생하게 된다. 

 

**distance weighted sampling** : distance 에 대해 uniformly sampling 하도록 pairwise distance 의 inverse 를 weight 로 설정하여 sampling 을 진행한다. 이 때, distance 가 작은 noisy sample 들을 줄이기 위해 weight 를 clip 한다. 

 

**margin based loss** : boundary b 를 기준으로 positive sample 은 margin a 보다 더 작은 distance 를 가지도록, negative sample 은 a 만큼 보다 더 큰 distance 를 가지도록 loss를 구성하였다. boundary b 는 flexible boundary parameter와  class-specific, example-specific term 의 합으로 구성되며, 모델과 같이 학습되게 된다.

 

**총평** : triplet loss, contrastive loss, margin based loss 에 대한 분석과 embedding 에 대한 수학적인 접근들을 정리해 놓은 좋은 논문이었다. 언급한 loss 및 embedding 에 관해 수학적으로 이해하는 데 도움이 되었다.
