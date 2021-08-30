# Improved Baselines with Momentum Contrastive Learning
### Xinlei Chen et al . (FAIR) - 2020 arxiv
#### Summarized by Suhyeon Jeong
---

 

**Overview : MoCo v2.** MoCo 에 SimCLR 처럼 MLP projection head 와 strong data augmentation 을 적용하여 성능을 끌어올림. (strong baselines that outperform SimCLR) SimCLR 와 비교해 large training batch 를 필요로 하지 않는다는 MoCo 의 장점을 그대로 유지하였음. 

 

**task** : unsupervised/self-supervised representation learning

 

**Method** : SimCLR 에서는 large batch size 를 통해 다양한 negative sample 들을 제공받고, output fc projection head 를 MLP head 로 replace 하였으며, stronger data augmentation 을 사용하였다. MoCo 는 queue 를 통해 large batch 없이도 많은 negative sample 을 얻을 수 있으므로 제외하고, 나머지 두 SimCLR 의 design aspect를  MoCo 에 도입하였다. 
* MoCo 의 fc head 를 2-layer MLP head 로 교체 ( only using this MLP head while unsupervised training stage, like SimCLR)
* 기존의 augmentation 에 blur augmentation 적용.
* SimCLR 와의 fair comparison을 위해 SimCLR 에서 사용했던 cosine learning rate schedule 도입 

 

**Experiment: **
1) MLP head 를 추가하는 것은 기존 MoCo baseline 에 비해 ImageNet accuracy 에서 큰 성능 향상을 보였다. (가장 effective 한 것으로 보임)

2) 특이한 점은, VOC detection task 로 transfer  하여 측정했을 때는 MLP head 를 추가하는 것 보다 augmentation 을 추가하는 것이 더 좋은 성능 향상을 보였다. (linear classification accuracy is not monotonically related to transfer performance in detection)

3) SimCLR 에서는 strong color distortion 이 매우 효과적인 것으로 나왔으나, MoCo 의 higher baseline 에서는 오히려 성능 저하를 보였다고 한다. 대신, blur augmentation 을 사용하였다.

4) 위에서 제안된 MLP head, augmentation, consine scheduler 를 전부 적용했을 때, same epochs and batch size 하에서 SimCLR 보다 5.6% higher ImageNet accuracy 를 달성했다고 한다. (200 epoch pretraining , 256 batch-size). 이는 simCLR with 8192 batch size 보다 0.9% higher accuracy 이다. 

5) SimCLR 를 large batch size 로 학습했을 때, 충분한 epoch 하에서 여전히 MoCo v2 의 ImageNet acc. 이 더 높았다고 한다.  SimCLR with 4096 batch size /1000 epochs : 69.3%,  MoCo v2 with 256 batch size/800 epochs : 71.1%

 


총평 : 사실 2페이지 짜리의 매우 짧은 논문이라 큰 내용은 없었다. 그냥 SimCLR 의 strong augmentation 과 MLP head 를 도입해 보았다는 것이 핵심이다. 읽으면서 초반에 읽어서 잘 기억이 나지 않았던 SimCLR 를 다시 복습할 수 있었다. 
