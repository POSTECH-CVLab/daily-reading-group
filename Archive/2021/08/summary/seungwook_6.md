# End-to-End Object Detection with Transformers
### Nicolas Carion et al., FAIR - ECCV2020 Oral
#### Summarized by Seungwook Kim
---

**Task**: Object Detection
* Easily extended to panoptic segmentation 

**Motivation**: Mainly compares vs. Faster R-CNN, the most famous and well-performing competitor
* previous methods needs many hand-designed components to encode prior knowledge
  * NMS procedure
  * anchor generation

In contrast, DETR does not require any customizerd layers
* can be reproduced easily with standard CNN and transformer classes

Novelty => Motivation achieved + Easy extension to more complex tasks (panoptic segmentation)

**Method**: 
1. Object Detection as a **Set Prediction** task
    * fixed size N predictions ( N > typical number of objects in image )
    * produces an optimal bipartite matching between predicted and GT objects (including "no object")
2. Transformer Encoder + Decoder Architecture
    * Transformer used for its **global computation & feasible memory(unlike RNNs)**
    * Auto-regressive sequence models were used for set prediction 
        * Since RNNs -> Transformers in NLP, pick Transformers here too
        * Transformers can handle sets as well
    * **Encoder input**: Features from CNN backbone, reduced channel size using 1x1 conv
        * fixed positional encodings added at each attention layer
    * **Decoder input**: Encoder outputs + **N input embeddings**
        * each input embedding is for each of the N final predictions
        * learnable arguments named "object queries" (also added to each attention layer)
3. FFN (MLP) for prediction: 3-layer MLP with ReLU + Linear projection layer
    * FFN input: Transformer decoder output
    * predicts **Normalized coordinates, height, width of bbox w.r.t the input image**
    * Linear layer predicts the class label using softmax

**Experiments & Evaluation:**
* At inference time, some slots may predict empty class
    * overridden with second highest scoring class for AP optimization
* SoTA or comparable with Faster R-CNN
    * Faster R-CNN used for comparison is an improved version proposed in this paper
        * improved using generalized IOU loss to the box loss
        * improved using random crop augmentation
        * improved using longer training
    * Better for larger objects (due to global context?), worse on smaller objects (future direction)
* After encoder, already seem to separate instances.
    * Decoder only needs to attend to the extremities to extract the class and object boundaries (hypothesis)
* Performance drops 2.3AP without FFN
* NO positional encoding < Positional Encoding at input < Positional encoding every attention
    * but the differences are not very big between `at input` and `every attention`
    * **without PE**, drop of 7.8 - still achieves something! 
* Generalizes well to unseen numbers of instances (below N)
    * tested on synthetic inputs
* Easily extends to panoptic segmentation (SoTA)
    * mask prediction network after box prediction

**Questions & 정리:**
* Transformer에는 oversmoothing문제가 있으며, 후반부일수록 비슷한 embedding을 학습한다는 결과들이 있는데, 여기서는 encoder에서 벌써 instance discrimination이 진행된다 (oversmoothing X). 이는 아마도 token-wise loss가 적용하기 때문 (backprop from FFN, box prediction)일 것으로 예상. 따라서 oversmoothing 문제 해결법은 사실 이전에 암시되어 온게 아닐까?
* Set prediction도, RNN이나 MLP를 사용해서 이를 해결하는 framework도 존재하였기에 사실 transformer를 사용해서 object detection을 푼 것 자체에 큰 novelty가 있지 않다. 오히려 decoder단에서 learnable PE를 통해 (object query) box prediction을 가능하도록 만든 부분이 가장 큰 novelty로 보인다.
* Box prediction이 잘 되니 segmentation으로 extension이 잘 되는것은 뭔가 당연해보이는 것 같기도 하다. 
* Xavier Initialization을 하는데, 이를 하고 안하고의 차이가 클까?
* PE를 attention layer마다 넣어주는 게 더 좋은 효과를 내는지는 처음 알았음. 다른 domain에서도 마찬가지인가?
* 전반적으로 아주 clear하게 작성되어있으며, Related work + a의 느낌이 강해서 어색한 부분도 없다. Transformer를 도입하는 motivation 또한 강하며 (handling sets, permutation invariant, global computation, feasible memory compared to RNN), decoder 단에서 object query를 사용하여 box prediction을 하는 부분이 가장 큰 contribution이 아닐까 싶다.
  * 사실 이 부분도 기존 architecture에서 존재했을 수도 있다. 확인해보지 않아서...
* 아마 그렇기 때문에 image classification에 적용된 ViT가 더 큰 transformer열풍을 불러온 건 아닐까

