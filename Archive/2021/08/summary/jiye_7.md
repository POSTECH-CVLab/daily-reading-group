# Strategies for pre-training graph neural networks
### Weihua Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay Pande, Jure Leskovec - ICLR 2020
#### Summarized by Jiye Kim

---

**Task** : pretraining graph neural networks



**Summary** : 
- GNN을 pretrain하는 여러가지 방법을 제안했다. 논문이 주장하는 성공의 요인은 node-level, graph-level pretraining을 같이 수행함으로서 local and global representation을 동시에 효과적으로 학습할 수 있었기 때문이라고 한다.
 


**Method** :

1. Node-level pretraining

1-1) Context prediction
- context prediction은 subgraph를 사용해서 surrounding graph structure를 예측하게 하는 task이다.

- 먼저 K-hop neightborhood of node v와 context graph of node v를 정의한다. K-hop neighborhood는 node v로 부터 K-hop 만큼 떨어져있는 subgraph이고, context graph 는 node v를 기준으로 r_1-hop, r_2-hop (r_1 < r_2) 사이의 있는 subgraph를 말한다. 이 때, r_1 < K 를 만족하도록 해서 context graph와 k-hop neighborhood 사이에 겹치는 노드가 있도록 한다. 여기서 K-hop neighborhood를 이용해서 context graph를 예측하는 것이 task이다. 구체적인 learning objective는 특정 neighborhood와 특정 context graph가 같은 노드에 속하는지를 예측하는 binary classification problem이다. 
 

2-2) Atom masking
- graph에서 node나 edge feature를 masking하고 주변 정보로 부터 예측하게 하는 task이다.

2. Graph-level pretraining

2-1) Supervised graph-level property prediction

- graph-level multi-task supervised pretraining을 수행한다.

3. 본 논문이 target하는 downstream task가 graph-level property prediction task이기 때문에, pretraining은 node-level pretraining → supervised graph-level pretraining 순으로 진행한다.


**Experiment**:

- 다른 여러 graph architecture보다 GIN을 사용할 때 성능이 좋았다. 다른 architecture 들은 똑같은 setting에서 했을 때 negative transfer가 발생하기도 했다.

- graph-level multi-task supervised pretraining, node level pretraining을 단독으로 했을 경우 negative transfer가 발생하는 경우가 있었다. 하지만 두가지를 합쳤을 때 negative transfer를 피할 수 있는 것을 확인했다.

- chemistry domain의 경우 Context prediction + graph-level multi-task supervised pretraining이 가장 성능이 좋았고, biology의 경우 attribute masking + graph-level multi-task supervised pretraining이 가장 좋았다.

- non pretrained models 보다 orders-of-magnitude faster training and validation convergence을 보였다.
 

**총평**:
- node-level, graph-level pretraining을 동시에 수행해서 좋은 성능을 낸 모델이다. 여러 pretraining 방법을 시도해보고 실험적으로 가장 좋은 방법을 찾아서 분석해놓았다. 거의 처음으로 graph pretraining을 제시한 논문이라서 읽어볼만 한 것 같다.
