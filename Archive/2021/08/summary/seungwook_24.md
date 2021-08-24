# Do Vision Transformers See like Convolutional Neural Networks?
### Maithra Raghu et al., Google Research/Brain - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**:
* 이전에 정리했던 "How to train your VITs"의 하위호환 격의 논문이라고 생각함. ViT와 CNN의 차이를 분석하고자 하는 성격은 동일함
* 크게 새로운 사실은 없으며 (많은 다른 논문들을 통해 이미 알려진 사실들이 많음), ViT 모델만을 가지고 실험을 진행하기 때문에 (DeiT, TnT등은 없음) 사실 제한된 세팅에서의 비교실험이라고 할 수 있을 것 같음.
* 또한 실험적인 결과와 결론을 사용하고, 그 뒤에 "왜?"인지에 대한 이론적 배경 서술은 부족하기 때문에 크게 novelty가 있다고 느껴지지 않음
* 다만 해당 논문을 통해 밝혀진 empirical한 결과들을 설명하기 위한 theoretical 내용을 새로운 novelty로 내세운 논문이 나올 수 있을 것 같음.
* Visual Transformer에 대한 이해가 아직 많이 부족한 시점이라고 생각됨.  
---


**Task**: Explore how vision transformers solve vision tasks
* Differences vs CNN
* Explore information aggregation, spatial locazliation, effect on transfer learning...

**Novelties & Contributions**:
* Experiments comparing CNNs (ResNets) and ViTs 
* Empirical results & analyses through extensive experiments

**Findings**

> Note: Used Centered Kernel Alignment (CKA) for quantitative comparisons of representations across networks

1. Lower and higher layers in ViT show greater similarity than in ResNet
   * ViT propagates representations between lower and higher layers more strongly
2. Many more lower layers in ResNet are needed to compute similar representation to the lower layers of ViT
3. Highest layers of ViT have quite different representations to ResNet
   * mostly for CLS token representation manipulation
4. Even in the lowest layers of ViT, self-attention layers have a mix of local heads (small distances) and global heads (large distances)
   * In ResNet, only attend locally in the lower layers
   * With not enough data (ImageNet instead of JFT), ViT does not learn to attend locally in earlier stages
     * results in lower performance
     * **Using local information early on for image tasks is important for strong performance**
     * This property is hardcoded in CNNs (locality)
5. First half of transformer: CLS token representation is primarily propagated by skip connection, while spatial token representations largely come from the long branch (not skip connection)
   * reversed in latter half 
   * NOT explained why, or what this suggests
6. Removing skip connections in ViTs is much more critical than in CNNs
   * 4% performance drop when skip connection removed from middle layers
   * (representation propagation relies largely on skip connection)
7. Spatial information is better preserved in transformers than in CNNs (CKA between corresponding patch position)
   * This is thanks to the usage of CLS token
   * If Global Average Pooling is used for transformer, the spatial information is not preserved better than CNNs 
   * 개인적으로 misleading한 설명이라고 생각함. Representation 이 비슷하더라도 (CKA를 통해 확인), 그 위치에 대한 representation preservation이 좋은거지 "spatial information"을 잘 preserve했다고 할 수 있나? Locality가 있는 CNN이 더 우수할 수 밖에 없는 부분이 있을텐데...
8. 더 많은 데이터로 pretraining하는 게 transfer learning에 더 도움이 됨
   * 모델이 클수록 마찬가지

개인 의견:
* 4번에서, lower layer of transformer에는 local & global context를 같이 본다는 게 신기하다. (global만 보지 않는다는 뜻)
  * 다만 데이터를 적게 사용하면 local attention이 줄어든다는 결과는, 과연 데이터의 개수때문인지 아니면 데이터셋의 난이도 때문인지 확인할 필요가 있어 보인다. 단순히 개수가 적은 데이터셋에서는 난이도가 낮아서 local하게 볼 필요가 없었다거나...
* 5번에서, CLS token/Spatial token representation이 skip connection/long branch를 통해 오는 이유에 대한 파악이 필요해보인다. Transformer의 후반부는 CLS token manipulation에 대부분 사용된다는 것인데, 어떠한 이론적인 접근이나 해석이 있으면 좋을 것 같다.
