# Where and What ? Examining Interpretable Disentangled Representations
### Xinqi Zhu et al. The University of Sydney  - CVPR 2021 oral
#### Summarized by Suhyeon Jeong
---

**Overview** : supervision 없이 interpretability 측면에서 disentangled representation 을 학습할 수 있도록 돕는 module과 loss 를 design 하고 간단한 unsupervised model selection method 를 제안하였다. 

**task** : learning disentangled representation / Generative model

 

**Motivation** : Disentangled representations 는 data variation 에서 independent factor 를 포착해낸다. disentanglement 는 세 가지 갈래로 characterize 할 수 있는데, 이는 informativeness, independence, 그리고 interpretability 이다. 이 중 interpretability 는 unsupervised setting 에서 거의 다루어지지 않았다. 언뜻 보기에 interpretability 는 human-defined concept 와 representation 과의 관계라 ground-truth label 없이는 학습이 어려워 보이지만, 저자는 human's definition of concept 에 some general biases 가 있다는 점에서 착안하여 두 hypotheses 를 정의하고 이를 바탕으로 module 과 loss 를 design 하였다.

**Method** : 저자는 interpretability 에 대한 두 hypothesis 를 세웠는데, 이는 각각 다음과 같다.


**1) Spatial Constriction**:  a representation is usually interpretable if we can consistently tell where the controlled variations are in an image


**2) Perceptual Simplicity** :  an interpretable code usually corresponds to a concept consisting of perceptually simple variations

이 중 Spatial Constriction 에서 착안하여 feature map 상 영역별로 latent code 의 영향을 규제하는 module 을 design 하고, latent dimension 에 간단하게 data variation 을 embed 하도록 돕는 loss 를 design 하였다.

**Enforcing Spatial Constriction - SC Module** : AdaIN 을 이용하여 latent code c 와 Input feature map 을 받아 modified feature map 을 생성하고, input feature map 으로부터 soft-version of binary rectangular mask 들을 generate 하여 combined rectangular 영역에만 modified feature 가 들어가도록 feature map 을 update 한다. 이를 통해 controlled variation 이 필요 영역에만 나타나도록 disentangled representation 을 학습한다.

**Encouraging Perceptual Simplicity - PS loss** : generated image 로부터 latent code 를 추측하는 recognizer Q 를 추가하여 latent code c 와 c의 일부 dimension 에 perturbation 을 더한 c' 으로부터 generate 된 두 image 를 이용해 c 와 c' 을 추측하도록 한다. 이 loss 를 dimension wise MSE loss 로 디자인하였다. 이 loss 를 줄이기 위해 모델은 specific latent axis(perturbation 이 추가된 일부 dimension) 상에 easily recognizable variation 을 embed 하게 된다. perturbation 이 추가되는 non-shared dimension 은 매 iteration 마다 새로 randomly select 되므로 training distribution 을 전부 matching 하기 충분하다. 

저자는 위의 SC module 과 PS loss 를 둘 다 적용한 PS-SC model 을 구성하였고, 이들이 우수한 disentangled representation 을 학습함을 실험적으로 보였다. 추가적으로 저자는 Perceptual Simplicity 를 측정하는 model selection method , TPL을 제안하였다. 

**Traversal Perceptual Length** : latent 의 individual axis 가 pure variation 을 controlling 한다는 것을 확인할 수 있는지 알기 위해 우선 저자는 accumulated perceptual distance 를 정의하여 latent axes 상의 variation 이 other direction 보다 simple 하다는 것을, 즉 preceptually anisotropic 함을 보였다. 이에 착안하여 all latent axes 상의 accumulated perceptual distance score 을 측정하는 Traversal Perceptual Length(TPL) 을 제안하였다. TPL 은 다른 model selection method 와 비교해 단일 모델만으로 측정 가능하고 classifier 에 의존하지 않는 등 다양한 장점을 가지고 있다.


**총평** : 해당 분야에 대해 잘 알지 못하는 사람조차 이해가 가능하게 하는 깔끔하고 명료한 storytelling 과 writing 이었다. 아직 해당 분야에 대한 식견이 좁아 비슷한 연구가 있었는지는 모르지만 disentangled representation 에 대한 두 hypothesis 의 아이디어와 이를 적용한 방식이 참신하고 재미있었다. 
