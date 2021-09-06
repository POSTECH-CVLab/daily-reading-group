# E(n) Equivariant Graph Neural Networks
### Victor Garcia Satorras, Emiel Hoogeboom, Max Welling - arxiv 2021
#### Summarized by Jiye Kim

---

**Summary** : 
- Translation, rotation, reflection (+ permutation)에 equivariant한 gnn 구조를 제안했다.

- E(n) equivariance가 보장되어야 할 3개의 task (dynamical systems modeling, representation learning in graph autoencoders, predicting molecular properties)에서 좋은 성능을 보이는 것을 확인했다.

 


**Method** :

- Stardard gnn message passing 식을 바꿔 equivariant하게 만들어주었는데 첫째로 message from node i to node j 를 계산할 때 coordinates i, j의 relative squared distance를 추가로 넣어주었고(equation 3) 둘째로 coordinates updates 식(equation 4)이 추가하였다. 이렇게 식을 바꿈으로서 E(n) equivariant하게 만들 수 있다. (appendix A.에 증명)

- dynamical system같은 node에 velocity 정보가 추가로 있는 경우를 위해서 기존 method에 momentum이 추가된 방법을 제안했다.

- point cloud와 같이 explicit edge connection information이 없는 경우엔 fully connected graph라고 생각하고 edge의 weight를 다르게 주는 방법을 사용했다.


**Experiment**:

- dynamical system: N-body system

particles들의 몇 초 후의 position을 예측하는 task이다. position의 MSE를 계산했을 때 SOTA를 기록했다.

- Graph autoencoder

여기서 equivariant gnn을 써야하는 이유는, symmetry problem이 존재하기 때문이다. symmetry problem은 예를 들어 node featureless cylcle graph의 경우 모든 node가 같은 embedding을 가지게 되는데, 이렇게 되면 decode에서 embedding의 relative distance로 edge의 존재 여부를 계산하는데 이것을 할 수 없게 된다. symmetry problem을 해결하는 방법은 input node에 gaussian noise를 줘서 각각 다른 node feature를 갖게 하는 방법이 있는데, 이렇게 되면 network가 새로운 noise distribution에 대해서도 학습해야하는 단점이 있다. 여기서 EGNN을 쓰면 input noise가 equivariant하게 output되기 때문에 noise를 노드간에 distinguish 하는데에만 사용할 수 있다.

- Moleculer property prediction

QM9 dataset의 경우 각 atom의 3D position 정보가 있고 예측해야할 property가 12개 있다. 이 property들은 atom position에 invariant하기 때문에 EGNN이 suitable한 상황이다. 12개의 chemical property prediction task에서 9개에서 sota를 기록했다.


 

**총평**:
- 간단한 방법으로 기존 GNN을 Equivariant하게 바꾼 equivariant gnn을 제안한 논문이다. 이론적 분석도 잘 되어있고, equivariant gnn이 필요한 상황에 대한 실험도 적절하게 한 것 같다.
