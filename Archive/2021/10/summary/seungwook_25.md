# Learning to resize images for computer vision tasks
## Hossein Talebi et al., Google Research - ICCV 2021
### Summarized by Seungwook Kim
---

**총평**:
* Bilinear/Bicubic 등의 기본적인 resize 방법보다 유의미한 성능 gain을 보이는 논문이었다. 향후에 image관련 모델을 사용할 때, engineering을 해도 괜찮은 상황이라면 적용해볼만 한 것으로 보인다.
* 엄청난 novelty를 제안하는 것은 아닌 것 같은데, 누구나 생각할 수 있는 방식으로 논문을 작성한 것이 인상깊음
* 앞으로 나도 아이디어가 있으면 바로바로 구현에 옮겨보고, novelty를 가늠해본 뒤 제출해보는 방향도 고려해봐야겠음

**Task**: Learnable resizing of images
* Replace traditional bi-linear or bi-cubic resizing


**Method**: CNN model to resize images
* Uses a bilinear feature resizer in-between
  * Allows arbitrary up/down scaling factors
* jointly trained with the baseline model loss
  * objective: learn the optimal resizer for the baseline vision task
  * do not apply any loss or regularization constraint on the resized image.

**Results**:
* Improved results on ResNet classification
* Improved results on Image Quality Assessment
