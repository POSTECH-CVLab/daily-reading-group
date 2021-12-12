# Data Augmentation Can Improve Robustness
## Rebuffi et al., DeepMind - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* Very well-written, well-motivated (dichotomy in previous studies), and well-experimented
* Lacks technical novelty in comparison
* The reviews are also very informative - could learn many aspects of 1. what aspects of writing can cause confusion 2. how to strengthen a paper.

**Task**: Mitigating robust overfitting

**Motivation**:
* Existing methods either consider data augmentation as useful / not useful
    * aims to clarify whether they are / are not useful
* weight averaging is effective for training, but is effective against robust overfitting ONLY WHEN the original model is resilient against robust overfitting
    * Shows that certain data augmentations mitigates robust overfitting & improves performance
    * and thus the combination of certain data augmentation + weight averaging yields SoTA results

**Dataset**: ImageNet

**Method**:
* All are experimental evaluation of hypotheses provided in the paper
* Finds out that CutMix/CutOut augmentations mitigates robust overfitting unlike MixUp/Other augmentations (RandAug, AutoAug)
    * "A possible explanation is that low-level features tend to be destroyed by MixUp, whereas composition techniques locally maintain these low-level features."
* Confirms that CutMix + WA yields the best results against all adversarial examples when included in the train set.
