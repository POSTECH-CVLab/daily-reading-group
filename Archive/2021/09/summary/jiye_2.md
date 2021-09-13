# On the bottleneck of graph neural networks and its practical implications
### Uri Alon, Eran Yahav - ICLR 2021
#### Summarized by Jiye Kim

---

**Task** : GNN analysis



**Summary** : 
-  GNN은 layer를 깊게 쌓아도 성능이 올라가지 않는 문제가 있었는데, 이전 논문에서는 이 문제의 이유로 over-smoothing을 들었다. over-smoothing은 layer를 너무 깊게 쌓게 되면 node representation이 다른 노드와 indistinguishable 하게 되어 노드간의 구별이 안되어 성능이 떨어지는 문제이다. 하지만 본 논문은 GNN이 layer를 깊게 쌓아도 성능이 올라가지 않는 이유를 over-squashing 문제라고 주장한다. over-squashing 문제는 GNN의 layer가 깊어질수록 한 노드가 정보를 받는 이웃 노드의 개수가 exponential 하게 증가하기 때문에, (특히 long-range information이 필요한 task의 경우) exponential하게 많은 이웃 정보들이 fixed size vector로 압축되다 보니까 information loss가 크게 일어나고 long-range information이 잘 전달이 안되는 문제이다.

- 논문에서 over-squashing 문제를 제안하고 이를 입증하기 위해 두가지 실험을 디자인했다.

 
**Experiment1: Neighborsmatch** : 

- problem radius r (problem's required range of interaction)을 임의로 조절할 수 있는 Neighborsmatch라는 task를 디자인하고 problem radius r을 바꿔가며 실험했다. GNN layer 수는 K≥r으로 함으로서 GNN이 정답에 대한 정보를 확실하게 얻을 수 있게 했다. GNN 모델을 training set에 overfitting 시켜서 training accuracy를 재보았을 때, r≤3 인 경우는 accuracy가 모든 모델에서 100%가 나왔지만 r이 8까지 증가할 수록 accuracy가 떨어졌고, 따라서 problem radius가 깊어졌을 때 모델이 training set에 perfectly fitting하지 못한다는 것을 발견했다.

- GGNN, GAT, GIN, GCN 모델을 테스트해보았을 떄 GIN, GCN 모델 성능이 더 빨리 떨어졌는데, 저자는 이를 GAT와 GGNN의 경우 attention기반 모델로 불필요한 information의 가중치를 다르게 둘 수 있는데 GIN, GCN은 모든 노드의 information을 equally 받아서 성능이 더 떨어진다고 주장했다.


**Experiment2: Add fully-adjacency layer (FA)** :

- K layers GNN의 last layer (Kth layer)만 fully adjacent하게 바꿔서 실험. (마지막 layer에서는 모든 노드가 연결되어있다고 가정. 따라서 모든 노드로부터 정보를 얻을 수 있음)

- QM9 dataset (chemistry), NCI1, ENZYMES dataset (biology)에 대해 6개의 모델 (R-GIN, R-GAT, GGNN, MLP, R-GCN, GNN-FiLM) 의 마지막 layer만 FA로 바꿔서 실험해보았을 때 대부분의 모델에서 상당히 성능이 올랐다. 이런 성능 향상이 over-squashing이 해결되어 long-range information이 더 잘 전달되었기 때문인지 애초에 layer 개수가 부족한 under-reaching 상태였는지 확인하기 위해서 QM9 graph diameter를 재보았을 때 90%가 layer 수보다 작은 것을 확인했고, 추가로 layer를 10으로 늘려서 실험했을 때도 성능향상은 없었다고 한다. 따라서 under-reaching 상태는 아니었음을 보였다. 추가 실험으로 모든 layer를 FA로 바꿔서 실험해보았을 때(graph structure정보를 아예 배제하고 실험), 1500%(worse) error rate를 보였다고 하고 따라서 graph structure를 encode할 수 있는 GNN은 필요하다고 한다.

 

**총평**:
- GNN이 long-range information propagation이 잘 안되는 이유를 설명한 논문. 가설에 대한 실험 설계를 잘한 것 같다. 여러가지 의문이 들 수 있는 setting을 모두 실험을 통해 보여준 점이 좋았다.
