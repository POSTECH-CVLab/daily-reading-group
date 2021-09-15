# Movement Pruning: Adaptive Sparsity by Fine-Tuning
## Victor Sanh et al., Huggingface - Neurips 2020
#### Summarized by Seungwook Kim
---

**총평**: 
* Transformer계의 torchvision/timm인 huggingface가 저자여서 괜히 더 신뢰와 관심이 가는 논문이었다.
* Arxiv 2021논문인 Block Pruning의 전신이 되는 논문이기에 읽어보았다.
* 수학적인 background와 구현 detail까지 모두 이해하려면 조금 복잡할 수 있으나, 중심이 되는 아이디어와 컨셉은 아주 명료하고 설득력 있다.
* writing 또한 깔끔하며, transfer learning에 제한된 상황 + 실제 end-device를 고려할 때 도움이 될 pruning 기법이라고 생각한다.
* 다만 L0 pruning과 정확히 어떻게 다르며, 어떤 이점이 있는지에 대한 서술이 부족하다고 느껴진다.

**Task**: Network Pruning

**Motivation / Contributions**
* Magnitude pruning (leaving weights with large magnitude) is a widely used strategy
    * Less effective for transfer learning scenarios
        * weight values mostly predetermined by original model
        * prevents "magnitude pruning" from learning to prune based on finetuning step
* Propose **"movement pruning"**
    * prune based on **change in weights**
    * Weights that **shrink in magnitude** are pruned
        * both low and high magnitude weights can be pruned
* Outperforms other pruning methods in **highly sparse regimes ( <15% remaining weights)


**Method outline**

Refer to the paper for details in:
* Pruning decision (0th order vs 1st order)
    * movement pruning is 1st order
* Masking function
* Pruning structure (Local vs Global)
* learning objective
* Gradient form (Gumbel softmax? Straight-through?)
* Score matrix calculation formulae

The main outline is that: **weights are pruned based on their 'change in value' i.e. movement**
* Weights of any magnitude can be pruned (unlike magnitude-based pruning)
* L0 regularization is also 1st order pruning method, but differs in masking functions, pruning structure, etc

**Evaluation / Results**

Pretrained BERT model, finetuned on:
* question answering (SQuAD v1.1)
* natural language inference (MNLI)
* sentence similarity (QQP)

Magnitude pruning outperforms all methods at low sparsity values
* more than 70% remaining weights
* performs poorly at high sparsity

First-order methods (movement pruning, L0 regularization pruning) show strong performance in high sparsity scenarios

Distillation further improves performance (of all pruning types)
