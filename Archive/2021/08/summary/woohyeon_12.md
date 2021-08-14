# InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets
### Xi Chen et al., UC Berkely - NeurIPS 2016
### Summarized by Woohyeon Shim

**Task:** learning disentangled representation by mutual information maximization

**Related work:**
* vs. supervised approaches: trains a subset of the representation to match the supplied label.
* vs. weakly supervised models: given a pair of data that are known to match or using consecutive frames in videos.
* vs. unsupervised way: only one work, a higher-order extension of the spike-and-slab restricted Boltzmann machine => restricted to disentangle discrete latent factors and having exponential time complexity w.r.t # of factors.

**Background: Mutual Information**
* I(X; Y ) = **H(X) − H(X|Y ) = H(Y ) − H(Y |X)**
* I(X ; Y) is the **reduction of uncertainty in X when Y is observed.**
* **“amount of information”** learned **from** knowledge of random variable Y **about** the other random variable X.
* If X and Y are **independent**, then **I (X ; Y ) = 0**, because knowing one variable reveals nothing about the other. By contrast, if X and Y are related by a **deterministic**, **invertible** function, then **maximal mutual information** is attained.
	
**Method**
* **Decompose the input noise vector into two parts**
	* z: unstructured code as a source of noise
	* c: latent code that is linked with a salient attribute features (like angle and thickness of a digit's stroke); this is a concatenation of all latent variables c_i.
* **Information-theoretic regularization**
	* Need to avoid trivial solution: PG(x|c) = PG(x).
	* There should be high mutual information between latent codes c and generator distribution G(z, c). Thus I(c; G(z, c)) should be high.
	* There should not be lost of the information in the latent code c in the generation process. Thus entropy of PG(c|x) should be small.
	* Ideal objective: minG maxD V(D, G) = V(D, G) − λI(c; G(z, c))
* **Variational mutual information maximization**
	* direct maximization is hard; access to the posterior P(c|x) is limited.
	* compute lower bound by approximating P(c|x) with an auxiliary distribution Q(c|x); known as variational information maximization.
	* I(c; G(z, c)) = H(c) − H(c|G(z, c)) = Ex∼G(z,c) [**Ec′∼P(c|x) [logP(c′|x)]**]+H(c) = Ex∼G(z,c) [**DKL(P(·|x) ∥ Q(·|x)) + Ec′∼P(c|x)[logQ(c′|x)]**]+H(c) ≥ Ex∼G(z,c)[**Ec′∼P(c|x)[logQ(c′|x)]**]+H(c)
		* fixing the latent code distribution ⇒ treating H(c) as a constant.
		* lower bound becomes tight as the auxiliary distribution Q approaches the true posterior distribution: Ex[DKL(P(·|x) ∥ Q(·|x))] → 0.
* **Reparameterization trick**: Approximate Monte Carlo simulation
	* Lemma: For random variables X, Y and function f (x, y) under suitable regularity conditions: **Ex∼X,y∼Y|x [f(x, y)] = Ex∼X, y∼Y|x ,x′∼X|y [f(x′, y)].**
	* **LI(G,Q) = Ec∼P(c),x∼G(z,c)[log Q(c|x)] = Ex∼G(z,c)[Ec′∼P(c|x)[logQ(c′|x)]]**
	* **Final Objective:** minG,Q maxD V(D, G, Q) = V (D, G) − λLI (G, Q)
* **Implementation**
	* Q(c|x) is modeled with extra fully connected layer in D; only adds a negligible computation cost to GAN.
	* For categorical latent code ci, Q(ci|x) is obtained by softmax nonlinearity.
	* For continuous latent code cj, Q(cj|x) is treated as a factored Gaussian.
* **Observation**
	* LI (G, Q) always converges faster than normal GAN objectives; InfoGAN essentially comes for free with GAN.
	* hyperparameter λ is easy to tune, setting simply to 1 for discrete latent codes and make smaller for continuous variables to ensure that λLI (G, Q) is on the same scale as GAN objectives.
		
**Experiments**
	* **investigating mutual information** ⇒ the lower bound is quickly maximized to H(c), but remains the same without mutual information maximization.
	* **disentangling of latent codes on MNIST, Chair, SVHN and CelebA**
		* MNIST: control digit shape by discrete code and style by two continuous codes (Unif(-1, 1)).
		* Chair: control azimuth (pose), elevation, and lighting by five continuous codes (Unif(-1, 1)).
		* SVHN: make use of four 10-dimensional categorical variable and two uniform continuous variables, as the dataset is noisy, containing distracting digits and does not have multiple variations of the same object.
		* CelebA: use 10 uniform categorical variables, each of dimension 10. \
	⇒ + can continuously interpolate by varying a continuous code with the others fixed. \
	⇒ + show generalizability to unseen latent code. \
	⇒ + can discover salient variation on its own (hair style, presence / absence of eyeglasses, and emotions) \
	⇒ + competitive with representations learned by existing supervised method
		
**총평:** 문제와 해결 방식을 아주 매끄럽게 연결시키고 중간에 등장하는 개념도 쉽고 친절하게 설명한 논문. 결과도 인상적이고 분석도 잘 한 것 같아 다른 분들도 읽어보면 좋겠음. 핵심을 다시 정리하자면 unsupervised로 interpretable and disentangled representations을 배우기 위해 latent code와 G사이의 variational mutual information maximization 및 reparameterization trick을 도입한 논문!
