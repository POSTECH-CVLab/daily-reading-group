# The functional correspondence problem
## Zihang Lai et al., CMU - ICCV 2021
#### Summarized by Seungwook Kim
---

**총평**:
* Instance-level 과 semantic-level을 넘어 functional-level correspondence라는 task를 새로 제안함.
* 유의미한 approach라고 생각은 하지만, unseen pair가 아닌 unseen instance에 대해서도 generalization이 가능한지가 궁금해진다. 과연 정말로 'functionally' 일치하는 부분을 찾고 있는지가 궁금하다.
* 그래도 functional correspondence라는 주제가 흥미롭다고 생각하여, 이 연구를 확장할 수 있는 방향이 없을지 고민 중
* Intra-category functional matching은 semantic matching과 다를 게 없다. 하지만 5개의 keypoint annotation만 사용하여, 기존의 데이터셋에 적용하기에는 무리가 있어보인다. 

**Task**: Functinal (Affordance) correspondence

**Motivation**:
* Unlike instance- and semantic- level matching, humans can also match functional parts
* When it comes to intra-category functional matching, it becomes the same as semantic-level matching

**Dataset**: FunKPoint
* 10 tasks from TaskGrasp dataset
* 5 object categories per task
* For each category, 100 images from ImageNet or Google iimge search
* Filter out images with multiple objects / missing or occluded parts
* 4044 train pairs and 741 test pairs

**Method**: Task-driven modular architecture

ResNet-50 feature --> N layers with M convolutional modules each.
* input to a module is a weighted sum of the outputs of the modules in the previous layer
* the weights vary by task
    * calculated from (learnable) task embedding -> Gating network.
* Naive & Straightforward architecture to learn task-dependent features. (and weights)

**Loss**: Contrastive learning objective
* Features of keypoints from each iamge are identicla only when they are functional correspondences

**Results**:
* No significant baseline - SoTA on FunKPoint, PCK ~60 
    *  Using baseline ResNet: ~22
    *  Human annotator: ~80
* Proposes that its learned features are better at few-shot learning/grasp prediction/other applications
    * but the main comparison is done against ResNet backbone
    * This method uses "mean" of all possible output features (w.r.t task embedding), which would of course hold more information compared to results of a single ResNet backbone
    * Not sure if this is fair
