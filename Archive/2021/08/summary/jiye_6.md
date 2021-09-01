# Unsupervised Learning of Visual Features by Contrasting Cluster Assignments (SWaV)
### Mathilde Caron, Ishan Misra, Julien Mairal, Priya Goyal, Piotr Bojanowski, Armand Joulin - NeurIPS 2020
#### Summarized by Jiye Kim

---

**Task** : Unsupervised representation learning



**Main Idea** : 
- contrastive learning 방법은 일반적으로 이미지의 feature들을 직접 비교했다면, 본 논문은 같은 이미지로 부터 나온 augmented images들에 같은 cluster가 할당되도록 cluster assignments의 consistency를 맞추는 방법으로 학습을 진행했다.

 
**Motivation** : 

- contrastive learning에서 주로 pairwise feature comparison을 수행하는데, 이것이 computationally challenging하기 때문에 feature를 바로 비교하지 않고 비슷한 feature를 갖는 이미지들의 cluster assignment만 맞추자는 것이 motivation이다. (task의 난이도를 낮추자)


**Method** :

- 먼저 하나의 이미지를 augment해서 두 개의 이미지를 만들고 feature를 뽑는다(f_1, f_2). 각 feature는 prototypes vector C를 통해 codes Q로 매핑되게 된다. code Q가 각 feature의 cluster assignment 역할을 하게 된다. 여기서 f_1은 f_2의 code인 q_2를 예측하게 하고, f_2는 q_1을 예측하게 한다. 이렇게 하는 이유는 f_1과 f_2가 비슷한 정보를 가지고 있다면 f_1를 통해 q_2를 예측하는게 가능할 것이고, 반대로 f_2를 통해 q_1를 예측하는게 가능할 것이기 때문이다. (swapped prediction)

- 배치 단위로 학습을 할 때, 어떤 경우에는 prototypes C에 의해 mapping된 codes가 모두 같아질 수 있다. 이렇게 배치 안의 모든 feature가 C에 의해 같은 code로 매핑되는 trivial solution을 막기 위해, entropy term을 도입하여 배치 안의 샘플이 서로 다른 code로 어느정도 균등하게 배분될 수 있게 한다.

- Q가 optimal transport가 되도록 Q에 constraint를 주었다고 하는데 이 부분은 잘 이해를 못했다.

- multi-crop이라는 새로운 augmentation 방법을 제안했다.

 

**총평**:
- contrastive learning 방법과 deep clustering을 합친 것 같은 논문이다. 차이점은 feature를 바로 비교하지 않고 cluster assignment의 consistency를 맞추게 하였다는 점과, online clustering이 가능하도록 prototype vector를 도입했다는 점이다. method는 단순한데, 논문이 이해하기 어렵게 적혀있는 것 같다.
