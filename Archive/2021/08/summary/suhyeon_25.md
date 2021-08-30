# MLP-Mixer : An all-MLP Architecture for Vision
### Ilya Tolstikhin et al. (Google Research, Brain Team) - Arxiv 2021
#### Summarized by Suhyeon Jeong
---

 

**Overview** : pretraining, regularization 사용 시 image classification task 에서 SOTA 모델만큼 좋은 성능 및 accuracy-compute trade-off 를 보이면서 오로지 MLP 로만 이루어진 architecture, MLP-Mixer 를 제안함.

 

**task** : base architecture (?)

 

**Motivation** : vision architecture 들은 1*1 convolution 과 같이 per-location operation (channel-mixing) 만 진행하거나, 일반적인 convolution, attention-based network 에서처럼 cross-location(token-mixing) operation 을 동시에 진행하는 layer 들을 가진다. 이러한 per-location operation 과 cross-location operation 을 clearly separate 하는 것에서 아이디어를 얻어 MLP-mixer 를 디자인하였다고 한다.

 

**Method** : MLP-Mixer 의 핵심이 되는 Mixer-Layer 는 앞서 언급한 두 operation, cross-location operation(token-mixing) 과 per-location operation(channel-mixing) 으로 이루어진다. input 으로는 이미지를 자른 sequence of non-overlapping patch 들이 들어가고 각 patch 들은 per-patch FC layer 를 통해 embedding 되어 stacked Mixer layer 로 넘겨진다.
Mixer layer 는 다음의 두 단계가 순차적으로 이루어진다. 
**1)** token mixing 


	
* Layer normalization 을 거친 patch features 를 transpose 하여 parameter tying 된 MLP 로 각 spatial location 마다 연산을 진행한다.  이후 다시 matrix transpose 하여 원래 shape 로 되돌린다.
	
* Layer normalization 직전 feature 와 result 간의 skip connection

**2)** channel mixing


	
* Layer norm 을 거친 feature 를 parameter tying 된 MLP 로 각 spatial location 마다 연산 진행. 
	
* Layer normalization 직전 feature 와 result 간의 skip connection


 

parameter tying 으로 인해 feature 의 hidden dimension 이나 sequence length 를 늘리더라도 모델 size 가 급격하게 증가하지 않아 significant memory saving 이 가능하다. 이렇게 parameter tying 을 진행하더라도 그렇지 않은 경우와 비교해 performance 차이가 없었다.

 


**Experiment**


	
* additional regularization 사용 시 ImageNet 에서 기존 SOTA 모델들과 비슷한 성능을 달성하였음. (SOTA 보다 조금 낮은 성능) Regularization 이 없으면 overfit 한다고 함.
	
* 작은 data size 에서는 Mixer 의 성능이 VIT 나 BiT 에 비해 떨어지는 경향을 보였으나 data size 가 커질수록 비슷하거나 (조금)더 높은 성능을 달성하였음. 


 

**총평** : MLP 만으로 CNN/ attention based model 과 competitive 한 성능을 낼 수 있다는 것이 흥미로운 논문이었다.
