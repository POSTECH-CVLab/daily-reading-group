# When does self-supervision help graph convolutional networks?
### Yuning You, Tianlong Chen, Zhangyang Wang, Yang Shen - ICML 2020
#### Summarized by Jiye Kim

---

**Task** : self-supervised graph representation learning



**Contribution** : 
- GCN에 적용할 수 있는 3개의 self-supervision schemes(Pretraining& finetuning, self-training, multi-task learning)를 설명하고 multi-task learning scheme이 다른 두개의 방법보다 좋다고 주장한다.

- 2개의 새로운 self-supervised learning 방법을 제안했다.

- self-supervision을 통해 adversarial attack에서 robustness를 향상할 수 있다고 주장한다.


**Method** :

1. Three schemes

- pretraining & finetuning: 가장 많이 쓰이는 방법이지만, pretraining(self-sup)과정과 finetuning(supervised) 에서의 objective가 달라지기 때문에, 특히 shallow GCN에서는 pretraining 으로 얻은 정보가 쉽게 손실(overwritten)된다고 한다.

- self-training: 적은 label에서 시작해서 얻은 highly confident unlabeled sample에 pseudo labels을 부여하여 점점 label을 늘려가며 학습하는 방법이다. 논문에서 지적한 단점은 label rate이 높아질 수록 self-training을 통한 performance gain이 쉽게 saturation 된다고 한다. 또한, self-training으로 줄 수 있는 label이 한정적인 것도 단점으로 지적한다.

- multi-task learning: supervised objective와 self-supervision objective를 weighted sum하여 multi-task로 동시에 학습시키는 방법이다. 여기서 self-supervision task는 regularization 역할을 한다. 3개의 scheme 중에 가장 general하고 가장 효과적인 self-supervising 방법이라고 주장한다.

 

2. Self-supervised Tasks

- Node clustering: node의 feature vector를 기준으로 clustering을 수행하여 이를 pseudo label로 학습하는 방법이다.

- Graph partitioning: graph를 minimize edgecut하면서 k개의 subgraph로 나눈다. 이때 balance constraint(각 subgraph가 비슷한 개수의 node를 가지도록)를 추가로 준다. 이렇게 graph partitioning을 수행하고 나온 partition indices를 self-supervised label로 준다.

- Graph completion: target node의 feature를 지우고 주변 노드로 부터 target node의 feature를 예측하게 하는 방법이다.

**Experiment**:

- 위의 세개의 scheme중에 multi-task learning 방법이 가장 성능 향상이 높았다고 한다.

- 위의 세개의 self-supervised task를 각각 적용해보았을 때, 각 dataset에 따라 가장 잘되는 task가 달랐다.

**총평**:
- self-supervised task를 제안하고 많이 쓰이는 self-supervision schemes을 분석해놓은 논문이다. 3개의 scheme을 분석해놓은게 흥미로웠다.
