# Neural Discrete Representation Learning (VQ-VAE)
### Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu - NIPS 2017
#### Summarized by Jiye Kim

---

### **Task** : 
Generative models



### **Main Idea** : 
-  VAE는 일반적으로 latent space를 continuous한 gaussian distribution으로 모델링하는데, 이 논문에서는 vector quantization (VQ)방법을 사용해서 categorical distribution으로 latent space를 모델링했다는 점이 차이점이다.

### **Motivation** :
- 기존 VAE 구조에는 posterior collapse 문제가 흔하게 일어나는데, 이 문제는 VAE의 encoder가 주는 z에 대한 정보가 너무 약하거나(모든 인풋에 대해 비슷한 z만 내보냄) noisy해서 (latent vector z가 unstable함) decoder가 latent vector를 무시하고 생성을 해버리는 문제이다. 특히 VAE구조에 powerful decoder (e.g. pixelCNN decoder)같은걸 붙였을 때 더 많이 발생한다고 한다. (모델이 decoder의 성능만으로 생성해버림.) 이 논문은 latent를 discrete 하게 모델링 함으로서 이와 같은 variance issue를 해결할 수 있고 powerful decoder를 붙였을 때도 잘 동작한다고 한다. 또한 일반적으로 discrete한 정보를 가지고 생성을 해야할 때가 많은데 (e.g. class conditions are discrete) 이것을 가능하게 할 수 있다.


### **Method** :  
VAE는 크게 encoder, prior, decoder 부분으로 구성되어있다. posterior는 k-categorical distribution으로 모델링된다.

1. input x 가 encoder를 통과하여 K*D dimensional vector z가 나온다.
2. 이 z와 k개의 embedding dictionary e1, ..., ek와의 거리를 계산하고 가장 가까운 embedding과의 확률을 1, 나머지는 0으로 내보낸다. (one-hot)
3. 이렇게 뽑힌 embedding dictionary ei을 decoder의 인풋으로 넣어준다.


### **Learning** : 
- 학습 파라미터는 encoder, decoder, embedding dictionary이렇게 된다. (embedding dictionary도 학습됨)

- 위의 방법에서 argmin을 취하여 one-hot vector로 만들어 인풋으로 집어넣는 부분이 differentiable 하지 않기 때문에, 그냥 decoder input에 대한 gradient를 encoder output에 바로 넘겨주는 copy gradient 방법을 사용한다.



- loss는 3개의 term으로 구성되는데,

1) reconstruction loss (encoder, decoder가 학습됨.),
2) embedding dictionary에도 gradient를 주어야하기 때문에 encoder의 output과 비슷하도록 embedding dictionary에 gradient를 줌,
3) encoder output에 대한 constraint를 주지 않으면 임의로 커질 수 있기 때문에 (그리고 그것에 맞춰서 embedding dictionary가 충분히 빨리 학습이 안될 수 있음.) encoder output에 대한 constraint도 줌.
- ELBO loss에 들어가있는 KL term은 uniform prior 가정을 했을 때 constant가 나오기 때문에 생략한다.


### **Experiment** :
- image, sound, video generation 에 실험을 진행함.
- long range sequence를 modelling할 수 있음
- likelihood가 continuous VAE와 competitive함.

### **총평**:
- vae구조에서 처음으로 discrete latent variable을 모델링하려고 시도했다는 점에서 contribution이 큰 것 같다. 방법론도 간단하고 motivation과도 잘 연결한 것 같다.
