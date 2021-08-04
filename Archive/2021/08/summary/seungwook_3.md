# Spatial-Temporal Transformer for Dynamic Scene graph Generation
### Yuren Cong et al., Leibniz University, University of Twente - ICCV2021 Oral
#### Summarized by Seungwook Kim
---

**Task**: Dynamic (Video) Scene graph generation
 
**Motivation**: \
Scene graph generation from videos (dynamic) is a new field \
Challenging because of dynamic relationships between objects and temporal dependencies \
Scene graph generation: promising approach towards holistic scene understanding and acts as a bridge connecting large gap between vision and language
 
**Contributions/novelty:** \
@Spatial-Temporal Transformer (STTran): Spatial Encoder + Temporal Decoder to infer dynamic relationships \
--> Takes varying input length \
@Multi-label classification is applied in relationship prediction \
@Verify that temporal dependencies have a positive effect on relationship prediction \
@ SoTA on Action Genome (the only dataset in this field?)
--> Previously all scene graph generation methods were for static images
 
**Method**: \
**Faster R-CNN for region proposal** \
Initialize representation vector (relationship between objects) as concatenation of various position/semantic/weighted features
 
**Spatial Transformer**: Per single frame, takes as input all relationships within the frame. \
@ Just a single layer of encoder is used in practice \
@ Does not use pos. encoding (all relationships are not in a certain order) \
**Temporal Decoder**: Uses learnable frame encoding (positional encoding)
@ Uses window size 2 for each input (t. t+1 from previous), stride 1 \
@ (1 2) (2 3) (3 4).... \
@ 하지만 이러면 2부터 2번씩 등장하게 되는데 (1 2)(2 3)... 먼저 나온 output을 결과로 쓴다고 함 \
@결론적으로 temporal이라고는 하지만 순서가 엄청 잘 고려된 것 같진 않은 느낌 (frame encoding도 2개의 포지션에 대해서만 학습되고)
 
**Graph generation**: \
Semi Constraint--> multilabel classification으로 relationship을 정의한 뒤, confidence가 threshold이상이면 (0.9 < ) prediction으로 사용. \
(With Constraint --> Top 1 만 사용, No Constraint --> Threshold 없음)
 
**Results**: \
SoTA on AG dataset in terms of differnet metrics (PredCLS, SGCLS, SGDET)
Video 순서를 reverse/shuffle하면 성능이 (소폭) 하락하는 것으로 보아 temporal dependency가 중요함을 보임
 
**총평:** \
evaluation할 데이터셋이 단 하나밖에 없는 (Action Genome) 블루오션 같습니다.
AG데이터셋을 제안하는 논문 이후로 첫 논문인지 비교하는 baseline은 다 기존에 static image에 사용하던 SGG 기법들입니다. \
또한 제안하는 Transformer가 단순히 Spatial -> Temporal로 이어지는 sequential구조인데,
Spatial Transformer만을 기존의 Static Image SGG 기법과 비교했을때는 오히려 떨어지는 성능을 보였습니다. \
또한 현재 제안된 Temporal Transformer의 sliding window (window size=2)는 지나치게 naive한 기법이라고 생각이 들었습니다. \
Naive한 기법에, 완전하지 않은 individual model임에도 불구하고 oral paper로 억셉된 이유는 새롭지만 중요한 분야이고, 적당한 베이스라인을 제안했기 때문이라고 생각합니다.
dataset에서 사용되는 relationship type 개수가 25개인데, 왜 R@50이 100이 아닌지는 살짝 의문입니다. \
저도 한 번 시도해보고싶을 정도로 발전할 여지가 많은 분야인 것 같습니다.