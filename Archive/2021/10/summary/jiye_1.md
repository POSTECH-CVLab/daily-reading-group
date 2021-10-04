# Reliable fidelity and diversity metrics for generative models
### Muhammad Ferjad Naeem, Seong Joon Oh, Youngjung Uh, Yunjey Choi, Jaejun Yoo - ICML 2020
#### Summarized by Jiye Kim

---

### **Task** : 
Evaluation metric for image generation model



### **Main Idea** : 
-  기존에 많이 쓰는 metric인 FID, IS score 같은 경우 fidelity와 diversity를 구분하지 못한다. 그리고 기존에 있는 precision and recall, improved precision and recall metric은 fidelity와 diversity를 따로 평가하기 위해 제안되었지만, 여전히 단점이 존재한다. Precision & recall의 경우 embedding space가 uniformly dense하고 k-means algorithm을 사용해서 계산이 된다는 단점이 있다. 이 단점을 해결하기 위해 improved precision & recall이 제안되었지만, 여전히 단점이 존재하는데 1) k-nearest neighbor로 manifold를 계산하기 때문에 real outlier, fake outlier 둘다에 취약하여 manifold를 overestimate한다 2) recall을 계산할 때 Fake sample embedding마다 KNN을 수행하기 때문에 computationally inefficient하다.

이 논문은 위의 단점을 해결하는 density and coverage라는 metric을 제안했다.



### **Method** :  
Density:

- precision의 대안으로 제안됨. 기존 improved precision은 하나의 real outlier때문에 Real manifold가 over-estimate되어 fake samples들이 모두 real manifold에 들어가게 되는 문제가 있었다. Density는 (fake sample이 몇개의 Real sample의 ball에 들어가는지) / (Knn의 k의 개수) 로 정의되어, fake sample이 real manifold에 들어갈지라도 몇개의 real sample의 ball에 들어가는지까지 고려하기 때문에 real samples이 densely packed되어 있는 region에 중요도를 더 준다. Real samples의 density까지 고려할 수 있는 metric이다.

Coverage:

- 기존 recall은 fake sample기준으로 manifold를 구성하는데 이에 따라 두가지 문제가 발생한다. 1) precision과 똑같이 fake outlier가 있을 때 fake manifold를 overestimate해서 real sample이 모두 fake manifold에 들어가게 되는 문제, 2) fake sample의 embedding마다 knn을 계산해야되서 computationally inefficient함(knn - O(kMlogM)). 이를 해결하기 위해 coverage는 fake sample이 아닌 real sample을 기준으로 manifold를 구성한다. 이유는 1) real sample이 fake sample 보다 outlier가 적기 때문이고, 2) 매번 knn을 할 필요없이 real sample embedding에 대해 한번만 하면됨.
- Coverage는 "fraction of real samples whose neighborhoods contain at least one fake sample"로 정의된다.

Precision & recall은 두 distribution이 같을 때 1이 나오지 않는데 density coverage는 1이 나오는 것을 analytic하게 보였다.




### **Experiment** :
Toy data, real data에 대해 각각 실험을 진행했다.

1. Toy data

- Gaussian distribution을 하나 만들고 outlier를 각각 다른 위치에 두면서 precision recall density coverage를 계산. outlier때문에 앞에서 설명한 것과 같이 precision, recall은 원하지 않는 지점에서 1이나오는 것을 확인. 두 Gaussian이 완벽하게 겹치는데도 불구하고 precision, recall은 1이 나오지 않느는 것을 확인, 반면 density coverage는 이런 문제가 발생하지 않음.
- Real distribution을 기준으로 mode dropping을 수행. Simultaneous dropping(여러개의 mode의 sample수를 점진적으로 감소)의 경우 coverage는 점진적으로 감소하지만 recall은 줄어들지 않다가 갑자기 감소하는 것을 보임. → Coverage는 implicit하게 fake sample의 density를 고려할 수 있다.

2. Real data

- fake sample에 의도적으로 outlier를 추가함. recall은 outlier를 추가할 수록 증가하는 모습 → outlier에 vulnerable함. coverage는 증가하지 않음.
- Mode dropping을 수행. 위의 fake data와 같은 결과가 나옴. (recall은 갑자기 감소, coverage는 점진적으로 감소.)
- Fidelity와 diversity를 잘 capture하는지 확인하기 위해 truncation technique을 사용해서 확인. Z의 threshold를 늘려갈수록 density는 감소하고 coverage는 증가하는 것을 확인.
- VAE구조에서는 NLL(negative log likelihood)를 계산할수있어서 truncation techinique을 사용해봄. NLL은 거의 변하지 않아서 NLL만 사용하는 것은 fidelity, diversity에 대한 충분한 정보를 주지 않는것을 확인. D&C는 많이 변함.

또한 추가적인 실험으로 imagenet과 많이 다른 dataset에 대해 학습된 generative model을 평가할 때는 imagenet pretrained model이 잘못된 bias를 줄수 있음으로 random initialized된 model embedding을 사용하는게 더 좋다는 것을 보임.



### **총평**:
- Precision & Recall의 문제점을 정확히 분석하고 해결방법을 제시하고 실험적으로도 이를 잘 보인 논문이다. metric이 좋다고 주장하기 위해 필요한 실험 설계를 잘 한것 같다. 어느 정도 특정한 상황을 가정하고 그것에 맞는 해결책을 보인 것 같은 느낌이 드는데, knn으로 manifold를 계산하는 이상 계속 발생할 것 같은 문제같다.
