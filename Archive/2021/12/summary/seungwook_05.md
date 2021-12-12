# SOFT: Softmax-free Transformer with Linear Complexity
## Jiachen Lu et al., Fudan University - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* Very similar to NystroFormer (in terms of method / motivation), but points out the theoretical flaws of NystroFormer
* The main idea is that "for linear transformers with transformer decomposition", SOFTmax should be eschewed
    * Thus, softmax-free transformer.
* Great novelty and meticulous ideation, and SoTA results when using large models (as this model has linear complexity) to match quadratic-complexity methods.
* Also evaluates on NLP benchmarks to prove the efficacy of the method.
* It was unfortunate that I could not capture all the theoretical details (Newton-Raphson method, Moore-Penrose inverse). This motivates further studying in various area of maths as well.

**Task**: Linear-complexity transformers without softmax using Nystrom.

**Motivation**:
* The usage of SoftMax for linear transformers with matrix decomposition is not theoretically well-justified.
* NystroFormer already uses Nystrom, but its ideations are not theoretically sound.

**Dataset**: ImageNet

**Method**:
* SoftMax-free self-attention
    * standard self-attention needs to apply row-wise softmax normalization on the full attention matrix
    * a direct application of matrix decomposition is infeasible. 
    * As a workaround, softmax is simply applied to all the ingredient matrices
    * this approximation IS NOT theoretically guaranteed.
    * replaces dot-product with Gaussian Kernel
    * W\_q and W\_k are identical to ensure symmetry (not sure why this is necessary)
* Low-rank regularization via matrix decomposition with linear complexity
    * Same as NystroFormer
    * only difference is that sampling is either done through 2DConvolution/AverageSampling instaed of random sampling
        * Shows that average sampling has shown the best results
* Could not fully understand why the implementation of Newton-Raphson and Moore-Penrose Inverse was necessary
    * needs more studying...
