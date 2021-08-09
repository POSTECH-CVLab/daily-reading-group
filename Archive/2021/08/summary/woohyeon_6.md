# ACE: Ally Complementary Experts for Solving Long-Tailed Recognition in One-Shot
### Jiarui Cai et al., University of Washington - ICCV 2021 (Oral)
### Summarized by Woohyeon Shim

**Task:** one-stage long-tailed recognition
	
**Related Work**

* **One-stage approach** \
⇒ strong data augmentation can compensate the insufficiency of data and improve the model's generalizability (MixUp, ReMix) \
⇒ re-sampling (under-sampling of the head classes, over-sampling of the tail classes) and re-weighting (adjust loss function by the frequency or importance of the samples) scheme for re-balancing training set. \
** both exhibit "seasaw" phenomenon: the promotion of tails accuracy sacrifice the majority classes' accuracy or vice versa; the contradiction between representation learning and classifier learning, i.e., instanced-based (bias) sampling learns the most generalizable representations while the unbiased classifier is less likely to overfit the re-sampled set.
		
		
* **Two-stage & Multi-stage approach** \
⇒ pre-training with whole imbalanced set, then fine-tuning on balanced set by re-sampling or building diverse experts for various tasks in cascading stages. Also transfer learning in either image domain (major-to-minor translation [11]) and in feature domain (OLTR [15]) are proved useful. \
** sensitive to hyper-parameters and hard to find a sweet spot. \
** redundant and less practical are multi-stage models to be integrated with other tasks simultaneously, e.g., detection [22] and segmentation [29].
		
* **Ally complementary experts (ACE)**
  * **Distribution-aware Planner**
	* Manually distributes overlapping category splits for each expert, including target categories (TC) and interfering categories (IC).
	* Training for TC simply proceeds with CE loss, but for IC the logit is suppressed by l2 norm to learn the experts without being disturbed by the classes they have never seen.

  * **Distribution-adaptive optimizer**
	* Controls the update of each expert according to the volume of its training set and avoid over-fitting. Following linear scaling rule, scale the learning rate by k when the minibatch size is multiplied by k. (All the other hyper-parameters [weight decay, momentum, etc.] are kept unchanged.)
	* The loss of E(xpert)1 updates the backbone and parameters of E1 and L_i of i > 1 only updates the expert itself. The reason is the backbone could be corrected multiple times due to the same error. Here, the number of samples is assumed in descending order (the majority of samples are assigned to E1).
		
* **Experiments**
  * This work is the first one that improves performance on all the three frequency groups (many-shot, medium-shot and few-shot)
	* The suppression of the logits for IC is the principal reason for accuracy booms. But the manual distribution of samples was disappointing.
	
**총평:** 시작이 거창하고 결과도 유의미하며 전반적으로 글이 아주 잘 써져있었으나 접근 방법과 분석이 아쉬운 논문. 사실 방법이 너무나 단순하여 분석하는게 쉽진 않아보임. 그래서 언뜻 보기엔 발전 가능성이 많아 보이는 분야 같기도 함. Oral로 합격된 것은 최종 성능이 많이 높아진 것과 다른 방법들의 상세한 서술과 성능을 비교한 것에 있지 않을까 싶은데 관련 웍을 한다면 꼭 읽어보아야 하는 논문인 것 같음.
