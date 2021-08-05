# An Empirical Study of Training Self-Supervised Vision Transformers
### Xinlen Chen et al., FAIR - ICCV 2021 Oral
#### Summarized by Seungwook Kim
---

**Task**: Self-supervised Vision Transformers \
Also: Convolution vs Transformers, Training receipes for vision transformers, instability in transformers

**Contributions / Novelty**:
1. SSL in ViT based on Siamese networks, unlike masked auto-encoding SSL (ex. iGPT)
2. Investigate fundamental components of training transformers
* Batch size, learning rate, optimizer
3. Propose a simple trick to improve stability of ViT self-sup training
* Does not result in catastrophic failure, but "mild" degradation in performance
* **Solved by freezing the patch projection layer in ViT**
    * Consistently improves accuracy
4. For very large transformers, SSL pretraining can outperform supervised counterparts
* Proves that self-supervision pretraining may be needed (over full supervision)
5. Self-supervised ViT has competitive results vs big CNN ResNets 
* proves potential of ViT (lesser inductive biases)
6. Proposes rooms for ViT model to improve
* ex) removing positional encoding in ViT only degrades accuracy a little
    * ViT can learn strong representation without position bias?
    * Currently not exploiting position information sufficiently?
7. MoCo V3, an incremental improvement of MoCo v1/2
    * sligthly better linear probe accuracy (+1.6%) on ImageNet
    * due to **extra prediction head and large batch (4096) training**

**Stabilty of Self-supervised Transformer Training**:
* KNN shows failure patterns for increasing batch size
* KNN shows failure patterns for increasing LR
    * low LR shows underfitting
* LAMB optimizer is sensitive to LR compared to AdamW (Final choice of optimizer: AdamW)

**Trick for improving stability**
* freezing the projection layer
    * random patch projection layer (untrained) to embed patches
    * Done by stop-gradient (`requires_grad=False`, or `layer.detach()`)
    * shown to be effective in all self-sup frameworks using ViT
* Gradient clip is useful if given a sufficiently small threshold
    * which is equal to freezing the layer at the extreme

> Note: Can still be unstable if learning rate is too big. \
> Freezing the layer is not a fundamental solution to be problem.

**Experiments/Evaluation/Results/Discussions**:
* TPUs scale up more favorably than GPUs with increasing number of devices
    * 본 실험에서 TPU를 256 ~ 512개씩 사용함 (ㅎㅎ;)
* Positional encoding: Sine-cos >= Learned >= None 
    * Not a large difference between no positional encoding 
      * Model can learn strong representations by just a SET of patches?
      * Current ViTs cannot exploit position information efficiently?
* Class token: With class token >= No class token + no LN > No class token with LN
    * CLS token is not essential (not much difference)
    * Choice of normalization layers can make a difference
* Classification head with BN > no BN
    * No BN is quite competitive
    * BN may not be necessary for contrastive learning
* Larger SSL Vit is better than supervised counterpart when trained in ImageNet-1K
    * "suggests" that SSL is **less prone to overfitting**
* Results are saturated overall , unlike NLP where bigger transformers are always better
    * limited power of instance-based frameworks?
    * underlying instance discrimination task as a pretext task may be **too easy to achieve**
        * may insufficeint to learn stronger representations

**Questions/Potential directions + 총평**:
1. What could be a better pretext task for a strong representation of images?
2. How can different normalizationm methods affect the learning process (in detail?)
    * Weight norm, Layer norm, batch norm, group norm...
3. MLP with BN shows improvement: Is BN (and other normalization) also a form of bias?
4. What could be a better exploitation of position information apart from positional encoding?
5. What could be the fundamental problem/solution to instability in ViTs?
    * **NOTE:** BiT and ViT also shows to suffer from these instabilities
6. Is there a **theoretical** explanation behind why SSL outperforms full-sup on certain fields?

전반적으로 GPU를 많이 사용하여 다양한 실험을 할 수 있는 그룹 (FAIR)에서 할 수 있는 연구였지만, 많은 한계와 문제점을 여과 없이 보여줌으로서 전반적인 학계를 위한 연구 방향성을 제시한 중요한 논문이라고 생각합니다. \
논문에 기재된 연구 자체는 많은 GPU가 필요하겠지만, 개별적인 질문들/제한에 대한 연구는 그렇지 않을 수도 있다는 점에서 GPU 사용이 비교적 자유로운 그룹에서 내는 '이상적인' 논문이라고 (개인적으로) 생각이 듭니다. \
중요한 점들이 많이 제안되었다고 생각하며 transformer관련 연구를 하는 분들은 꼭 한번즘 읽어보는 게 좋을 것 같습니다.
