# InfoGraph: Unsupervised and semi-supervised graph-level representation learning via mutual infromation maximization
### Fan-Yun Sun, Jordan Hoffmann, Vikas Verma, Jian Tang - ICLR 2020
#### Summarized by Jiye Kim

---

**Task** : Self-supervised graph representation learning



**Main Idean** : 
- Image에서 input data와 learned representation의 mutual information을 maximize 하는 deep infomax를 graph domain에 적용한 논문. 이 논문은 self-supervised, semi-supervised 두 개의 모델을 제안하는데,
1. Infograph: 전체 그래프의 representation과 graph 의 substructures의 mutual information을 maximize함 (self-sup setting),
2. Infograph*: student-teacher framework를 적용하여 student encoder는 supervised objective로 labeled data에 대해서 학습하고, teacher model은 위의 infograph를 사용하여 unlabeled data에 대해 학습함. student가 teacher로부터 배울 수 있도록 두 encoder의 intermediate representation의 mutual information을 maximize하는 term을 추가한다.
- Infograph에서 mutual information maximization 학습 방법: discriminator takes a (global representation, patch representation) pair as input and decides whether they are form the same graph. Jensen-Shannon MI estimator로 계산한다고 한다. 

**총평**:
- deep infomax를 graph domain에 적용한 논문. 이전 논문인 deep graph infomax와 방법론이 똑같은데 크게 차이점이 뭔지 잘 모르겠다. semi-supervised로 확장하는 방법도 제안했다. writing이 이해하기 쉽게 잘 적혀있다.
