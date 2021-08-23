# Mobile-Former: Bridging MobileNet and Transformer
### Yinpeng Chen et al., Microsoft / University of Science and Technology China - Arxiv 2021
#### Summarized by Seungwook Kim
---

**Task**: Efficient Architecture for Image classification & Object detection
* Mainly compared models: MobileNet 계열

**Novelties & Contributions**:
* Leverage MobileNet (local processing) and transformers (global interaction) together
* Instead of series (local processing -> global interaction) as proposed in previous work, proposes **parallel** design (local processing + global interaction)
  * 논문의 그림을 보면 더 잘 이해 될 것 같습니다.
  * 병렬적으로 MobileNet과 Transformer를 사용하며, 서로 two-way bridge (cross-attention)을 통해 interaction.
* MAC / Accuracy 대비 MobileNet 계열/다른 Transformer model들 이김
   * SoTA는 아님! (FLOP이 제한된 경우에서만 SoTA)

**Method**: **Parallel Mobile-Former**\
Input: 
* Local Feature map (Image processed with 1 conv layer) 
* Global tokens (random init, ~6 tokens)
  * 특이하게, image-specific한 token을 만들어내는 것이 아님.
  * 아마 mobileNet과의 커뮤니케이션을 통해 iamge-specific해진다는 디자인 choice인듯
  * 잘 설명이 안 되어있음..

**Mobile sub-block (MobileNet)** \
MobileNet 사용
* ReLU 대신 Dynamic ReLU
  * ReLU vs Parameteric ReLU : PReLU는 negative 값에 대한 gradient를 어떻게 할지 학습함
  * PReLU vs DY-RELU: DY-RELU는 postiive 값에 대한 gradient까지 학습으로 결정함
  * 왜 DY-RELU를 택했는지는 설명 안함 


**Former sub-block (Transformer)**
* 일반적인 Transformer block
* Token 개수를 6개로 고정 (매우 적은 개수)
  * 이후 ablation을 보면 1개만 사용해도 크게 성능이 떨어지지 않음
  * 6개 넘게 쓴다고 성능이 높아지지 않음
  * 단순히 Mobile sub-block을 통해 image-specific 해지는 정도가 아닌가 생각됨

**Mobile->Former bridge (Cross-attention)**

Cross-Attention module
* Mobile에서 들어오는 token들을 따로 Key/Value 로 mapping하는 weight을 없앰 (lightweight reasons)

**Former->Mobile bridge (Cross-attention)**
Cross-Attention module
* Former에서 들어오는 token을 따로 Query 로 mapping하는 weight을 없앰 (lightweight reasons)

전반적으로 ImageNet classification / COCO object detection에서 FLOP대비 가장 좋은 성능을 냄
* 하지만 구성 component가 많아서 parameter 개수는 조금 많은 편임 (limitation으로 기술되어있음)

**총평**:
* existing architecture + tranformer 연구 중 하나. 자칫 흔해보일 수 있으나, 이 과정을 **parallel하게 진행하며, FLOP/MAC이 많이 요구되지 않는 디자인**으로 구현한 여러 디자인 초이스 (요약에 다 다루지 않음) 이 큰 novelty로 느껴지며, 성능도 FLOP대비 잘 나온다.
* 하지만 design choice들에 대한 설명이 부족할 때도 많으며, Param개수는 비교적 높기 때문에 아직 발전의 여지가 많다.
* 따라서 design choice/parallel design이 유일한 novelty인데, 이정도로도 architecture를 만들 수 있는 하나의 다양성이 추가되었다고 생각하여 괜찮은 novelty같다.
* ICCV format처럼 생겼는데, 과연 붙었을지 궁금하다.
