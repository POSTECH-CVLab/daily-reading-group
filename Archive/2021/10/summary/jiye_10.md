# Efficient Graph Generation with Graph Recurrent Attention Networks (GRAN)
### Renjie Liao, Yujia Li, Yang Song, Shenlong Wang, Charlie Nash, William L. Hamilton, David Duvenaud, Raquel Urtasun, Richard S. Zemel - NeurIPS 2019
#### Summarized by Jiye Kim

---

### **Task** : 
Graph Generation




### **Main Idea** : 
-  기존에 autoregressive하게 graph 생성하는 방법인 graph-rnn의 경우 최대 O(N^2)의 time complexity가 걸렸다. 이 방법은 one block of nodes에 대한 edge connectivity를 한번에 생성함으로서 O(N) time complexity가 걸리게 된다. 또한 one shot으로 생성하는 것에 비해 edge dependency를 모델링 할 수 있다는 장점이 있고, 또한 graph rnn는 long term dependency를 모델링하기 힘들다는 단점이 있는데, GRAN은 autoregressive하게 생성하긴 하지만 현재까지 만들어진 graph를 gnn으로 embedding한 후 새로운 node에 대한 connectivity를 고려하기 때문에 long-term dependency를 더 잘 고려할 수 있다.


### **Method** :  
- 매 step마다 block of nodes를 더함. 이 node들과 그 전에 생성된 node들간의 모든 edge를 연결해서 augmented graph를 만듬. 이 그래프를 기반으로 gnn을 통해 node embedding을 구하고 이 node embedding으로 부터 graph edge probability를 추출.

- row by row generation으로 O(N) time complexity

- block size, sampling stride → trade off between sample quality and efficiency

- output을 mixture of Bernoulli로 parametrize → capture the correlation among generated edges within the block

- node ordering: marginalizing over a family of canonical ordering으로 해결. default ordering used in the data, node degree descending ordering, ordering of BFS/DFS, novel core descending ordering




### **Experiment** :
- Grid, Protein, Point Clouds, Lobster dataset을 사용
- 평가 방법은 real graph, generated graph의 graph statistics (degree distributions, clustering coefficient distributions, number of occurence of all orbits with 4 nodes)의 MMD distance를 구함. Gaussian EMD kernel로 MMD를 계산하는게 너무 오래걸려서 EMD대신 total variance (TV)로 계산했다고 함. 추가로 eigenvalues of the normalized graph Laplacian도 비교했다고 함. (→ 이게 무슨의미인지는 모르겠음.)
- GraphVAE, Graph-RNN과 비교. DeepGMG와의 비교는 computational time이 너무 많이 필요해 생략했다고 함.




### **총평**:
- Graph generation초기 연구로서 molecule generation이 아닌 feature-less 한 간단한 graph dataset에 대해서만 실험을 진행했음. node feature가 있고 더 복잡한 Molecule generation에 이 방법을 쓰면 어떨지 궁금함.
- 이렇게 augmented graph를 만들어서 edge prediction 하는 방법은 좋은 것 같음.
- MLP를 사용해서 predefined maximum size내에서만 생성을 해야한다는 것은 단점.
