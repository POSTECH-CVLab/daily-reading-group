# Constrained Generation of Semantically Valid graph via regularizing variational autoencoders
### Tengfei Ma, Jie Chen, Cao Xiao - NIPS 2018
#### Summarized by Jiye Kim

---

**Task** : Graph Generation



**Main Idea** : 
- graph를 generation하는 방법은 여러가지가 있는데 (sequential하게 node를 하나하나 이어붙이는 방법, graph adjacency matrix를 one-shot으로 generation하는 방법 등.) matrix를 one-shot으로 generation할 때 문제점은 probability matrix에서 각 edge와 node의 sampling이 independent하게 일어나기 때문에 전체적인 graph의 validity를 고려하지 않고 생성된다는 문제가 있다. 따라서 이 논문은 vae 구조에 penalty term을 넣어서 전체 graph의 validity를 높이게 했다.
 
**Method** : 

- optimization에서 constrained optimization을 Lagrangian multiplier를 사용하여 unconstrained optimization 문제로 바꾸는 방법을 사용했다.

- 위에서 언급한 graph가 만족해야하는 constraint들 (molecular graph의 경우 atom의 valency constraint를 맞추기, protein-protein interaction graph의 경우 같은 gene ontology term이 있을 경우에만 connectivity를 부여) 등을 optimziation problem의 constraint로 정의했다.

- 위와같이 constraint를 부여하면 기존의 VAE ELBO loss term에 Lagrangian multiplier * constraint term 이 추가되게된다.


**Constraint Formulation** :
- 논문에서는 3가지 constraint formulation 방법을 제안한다.

1. Ghost node and Valence

- Ghost node (node type이 0으로 assign 된 node) 는 incident edge가 없어야한다.

- Valence: atom 의 총 capacity(valence)와 현재 capacity의 차이가 0이 되도록 constraint를 두었다.

2. Connectivity

- ghost node와 connectivity의 관계를 constraint로 두었다. ghost node는 어떤 노드와도 연결될 수 없기 때문에 ghost node일 경우 어떤 node와도 connectivity가 없도록 constraint를 두었다.

3. Node compatibility

- protein protein interaction graph같은 경우 같은 종류의 protein 끼리만 edge connectivity가 존재해야한다. 이러한 node compatibility도 constraint 중 하나로 두었다.

**Experiment** : 
- QM9, ZINC, 그리고 synthetic graph를 만들어 실험을 진행했다. baseline 모델인 smiles 기반 generation model GVAE, CVAE와 비교해보았을 때, validity, novelty 가 훨씬 높게 나왔다. 또한 regularization term을 부여하지 않은 기본 vae 구조와 비교했을 때 validity는 훨씬 높아졌다. Latent space를 visualize했을 때도 smooth하게 변하는 것을 확인했다.

**총평**:
- Constrained optimization을 unconstrainted optimization problem으로 바꾸는 방법을 사용해서, graph가 만족시켜야하는 condition들을 explicit하게 하나하나 constraint로 두어서 만족시키게 하는 방법론을 제안했다. constraint를 부여하는 과정에서 heuristic이 굉장히 많이 들어가야하고, graph가 만족시켜야하는 조건을 하나하나 constraint로 줘야한다는 부분이 조금 아쉬운 점인 것 같다. 또한 method는 일반적인 graph에서 범용적으로 쓰일 수 있는 방법론을 제시한 것처럼 쓰여있는데, 실험은 molecule graph의 validity를 높이는 것만 있어서 아쉬웠다. Graph generation 초기 연구로서 naive하게 validity를 높일 수 있는 방법을 제안한 논문인 것 같다.
