# Assessing generative models via precision and recall
### Mehdi S. M. Sajjadi, Olivier Bachem, Mario Lucic, Olivier Bousquet, Sylvain Gelly - NIPS 2018
#### Summarized by Jiye Kim

---

### **Task** : 
Evaluation metric for image generation model



### **Main Idea** : 
-  이전에 리뷰했던 improved precision and recall metric for assessing generative models의 전 논문으로 FID와 IS가 single-valued score이기 때문에 이미지 생성의 중요한 두가지 aspects - diversity and fidelity - 를 구분하지 못한다고 지적하면서 처음으로 두가지를 구분할 수 있는 precision, recall measure를 제안한 논문이다.



### **Method** :  
우선 reference distribution P, generated distribution Q를 각각 두가지 term으로 쪼갠다

$P= \beta\mu + (1-\beta)\nu_P$

$Q=\alpha\mu+(1-\alpha)\nu_Q$

의미상으로 $\mu$ 는 P와 Q가 겹치는 부분에 대한 distribution, $\nu_P ,\nu_Q$는 각각 P, Q에서 $\mu$로 커버되지 않는 부분에 대한 distribution이다.

따라서, $\alpha$는 precision: 생성된 이미지들이 얼마나 실제 이미지에 속하는지

$\beta$는 recall: 실제 이미지들 중 생성된 이미지가 얼마나 커버하는지를 나타낸다고 볼 수 있다.



위의 식을 통해 PRD(Q,P)를 정의할 수 있는데, 어떤 $\alpha$ , $\beta$에 대해서 위의 식을 만족하는 임의의 distribution $\mu,\nu_P,\nu_Q$가 존재하면 이 $\alpha, \beta$는 PRD(Q,P)에 들어간다고 정의한다. 이렇게 나온 PRD curve를 통해 precision, recall 의 tradeoff를 확인할 수 있다.



하지만 모든 가능한 $\alpha$ , $\beta$에 대해서 위의 식을 만족하는 $\mu,\nu_P,\nu_Q$이 있는지 확인하는 것은 매우 힘들기 때문에 Thm2를 통해 다른 방법으로 PRD를 계산할 수 있는 방법을 제안한다.

practically 어떻게 사용되나?

- FID 와 비슷하게 pretrained inception network를 사용해서 real, fake sample의 embedding을 계산한다. 이 sample들의 embeding의 union을 mini-batch k-means (k=20)을 통해 clustering한다. 그러면 각 cluster assignment에 대한 1 dimensional histogram이 나올텐데 (histogram for real samples, histogram for fake samples) 이 histogram들을 각각 distribution으로 간주하여 위의 방법으로 PRD를 계산한다. (직관적으로 각 cluster assignment에 비슷한 수의 real, fake sample이 있어야 잘 생성되었다고 생각할 수 있음.)




### **Experiment** :
- MNIST dataset으로 real sample은 class 5개만을 담도록 고정해놓고, generated sample은 class 1~10까지 바꾸면서 PRD curve를 재봄. 1에서 5까지 갈때는 precision은 그대로, recall은 올라야하고, 5에서 10까지 갈때는 recall은 그대로 precision은 올라야한다. 이를 반영하는 것을 실험적으로 보임.
### **Other details** :

- 해당 방법은 PRD curve라는 커브 형태로 measure를 하기 때문에, 다른 모델과 비교가 용이하도록 하기 위해서 이 curve를 summarize할 필요가 있다. 이 논문에서는 F_1 score의 변형, maximum F_beta score를 사용하는 것을 제안하는데 F_(1/8) 과 F_8을 사용하는 것을 제안한다. F_8은 precision보다 recall 에 가중치를 더주고, F_(1/8)은 recall 보다 precision에 가중치를 더 주는 measure이다.

### **limitations** :
- k-means 를 매번 수행해야함. k-means는 random성이 있기 때문에 여러번 수행해서 average를 해야함.
- 논문에서 F_8, F_(1/8)을 쓰라고 제안했지만 사실상 infinitely many measure가 나올 수 있음.
- embedding space 가 uniformly dense하다는 것을 가정한다.

### **총평**:
- FID, IS 이후로 생성 이미지의 diversity, fidelity를 따로 고려해야한다는 motivation은 좋지만 제안한 precision, recall의 formulation이 너무 복잡한 것 같다. 이렇게 formulation을 한 의도도 잘 이해되지 않았다. 내용이 어렵고 잘 와닫지 않는 논문이었다. 장점은 PRD curve를 그릴 수 있기 때문에 어느정도 recall범위에서 precision이 어떻게 되는지 등 세부적인 분석이 가능하다는게 장점인 것 같다.
