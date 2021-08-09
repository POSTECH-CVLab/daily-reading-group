# Non-local Neural Networks
### Xiaolong Wang et al. (Carnegie Mellon Univ. FAIR) - CVPR 2018
#### Summarized by Suhyeon Jeong
---

**Overview** : vision task 에서 일반화된 non-local operation를 정의하고, 이를 이용해 모델에 적용이 용이한 non-local block 을 디자인하였다. non-local block 을 video classification task 의 Resnet 기반 모델에 삽입한 non-local neural network는 우수한 성능을 보였다.
 

**task** : attention

 

**Motivation** : long-range information 을 보기 위해 CNN 같은 local operation 같은 경우 깊게 레이어를 쌓아서 receptive field 를 키워야 하는데, 이는 computation 측면에서 매우 비효율적이다. 이에 long-range dependency 를 directly 하게 계산하는 non-local operation 을 정의하고 몇몇 non-local operation 들의 구성을 제안하였다.

 

**Method** : 

**1)non-local operation**: 
논문에서는 일반화된 non-local operation 에 대해 다음과 같이 정의하였다. 

y_i = 1/C(x) * sum( f(x_i,x_j) g(x_j) )    (논문의 식 1 참조)

pairwise function f 는 i, j 사이 relationship 을 계산하고, g 는 j 의 representation 을 계산한다. C(x) 는 normalization factor 이다. 이 f 와 g 는 다양한 variation 이 존재할 수 있는데, 본 논문에서 g 의 경우 linear embedding 만 고려하였다. 
f 에 대해서는 다음과 같은 네 가지 operation 을 제안하였다. 

1) Gaussian
2) Embedded Gaussian 
3) Dot product
4) Concatenation


이 중 embedded gaussian 을 사용하는 경우, self-attention module 의 general form 이 된다.

**2)non-local block** :
non-local operation 의 output y_i 를 바로 사용하는 대신 residual connection 과  y에 곱해지는 weight metrix W 를 추가하였다. residual connection 덕분에 W 를 0 으로 initialize 하는 경우 pretrained model 의 initial behavior 을 그대로 유지하면서 non-local block 을 모델에 삽입할 수 있다.

**Experiment** : 
1) f 의 종류에 따른 큰 성능 차이는 없었다. non-localty 그 자체만으로 학습에 도움이 됨을 시사한다.
2) 네트워크의 가장 뒤쪽에 non-local block 을 삽입하는 것 보다 좀 더 network 의 중앙 쪽으로 배치하는 것이 성능이 좋았다.
3) non-local block 을 많이 사용할 수록 성능이 높아 졌다. 어느 정도 이상 삽입한 경우 성능 변화가 거의 없었음.

 

**총평** : non-local operation 의 정의와 그 효과에 대해 생각해 볼 수 있는 좋은 논문이었다. 기본적인 논문 답게 내용도 어렵지 않고 writing 도 깔끔해 쉽게 읽을 수 있었다.
