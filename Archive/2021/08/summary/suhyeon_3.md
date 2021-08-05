# Scaling Local Self-Attention for Parameter Efficient Visual Backbones
### Ashish Vaswani et al. Google Research - CVPR 2021 (oral)
#### Summarized by Suhyeon Jeong
---

**Overview** : high performing convolutinal model 들의 성능을 상회하는 self-attention model , HaloNet 을 제시하였음. parameter-limited setting 하에서 ImageNet classification benchmark 의 SOTA 성능을 달성하였음. SASA 저자 들의 후속 연구.
 

**task** : self-attention / 2d image tasks

 

**Motivation** : SASA 모델에서는 일반 convolution 과 같이 target pixel 을 중심으로 k * k size 의 window 를 구성하였다. 해당 window 의 size 가 클수록 유의미한 성능 향상을 관측한 만큼, FLOPs 와memory 증가량을 최소화하면서 receptive field 를 늘리는 방법의 중요성이 매우 크다. 이에 저자들은 translational equivariance 를 relaxing 하는 대신 speed-memory 측면에서 강점을 살린 strided self-attention layer 를 제안하고, 이를 이용하여 모델을 구성하여 성능을 측정하였다.

 

**Method** : 
*blocked local attention*: 각 pixel 을 query 로 두었던 SASA 와는 달리, HaloNet 은 image 를 block 으로 나누어 같은 block 내의 pixel 들끼리 공유하는 local neighborhood 를 한꺼번에 extract 하여 연산량 및 receptive field 증가 시 memory/speed 패널티를 줄였다. 각 block 은 query 들의 group 처럼 동작한다. 단, 이렇게 pixel 별이 아닌 block 별 attention 을 진행함으로서 pixel-level translational equivariance 가 깨지게 된다. pixel-level translational equivariance 가 block-level translational equivariance 로 relax 되는 것이다. 하지만 저자는 실험적으로 이러한 relaxing translational equivariance 로 인한 성능 저하보다 receptive field 가 증가함으로서 생기는 이익이 더 크다는 것을 보였다. 
*attention downsampling* : SASA 에서는 average pooling 으로 처리했던 downsampling 을 HaloNet 에서는 query 를 subsampling 하여 single strided attention layer 만으로도 convolution 과 같은 downsampling 효과를 내었다. subsampling 한 query 만 연산하면 되기에  FLOPs 가 몇 배로 줄어들지만 accuracy 에는 큰 영향이 없었다고 한다. 이로 인해 computational cost 가 너무 커 학습이 어려웠던 large self-attention model 들을 개선할 수 있게 되었다 


 

**총평** : 저자들의 이전 논문, SASA 의 내용들과 중복되는 부분이 많고 이들과 본 논문의 기여를 명확하게 구분할 수 있도록 적혀져 있지 않아서(특히 section 2.1) misunderstanding 을 유발했던 것 같다. local 한 writing 은 깔끔했으나 global 한 writing 구성이 깔끔하지 못하다는 느낌을 받아서 아쉬웠다. 하지만 그와는 별개로 attention 모델의 memory/speed 를 개선하고, 또 high performing convolutional model 의 성능에 준하는 결과를 내었다는 점에서 중요한 논문이라고 생각된다.
