# An Image is worth 16x16 words : Transformers for Image Recognition at Scale
### Alexey Dosovitskiy et al., Google Research, Brain team - ICLR 2021 oral
#### Summarized by Suhyeon Jeong
---

**Overview** : convolution 을 완전히 배제한 기존 attention based model 들 보다 effectively scalable 하며 large scale data 로 pretrain 시 훨씬 적은 computational resources 만으로 convolution based SOTA model 과 비등한 성능을 내는 model, ViT 을 제안함. Original transformer encoder 구조를 최대한 유지하면서 image data 에 적용시킴.

**task** : attention model, image classification

**Methods** : image 를 patch 로 잘라 embedded patches + class embedding 을 transformer encoder 의 input 으로 넣음. class embedding 의 encoder output 을 사용하여 MLP head 로 classification 진행

* 기존 attention 사용 모델들은 pixel 별로 attention 을 계산하여 과도한 연산량을 요구하거나, local neighborhood 끼리 attention 을 진행하여 연산량은 적절해도 hardware accelerator 를 efficient 하게 사용하기 위해서는 complex engineering 필요한 경우가 많음/ 혹은 너무 작은 patch 를 사용해서 small resolution image 에서만 잘 학습함 **->** image 를 적당히 큰 patch 로 잘라서 transformer encoder 에 넣어줌 : input length 에 quadratic 한 attention 연산량도 줄이고 mid-resolution image 에서도 잘 동작하게 됨

* 각 2d patch 를 1d 로 flatten 한 것을 linear projection 하여 input 으로 이용함. Linear projection layer 로 인해 Patch size 는 pretraining-fine tuning 두 경우 다 동일하게 설정.

* patch 들의 2d position 을 나타내기 위해 sequential 한 1d positional embedding 을 사용함(ablation study 에 따르면 2d positional embedding 이랑 성능 차이가 없음). Patch size 가 고정이라 resolution 이 바뀔 시 patch 개수도 바뀌게 되는데, 기존 positional embedding 과 actual 2d position 이 잘 대응하도록 기존 1d positional embedding 을 interpolate 하여 사용함.
* classification 을 위해 input patch 외에 extra learnable class embedding 을 추가해줌. (BERT 에서 사용된 방식과 유사) linear projection 을 거친 모든 patch 와 class embedding 은 position embedding과 결합되어 transformer 의 input 으로 들어가게 됨. transformer encoder 를 통과한 class embedding 은 다른 patch 들과의 relation 을 통해 image representation y 를 생성한다. 이 y 를 MLP classifier 를 통과시켜 최종 class prediction 을 얻는다.

**Experiment** :
* it is often beneficial to fine-tune at higher resolution than pre-training
* When pretrained on large scale dataset and transferred to tasks with fewer data points, ViT approaches or beats SOTA on multiple image recognition benchmarks. But on mid-sized datasets , convolution based SOTA model is much better => convolution based model 에 비해 적은 inductive bias 때문. small inductive bias를 커버할 정도로 충분히 많은 데이터가 요구됨
* data size 가 performance bottleneck 이 되지 않을 정도로 충분히 큰 데이터셋에 대해 ViT 가 ResNet 보다 performance/compute trade-off 가 좋았음 (2-4 배 정도)
* data size 가 적을 수록 large ViT model 의 성능은 떨어짐. 그 정도가 small ViT model 보다 심해서 small size data 에서는 small ViT 가 더 성능이 좋음 (report 된 가장 적은 size 의 dataset 이 ImageNet 임)
* input 으로 linear projected patch 대신 cnn feature 를 사용한 hybrid 모델이 기본 ViT 보다 small computation budget 에서 조금 더 좋은 성능을 냈으나, model size 를 키우면 둘 사이 차이가 거의 없어졌음

**총평** : model size , pretrain/ fine tuning dataset 에 따른 ablation study 가 매우 상세하게 잘 되어 있어서 흥미롭게 읽었음. 좋은 성능을 위해서는 생각보다 너무 large scale 인 데이터들을 필요로 한다는 느낌이 들었음
