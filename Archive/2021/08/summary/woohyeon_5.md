# Twin Auxiliary Classifier GAN
### Minming Gong et al., University of Pittsburgh - NeurIPS 2019 (Spotlight)
### Summarized by Woohyeon Shim

**Task**: address the source of the low diversity issue of ACGAN
	
**ACGAN?** \
⇒ has 3 main objectives: marginal matching with JSD between Q_x and P_x (P: real data distribution, Q: fake data distribution), conditional matching (CE loss on real data, CE loss on fake data). \
⇒ CE loss on real data is equivalent to KL divergence between P_Y|X and Q^c_Y|X, where Q^c_Y|X is the conditional distribution induced by auxiliary classifier. This relation can be shown by adding the negative conditional entropy -H_p(Y|X), which is a constant term over training. \
⇒ In like manner, CE loss on fake data should reduce for conditional matching the KL divergence between Q_Y|X and Q^c_Y|X, where Q_Y|X is the conditional distribution specified by the generator G.
	
	
**Problem of ACGAN?** \
⇒ But - H_Q(Y|X) is not a constant term during training and this should not be ignored in the objective function! \
⇒ The authors shows the the optimal generator of ACGAN can deterministically relate the samples from the label and reduce the distributional support of each class (low diversity) even when the marginal distributions are perfectly matched by GAN loss. For this reason, ACGAN is disadvantageous when the supports of the class distributions have significant overlap.
		
**Solution: introduce additional auxiliary classifier for -H_Q(Y|X) estimation.** \
⇒ Proposition: minimizing -H_Q(Y|X) is equivalent to minimizing (1) mutual information between label and sample distribution, (2) the JSD between the conditional distributions {Q_X|Y=1, ... Q_X|Y=K} \
⇒ The authors minimize the JSD between multiple distributions by another minimax adversarial game. This works with additional auxiliary classifier which predicts the probability of X belong to a class Y=k. As a result, the additional objectives are: min_G max_C2 [log C2(G(z,y), y)]
	
	
**Experiments** \
⇒ Target distribution: 1D and 2D MoG, overlapping MNIST, CIFAR100, VGGFace2, ImageNet \
⇒ AC-GAN shows perfect separability leading to low-intra diversity and degenerate solution, especially where the class distributions have significant overlaps. ACGAN requires a very small weight on CE loss to succeed training. \
⇒ Projection cGAN fails to replicate the real distribution of MoG when using hinge loss, thus fragile to other than the standard setting, but hinge loss is more preferred for real data in practice.
	
	
총평: ACGAN의 문제와 해결 방법을 수학적으로 간단명료하게 보여주고 그것을 작은 실험 셋에서 검증한 것이 아주 흥미로웠던 논문. 최종 성능은 크게 인상적이진 않아서 처음엔 가볍게 넘겨 보았지만, 다시 살펴보니 분석과 가설을 검증하는 방식에서는 아주 배울점이 많은 논문인 것 같음. 한가지 의문은 JSD between the conditional distributions {Q_X|Y=1, ... Q_X|Y=K} 이것이 물리적으로 어떤 의미를 가지는 가인데, 탐구해보면 좋을 것 같음.
