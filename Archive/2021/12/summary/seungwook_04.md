# TransMatcher: Deep Image Matching Through Transformers for Generalizable Person Re-identification
## Shengcai Liao et al., IIAI - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* Deep image matching using transformers - not a novel idea anymore, but seems to be a novel component when integrated with Person-reid
* It has already been shown that using imag ematching for explicit prior for person reid (metric learning) is beneficial, so the only technical novelty remaining is 'deep image matching using transformers'
* It may have been much more interesting if they have run ablation tests on using other matching algorithms (NCNet, CHM, etc) instead of their own implemented transformer-based image matcher
    * For one, it does not show enough information to decide whether previous matching methods are not as effective
    * Second, it does not show enough information to decide whether the design choices made in this work for transformer-based image matching is sensible.
* Also, no results (other than very limited qualitative results on person re-id datsets) on image matching.

**Task**: Person re-id using transformer for deep image matching

**Motivation**:
* QAConv showed that explicitly performing image matching helps generalization of learned model in person re-id
* Investigate the possibility of applying transformers for image matching and metric learning.

**Dataset**: CUHK03-NP, Market-1501, MSMT17

**Method**:
* Use transformer encoder for query & gallery
* In decoder stage, dot-product similarity between query & gallery features
    * Layerwise features are used, since multiple transformer layers are stacked
    * The scores are added along the many layers
    * Dot product results -> \* score embedding with sigmoid (0~1) -> GMP (max pooling) -> BatcnNorm -> MLP head + addition with previous score
    * GMP is used to enforce "hard" attention.
* Uses single-head, multi-head has shown similar results
* SoTA on all datasets, better results compared to using vanilla transformer decoder (with softmax, no score embedding)
