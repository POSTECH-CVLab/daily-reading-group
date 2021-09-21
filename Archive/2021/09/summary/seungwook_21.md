# torch.manual seed(3407) is all you need: On the influence of random seeds in deep learning architectures for computer vision
## David Picard, Ecole des Ponts - Arxiv 2021 report
#### Summarized by Seungwook Kim
---

**총평**:
* Random Seed에서 오는 차이가 확실히 유의미하다. Pretrained network의 경우, random seed에 의해 batch composition만 달라졌는데 (해당 실험 세팅의 경우) 그런 경우에도 0.5의 accuracy차이가 발생했다.
* 따라서 실험을 할 때 randomness에 대한 robustness study를 하는 것이 좋을 것 같다. Neurips를 보면 이미 실행되고 있는 것으로 보인다.
* 작은 규모로 진행된 시험이기 때문에, 더 큰 규모의 실험과 더 많은 seed를 사용한 실험을 통해 결과를 발전할 수 있으면 더 참고할만한 자료가 될 것 같다.

---

**Task**: Image classification

**Motivation**: Investigate the effect of random seed on the accuracy
* Is there a distribution?
* Are there black swans? (radically different results)
* Does pretraining on large datasets reduce variability from seed choice?

**Setup**
* To test large number of seeds, training has to be fast
* Use ResNet with 9 layers only
    * Taken from [DAWN benchmark](https://dawn.cs.stanford.edu/benchmark/about.html)
* CIFAR: from scratch
    * 10000 seeds, each taking 30 seconds to train & evaluate
    * 500seeds, each taking 1 minute to train & evaluate
        * make sure that it was close to convergence
* ImageNet: use pre-trained networks
    * trained for 50 seeds
    * Architectures:
        * supervised ResNet50: 2 hours per seed
        * SSL ResNet50 : 3 hours per seed
        * SSL ViT : 3 hours and 40 per seed
            * lower throughput & more steps: longer time needed
    * 50 seeds, 2hours training

**Limitations**:
* Budget constraint: could not reach up to SoTA results
    * variations of results in this paper "may" disappear after longer training times / better setup
    * but results are on par with SoTA results of 2016 when ResNet was first introduced
* Models are still evaluated on convergence

**Results**
* Cifar)accuracy values having 0.5% difference in accuracy are equally common across seeds
* Cifar)distribution: fairly concentrated and pointy, no skew can be seen in figure
    * variation does not converge after accuracy converges: **some seeds are just intrinsically better**
* Cifar)There are black swans - produces up to 1.82% accuracy difference
    * significant value!
* ImageNet)Same initial state, only the "batch composition" varies
    * still (max)-(min) accuracy of 0.5%
        * pretraining on large datasets does reduce variation, but does not mitigate it.
    * significant increase as well
    * variation may have increased more if tested with more than 50 seeds
