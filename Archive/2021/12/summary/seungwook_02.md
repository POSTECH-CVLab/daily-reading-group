# Post-Training Quantization for Vision Transformer
## Zhenhua Liu et al., PekingU, Noah's Ark Lab - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* The target problem is well-motivated, but the downsides of previous methods are vaguely proposed.
    * "Not suitable for transformer architectures with self-attention" - which does not always seem to be true.
* The motivation behind each solution/method proposed is well inspired and theoretically sound
* But the solution for each motivation does not seem to be "optimal" or well-searched
    * Which may not always be necessary, but it makes the paper look "easily improvable"

**Task**: As the paper title, post-training quantization for vision transformer

**Motivation**:
Previous methods are designed for CNNs and do not consider the unique structure of vision transformers (ex self-attention layers)

**Dataset**: CIFAR-10, CIFAR-100, ImageNet, COCO2017

**Method**:
* Similarity-aware quantization for Linear Operation
    * Such that post-quantization gives similar results after linear operation
    * similarity measure used is Pearson's correlation
        * which I don't think is usual in computer vision contexts, but not sufficiently explained "why"
* Ranking-Aware Quantization for self-attention
    * ranking loss is used such that the relative order of the output attention map is preserved after quantization
    * uses a hinge-function
* Bias correction
    * Quantization can shift the means of data (change in data distribution)
        * may lead to detrimental changes in following layers
    * subtract the expected error from the biased output such that the mean is preserved after quantization.
* Mixed Precision (not fixed precision for all different layers)
        
