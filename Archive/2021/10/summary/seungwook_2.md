# Learning Rate Annealing Can Provably Help Generalization, Even for Convex Problems
## Preetum Nakkiran, Harvard U - Arxiv 2020
#### Summarized by Seungwook Kim
---
**Task**: Learning rate scheduling

**총평**:
* 논문 기간동안 다양한 실험을 돌려보다가, '어떤 learning rate / lr scheduler를 써야할까'라는 고민을 하며 읽은 논문입니다. 간단한 이론을 간단한 예시로 보입니다.
* 일반적으로 learning rate/learning rate scheduler 가 novelty에 포함되는 경우는 없지만, 어떻게 해야 연구할 때 "가장 짧은 시간동안 가장 좋은 성능을 낼 수 있을까"를 고민하게 되었습니다. 실제로 논문을 읽다 보면 다양한 learning rate scheduling을 사용한 논문들을 심심치 않게 볼 수 있습니다.
* 결국 적절한 lr/scheduler를 찾는 것 자체가 시간이 부족한 상황에서 너무 큰 overhead라 생각해서 fixed lr로 진행하게 되었습니다.
* **여러분은 어떤 learning rate / scheduler를 사용하나요? 좋은 연구는 lr/scheduler에 영향을 크게 받지 않아야 한다고 생각하시나요?**

**Main Idea**: 
1. It has already been shown that Learning rate scheduling helps generalization.
    * but only been proven for non-convex problems
2. Shows that LR scheduling (annealing) can help generalization in **convex** problems as well.

**Method & Results**:
Shows a toy convex optimization example
* low learning rate (gradient flow) vs Learning rate annealing
* Shows that in the toy example, Learning rate annealing results in significantly lower test loss
* Occurs due to different loss landscape of train and test 
