# Recurrent Parameter Generators
## Jiayun Wang, Yann LeCun et al., UCB / FAIR / MIT / NYU - Submitted to NeurIPS 2921
#### Summarized by Seungwook Kim
---

**Task**: Recurrently using the **same parameters for many different convolution layers** to build a deep network
* Inverse approach to model compression / pruning
    * Model compression: Removing unused parameters from a large model
    * Proposed method: Squeeze more informatiomn into a small number of parameters

**Motivation**:
1. Model performance generally scales with number of parameters
    * model is significantly overparametrized
    * previously attended to by morel compression/pruning/etc

2. In a neural network, the model gets larger as it gets deeper
    * Propose RPG that **shares a fixed set of parameters in a ring and use them to generate parameters of different parts of a neural network**

**Contributions & Novelty**:
1. RPG: given a certain NN architecture, can flexibly choose any number of parameters to construct the network
2. on-par or SoTA performance compared to pruning methods.
3. Destructive weight sharing: Competitive performance to several recurrent weight-sharing methods.

> Destructive weight sharing: prevent different kernels from sharing the representation during weight sharing.

**Method**:
1. Recurrent Parameter Generator
* Create a single set of parameters to generate parameters for each convolution layer i.e. $\text{Kernel Weight} = \mathbf{R}_i \cdot \mathbf{W}$
* R is a generating matrix, one for each layer to create.
    * Not created, but predefined 
2. Destructive Generating Matrices
* Need to prevent kernels from sharing the representation during weight sharing
    * 아니면 같은 weight set을 사용한다는 이유로 redundant한 layer들이 만들어질 가능성이 있는 것으로 보임
* Random permutations / element-wise random sign reflections 등을 사용한다고 하는데, 이론적 배경을 잘 이해하지 못함..
    * Neurips 2019 : Superposition of many models into one 논문 참고
    * "tend to lead to destructive weight sharing and better utilization of the parameter capacity"
3. Even Parameter Distribution for different layers
* if random sampled elements from W, may not be optimal
    * some weights in W may never be used
* evenly sample from W for each individual layer.

**Evaluation & Results**
* Tested on classification (CIFAR/ImageNet), Human Pose estimation (MPII), Multitask regression (S3DIS)
* outperforms equilibrium models
* Global RPGs > Multiple RPGs
    * Can use multiple RPGs for different parts of the NN
* Compared to ResNet, ResNet-RPG achieves higher accuracy **with same parameter size**
    * Resnet18 vs ResNet34-RPG
    * ResNet18-RPG < ResNet34-RPG **at same parameter size**
        * larger final model is still better?
* Outperform SoTA pruning methods
* Higher out-of-distribution performance compared to original models
* As parameter size increases, so does the feature similarity
    * RPG itself can be pruned as well!
* Performance falls gracefully as parameter decreases

**총평**:
1. 연구분야와 상관이 없지만 재미있어보여서 읽었습니다. 결론적으로 정해진 pool의 weight에서 조합을 하여 neural network layer를 만들어낸다는 개념입니다. 따라서 훨씬 적은 parameter 수로 큰 model 을 근사할 수 있게 되는 것이 장점입니다.
2. 잘 이해하지는 못했지만 destructive weight sharing등의 도입으로 인해 같은 parameter size의 경우, 기존 모델보다 좋은 성능을 보이는 것이 신기했습니다.
3. 전반적으로 writing은 깔끔하지만, 조금 급하게 쓴 티가 납니다 (그림이 조잡함, 사소한 writing실수, attention model에는 설명 없음, evaluation에 대한 해석 부족)
4. 그래도 매우 재미있게 읽었으며, 앞으로 이런 방향의 연구들이 더 나오지 않을까 생각합니다.
