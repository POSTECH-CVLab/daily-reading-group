# Towards Reverse-Engineering Black-Box Neural Networks
## Seong Joon Oh et al., Max-Planck Institute for Informatics – ICLR ‘18
#### Summarized by Seungwook Kim
---

**총평**:
* GSAI QE 의 일환으로 읽게 됨
* Deploy된 black-box model을 어떻게 whitening할 수 있을지에 대한 방법론을 제시
* 컨셉은 참신하고 새롭지만 읽기 편하게 되어있고, 여러 궁금증을 해소할 수 있는 실험도 다양하게 준비되어있어서 읽기 좋았음

**Task**: Whitening black-box models
* Find out attributes (ex #conv layers, #fc layers, dropout used? max pooling used? nonlinear activation function used...etc)
* uses a series of queries and outputs to the black-box model

**Motivation**:
* To propose a threat to existing black-box models, and show that their attributes (architectural, training..) can be determined using a series of query inputs to the model

**Dataset**: MNIST-Nets, ImageNet
* Most experiments done on MNIST-Nets, a dataset of 11K Mnist models with various attributes
* ImageNet: Just a simple experiment to show that the 'backbone architecture used' can be classified
    * SqueezeNet, ResNet, DenseNet, VGGNet, VGGNet-BatchNorm

**Method**:
1. Kennen-o
    * sample data from validation set
    * Train time) provide these sample data as input, observe the output
    * Train & Test time) Use MLP over the output to predict model attributes.
2. Kennen-i
    * Traintime) gradient is backpropagated to the input image
    * Traintime) i.e. the input image is crafted for attribute prediction
    * One image for one attribute prediction
    * Outputs the attribute prediction STRAIGHTAWAY, without reasoning over the output
3. Kennen-io
    * Mixture of Kennen-o and Kennen-i
    * Craft inputs, and reason over the outputs

**Results**
* Kennen-io > Kennen-i > Kennen-o
* Kennen-o when used on ImageNet, can classify what family of architecture was used with >90% accuracy (when using >100 query images)
* Knowing which family of architecture was used can be exploited, because adversarial examples transfer better WITHIN a family of architecture.
