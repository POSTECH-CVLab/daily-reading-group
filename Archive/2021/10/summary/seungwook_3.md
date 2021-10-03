# Semantic Correspondence with Transformers
## Seokju Cho et al., Yonsei U - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**총평**:
* 현재 연구주제와 같은 transformer를 이용한 matching주제이지만, formulation이 많이 달라서 참고용으로 읽게 되었습니다.
* vanilla transformer의 원형을 그대로 사용하며, 메모리 문제로 4D 인풋에 대한 attention을 2D-2D로 따로 진행합니다. (메모리 문제)
* 또한 attention의 input으로 correlation tensor만 주는 것이 아닌, 각 source/target feature를 correlation tensor와 함께 input으로 사용합니다.
* 따라서 channel dim이 많이 커지기때문에, 메모리 문제로 transformer layer를 하나밖에 쌓지 못합니다.
* 기존에 semantic matching에서 사용하지 않았던 augmentation을 처음 적용했습니다. Augmentation을 하고 나서야 augmentation이 없는 기존 baseline들을 outperform하여 부족하다고 생각했지만, 아이디어의 참신성을 바탕으로 뉴립스에 합격했다고 생각합니다.

**Task**: Semantic correspondence

**Motivation**:
* Transformers are more well-suited with augmentation
* Global context of transformers
* Dynamic weights of attentions

Above characteristics motivate the use of transformers instead of convolutions.

**Method**
* Input: B N HWHW correlation tensor
    * from N different layers
* Attention input: B N (HW) (HW + C)
    * 4D HWHW sequence is too memory-consuming: not feasible
    * Separates to 2 (HW)(HW) sequences, considering the ordering (permutation)
    * Sequence: (HW)(HW), source/target feature: (HW)(C)
        * Concat the above 2 to obtain (HW)(HW + C) as attention input
        * HW + C is the channel dimension
* Uses augmentations: Random crops and stylizations

**Results**
* Prior to augmentation: worse performance than previous baseline
* with augmentation: Outperform SoTA on SPair-71K
    * Not on PF-Pascal dataset, but PF-Pascal is saturated (not a big negative factor)
* With/without augmentation
    * Larger improvement compared to conv-based models
        * proposes that transformers are more suitable for augmentations
    * but CHM shows equally high improvements with augmentation, outperforms this paper when using augmentations.
