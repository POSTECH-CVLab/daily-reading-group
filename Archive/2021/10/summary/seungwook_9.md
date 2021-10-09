# Deep Iterative Frame Interpolation for Full-frame video stabilization
## Jinsoo Choi et al., KAIST - SIGGRAPH 2019
### Summarized by Seungwook Kim
---

**총평**:
* GSAI QE시험의 일환으로, 조성현 교수님께서 추천해주셔서 읽게 됨.
* Frame video interpolation이라는 일반인도 친숙한 주제와, interpolation이라는 직관적인 솔루션을 도입하여, 해당 야를 잘 모르는 사람이라도 입문하기 쉬운 논문으로 보인다.
* Writing이 전반적으로 깔끔하나, 몇가지 design choice에 대해 설명이 명확하지 않다고 느꼈다. 그런 경우 혼자 고민을 해본 뒤 결론을 내리게 되었다.
* Metric 몇가지가 misleading하다고 생각한다. 
  * ex) "Cropping ratio"라는 metric은, video stabilization하는 과정에서 missing-view boundary를 없애기 위해 crop한 영역이 적을수록 좋은 metric이다.
  * 하지만 당연히 missing-view boundary가 없도록 하면 성능이 최고로 나올 수 밖에 없는 metric이기도 하다.
  * 그런 경우에는 퀄리티가 안 좋을테니, rendering quality와 cropping ratio가 동시에 고려되는 metric을 사용하는 게 더 옳을 것이라고 생각함.

**Task**: Video stabilization
* Recovering shaken videos
* I understood the paper as "improving intermediate frames" instead of "creating entirely new intermediate frames through interpolation"
* The **First** unsupervised framework for video stabilization

**Method**: Unsupervised full-frame interpolation
* Train model to generate middle frame (f_i from f_i-1 and f_i+1)
  * The two adjacent frames are warped towards each other through **optical flow**
* The two 'warped' frames -> U-Net -> create intermediate frame (f_int)
* intermediate frame & f_i -> ResNet -> **stabilized, interpolated frame**

Loss: 
* L1 loss (pixel-wise color-based loss)
* Perceptual loss function (L2-norm of difference in feature representation)

Un-supervision & design choices:
* f_i is NOT guaranteed to be the halfway point between adjacent frames (f_i-1 and f_i+1)
  * cannot be used as supervision
  * Define pseudo-gt frame : **randomly translated version of f_i**
  * (My opinion) The randomness acts as a sort of "augmentation", where the model therefore learns to use adjacent frames + original frame to result in a "targeted" pseudo-gt frame.
* I still think there is a discrepancy between the training and testing mechanism.
  * Train-time: optical-flow warping is done towards the pseudo-GT. The network has higher priors on what the output should be.
  * Test-time: The adjacent frames are simply warped towards each other (half-way). This is a much weaker prior compared to train-time.
  * I think the latter ResNet should be the main, stronger learner in this case.

