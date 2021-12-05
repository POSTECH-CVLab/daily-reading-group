# Florence: A New Foundation Model for Computer Vision
### Lu Yuan, et al. , arXiv 2021, Microsoft Florence Team
#### Summarized by Minguk Kang
---

총평: 

* UniCL 로스 함수의 temperature를 learnable하게 설정하며, Supervised Contrastive Loss와 D2D-CE 로스를 잘 혼합한 로스라고 볼 수 있음.

* 생각보다 모델 파라미터 수가 작은데 (893M: language transformer=256M and CoSwin-H transformer=637M), 학습시간은 오래 걸렸음 (512개의 A100 GPU머신으로 10일)

* 일부 테스크는 어뎁테이션을 위해 Dynamic Head, METER, Coswin 어뎁터들을 사용했는데, 이게 과연 foundation model이 맞나 의문이 들음.

* Twitter에서 해당 논문의 인기도에 비해 새로운 알고리즘을 제시하거나 엄청난 성능 향상을 보여준 논문은 아닌 것 같음. 오타가 조금 있지만 전체적으로 글은 잘 적은 것 같고 라지스케일 학습을 어떻게 하는지에 대해서 궁금하다면 빠르게 읽어보는 것도 좋은 것 같습니다.

Motivation:

* Human-like AI is not achieved by designing specific models to solve specific problems.

* CLIP, ALIGN, Wu Dao 2.0 are restricted to image to text mapping only tasks such as classification, retrieval, and tagging.
* What is the foundation model for computer vision?

Method:

* Foundation models for computer vision to be a pre-trained model and its adapters for solving all vision tasks in this Space-Time-Modality space.
* Present an emerging paradigm for building a vision foundation model, called Florence. Florence consists of data curation, model pre-training, task adaptations, and training infrastructure.
* For image encoder, they adopt hierarchical Vision Transformers (scale invariance nature and linear computational complexity w.r.t image size).
* use a unified image-text contrastive learning (UniCL, Yang et al., 2022?)
* Use ZeRO, activation checkpointing, mixed-precision training, and gradient cache to reduce the memory consumption.

Data:

* A new curated 900 million image-text pairs.

Results:

* show strength in zero-shot transfer in 12 classification downstream tasks (win 9 over 12, SOTA in ImageNet zero shot adaptation)
linear probe in 11 classification (9/11), and so on.
