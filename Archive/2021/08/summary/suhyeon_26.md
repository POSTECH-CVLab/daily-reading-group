# A Unified Objective for Novel Class Discovery
### Enrico Fini et al. - ICML 2021 oral
#### Summarized by Suhyeon Jeong
---

 

**Overview** : 기존 SOTA 성능을 크게 뛰어넘은 unified objective method 를 제안함

**Task** : Novel Class Discovery (NCD) - inferring novel object categories in an unlabeled set by leveraging from prior knowledge of a labeled set containing different, but related classes

**Motivation** : 기존 method 들은 supervised pretraining-clustering 두 step 으로 나뉘어졌으며(two separated objectives), feature 들이 known classes 에 biased 되는 것을 줄이기 위해 supervised pretraining 이전에 unlabeled, labeled data를 전부 사용하여 self-supervised pretraining 을 추가하기도 했다. 복수의 objective 들은 많은 hyperparameter tuning 을 요구한다는 점, 그리고 이러한 self-supervised pretraining 들은 unlabeled set 이 바뀔 때마다 다시 self-supervised pretraining 을 해주어야 한다는 단점이 있었다. 이에 self-supervised pretraining 없이 single loss function 으로 학습하는 method 를 제안하고 기존 SOTA 를 상회하는 성능을 보임.

**Goal** : increase classification accuracy for labeled sample and increase clustering accuracy for unlabeled sample (for clustering accuracy metric, see equation (6) in paper)

**Method** :
**1)** Unified objective (overall architecture for single-view) : CNN encoder 를 거쳐 classification head 로 output 을 생성하는 기본적인 구조를 base 로 한다. Unlabeled data 의 class 수는 사전에 주어진다. Labeled data 의 class 를 판별하는 Labeled head, Unlabeled data 의 class 를 판별하는 unlabeled head 두 개가 존재하며, Labeled head 는 linear classifier, Unlabeled head 는 MLP+ linear classifier 이다. Labeled head 와 Unlabeled head 의 output 을 concat 하여 single cross entropy loss 로 한꺼번에 train 한다.(핵심) 즉 한 image 에 대해 unlabeled class 와 labeled class 에 대한 prediction 을 전부 진행하는데, ground truth label 로는 labeled data 의 GT label 뒤에 unlabeled class 수 만큼 zero padding 을 추가하고 unlabeled data 의 pseudo label 앞에 labeled class 수 만큼 zero padding 을 추가한 것을 사용한다.  

**2)** pseudo-labeling : Unlabled head 의 output 을 이용. Pseudo label 이 항상 같은 label 을 생성하도록 학습되는 것을 막기 위해 entropy 항을 추가한 optimize problem 을 Sinkhorn-Knopp 알고리즘으로 solve 하여 pseudo label 생성 (detail 은 Self-labeling via simultaneous clustering and representation learning - ICLR 2020 을 참고하라고 함.)

**3)** Multi-view : self-sup field 에서 하는 것 처럼 single image 로부터 data-augmentation 을 적용하여 two view v1, v2 를 뽑아낸다. 두 view 에서 각각 위에 언급한 method 들을 적용하여 loss 를 계산하는데, 이 때 두 view 에서 생성한 pseudo label 을 서로 바꾸어 loss 를 계산한다. (Swapped prediction task)(Labeled data 의 label 은 v1,v2 둘 다 똑같으니 상관 없다) +이 때 pseudo label 에 stop gradient 를 주어 labeled head 만 학습시킨다고 하는데, 이렇게 하는 이유나 그럼 학습 시 swapped prediction 을 했다 안했다 하는 건지 궁금하다.

**4)** Overclustering, Multi-head clustering : unlabeled data 에 대해 alternative partition (which is more fine-grained) 를 생성하는 overclustering head 를 training time 에 추가한다. 위에서는 two-head 인 경우를 다뤘지만, 이를 확장하여 multi-head 로 사용 가능하며, overclustering output 은 기존 multi-head output 에 concat 하여 학습한다. 이러한 multi-view, multi-head, over-clustering 으로 powerful representation 을 학습 가능하여 self-supervised pretraining 이 필요하지 않게 되었다고 한다.

**Experiment** : 기존 SOTA 와 비교해 꽤 큰 성능 향상을 보였음. labeled data 로 labeled head 를 먼저 200 epoch pretraining 하고 이후 both labeled/unlabeled data 를 사용해 학습함.


	
* clustering 과 supervised learning 을 하나의 objective 로 training 한 경우, 그렇지 않은 경우보다 엄청난 성능 향상을 보였음 (성능 향상에 핵심적인 기여) 특히, labeled data 의 classification accuracy 가 unlabeled dataset 에 비해 많이 올랐음.
	
* Overclustering 의 사용 역시 unlabeled data 에서 1-3 % 의 accuracy 향상을 보였음. labeled data 의 accuracy 는 변화가 거의 없었음. supervision 만으로 충분히 좋은 representation 을 학습할 수 있어서 그런 것 같음.
	
* Unlabeled set class 의 개수를 알아야 한다는 것이 단점인데, ablation study 에서 (Learning to discover novel visual categories via deep transfer clustering -ICCV 2019) 논문에서 제안된 optimal number of cluster 를 찾는 방법을 사용하여 unlabeled class 수를 찾고, 이를 이용해 본 모델을 돌렸더니 CIFAR100-20 data(20 classes for unlabeled data) 에 대해 타 method 보다 더 좋은 성능을 보였다고 한다. 다른 데이터셋에 대한 실험 결과는 report 되지 않음.
	
* 실험은 전부 4-view 에 대해 진행되었는데, head 숫자에 따른 (특히 single view vs multi-view) 성능 차이에 대한 실험 결과가 없어서 아쉬웠음.


**총평** : task 자체가 굉장히 흥미로웠음. Novel Class Discovery task 에서 기존 SOTA 에 비해 상당한 성능 향상을 보였기에 관련 task 에 관심이 있으면 읽어봐야 할 논문인 것 같음. method 상 Unlabeled data 의 class 수를 사전에 알고 있어야 한다는 것이 단점이나, 이를 감안해도 인상적인 성능을 보인 논문이었음.
