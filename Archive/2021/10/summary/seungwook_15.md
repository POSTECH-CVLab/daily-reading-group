# A Closer look at Rotation-invariant Deep Point Cloud Analysis
## Feiran Li et al., Osaka University (Line Corporation) - ICCV 2021
### Summarized by Seungwook Kim
---

**총평**:
* Canonical 3D pose의 전반적인 연구 방향이 related work / ablation을 통해 아주 잘 정리되어있으며, 실험이 깔끔하다. Motivation이 명확한 동시에 아이디어는 간단해서 매우 재미있고 쉽게 읽혔다.
* 현재 진행중인 과제와 관련이 깊어서 아마 여러번 더 읽어볼 예정입니다. 3D point cloud관련 연구를 하고 계시다면 추천드립니다.
* 저자와 학회 중 이야기해보았는데, 메모리 이슈가 있어서 ModelNet데이터의 1000개가량의 포인트만을 바탕으로 실험해보았다고 합니다. 이를 어떻게 real-world scale의 point cloud로 scale할 수 있는지가 유의미한 연구 방향일 것 같습니다.

**Task**: Determining 3D point cloud canonical pose
* Main fundamental: Aligning point clouds boosts performance in works using 3D point clouds
* proves through classification / part segmentation etc

**Method / Experiments / Experiments**: 

Preliminary: PCA can be used to obtain canonical pose of point clouds
* However, this can introduce up to 24 ambiguities (4 X 6)
* Previous work has considered only up to 8
  * from which 4 were spurious considerations, actually harming the performance

Simple method of inputting all 24 possible point clouds, and outputting a single point cloud as a result through dynamic weighting
* prior to being input to target point cloud processing tasks (classification, segmentation...)
* Supervised using the end-task loss

Proves & shows through various ablations that:
* Using 24 considerations DO improve performance
  * not because more point clouds are considered, as they are theoretically sound
* Aligning point clouds DO results in performance boosts
* aligning point clouds are showing BETTER RESULTS than rotation-robust or rotation-invariant descriptors
  * mostly because "robust" is not invariant
  * and "invariance" means loss of expressibility.

