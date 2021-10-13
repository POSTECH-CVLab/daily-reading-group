# Towards Reverse-Engineering Black-box Neural Networks
## Seongjun Oh et al., Max-Planck Institute for Informatics - ICLR 2018
### Summarized by Seungwook Kim
---

**총평**:
* 인공지능대학원 QE 일환) 오태현 교수님의 추천으로 읽게 됨.
* Black-box model의 attribute를 예측해내는 모델을 디자인 한 부분이 흥미로웠다. 간단한 방법들로 이렇게까지 가능한 게 신기했으며, MNIST뿐만 아니라 ImageNet pretrained model에도 적용 가능함을 확인했다.
* 널리 쓰이는 비전 모델에는 또 어떤 취약점이 있을지 궁금하다.

**Task**: Reverse Engineering Neural Networks
* Architecture (activation function, dropout,,,) / Optimizer (Optimizer algorithm, batch size) / Data (data split / dataset size)

**Method**: 
Assume black-box test models \
Use a 'dataset of classifiers' to train (10000 MNIST modesls sampled from all possible model configurations) \
Prune out low-performance classifiers \
May use 'ensemble of models': results in 11,282 final models for MNIST

**Metamodel**: Model to process the query input-output of the neural network to output model attributes
* **kennen-o**
  * Use outputs of queries (ie classification output for queries) as input
  * 2-hidden layer MLP, 12 parallel linear layers for simultaneous prediction of attributes (total 12)
  * The query images are usually taken from the validation set - the query set of images are always fixed
  * overall) Query models with query images. Use their output as input to MLP for attribute prediction.
    * the 'output' may be just the top-1 value, bottom-1 value, all the logits, or the rankings of likelihood.
* **kennen-i**
  * "Condition" the query input, so that the output directly reveals an attribute value.
  * ie) original model takes MNIST image as input, outputs which number it is likely to be (0~9)
  * ie) we input a 'conditioned' image as input, which outputs the predicted value of an attribute (one attribute per conditioned image)
  * create conditioned image: initialized from a random image from valid dataset, "learn" the query image to output "predicted attribute value" using SGD.
    * somewhat like pertubation attack 
* **kennen-io**
  * Combination of kennen-o and kennen-i
  * i.e.) Use MLP with 12 parallel linear layers to simultaneously predict attributes from model outputs
  * i.e.) but also condition the input images for the cause 
  * for stability, train kennen-o first, then update kennen-i and -o components alternatively


> **Loss**: such that the estimated attribute value is close to the actual value

**Results & Analysis**
* Accuracy of attribute prediction by "chance" (ie random) : 34.9
* Using kennen-o: ~73.4
* Using kennen-i: ~52.7
* Using kennen-io: 80.1%
  * 80.1% accurate in estimating the type of activation, whether dropout was used, whether pooling was used, kernel size, number of convolution layers...etc
* For kennen-o: using bottom-1 output as input to MLP is better than using top-1
  * top-1 predictions are rather uniform across high-performance classifiers
  * bottom-1 predictions give much more auxiliary information
* What is blackbox-models (test model) is quite different from the models used in training?
  * still much better than 'estimation by chance', while worse than using 'random selection training' instead of having 'splitting attributes' to split on.

Small test on ImageNet dataset: to prove efficacy for more larger/public models
* use kennen-o (MLP) to estimate the model type (ResNet/ VGG / SqueezeNet / VGG-batchnorm / DenseNet)
  * \> 90% accuracy, depending on number of queries used
* **Knowing the network type enables making architecture-specific adversarial examples!**
  * Thus this information enables an adversary to make more effective adversarial examples for misclassification
