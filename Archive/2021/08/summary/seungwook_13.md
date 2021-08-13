# DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification
## Yongming Rao et al., TsinghuaU, UCLA - Submitted to Neurips2021
#### Summarized by Seungwook Kim
---

**Task**: Efficient Visual Transformers  
**Main Idea**: Dynamic Token sparsification \
**Motivation**:
1. Final prediction in vision transformers is based on a **subset** of most informative tokens
2. That means we can prune the tokens of less importance in the input instance!  

**Contributions & Novelty**:
1. Proposes DynamicViT, a lightweight prediction module to predict tokens to be pruned **dynamically** 
* Adopts gumbel-softmax for differentiable sampling from distribution 
* Attention masking for faster speedup  
* Can supervise the approximate amount of tokens to be pruned 
2. Reduce 31 ~ 37% GFLOPs and improve throughput by over 40%
* drop in accuracy is within 0.5% for different transformer architectures.

**Method**:
1. Hierarchical Token sparsification\
Gradually drop uninformative tokens as computations proceeds
* predicts a decision mask (one-hot tensor) 
    * Uses previous decision mask + tokens as input
    * Combine local features (tokens + decision mask) + global features (aggregation of local features) -> MLP -> Softmax -> Sample using Gumbel softmax (differentiable sampling!)
    * Once a token is dropped, it is never used


2. Handling zeroed tokens \
Same as conventional self attention, except that the **final softmax is performed only over non-zeroed elements**
* Why not just throw away the tokens?
    * Gumbel-softmax may zero out different number of 0s during training.
* Why not just leave them as zeros?
    * They affect the attention training at the softmax layer. 

3. Test time inference \
The zeroed-out tokens can now be just discarded
* Train time has minimal cost overhead (gumbel-softmax)
* test time is much faster & lighter! (discard unused tokens)

Losses used:
1. Classification Loss
2. Distillation loss
    * Distills from full, unpruned model 
    * make the finally remaining tokens of the DynamicViT close to the ones of the teacher model
        * kind of self-distillation?
3. KL divergence loss to minimize the prediction difference (teacher - student)
    * Different from distillation loss, distillation targets the token representations
    * This loss targets the final predicted class 
4. Ratio loss
    * constrain ratio of the kept values to a predefined value

**Results & Evaluation**:
* Comparable to SoTA(~-0.5%) with reduced GFLOPs (~37%) and higher throughput(~54%)
* SoTA trade-off between model complexity & top-1 accuracy 
* Dynamic token sparsification > Model scaling (as in efficientNet) to reduce size
* Visualizations show that DynamicViT finally focuses on the objects in the images
    * Better interpretability as well

**총평**:
1. 오늘 만진이형이 세미나에서 소개했던 What can eight tokens do? 와 비슷한 motivation입니다. 다만 그 논문은 token들을 aggregate하여 token의 개수를 줄인 것이며, input단에서 바로 줄이지는 못했습니다. 이 논문에서도 ablation을 진행하진 않지만 이론상 input단에서도 바로 줄일 수 있는 것으로 보이며, 기존 token들의 aggregation을 사용하지 않고, 계산을 통해 필요없는 토큰을 있는 그대로 버립니다. 따라서 처음에 교수님들께서 기대했던 formulation에 더 가까운 논문이라고 생각합니다.

2. 다만 Loss에서 distilation loss를 굳이 추가해준 이유가 궁금합니다. Sparsification과 cross-entropy loss만 사용하는게 더 sensible하다고 생각되는데, 굳이 fully-trained backbone에서 2개의 distillation loss를 해줘야 성능이 나오는걸지 궁금합니다. 해당 loss들 때문에 오히려 novelty가 떨어지는 느낌이며, 결국 fully trained model이 필요하다면 train-time때는 오히려 2개의 모델을 train해야하는 불편함을 감수해야 하는 것으로 보입니다.

3. 그래도 learnable sampling과 그에 따른 inference-time때의 시간/메모리/계산량 improvement가 인상적이며, 매우 읽기 쉽게 되어있습니다. 다만 sampling또한 이전에 제안됐던 (주홍이형의 DHPF에서도 사용되는) Gumbel-softmax를 사용하기에, "newly proposed method"라기보다는 "novel combination of existing novelties"가 될 것 같습니다. 과연 붙을지 궁금하네요!




