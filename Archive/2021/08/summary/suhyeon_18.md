# Relation Networks for Object Detection
### Han Hu et al et al. (Microsoft Research Asia) - CVPR 2018
#### Summarized by Suhyeon Jeong
---

 


**task** : Object detection

**Contribution** : suggested first fully end-to-end object detector (with experimental evidence)

**Method** : in-place, fully differentiable 하며 scaled dot-product attention 에서 아이디어를 얻은 object relation module 을 제안하고 이 module 을 이용해 object detection stage 중 instance recognition, duplicate removal stage 를 변형시켜 end-to-end model 을 구성하였다.
- **Object Relation module** : 일반적인 attention module 과는 달리, bbox 의 정보를 담은 geometric feature 를 추가로 사용하여 attention weight 를 생성하는 데 영향을 준다. 
1) all candidate 의 appearance feature 로 value, key 를 생성
2) target candidate 의 appearance feature 로 query 를 생성
3) key 와 query의 dot product 로 appearance weight 를 생성한다. 모든 pair 에 대해서 appearance weight 를 생성하므로, candidiate 들의 수를 n 이라 하면, n*n 개의 weight 가 생성된다.
4) 두 candidate 의 geometry feature 를 high dimension 으로 embedding 하고 linear -> ReLU 를 거쳐 geometiy weight 를 생성한다. ReLU 의 zero trimming 이 일부 필요한  geometric relationship 만 고려하도록 규제한다. 
5) appearance weight 와 geometry weight 로 attention weight 를 생성. (softmax 와 weighted sum 을 합친듯한 형태.. 논문 참조)
6) attention weight 로 value 를 weighted sum 하여 target candidate 의 relation feature 생성

이러한 relation 은 multi-head attention 처럼 여러 개 존재할 수 있다. 이 때 head 수 만큼 relation feature 의 dimension 은 작아지고, relation feature 를 전부 concat 한 값과 skip connection 으로 전달받은 원래 appearance feature 를 더해 final relation feature 를 생성한다.

- **Instance Recognition stage** : FC-FC-Linear 로 이어지는 구조에서 각 FC 직후에 Relation module 을 추가하였다. input 으로는 모든 candidate 의 (feature, bbox) 를 받아 각 candidate 의 ( classification score, bbox) 를 생성한다.

- **Duplicate Removal stage** : instance Recognition 단계의 마지막 relation module에서 생성된 final feature 와 classification score 를 이용해 appearance feature 를 생성하고, bbox geometric feature 와 함께 relation module 을 통과시켜 final transformed feature 로 linear classifier 를 거친 binary classification probability 를 생성한다. 이 classification probability 는 correct / duplicate 인지 나누는 probability 로, 이 probability 와 Instance Recogniton stage 에서 생성된 classification score 를 곱하여 final classificatio score 을 생성한다. ground truth box 와 threshold 이상의 IoU 를 가지는 detection box 중 가장 hightest score 를 가지는 candidate 를 correct 로 한다. ground truth bbox 가 없는 inference time 에는 score threshold 를 기준으로 컷하는 것 같다.

=> relation module 이전, score 와 feature 를 합칠 때 classification score 를 high dimension 으로 embedding 하기 전에 candidate 끼리 score rank 를 매긴 값을 사용하면 좀 더 좋은 성능을 보였다고 한다. (score 값이 큰 차이 없이 비슷한 값을 가지는 경우를 제외하고는 오히려 detail information 을 잃어버려 좋지 않을 것 같은데.. 의문이다)

**총평** : relation reasoning 논문들의 citation 을 타고 건너 들어가다가 읽게 된 논문이라 잘은 모르지만 first fully end-to-end object detector 를 보였다고 하니 상당히 중요한 논문인 것 같다.(이론적으로는 end-to-end 가 가능한 이전 논문들이 있긴 했지만 이들은 experimental evidence 를 보이지 않았다고 한다) attention 을 이용한 relation module 을 detection 모델에 적용한 방식이 재미있었다(필자가 detection 논문을 거의 보지 않아서 재밌었던 것일지도..).
