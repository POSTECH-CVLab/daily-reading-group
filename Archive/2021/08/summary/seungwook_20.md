# Relational Embedding for Few-shot Classification
### Dahyung Kang et al., POSTECH - ICCV 2021
#### Summarized by Seungwook Kim
---

**Task**: Few-shot classification

**Novelties & Contributions**:
* Learn self-correlational representation for few-shot classification
  * extracts transferable structural patterns within an image
* Cross-correlational attention module for few-shot segmentation
  * learns reliable cross-attention between images via convolutional filtering
* SoTA on four standard few-shot classification benchmarks

**Method**: Relational Embedding Network (RENet) \
Input: Support Images / Query \
Output: Image embedding for all support images & query image

Pipeline:

1. Self-correlational representation
   * HxWxC -> HxWxUxVxC through Hadamard product at each position with neighborhood (UxV)
   * HxWxUxVxC -> HxWxC through series of 2D conv without padding
   * This part learns "relational features", helping the learner understand "what to observe"
   * Add output HxWxC with input HxWxC (relation features + base features)

2. Cross-correlational attention
   * construct 4D correlation tensor between a support image and the query image
   * perform separable 4D convolution on the correlation tensor 
   * Average along support/query image dimensions of the output 4D tensor to obtain cross-attention maps for query/support
   * This part meta-learns cross-correlational patterns, helping the learner understand "where to attend"
3. Learning Relational embedding
   * Sum-pool ( Attention map X Feature map)
     * outputs final embedding

Finally, query is classified as class of its nearest support embedding

**Learning objective (Loss)**:
1. Anchor-based classification loss
   * Guides the model to correctly classify a query
2. Metric-based loss
    * Guides model to map query embedding close to average support embedding of the same class

**총평**:
* 실험 부분에 대한 요약은 따로 안했지만, Ablation 실험이 많이 진행되었습니다. 특히 self-correlation, cross-correlational을 보며 자연스럽게 self-attention / cross-attention을 떠올릴 수 있었는데, 이런 부분에 대한 ablation을 통해 오히려 convolution-based self/cross correlation이 더 좋았다는 것을 보였습니다.
* relational feature를 weight가 아닌 (attention처럼), 그 자체로 사용되는 것을 많이 보지 못해서 신기하게 읽었습니다. Few-shot setting에서 도움이 된다는 것을 잘 보인 논문이라고 생각합니다.
