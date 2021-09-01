# Transpose: Keypoint Localization via Transformer
## Sen Yang et al., School of Automation (China) - ICCV 2021
#### Summarized by Seungwook Kim
---

**총평**: 
* 아주 꼼꼼히 읽어보지는 않았지만, "Transformer를 이 task에 적용해 보았다" 외에는 별다른 novelty를 발견하지 못했다.
* transformer 자체의 특징인 global context / simple interpretability가 크게 작용하는 keypoint localization분야이므로, transformer 사용을 '처음 했다' 정도의 contribution 인 것 같다.
* CNN과 Transformer를 바꿔 사용하면 뭐가 다를까? 에 대한 예시로 적절한 논문이지만, 엄청 추천하는 논문은 아니다. 
* Human pose estimation을 위한다고 되어있으나, 일반적인 keypoint localization 이외에 human pose를 위한 추가적인 formulation / component가 없음.
* CNN architecture를 비판하는 데, 조금 위험한? 꼭 정확하지 않을 수 있는? 부분들에 대한 비판들이 있다고 생각돼서 있는 그대로 받아들이기엔 조심스러움


**Task**: Transformer for Human pose estimation


**Motivation / Contributions**
* Previous CNN architecture : challenging to figure out their decision processes due to
    * Deep non-linear modeles (transformer라고 다른 부분인가..?)
    * Implicit relationships (body part relation을 neuron단계에서 decouple하기 어려움)
    * 등등..
* CNN architecture: Poor scaling property
* Transformer: Good scaling property, views global context
* Keypoint localization based on transformer : conforms to interpretability of Activation Maximization
    * 설명을 어렵게 하지만 단순히 gradient를 통해 각 위치의 기여도를 알 수 있다는 뜻
* More lightweight & faster than mainstream CNN architectures

**Method / Architecture**

Truncated CNN for low level features + Transformers
* neuron activation to be maximized at GT keypoint location
* 이게 다임

**Results**

COCO & MPII datasets

더 작은 image size를 통해 FLOP/FPS는 CNN계열보다 더 높음
* 하지만 성능은 CNN(Darkpose, HRNet 등)을 이기지 못함, on par 정도

COCO pretrained -> generalization on MPII
* 여기서는 SoTA
* 하지만 다시 full-train 하면 CNN이 이김

Fixed pos encoding > Learnable > None
* Positional encoding은 항상 **뭐가 잘 되는지 다름**
* Absolute, relative, fixed, learnable을 다 조합해서 가장 잘 나오는 결과로 사용하는 게 일반적

Qualitative를 통해 더 좋은 interpretability가 있다고 주장
* Transformer에 inherent한 것으로 보이므로, 논문 자체의 contribution은 아닐 것으로 보임


