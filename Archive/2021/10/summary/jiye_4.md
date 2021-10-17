# MolGAN: an implicit generative model for small molecular graphs
### Nicola De Cao, Thomas Kipf - arxiv 2018
#### Summarized by Jiye Kim

---

### **Task** : 
Molecule generation


### **Main Idea** : 
-  MLP-based generator, R-GCN based discriminator & reward network를 결합해서 molecule generation을 수행하는 network를 제안했다. Deterministic policy gradient algorithm (DDPG)를 사용해 desired property 를 만족하는 molecule을 만들도록 했다.


### **Method** :  
Generator, Discriminator, reward network으로 구성된다.
1. Generator

- sample from a prior distribution and generates an annotated graph G (generates adjacency matrix A and node atom feature X)
- Predict entire graph at once using a simple MLP
- output: X (NT) - atom type, A (NN*Y) - bond type → probability로 표현됨.
- categorical sampling을 통해서 X, A로 부터 discrete, sparse한 X_bar, A_bar를 생성.
- 위의 discretization process는 non-differentiable하기 때문에 gradient-based training을 위해서 3방법중 하나를 사용 (1. continuous output을 그대로 사용, 2. Gumble noise를 추가, 3. Gumble softmax 사용)
- loss: linear combination of WGAN and RL loss

2. Discriminator

- Take generated sample and real sample and learn to distinguish them
- Loss: WGAN objective

3. Reward network

- Take generated sample and real sample and assign scores to them.
- If MolGAN outputs invalid molecule, it assigns zero reward.
- Reward network는 생성된 molecule의 property를 예측하는 역할을 한다. reward network는 분자에 대해서 external software로 computed된 property와의 mse를 줄이는 방향으로 학습되고, 이에 맞춰서 generator는 reward network의 output을 높이도록 DDPG방법을 사용해서 gradient update을 수행한다.

Other details:

- WGAN objective를 사용했지만 mode collapse가 발생한다고 함
- 초기에는 reward network가 property를 잘 예측하지 못해서 generator에 잘못된 gradient를 주기 때문에 처음에는 reward network는 학습하되 generator에 gradient를 주지 않음.







### **총평**:
- GAN을 사용해서 직관적으로 molecule generation을 수행한 논문이다. 머신러닝적인 novelty가 있다기 보단 기존 방법을 molecule generation에 처음 활용했다는 것이 contribution인 것 같다.
