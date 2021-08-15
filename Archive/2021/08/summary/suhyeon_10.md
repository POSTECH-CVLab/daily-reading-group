# FaceNet: A Unified Embedding for Face Recognition and Clustering
###  Florian Schroff et al. (Google) -  CVPR 2015
#### Summarized by Suhyeon Jeong
---

**Overview** : triplet-loss 를 제안한 유명한 논문.


**task** : metric learning / face recognition



**Method** : 

**Triplet loss :** anchor, negative pair, positive pair 가 있을 때, anchor -positive 사이 distance 가 0에 가까울수록, anchor-negative 사이 distance 가 클 수록 loss 가 작아진다. (e.g. negative pair 는 anchor 와는 다른 사람의 얼굴, positive pair 는 anchor 와 같은 사람의 얼굴)


	
**margin at loss** : negative sample 들이 positive sample 보다 margin 만큼 더 먼 distance 를 가지도록 유도한다. 
	
**semi-hard negative** : all possible triplet/random sampled triplet 으로 학습하는 경우, 대부분의 triplet 이 구별이 쉬운 case 들이어서 학습이 빠르게 converge 하지 않는다는 단점이 있다. 빠른 학습을 위해 다음의 triplet selection 을 제안하였다.
	

		
**->positive** : use all anchor-positive pairs in minibatch
		
**->negative** : semi-hard , 즉 positive 보다 distance 가 가까운 negative sample 들은 탈락시키고(hard case) , positive 보다 멀고, positive + margin 이내의 distance (still difficult enough)에 위치한 negative sample 을 선택한다. 
	
	


 

**harmonic embedding** : 기존에 학습된 모델 v1 의 embedding을 함께 이용하여 새로운 모델 v2 를 학습시키면 v1 의 성능을 능가하는 모델을 학습시킬 수 있다. 각 pair 들을 서로 다른 모델의 embedding 을 들고와 선택하여 학습하는 등, 두 embedding 을 혼용하여 모델을 학습시키면 기존 v1 에서 misclassified 된 face 들을 올바른 cluster 에 속하도록 embedding 을 발전시킬 수 있다. 학습이 잘 되도록, v2 모델은 last layer 부터 학습시킨 후, 이후 전체를 학습한다(knowledge distillation 의 냄새가 난다).

 

**총평**: triplet loss 를 제안한 유명한 논문. triplet loss 에 대해 (sampling 부분) 잘 몰랐던 부분이 있어 읽어 보았음
