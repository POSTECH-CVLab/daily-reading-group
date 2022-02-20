# Open-vocabulary Object Detection via Vision and Language Knowledge Distillation
## Xiuye Gu et al.,Stanford/Google - ICLR 2022
#### Summarized by Seungwook Kim
---

**Short-sentences summary**
* Object detection methods are usually trained/tested on predefined classes (predefined vocabulary). This paper aims to tackle **open-vocabulary** object detection to test detection method on 'novel' classes as well.
* The proposed method, ViLD, is a two-stage pipeline. First stage is class-agnostic region proposal ( such that it can be generalized to novel classes).
* The second step identifies the object idenfied from the proposal.
* The core component of ViLD is the usage of existing, large open-vocabulary classification models (CLIP, ALIGN...) to extract text and image embeddings for train the ViLD network with fully supervised training (text) / knowledge distillation (image).
* The idea is interesting and the results are good, but the method relies heavily on CLIP and ALIGN, which the paper proposes nearly no analysis on.
