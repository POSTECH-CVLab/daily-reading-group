# Auto-Encoding Variational Bayes
### Diederik P. Kingma and Max Welling, Universiteit van Amsterdam - ICLR 2014
### Summarized by Woohyeon Shim

**Task:** approximate marginal likelihood of x / approximate posterior of the latent variable z given an observed value x / joint optimization using standard stochastic ascent.

**Problem setting**
* prior: p(z), likelihood: p(x|z), posterior: p(z|x)
* marginal likelihood p(x) is intractable where the true posterior p(z|x) = p(x|z)p(z) / p(x) is intractable (i.e., we cannot evaluate or differentiate it).
	
**Approximate marginal likelihood**
* log pθ(x(1), · · · , x(N)) = Sum1~N log pθ(x(i)) s.t. θ: param. of dec.
* log pθ(x(i)) = DKL(qφ(z|x(i)) || pθ(z|x(i))) + L(θ, φ; x(i)) s.t. φ: param. of enc.
* log pθ(x(i)) ≥ L(θ, φ; x(i)) = Eqφ(z|x) [− log qφ(z|x) + log pθ(x, z)] \
= −DKL(qφ(z|x) || pθ(z)) + Eqφ(z|x(i)) log pθ(x|z) **← variational lower-bound** 
	* The KL-divergence DKL(qφ(z|x(i))||pθ(z)) can be integrated analytically.
	* The KL-divergence term can be interpreted as regularizing φ, encouraging the approximate posterior to be close to the prior pθ(z).
	* The second term Eqφ(z|x(i)) logpθ(x(i)|z) is an expected negative reconstruction error.
		
**Approximate posterior = recognition model (encoder) q(z|x)**
* Reparameterize the random variable z ∼ qφ (z|x)
	* Let z be a continuous random variable, and z ∼ qφ(z|x) be some conditional distribution.
	* It is then often **possible** to express the random variable z as a **deterministic variable z = gφ(ε,x)**, where ε is an auxiliary variable with independent marginal p(ε), and gφ(.) is some vector-valued function parameterized by φ.
	* For instance, let z ∼ p(z|x) = N(μ,σ2). Then a valid reparameterization is z = μ + σε.
* **This reparameterization** is useful for our case since it makes the Monte Carlo estimate of the expectation **is differentiable w.r.t. φ.**
* **The function gφ(.)** is chosen such that it maps a datapoint x(i) and a random noise vector ε(l) to a sample from **the approximate posterior for that datapoint**: z(i,l) = gφ(ε(l), x(i)) where z(i,l) ∼ qφ(z|x(i)).
	
**Joint optimization of the lower bound L(θ,φ;x(i)) w.r.t. both the variational parameters φ and generative parameters θ**

**Related Work**
* vs. stacked denoising autoencoder: unregularized auto encoder which maximize a lower bound of the mutual information between input X and latent representation Z. this is equivalent to maximizing the conditional entropy, which is lower bounded by the expected log likelihood of the data under auto encoding model, i.e. the negative reconstruction error. but, it is well-known that this reconstruction criterion is not sufficient for learning useful representation.
* vs. generative stochastic net and deep boltzmann machine; also targeted at either unnormalized models (i.e. undirected models)

**Experiments:** superfluous latent variables did not result in overfitting, which is explained by the regularizing nature of the variational bound.

**총평:** data의 marginal likelihood가 prior p(z)과 posterior p(z|x)의 KL divergence + reconstruction error p(x|z)로 optimize될 수 있음을 수학적으로 보여주고 AE와 연결시켜 VAE를 제안한 논문. 논문을 보면 정택이형이 종종 말씀하시는 것과 같이 generative model은 원래 목적은 "generation 그 자체가 아닌 p(x)를 잘 표현하는 latent vector(representation)를 찾는 것에 있음"을 알 수 있음. 여유가 될 때 한번쯤 읽어보면 좋은 논문.
