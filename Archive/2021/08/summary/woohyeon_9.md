# BIGRoC: Boosting Image Generation via a Robust Classifier
### Roy Ganz and Michael Elad, Technion - Submitted to ICLR 2022 (Probably Borderline paper)
### Summarized by Woohyeon Shim

**Task:** Improving the perceptual quality of the images by a robust classifier

**Motivation**
* Robust classifier has a property that exhibits "perceptually aligned gradients"	
* This means that a modification of an image to sharpen such a classifier’s decision yields visual features that are perceptually aligned with the target class.
* In this work they simply harness and utilize the above described phenomenon in image synthesis.
	
**Method**	
  * **A post-processing procedure via the guidance of a given robust classifier**
    * **Basic principle:** iterative update through Projected Gradient Descent (PGD) over the robust classifier.
    * **For conditional model:** update by maximizing the corresponding conditional probability.
    * **For unconditional model:** update by maximizing the probability of the most likely class predicted by the robust classifier.\
    **⇒⇒⇒ Model-agnostic method (both conditional or unconditional)**
		
  * **Issue: unbalanced label distribution for unconditional model**
    * **Solution1?** sampling debiasedly to attain close to uniform class estimation? → computationally heavy and not fair for quantitative comparison (requiring more samples to achieve a label-balance).
    * **Solution2:** calibrating logits to have more balanced class estimation? (shift classifier's logits to have the same mean logits value across all classes) → debiased logits can make unbiased class estimation!
	
  * **More application: Image interpolation given source and target images**
    * Extract multi-scale features
    * Add objectives in PGD that match source features to target features
    * Control the degree of interpolation by altering maximum perturbation values.
  
  * **Details**			
    * **choose l2 ball** as threat model since a change of ±e to every pixel l∞ ball with might not preserve the existing structure of the synthesized

**Experiments:** Image generation on CIFAR10 with a variety of image generators of different qualities, Image interpolation on ImageNet.

**총평:** 강점은 방법이 간단하고 model agnostic하고 additional training이 필요 없이 inference time에 적용할 수 있다는 점이지만, 단점으로 robust classifier에 전적으로 의존하며 기존 방법과 차별점이 거의 없고 어플리케이션만 달라진 것 같은 느낌을 줌. 그리고 generation 성능이 크게 향상되지 않으며 결과로 생성한 이미지는 작위적인 것 같음. large-scale 실험이 없는 것도 단점임.
