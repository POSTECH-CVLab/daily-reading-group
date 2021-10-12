# NeRF: Representing Scenes as Nueral Radiance FIelds for View Synthesis
## Ben Mildenhall et al., UC Berkely, Google Research - ECCV 2020
### Summarized by Seungwook Kim
---

**총평**:
* 지능형모바일시스템 프로젝트 주제와 관련하여 읽게 됨.
* 하나의 Scene을 하나의 MLP를 통해 전부 rendering할 수 있는 구조로 만들었다는 점이 main contribution이다.
* Discrete sampling이 가진 time&space complexity 를 continuous representation (MLP)로 바꿔서 lower storage cost  / higher rendering quality를 얻음.
* 기존의 view synthesis 방법과 아예 다른 방향이지만, 성능이 매우 좋으며, extension이 아주 다양하게 가능한 방법으로서 왜 많은 사람들이 NeRF를 발전시키고자 하는 연구에 뛰어들기 시작했는지 이해할 수 있었다. 
* 또한 간단한 방법인만큼, NeRF를 연구에 적용하고자 하는 움직임 (GAN, dataset)도 많이 보인다. 

**Task**: Novel view synthesis

**Method**: 
1. Neural Radiance Field Scene representation: **A 5D input 9-layer MLP per scene**
  * 3D position (x y z) and 2D viewing direction as input
  * outputs colour (r g b) and volume density (transparency?)
    * Density is only relevant to space, colour may change according to viewing direction
    * Therefore only use position as the input first to calculate volume density (8 layers)
    * Then additionally input viewing direction to calculate RGB colour (+ 1 layer)
2. Volume rendering with Radiance fields: A classic, differentiable volume rendering method
  * Not a new novelty of this paper
3. Optimizing Neural Radiance Fields for quality & efficiency
  * **Positional encoding**: map the 5D input coordinate to higher dimensional space using high frequency functions to facilitate learning
  * Hierarchical volume sampling
    * Coarse sample points along a ray
    * Depending on the result of coarse sampling, fine sample on the important regions (not empty spaces)
    * Efficient & Effective

**Loss**: Total squared error between rendered and true pixel colors for both coarse and fine renderings
  * Given N images, use a subset for validation
  * Use remaining images for training
  * Given this method: If number of images are limited, wouldn't this overfit and result in poor novel view synthesis?
    * Addressed by paper PixelNeRF (single image)
