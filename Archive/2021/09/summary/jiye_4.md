# How to find your friendly neighborhood: Graph attention design with self-supervision
### Dongkwan Kim, Alice Oh - ICLR 2021
#### Summarized by Jiye Kim

---

**Task** : Graph node classification, Graph attention


**Contribution** : 
- graph에서 edge information을 활용하여 attention을 explicit하게 줄 수 있는 self-supervised task를 제안했다. - attention value를 가지고 edge의 presence를 예측하는 binary classification task를 디자인
	
- 두 개의 commonly-used attention method, 1) GAT's original single-layer neural network(GO) - 두 node embedding을 concat해서 single-layer neural network를 통해서 scalar값을 output 하는 방법, 2) Dot product attention (DP) - 두 node embedding을 dot product해서 attention value를 계산하는 방법을 label-agreement task와 link prediction task를 통해 분석했다. GO는 label-agreement task에 DP는 link prediction task에 더 잘하는 것을 확인했다.
	
- graph attention을 여러 방법으로 design 할 수 있는데 이런 design choice의 성능은 graph의 average degree와 homophily에 달려있다고 주장한다. 따라서 attention을 design할 때, 다루는 graph의 average degree와 homophily를 고려해야한다고 한다.


**Details** : 

- 기존 graph attention 방법인 GO와 DP를 조금 변형하여, Scaled dot product attention (SD) - transformer에서 사용하는 attention, Mixed GO and DP (MX) - GO와 DP attention을 둘다 고려하려고 한 attention, 을 제안했다. 엄청 novel한 attention 방법은 아니어서 본 논문의 주된 contribution은 아닌것 같다.
	
- 기본 node classification task에, 위의 attention 기법으로 나온 attention value를 통해 edge의 존재 여부를 판단하는 binary classification을 auxiliary task로 붙여서 node label과 edge presence를 같이 학습하게 하는 방법을 제안했다.
	
- GO와 DP attention 방법이 label-agreement task와 edge prediction task에서 얼마나 잘하는지 각각 실험했다. Label-agreement task는 node k를 중심으로하는 label-agreement distribution과 normalized attention의 distribution의 KL divergence를 계산하였고, KLD가 낮을수록 잘한다고 할 수 있다. (label이 agree되는것에 attention을 더 주어야함) GO는 label-agreement에서 DP는 edge prediction에서 더 잘하는 것을 확인했다. 따라서 이 두가지 attention model은 label-agreement, edge presence를 동시에 encoding하지 못한다는 것을 확인했다.
	
- homophily (같은 node feature를 갖는 애들끼리 뭉쳐있는 정도), average degree가 어떤 graph attention을 써야하는지에 영향을 미친다고 가설을 세우고 이를 확인하기 위해 synthetic dataset을 만들어 실험을 진행했다. 이렇게 가설을 세운 이유는 edge label과 함께 학습된 graph attention network 라면 얼마나 label이 noisy한지 (how low the homophily is), 얼마나 많은 label이 있는지 (how high the average degree is)에 영향을 받을 것이기 때문이다. synthetic dataset은 다양한 average degree, homophily를 갖도록 만들었다. 결과는 low-homophily setting에서는 scaled dot-product attention with self-supervision이 가장 잘 동작했고, self-supervision이 도움이 되는 것을 보였다. 하지만 homophily와 average degree가 둘다 높은 setting에서는 attention model들끼리 차이가 없었다. (attention을 아예 사용하지 않는 GCN 포함)



**총평**:
- 굉장히 실험을 많이 진행했고, edge presence를 self-supervision task로 둔 점은 새로운 것 같다. Label agreement를 계산하는 방법을 제안한 것도 새로웠다. 그리고 graph attention을 여러 실험을 통해 분석하려는 시도도 좋은 것 같았다. writing 부분이 아쉬웠는데, 논문의 contribution은 많은데 이것들이 종합적으로 합쳐져서 무엇을 이야기 하고 싶은것인지 잘 와닫지 않았다.
