# Guiding Deep Molecular Optimization with Genetic Exploration 
### Sungsoo Ahn, Junsu Kim, Hankook Lee, Jinwoo Shin - NeurIPS 2020
#### Summarized by Jiye Kim

---

**Task** : Molecule generation



**Main Idea** : 
- genetic algorithm (GA)의 방법론을 사용하여 molecule generation을 수행함. apprentice policy와 expert policy가 있어서, apprentice policy는 DNN으로 구성되고, expert policy는 mutation과 crossover로 구성됨(학습 X). 직접적으로 분자를 생성하는 부분은 apprentice policy이고 expert policy는 추가적인 exploration을 주는 역할을 함.

- sample complexity를 줄이기 위해 max-reward priority queue를 도입.




**Method** :

Step 1) apprentice policy (DNN)이 set of molecules를 생성. max-reward priority queue Q에 K개의 max-reward를 갖는 molecules을 저장.
	
Step 2) expert policy가 Q의 molecules를 seed로 하여 molecules를 생성. Q_ex에 max-reward를 갖는 K개를 저장.
	
Step 3) {Q} union {Q_ex}의 molecules를 apprentice policy가 생성하도록 apprentice policy의 parameter를 update. i.e. objective: maximize log likelihood


- apprentice policy: LSTM networks that receive SMILES as input.

- expert policy: generate molecules in two steps.

  1) expert policy generates a child molecule by applying the crossover to a pair of parent molecules randomly drawn from Q (Cross_over: non_ring_crossover, ring_crossover)

  2) with a small probability, the expert policy mutates the child by atom-wise or bond-wise modification. (Mutation: atom_deletion, atom_addition, atom_insertion, atom_type_change, bond_order_change, ring_bond_deletion, ring_bond_addition)
	
- expert policy는 rl algorithm에 추가적인 exploration을 주는 것이라고 생각할 수 있음.

- max-reward priority queue: prevent the policies from forgetting the highly-rewarding molecules observed in prior

- why use union in step 3: because expert policy does not always improve the apprentice policy in terms of reward.



**Experiment**:

- (1) penalized logP score, (2) penalized logP under similarity constraint, (3) Guacamol benchmark consisting of 20 de novo molecular design tasks, (4) Guacamol benchmark evaluated under post-hoc filtering procedure. 이 4가지 실험을 진행. 각 실험에서 모두 좋은 성능을 보임.

 

**총평**:
- 방법론이 간단함. key contribution은 제안한 genetic operators과 max-reward priority queue인 것 같다. 위와 같은 genetic operator(mutation, crossover)을 사용하여 만들어진 molecules이 다른 constraint없이 chemically valid하고 좋은 property를 갖는것이 보장된다는 게 신기하다.
