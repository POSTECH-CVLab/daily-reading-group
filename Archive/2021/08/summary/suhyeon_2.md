# Stand-Alone Self-Attention in Vision Models
### Prajit Ramachandran et al. Google Research  - NeurlPS 2019
#### Summarized by Suhyeon Jeong
---

**Overview** : 당시 attention 은 convolution model 과 함께 쓰이는 것이 일반적이었는데, 최초로 convolution 없이 attention 만으로 이루어진 Stand-Alone Self-Attention(SASA) model 을 제안함으로서 attention 도 그 자체만으로 stand-alone primitive 가 될 수 있음을 보였다. 저자는 ResNet 의 convolution layer 들을 local attention layer 로 치환하여 classification 과 detection 에서의 모델 성능을 측정하였다.

**task** : self-attention / 2d image tasks

 

**Motivation** : 이제껏 attention module 들은 computer vision task 에서 중요하게 쓰여왔지만, convolution layer 를 대체하지는 못했다. 이에 저자들은 convolution layer 를 대체하고 hierachy 를 구성할 수 있는 local self-attention layer 를 제시하였다. 
 

**Method** : 


**1) local attention layer**: convolution 처럼 local 한 image 일부에 대해서 single attention 을 진행하도록 구성하였다. 예를 들어, spatial extent 가 3 인 경우, target feature 을 중심으로 하는 3x3 범위의 pixel 들을 이용해 key 와 value 를 생성한다. 이 때 query 는 target feature 만으로부터 생성된다. 
query 와 key 를 내적한 값에 2d relative positional embedding 을 포함한 항을 추가하여 attention 을 생성한다. 마지막으로 softmax 를 거친 attention 값을 value 와 element-wise 하게 곱한 값들을 sum 함으로서 target feature 에 대한 최종 output 을 생성한다.

이는 attention 을 이용해 content-based filter 를 생성한 것과 같다. query 와 key 의 조합으로 self-attention 의 content-based interaction 으 강점을 살리고, relative positional embedding 을 추가하여 query 와 relative position of key pixel 간의 content-geometry interaction 을 학습함으로서 translational equivariance 한 효과를 유도하였다.



**2) fully attentional vision models** : ResNet 에서 spatial convolution 들을 local attention layer + max pooling 으로 대체한다. convolutional stem 의 경우 distance based information 을 1 x 1 pointwise convolution 시 추가해 주어 distance based weight parametrization 을 가지는 convolution 과의 격차를 해결하였다. 

 

**총평** : 성능 면에서 CNN based model 을 대체할 만큼 우수한 성능을 보이지는 못했지만 self-attention 만으로 이루어진 model 을 구성했다는 점, 파라미터를 절감하고도 CNN baseline(Resnet 50) 에 대해 competitive 한 성능을 내는 모델을 구성했다는 점에서 역사적인 논문이다. 
