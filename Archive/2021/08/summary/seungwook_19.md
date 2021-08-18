# PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space
### Charles R. Qi et al., Standord University - NeurIPS 2017
#### Summarized by Seungwook Kim
---

**Task**: Learning on Point Clouds (Point sets)

**Main Idea**: 
* PointNet, the SoTA pointset processing network at the time
    * **does not capture local structure**
    * but local structure has proven to be important in CNNs

**Main Novelty**: Proposes PointNet++
* Recursive application of POintNet recursively on a nested paritioning on the input set
* leverages neighborhood at multiple scales to achieve both robustness and detail capture
  * lower scale: detail capture
  * larger scale: robustness, in case where lower scale has not much detail to capture

**Method**:
1. Hierarchical Point Set Feature Learning
   * Sample centroids using **Farthest Point Sampling algorithm**
   * Use ball query to group points w.r.t centroids 
   * Perform PointNet on each group to output sampled point & learned features
2. Robust Feature learning under Non-uniform sampling density
   * Point sets may come with non-uniformity
     * learned on dense data only - may not generalize to sparsely sampled regions
     * learend on sparse samples - may not recognize fine-grained local structures
   * 3 Design choices:
     * Single-scale grouping: Naive grouping
     * Multi-scale grouping: Group same region using multi scales (varying values of K) and concat
        * computationally expensive
     * Multi-resolution grouping: Group same region N times (decreasing number of points every time) and concat
       * more compuntationally efficient!
   * Additional training strategy:
     * Randomly drop out input points with randomized probability for instance.
     * present the network with training sets of various sparsity and varying uniformity
3. Point Feature Propagation for Set segmentation
4. Point Feature propagation for set segmentation
   * For segmentation, need point-wise results!
   * However, group-wise PointNet decreases the number of points
     * propagate features from the decreased points to the original points
     * Interpolatie feature values w.r.t k nearest neighbors (inverse distance weighted)

**Evaluation & Results**
* SoTA on 2D/3D object classification
* SoTA on point set segmentation

**총평:**
* Writing이 아주 읽기 편하게 되어있으며, PointNet에 대한 소개도 포함되어있어 PointNet을 읽어보지 않고도 편하게 읽을 수 있는 논문입니다.
* Motivation이 clear하며, Motivation을 해결하기 위해 소개된 방법론들이 크게 heuristic/억지스럽다고 느껴지지 않으며, 깔끔하면서도 성능도 좋아 보입니다.
* Neurips2017논문인만큼 이후 성능을 더 끌어올린 논문이 많이 나왔겠지만, 여전히 매우 유명한 baseline/point set encoder 중 하나입니다.
