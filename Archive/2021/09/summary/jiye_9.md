# Junction Tree variational autoencoder for molecular graph generation
### Wengong Jin, Regina Barzilay, Tommi Jaakkola - ICML 2018

#### Summarized by Jiye Kim

---

### **Task** : 
Molecular graph generation


### **Main Idea** : 
-  Molecule을 clusters을 기준으로 하나의 노드로 만들어 tree 형태로 만든 후(tree decomposition), molecular graph와 tree graph를 각각 latent vector z_g, z_t로 encoding한다. z_t에서 먼저 tree를 decode하고 decode된 tree와 z_g를 받아 최종적으로 molecular graph G를 decode하는 과정을 거친다. 단순히 atom을 하나하나씩 이어붙이는 것보다 cluster를 이어붙이는게 molecular validity를 만족하는게 더 쉽다고 한다.
 
### **Method** : 

1. 먼저 training set ZINC250k에서 vocalbulary of valid components를 추출한다. Vocabulary는 1) rings, bonds, atoms의 형태로 이루어지고 molecule을 다 덮을수 있을 정도로 많다.

2. Molecular graph → tree decomposition

- Molecular graph에서 모든 simple cycles과 cycle에 포함되지 않는 edge들을 찾는다. 두개의 cycle이 2 atom이상 겹치면 merge한다. (a specific structure called bridged compounds) 이러한 cycle과 edge들을 cluster라고 생각하고 tree의 node가 된다. 각 cluster끼리는 최대 2개의 atom만 겹치기 때문에 garph decoding phase에서 efficient하다고 한다.


3. Encoding molecular graph and tree graph

- Molecular graph와 tree graph를 각각 encode해 latent vector [Z_g, Z_t]를 만든다. Molecular graph를 encode하는 방법은 단순 graph messaging passing을 수행하고 average pooling을 해서 나온 graph feature로 부터 mean and log variance of variational posterior를 뽑아낸다. Tree graph를 encode하는 방법은 하나의 leaf node를 root로 정하고 다른 leaf nodes로 부터 bottom-up으로 message passing을 수행한다. 그렇게 나온 root node feature, h_root 를 tree representation으로 하여 variational posterior parameter를 계산한다. Molecular graph와 다르게 average pooling이 아닌 bottom-up fasion으로 하는 이유는 나중에 tree decoding을 수행할 때 root에서 순차적으로 generation을 하기 때문에 tree decoder에게 그 정보를 주기 위함이다.


4. Tree decoder

- Top-down fasion으로 root node로 부터 node를 순차적으로 generate한다. Depth-first order로 1) topological prediction, 2) label prediction을 진행하는데, topological prediction은 child node가 있는지 없는지를 나타내는 binary classification이고 label prediction은 child node가 있다면 vocabulary 중에 어떤것인지 multiclass classification을 수행한다. 학습은 gt와 cross entropy loss를 통해 진행되고 teacher forcing을 사용한다.


5. Graph decoder

- Tree 형태로 부터 graph를 복원해야하는데, tree에서 두 node는 여러가지 형태로 assemble될 수 있다. computational efficiency를 위해서 tree의 root노드로 부터 하나하나 이어붙이는 방법을 취한다. Scoring function을 통해 assemble했을 때 가장 높은 score를 내는 assembly를 택한다. scoring 방법은 두 cluster를 assemble했을 때 합쳐진 graph를 G_i라고 할때 G_i와 z_g의 내적을 score로 한다. 이 score가 가장 높게 나오는 조합을 택하게 된다.



### **Experiment**:
3가지 실험을 진행한다.

- input molecule을 얼마나 잘 reconstruct하는지. molecule validity test.

- Bayesian optimization: latent space에서 bayesian optimization을 수행하여 property optimization을 수행하고, 가장 높은 property를 갖는 molecule 3개를 report한다. 또한 log-likelihood, RMSE값을 Report한다.

- constrained optimization: input molecule의 similarity가 어느정도 보장된 상태로 property optimization을 수행한다. latent space에서 property prediction f를 학습시키고 predicted score f()를 향상하도록 gradient ascent in latent space를 수행한다. 이때 improvement의 정도와 success rate를 Report한다.

위의 3개 실험에서 기존 baseline보다 우수한 성능을 내는것을 보였다.

### **총평**:
- molecule의 substructure를 가지고 tree 형태로 encoding, decoding을 수행하여 molecular validity를 보장하도록 한 논문이다. quantitative, qualitative result가 모두 좋은 것을 보였지만 방법론 자체가 너무 복잡한 것은 단점이다. generation하는데 heuristic이 들어간 부분이 많은 것이 아쉽다.
