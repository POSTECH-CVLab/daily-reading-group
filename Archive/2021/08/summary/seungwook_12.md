# RobustNet: Improving Domain Generalization in Urban-Scene segmentation via Instance Selective Whitening
## Sungha Cho et al., LG AI Research, Kaist, Korea Univesity, Sogang University - CVPR 2021 Oral
#### Summarized by Seungwook Kim
---

**Task**: Domain Generalization, Semantic Segmentation

**Contribution/Novelties**: 
1. Disentangle domain-specific style and domain-invariant content
* encoded in higher statistics (covariance)
2. Selectively remove only the style information (which causes the domain shift)
* Using whitening transformation
    * removes feature correlation and makes each feature have unit variance
    * i.e. non-diagonal entries of feature covariance matrix -> 0
* Simply applying whitening transformation may eliminate domain-invariant content as well
    * proposes a selection method to remove ONLY the style information
* Instance-selective whitening loss
    * easy use in existing methods with negligible computational cost
3. SoTA over existing approaches in both qualitative / quantitative manner

**Method**:
1. Instance whitening loss
    * Whitening loss induces conflict between diagonals / non-diagonals of covariance
    * Use instance standardization --> now can only consider non-diagonal entries of the covariance matrix
    * removes feature correlation and makes each feature have unit variance
    * Since covariance matrix is symmetric, penalize just the upper triangle of the covariance matrix
2. Margin-based Relaxation of whitening loss
    * Instead of moving all non-diagonal entries to 0, make it have a certain amount of values
        * add amrgin to the Instance whitening loss
    * Gives room to keep discriminative features
    * Shows better performance
3. Separating Covariance elements
    * Whitening everything may suppress the domain-invariant content information as well
    * Add Photometric augmentations to image -> obtain pair of same image, with style difference
        * calculate the **variance of their covariance matrices**
        * regions of the variance matrice with high values --> attributes to style!
        * mask the regions with high variance values, and apply whitening loss to them only
    * End up with: domain-invariant feature learning

**Evaluation / Results**:
* Outperforms DG and DA methods
* Negligible computation cost
* Reconstruction from features after whitening shows that reconstructed images have **suppressed domain-dependent features** (illumination, blurring...) but maintains content


**총평**:
* Whitening이라는 이미 존재하는 기법과, 그에 대한 이미 알려진 문제점을 시작점으로 삼은 논문.
* Writing은 군더더기 없으며, Whitening 기법을 Domain Generalization에 적용할 수 있도록 방법론을 제시함.
* Covariance matrix를 통해 selective whitening을 하는 과정이 꽤나 깔끔하나, 나름 heuristic 한 부분들이 있는 것으로 보임.
* 깔끔한 문제정의와 해결을 통해 Domain Generalization에 whitening을 도입한 것을 높이 사서 oral로 accept된 것이라고 생각함.
