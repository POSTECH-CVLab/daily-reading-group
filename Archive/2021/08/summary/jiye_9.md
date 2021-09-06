# Self-supervised graph transformer on large-scale molecular data
### Yu Rong, Yatao Bian, Tingyang Xu, Weiyang Xie, Ying WEI, Wenbing Huang, Junzhou Huang - NeurIPS 2020
#### Summarized by Jiye Kim

---

**Task** : self-supervised graph representation learning



**Contribution** : 
- GNN과 transformer를 합친 새로운 architecture를 제안했다.

- 2개의 새로운 self-supervision tasks를 제안했다.


**Method** :

1. Model architecture

- transformer의 attention block은 vectorized input을 받기 때문에, graph를 vector 형태로 바꿔주기 위해서 GNN을 사용했다. GNN+ Transformer 구조로 bi-level information extraction이 가능하다고 한다.

- original Transformer 는 여러개의 short-range residual connection을 사용했는데, GTransfomer는 single long-range residual connection을 사용했다. 이를 통해 1) vanishing gradient problem, 2) over-smmothing problem in message passing process 를 해결할 수 있다고 한다.

- Dynamic Message Passing Network: GNN은 기본적으로 number of layers가 고정되어 있어서 pre-specified number of hops K 만큼의 이웃 정보를 받을 수 있다. 이렇게 number of hops를 고정해놓지 않고 number of hops를 random 하게 뽑아 학습시키는 구조를 제안했다.

2. Self-supervised task

- Contextual property prediction: Target node를 기준으로 k-hop 만큼의 local subgraph를 추출하고, 이 subgraph의 statistical properties를 계산한다. 구체적으로는 center node를 기준으로 이웃에 있는 (node, edge) pair를 count하여, e.g. C_N-DOUBLE1_O-SINGLE1 처럼 statistical property를 나타낸다. 그리고 위의 network를 통과한 node embedding이 statistical property를 prediction할 수 있도록 multi-class prediction problem으로 학습시킨다.

- Graph-level motif prediction: Motifs는 input graph에 등장하는 recurrent subgraphs를 말한다. molecules에서 motifs는 functional groups이 될 수 있고, 해당 functional group이 한 molecule에 있는지 없는지 나타내는 multi-label classification problem으로 학습한다.


**Experiment**:

- Pretraining dataset: ZINC15와 Chembl에서 11 million unlabelled molecules

- Finetuning task: 11 benchmark datasets from the MoleculeNet

- 11개의 downstream tasks에서 모두 sota를 기록했다.

**총평**:
- GNN+transformer를 합친 GTransformer 구조를 제안하고, 2개의 self-supervised method를 제안한 논문이다. 
