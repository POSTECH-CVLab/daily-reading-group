# Momentum Contrast for Unsupervised Visual Representation Learning 
### Kaiming He et al. (FAIR) - CVPR 2020
#### Summarized by Suhyeon Jeong
---

 

**Overview** :  introduced Momentum Contrast(MoCo) which is pretext-agnostic method for unsupervised representation learning.

 

**task** : unsupervised/self-supervised representation learning

 

**Motivation** : larger dictionary 는 better representation 을 학습하는 데 도움이 된다는 가정에서 출발하여 larger dictionary 를 사용할 수 있는 computationally efficient 한 method, MoCo 를 제안

 

**Method** : 
한 image 에서 data augmentation 으로 query와 key 를 생성한다고 할 때, 이들은 positive pair 이다. 이를 기반으로, MoCo 의 method 는 다음과 같이 정리될 수 있다. key query 와 key encoder 의 momentum update 가 핵심이다.
* current batch 에서 positive pair 인 query 와 key 생성
* 최근 일부 batch 의 key 들을 보관하는 query 도입, query 에 보관되어있는 key 들을 sample 하여 negative pair 생성
* gradient-discent 로 query encoder update, query encoder parameter 로 key encoder 를 momentum update 
* queue update : remove the oldest batch's keys, and put current batch's keys

 

queue 에 이전 batch 들의 key (encoded feature of augmented image) 를 저장하여 이들로부터 현재 batch 의 nagative pair 를 sampling 하는 방법을 통해 두 가지 이점을 얻는다. 
**1)** 보다 방대한 다양성을 가진 negative pair 사용 가능. dictionary size larger than typical mini-batch size
**2)** 이전 mini-batch 들의 encoded key 들을 재활용함으로서 현재 batch 에서 새로 negative pair encoding 을 하지 않아도 되는 이점이 있음

 

하지만 이로 인해 large dictionary 를 사용하게 되면서 key encoder 를 학습시키기 어렵게 되었다. queue 의 key 들을 전부 사용하게 되므로 key encoder 를 gradient-discent 로 update 하려면 모든 queue 의 element 로부터 gradient 를 계산해야 하는 문제가 생김. 그리하여 query encoder 의 weight 로 key encoder 를 update 하는데, query encoder 의 weight 를 그대로 가져와 적용할 경우 , key encoder 의 weight 가 너무 빨리 바뀌어 queue 의 오래된  key 들과 최근 key들 사이의 괴리가 커지게 된다. (각 key 를 encoding 한 encoder 들이 너무 달라져 버리므로) 즉, large queue 를 더 이상 유지할 수 없게 되므로 이를 방지하기 위해 엄청 큰 momentum 을 적용하여 key encoder  를 update 한다. ( m = 0.999 인 매우 강력한 momentum 을 사용하였다) 이렇게 할 시 queue 내의 시간적 차이를 무시할 수 있을 정도로 key encoder 의 weight 이 적게 변화하여 queue 의 key 들을 현재의 negative pair 들로 합당하게 사용할 수 있다.
 
*  loss function 으로 InfoNCE를 사용하였다

 


**총평(이라기보단 개인적인 견해)** : 유명한 self-sup 연구 중 하나인 MoCo 논문을 읽어 보았다. large dictionary 를 참조할 수 있다는 것이 성능 향상에 도움을 준 것 같으나, queue 에 이전 batch 의 sample 들을 별도의 거르는 과정 없이 전부 저장한다는 점에서 easy negative sample 들의 비중이 많아져 실질적으로 학습에 많은 도움을 줄 수 있는 건지 의문이 들었다.(feat. Sampling Matters in Deep Embedding Learning(ICCV 2017)). queue 를 도입한 방식 때문에 강력한 key encoder momentum 이 강제적이게 된 것이 단점인 것 같다. (key encoder 가 거의 바뀌지 않는 것이 어느 정도 성능에 disadventage 를 줄 것 같다는 intuition을 가정한다면) 
