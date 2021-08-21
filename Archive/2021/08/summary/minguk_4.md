# Unsupervised Learning of Visual Features by Contrasting Cluster Assignments
## Mathilde Caron, Ishan Misra, Julien Mairal, Priya Goyal, Piotr Bojanowski, Armand Joulin - Neruips 2020
#### Summarized by Minguk Kang
---

**Overview**: SwAV는 CPC, CMC, MoCo, SimCLR, SimCLR2, MoCO2, BYOL, SwAV, SimSiam으로 가는 Self-supervised learning 족보에서 거의 마지막을 담당하고 있으며 기존의 contrastive instance discrimination (data-to-data relationships을 explicit하게 본다)과는 다르게 prototype이라는 것을 도입하여 data-to-prototype 관계를 학습하여 representation learning을 하는 모델입니다.  ImageNet linear evaluation Top-1 결과는 75.3%로 BYOL (74.3) 보다 살짝 높다는 특징을 가지고 있습니다. 

**Method**: 주어진 데이터 x를 augmentation하여 새로운 이미지 x_1과 x_2를 만듭니다. 이를 feature extractor에 넣어 image embeddings z_1, z_2를 추출하게 되는데 여기 까지는 기존의 self-supervised learning과 같은 방법을 사용합니다.  그 이후가 상당히 다른데 주어진 배치의 상태를 고려하여 prototype을 초기화 하고 (배치 내의 이미지들이 프로토 타입에 유니폼하게 분배되도록 초기화를 진행) soft assignment 하여 code matrix Q*를 구해줍니다. 이렇게 구해진 Q를 가지고 swap prediction을 학습하게 되는데 (z_1은 q_2를 예측하도록, z_2는 q_1을 예측하도록), 이러한 consistency restriction이 이미지의 공통된 부분을 인식하여 좋은 표현학습을 할 수 있게 해준다고 주장하고 있습니다. 마지막으로, cropping을 조금 더 memory efficient하게 하기 위해 multi-crop이라는 것을 도입하는데 이는 various resolutional crop을 통해 swap prediction을 하는 방법을 의미합니다. 

 

**Experiments**: linear prob, transfer learning on downstream task, training in small batch setting 등 다양한 세팅에서 실험을 수행하였고 역시 잘된다!

 

**총평**: 논문이 그렇게 친절하게 작성되어 있는 것 같지는 않다. 저자의 이전 워크인 Deep cluster를 공부하고 읽는다면 쉽게 읽을 수 있지만 그렇지 않다면 정신을 바짝차리고 읽어야 이해되는 논문. Self-supervised learning의 마침표 같은 느낌이라 시간이 난다면 다들 읽어보는 것을 강추한다.
