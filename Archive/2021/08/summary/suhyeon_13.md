# Relational recurrent neural networks
### Rasmus Berg Palm et al. (Technical University of Denmark) - NeurIPS 2018
#### Summarized by Suhyeon Jeong
---

 

**Overview** : single step relational reasoning 만 학습할 수 있었던 Santoro et al. 의 relational network 와 달리 multi-step relational reasoning 을 학습할 수 있는 recurrent relational network 를 제안함. 또 relational reasoning 을 위한 적절한 난이도의 데이터셋, Pretty-CLEVER 를 제시함

 

**task** : relational reasoning

 

**Method** : 
**Recurrent Relational Networks**: 스도쿠와 같이 각 step 마다의 결정이 다음 step 의 결정에 영향을 미치는 relational problem 을 graph 로 표현한 후, 이를 recurrent relational network 로 팍습하게 된다. 결정해야 할 state (스토쿠 숫자) 를 노드로, 이에 영향을 주는 다른 state (row, column, square 의 모든 숫자) 와의 edge 를 생성한다.


**1) massage passing** : 각 edge 마다 edge message 를 계산한다. edge 의 두 node 의 hidden state 를 concatenate 한 뒤, 파라미터를 공유하는 MLP f 에 통과시켜 edge message 를 생성한다. 이후, 노드에 연결된 모든 edge 의 message 를 sum 함으로서 해당 step 에서 최종 node message 를 결정한다. 


**2) node update** : 이전 step 의 hidden state, 계산된 현재의 node message, input feature vector 이 세 vector 를 concat 하여 node function g 에 통과시킨다. 

 

**Experiment** : 
sudoku , bAbI, Pretty-CLEVER 데이터셋에 대해 성능을 측정하였으며, 당시 bAbI dataset 에서 모든 task 를 풀고 SOTA 를 달성하였다. 또, hardest sudoku puzzle 에서 타 comparable method 와 비교해 sota 를 달성하였다. (solved 96.6% puzzle)

 

**총평** : recurrent network 를 이용해 순차적으로 puzzle solving 을 한다는 점에서 흥미로웠다. 단, 오래 전에 나온 논문인 만큼 이 논문을 cite 한 다른 후속 연구들이 더 흥미로워 보인다.
