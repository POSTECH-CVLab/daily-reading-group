# NICE: Non-linear Independent Components Estimation
### Laurent Dinh et al., Universite de Montreal - ICLR 2015 Workshop
### Summarized by Woohyeon Shim

	
**총평:** Independent Component Analysis(ICA)에서 도입되었던 change of variable formula로 high-dimensional density를 sampling 기법 없이 tractable하게 모델링할 수 있는 방법을 제안한 논문. 논의의 핵심은 Jacobian determinant를 구하기 쉽도록 triangular하게 만드는 것에 있었는데 본 논문은 additive coupling layer의 방식으로 unit determinant를 갖게함. 추가로 논문에서 제안한 방법을 VAE와 상세하게 비교를 하는데 재미있게 보려면 VAE를 읽고 보는걸 추천.
	
**Task:** learning complex high-dimensional densities with a factorized distribution
	
**Unsupervised learning?**
* capturing data distributions with the most important factor of variation.
* learning a good representation in which the data distribution is easy to model.

**NICE:** learning a bijective transformation h=f(x) of the data into a new space such that the resulting distribution factorizes, i.e., the components h_d are independent.
* pH(h) =Prod_d pHd (hd). <== each component is modeled as gaussian or logistic.
* pX(x) = pH(f(x)) | det ∂f(x) / ∂x | <== change of variable rule
* learning a transformation f via maximum likelihood.
	* the trivial solution is to increase likelihood arbitrarily simply by contracting the data.
	* but, the determinant of the Jacobian matrix of the transform f penalizes contraction and encourages expansion in regions of high density (i.e., at the data points).
	* also, using the factorized structure of the prior pHd encourages the model to discover meaningful structures in the dataset.
* If we use a layered or composed transformation f = fL ◦ . . . ◦ f2 ◦ f1,
	* the forward (f, encoder) and backward computations (f-1, decoder) are the composition of its layers’ computations.
	* Jacobian determinant is the product of its layers’ Jacobian determinants.
		
**Key properties of the transformation f**
* "easy determinant of the Jacobian"; triangular structure
* "easy inverse"; allows us to sample from pX(x) easily: h~pH(x), x=f^-1(h)
* "expressive to learn complex transformtion"
	
**Suitable function: neural network with triangular weight matrices**
* determinant is simply the product of their diagonal elements.
* inverting triangular matrices at test time is reasonable in terms of computation.
* many square matrices M can also be expressed as a product M = LU of upper and lower triangular matrices.
	
**Final building block of f: Coupling layer with triangular Jacobian**
* Triangular matrices & bijective function is highly constrained, so we can consider as an alternative a family of functions with triangular Jacobian.
* **Additive coupling layer:** split x into two dim (d, D-d) ⇒ coupling these with (coupling) function m defined on R^d
	* transformation: (x1, x2) → (y1, y2) = (x1, x2 + m(x1))
		* m is arbitrarily complex function (a ReLU MLP in this paper, with d input units and D − d output units.)
		* this building block has a unit Jacobian determinant for any m and is trivially invertible: (y1, y2) → (y1, y2 - m(x1)) = (x1, x2)
	* coupling law g(a, b) = a+b ⇒ g(x2; m(x1)) = x2 + m(x1)
	* could also choose other types of coupling, such as a mutiplicative coupling law g(a;b) = a⊙b, b ̸= 0 or an affine coupling law g (a;b) = a⊙b1+b2, b1 ̸= 0, but chose additive coupling layer for numerical stability.
* Since a coupling layer leaves part of its input unchanged, we need to exchange the role of the two subsets in the partition in alternating layers, so that the composition of two coupling layers modifies every dimension. ⇒ we observe that at least three coupling layers are necessary to allow all dimensions to influence one another.
	
**Rescaling the diagonal**
* introduce a diagonal scaling matrix S at the top layer since additive coupling layers and their composition have a unit Jacobian determinant.
* the larger Sii is, the less important the dimension i is. The prior term encourages Sii to be small (contraction), while the determinant term log Sii prevents Sii from ever reaching 0.
* NICE criterion has the following form: log(pX (x)) = Sum i=1~D [log(pHi (fi(x))) + log(|Sii|)].
	
**Related Work**
* vs deep boltzmann machine (DBM): undirected graphical model, log-likelihood is intractable, need MCMC sampling, slowly mixing when the target distribution has sharp mode.
* vs. VAE: directed graphical model, variational lower bound on the log-likelihood of data, might be sub-optimal, might inject a significant amount of unstructured noise in the generation process.
* vs. autoregressive model: NADE use strictly triangular adjacency matrix for tractability, but unparallelizable and not applicable on high-dimensional data.
* NICE: very similar to VAE, can be seen as perfect auto-encoder pair, this leaves KL divergence term of the variational criterion, log(pH(f(x))) can be seen as the prior term, which forces the code h = f(x) to be likely with respect to the prior distribution, and log(|det ∂f(x)/∂x|) can be seen as the entropy term. This entropy term reflects the local volume expansion around the data.
