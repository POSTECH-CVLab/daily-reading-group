# Momentum Contrast for Unsupervised Visual Representation Learning
### Kaiming He et al.(Facebook AI Research) - CVPR 2020
#### Summarized by Jinoh Cho
	
# Task: unsupervised visual representation learning
	
# Motivation:
	 
Unsup representation learning have shown successful results in NLP field such as GPT and BERT.
		
Unsup representation learning의 성공을 컴퓨터 비전 분야에도 contrastive learning approach를 사용해서 확장하려고 함.
		
먼저, contrastive learning의 경우 negative와 positive sample들에 대한 representation을 담고 있는 dictionary look-up으로 볼 수 있는데,
좋은 dictionary를 만들기 위해서는 (1) large(다양한 negative pair를 갖춘 샘플수가 많은), (2) consistent dictionary 라는 특성을 갖추어야 한다.
	
	



# Method:

좋은 dictionary의 조건으로 (1) large, (2) consistent 라는 가정을 하고 시작한다.
		
이러한 좋은 dictionary가 갖추어 졌다면 좋은 representation을 배울 수 있을 것이다.
		
이러한 조건을 위해서 MoCo에서는 large dictionary를 위한 queue라는 data structure를 도입하고, Consistent한 표현을 extract하기 위해서 느리게 업데이터 되는 (Momentum을 가지고)업데이트 되는 key encoder가 필요하다.
		
먼저, MoCo에서는 앞에서 말했듯이 dictionary를 queue로 만들었다. 이를 통해서 이전 mini-batch에서 사용했던 encoded key를 재사용 함으로써 negative samples의 수를 늘릴 수 있다는 장점이 있다. 이를 통해서 최근의 mini-batch는 새로운 queue로 들어가고, 오래된 mini-batch에 대한 representation은 queue에서 제거하게 된다.
		
하지만 queue를 무작정 크게 늘리게 된 상태에서 key encoder와 query encoder를 업데이트 하게 되면(두 인코더는 다를 수 도 있고 같을 수도 있음), back-prop을 통해서 업데이트를 하기엔 연산량의 문제가 있음.
		
이에 대한 가장 간단한 솔루션으로는 key encoder parameter를 query encoder로 부터 그대로 복사해오는 것인데, 이는 parameter를 급격하게 바꾸기 때문에 성능이 별로 좋지 않다는 것을 실험적으로 보여준다.
		
따라서, 이 논문에서는 consistent한 key encoder를 학습을 하기 위해서 느리게 학습되는(모멘텀을 가지고 학습되는) key encoder학습 기법을 제안한다. query 인코더만 단순하게 back prop을 통해서 학습을 시키고, key encoder 파라미터를 업데이트 할 때에는 다음과 같이 업데이트 한다.
		
θk ← mθk + (1 − m)θq. 여기서 theta_k는 key인코더의 파라미터, theta_q는 queue인코더의 파라미터이며 m은 0.9나 0.999와 같은 값을 가진다.
		
기존의 key 인코더의 파라미터에 가중치를 더 많이두고 백 프롭으로 업데이트 된 query encoder에는 적은 가중치를 두고 업데이트를 하는 방법으로, 기존 파라미터 값에 대한 관성을 가진체로 key 인코더가 천천히 업데이트 된다고 보면 된다.
		
# Strong Point :
	
1. MoCo can outperform its ImageNet supervised per-training counterparts in 7 detection or segmentation tasks. 이 외에도 여러 task에 on par한 결과를 보여줌.
=> MoCo has largely closed the gap between unsupervised and supervised representation learning in multiple vision tasks.

2. MoCo can perform well on large-scale, relatively uncurated dataset
	
# Weak Point :
	
1.Long training time, large computation power needed ??? need to be checked carefully.(모멘텀을 가지고 업데이트 해나가서 학습이 오래 걸릴 거 같음??)
	 	
