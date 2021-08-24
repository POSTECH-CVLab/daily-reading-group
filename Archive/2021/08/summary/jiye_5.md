# Augmenting Genetic algorithms with deep neural networks for exploring the chemical space
### AkshatKumar Nigam, Pascal Friederich, Mario Krenn, Alán Aspuru-Guzik - ICLR 2020
#### Summarized by Jiye Kim

---

**Task** : Molecule generation



**Main Idea** : 
- genetic algorithm을 사용하여 molecule generation을 수행한 방법. 생성된 molecules의 diversity를 높이기 위해서 neural network based adaptive penalty(discriminator)를 적용하고, robustness 를 위한 SELFIES molecule representation을 사용한 것이 특징이다.

 
**Motivation** : 

- 기존 VAE, GAN, RL 기반 molecule generation method들은 reference dataset distribution을 따라하도록 학습된 모델이기 때문에 vast chemical space를 explore하지 못한다. 본 논문은 genetic algorithm을 사용하여 exploration ability를 높였다.
 

**Method** :

1) Overview

Generator: genetic algorithm으로 m개의 molecules (initialized with simple methane molecules)로 시작하여, random mutation and crossover를 통해 새로운 molecule을 만든다. 생성된 molecules는 fitness라는 score를 통해 평가되고 (높을수록 좋음) 높은 fitness를 가진 molecule일수록 다음 generation과정까지 살아남게 된다.

F(m) = J(m) + beta * D(m)

Fitness는 위와 같이 정의되고, J(m)은 optimize 시키고 싶은 molecular property (ex. logp, SA score), D(m)은 discriminator의 output이다(생성된 molecule은 discriminator를 통해 real molecules과 비교되어 0~1 값을 내보냄).

 
2) Mutation and crossover

cross-over rule은 사용하지 않는다.

mutation의 경우 robustness of SELFIES 특징을 이용하여, SELFIES character를 replacement, insertion을 통해 변형시킨다. domain-specific rule은 하나 사용하는데, 4%의 확률로 phenyl group을 추가한다.

 
3) Role of the discriminator

Discriminator의 역할은 너무 길게 살아남는 molecule을 없애주는 것이다. 예를들어, generator가 local optima에 빠졌다고 할 때, local optima에서 생성된 molecule은 subsequent generation까지 계속 살아남을 것이다. 이들을 제거해주기 위해서, discriminator를 도입하는데 discriminator는 이렇게 오래 살아남는 fake molecule을 더 오래보기 때문에 (여러번 학습됨) 0에 가까운 값을 내보낼 것이고 위의 fitness score도 따라서 낮아진다.




**Experiment**:

- penalized logP socre를 기준으로 molecule generation을 했을 때 SOTA를 기록했다.
	
	
	
- adaptive penalty (discriminator)의 도입으로 더 넓은 chemical space를 보는 것을 확인하고, 덕분에 더 optimized 된 property를 갖는 molecule이 생성되는 것을 확인했다.
	
	
	
- 생성이 진행될 수록 여러 classes의 molecules이 생성되는 것을 확인했다. 생성된 molecules를 K-means clustering을 하고 각 class 마다 logp 수치를 계산한 후, 가장 높은 logp 수치를 내는 class의 representative examples(cluster center와 가장 가까운 것)을 뽑아보았다. Representative examples이 주로 aromatic rings, conjugated carbon chains, linear sulfur chains를 가지고 있는 것을 확인했고 이런 design rules를 이용해 molecule을 생성해본 결과 위의 GA 방법보다 훨씬 높은 logp score를 가진 것을 확인했다.
	
	
	
- F(m) 을 다른 form으로 바꿔서 여러 다른 task에 적용할 수 있다.
	
	
	
- logP와 QED를 동시에 optimize 시켜보았다. ZINC, GuacaMol dataset을 보면 동시에 optimize되는 것이 불가능하다는 것이 보였지만, GA방법을 통해 생성된 molecules은 그 boundary부분에서 생성하는 것을 확인했다.

 

**총평**:
- 방법론이 새롭고 간단해서 좋았다. 여러가지 흥미로운 실험들을 많았다.

- molecule generation에 한정되지 않고 다른 분야의 optimization에서도 사용될 수 있다고 한다.

- F(m) form을 여러가지로 쉽게 바꿀 수 있어서 좋은 것 같다.
