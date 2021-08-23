# Variational Inference with Normalizing flows
### Danilo Jimenez Rezende, Shakir Mohamed. Google DeepMind. - ICML 2015 
#### Summarized by Jiye Kim

---

**Task** : Generative model

**Main Idea** : variational inference에 normalizing flow를 적용하여 posterior distribution을 arbitrary complexity까지 만들 수 있게 한 방법.
 

**Motivation** : Variational inference를 수행할 때 posterior distribution이 intractable하기 때문에 일반적으로 mean-field approximation이나 simple distribution(ex. standard normal)으로 가정하고 수행한다. 하지만 richer posterior approximation이 성능 향상에 도움이 된다는 점이 이전 논문들에서 보여졌었고, approximated posterior distribution는 true posterior를 완벽하게 근사할 수 없다는 것이 문제이다. 따라서, normalizing flow를 사용하여 posterior distribution을 arbitrary complex distribution까지 modeling할 수 있게 함으로서 true posterior distribution을 더 잘 근사하게 한다.

 
 

**Method** :


Normalizing flow는 simple initial distribution(ex. standard normal)이 invertible transformation을 순차적으로 거치면서 arbitrary complex distribution이 되는 방법이다. 이 논문은 VAE에 normalizing flow를 합친 방법을 제안한다 (vae + normalizing flow). 방법은 단순한데 기존 VAE의 encoder가 gaussian의 parameter (mean과 variance)를 뽑아내고 latent vector z를 sampling하는데, 이 z를 바로 decoder에서 쓰는게 아니라 z를 K layers의 normalizing flow를 통과하는 과정이 추가된다. 이렇게 하면 z가 더 complex distribution에서 sampling 된 vector가 된다.
	
Normalizing flow에서 사용되는 transformation은 invertible해야하고, likelihood objective를 계산할 때 transformation의 Jacobian의 determinant를 계산하는 과정이 필요하다. 일반적으로 Jacobian의 determinant를 계산하는 과정은 O(D^3) (D: dim of hidden layers)의 complexity가 드는데, transformation을 잘 디자인하면 linear-time complexity O(D)까지 만들 수 있다. 본 논문에서는 Planer flow와 radial flow를 사용했다. 따라서, 기존 VAE inference과정에서 only linear time complexity만 추가한다고 한다.
	
Normalizing flow의 transformation을 어떻게 design하느냐에 따라서, 여러 rich posterior distribution을 capture할 수 있다. 논문에서 Infinitesimal flow라는 개념으로 Langevin flow와 Hamiltonian Flow를 짧게 설명하는데 이 부분은 잘 이해를 못했다.



**Experiment**:

여러 multi-modal, periodic (한마디로 complex한) distribution을 잘 capture하는 것을 확인했다.
	
Flow length가 길어질 수록 approximation quality가 올라가는 것을 확인했다.
	
본 논문에서 사용한 일반적인 normalizing flow 방법이 이전의 volume-preserving approach인 NICE보다 더 좋은 성능을 내는 것을 확인했다.
 


 

**총평**:

Normalizing flow를 사용하는 하나의 예시를 제안한 논문.
	
방법이 직관적이고 간단하다.
	
Posterior를 정확하게 근사하는게 중요하다는 것을 이전 논문과 이론을 통해 보였지만, 아직 직관적으로 이해가 잘 안되는데 더 공부를 해봐야겠다..
