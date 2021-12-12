# Adder Attention for Vision Transformer
## Han Shu et al., Noah's Ark Lab - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* The inspiration is simple but straightforward - one of those "natural" papers that were bound to be introduced
* The theoretical analysis for the proposed components and the results shown are interesting
    * I've usually seen more papers filled with empirical results rather than theoretical analyses
    * I'm not sure if one is better than the other, but I could realize that I lack theoretical analysis compared to empirical analyses (study maths..?)
* Results are great, paper is not greatly easy to follow due to tedious theoretical analyses
* Not sure why they reported energy, but not parameters / FLOPs / latency.

**Task**: Efficient and effective transformer architecture using l1-distance (implemented by addition) instead of multiplication-like operations in vanilla transformer

**Motivation**:
* AdderNet reimplemented convolutional networks (multiplication -> L1 distance)
    * "additiveization of CNNs"
    * avoids massive computation cost
* Proposes to take a similar approach to transformers

**Dataset**: MNIST, CIFAR, ImageNet

**Method**:
* For Linear Transformation, take similar approach to AdderNet
    * replace XW matmul to |X - W| like l1-distance
* For adder multi-head self attention, also replace matmul with l1-distance
    * also changes the scaling term to match the l1-distance implementation
    * which is a necessary step as "the adder layers output values with large magnitude"
    * the formulation behind the new scaling parameter is provided in the supplementary
* Rank analysis on adder attention matrix shows that using adder multi-head attention outputs attention matrix with very low rank (when compared to vanilla transformer)
    * main information is concentrated in the less large singular values for adder attention
    * theoretically shows WHY this happens (hard to understand)
    * and shows that adding an identity mapping (I) alleviates this problem (also hard to understand)
        * Does not justify that this is the "best" method to alleviate the low ranked problem
