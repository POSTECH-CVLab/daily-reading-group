# A simple neural network module for relational reasoning
### Adam Santoro et al et al. (DeepMind) - NeurIPS 2017
#### Summarized by Suhyeon Jeong
---

 


**task** : relational reasoning 

**Overview** : Relation Networks 라는 간단한 in-place module 을 제안하고 이를 적용한 모델로 visual question answering 의 CLEVR 데이터셋에서 당시 sota 및 super-human performance 를 달성하였다. 강력한 convolution network (Resnet) 들과는 달리 relation network 는 relational question 을 위한 general capacity 가 있음을 실험적으로 보였다. 

**Method** : 
구조는 매우 간단하다. set of features(objects) 를 input 으로 하여 모든 feature pair 에 대해 두 feature를 concat 하여 MLP g 를 통과시킨 값들 생성한다. 이 값들을 relation 이라 부른다. 이 때 g 는 shared parameter 로 이루어져 있으며 이것이 사실상 핵심이다. 모든 relation 들을 sum 한 후, 그 값을 MLP 에 통과시킨 값이 final output 이다. 
relation 을 계산하는 g 의 parameter 가 shared 된다는 것이 MLP 와의 차이점이며, relation network 가 overfit 하지 않고 great generalization 을 가지는 원인이다. 

- k-dim channel 을 가지는 CNN feature 를 사용할 때는 w*h 개의 k-dim feature map 에 relative spatial position 을 붙여서 object 로 사용한다.

- question 별로 다른 relation 을 필요로 하는 task 같은 경우에서는 question embedding q 를 feature pair 과 함께 concat하여 MLP g 를 통과시킨다. (conditioning)


**총평** : relation reasoning 에 효과적인 architecture 구조를 제안한 논문. 간단한데다가 오래 되어서 딱히 detail 하게 읽을 필요는 없는 논문인 것 같지만, visual question answering  ,  text-based question answering, dynamic physical system reasoning 등의 task 에서 RN 의 성능을 측정하여서 궁금하다면 읽어 볼 만한 것 같다. 2017 년 논문임을 감안하면 현재로서는 큰 의미는 없을 수도.
