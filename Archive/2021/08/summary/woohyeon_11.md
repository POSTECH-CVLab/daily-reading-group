# f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization
### Sebastian Nowozin et al., Microsoft Research - NeurIPS 2016
### Summarized by Woohyeon Shim

**Task:** deriving GAN objectives from f-divergence.

**Generative neural samplers?** is the same with generative model that takes a random vector and produces corresponding samples from a neural network.

**f-divergence?**
* Df(P||Q) = Int_X [q(x) f(p(x)/q(x)) dx]
* A difference between two given probability distributions P, Q w.r.t a base measure dx defined on the domain X.
* f: R+ → R is a convex, lower-semicontinuous function and satisfies f(1)=0.
	* ex) f(u) for KL: ulogu, Pearson: (u-1)^2, JS: -(u+1)log[(1+u)/2] + ulogu
		
**Variational estimation of f-divergences**
* **Variational representation of f** \
	f(u) = sup_{t \in dom_{f*}} tu - f*(t).
	* f* is a convex conjugate function of f, a.k.a Fenchel conjugate.
	* f* is dual form of f i.e., f** = f and again convex and lower-semicontinuous.
* **Variational lower bound of f-divergence** \ 
Df(P∥Q)= Int_X [q(x) sup_{t \in dom_{f*}} {t p(x)/q(x) −f*(t)} dx  (substituting variational form into Df(P|Q)) \
≥ sup_{T} [Int_X p(x)T(x)dx - int_X q(x)f*(T(x)) dx] \ 
= sup_{T} [Ex~P T(x) - Ex~Q f*(T(X))] \ 
	* T is an arbitrary class of function T: X → R.
	* This derivation is came from two reasons: (1) Jensen's inequality when swapping the integration and supremum operations, (2) the class of function T may contain only a subset of all possible functions.
* **The bound is tight when T(x) = f' (p(x) / q(x))**
	* f' denotes the first order derivative of f.
	* This condition works as a guide to choose f and design the class of function T; KL divergence corresponds to f(u) = -log(u) resulting in T*(x)=-q(x)/p(x).
		
**Variational Divergence Minimization**
* Generative adversarial learning finding saddle point (almost the same as original GAN objective) \
F(θ,ω) = Ex∼P [Tω(x)] − Ex∼Qθ [f∗(Tω(x))].
	* Qθ: generator, Tω: discriminator
* Reflect the domain of the conjugate function f* by replacing Tω(x) ⇒ gf(Vω(X)).
	* Vω: X → R; output logits.
	* gf: activation function specific to f-divergence.
* − Ex∼Qθ [f∗(gf(Vω(x)))] ⇒ +Ex∼Qθ [gf(Vω(x))] is more useful in practice as also noted in GAN paper.
		
**Experiments ⇒** found that divergence functions has strong influence on which model is learned.

**총평:** GAN의 새로운 목적식을 제안하기 보다는 이전에 제안된 방식을 하나로 통합한 논문. 저자는 GAN뿐 아니라 다른 generative model에 대해서도 다방면으로 꿰고 있는 것 같아 인상 깊었음 (from related work). 논문을 보며 현재 연구하는 분야를 대표하는 논문, 즉 generative model에서는 VAE, diffusion probabilistic model와 flow(invertible model) 정도는 알고 있어야 되지 않을까라고 생각함.
