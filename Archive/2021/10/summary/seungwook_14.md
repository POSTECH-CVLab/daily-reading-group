# Revealing Scenes by Inverting Structure from Motion Reconstructions
## Francesco Pittaluga et al., University of Florida - CVPR 2019
### Summarized by Seungwook Kim
---

**총평**:
* 인공지능대학원 QE 일환) 오태현 교수님의 추천으로 읽게 됨.
* SfM의 결과 point cloud와, 그에 대응하는 SIFT feature만으로 source image를 얻어낼 수 있다는 결과를 보인다.
* Sparse한 point cloud데이터임에도 불구하고 output을 보고 input을 infer해내는 방법론을 제시해낸 것이 main novelty이다.
* 이전에 리뷰한 input-output을 보고 model에 대해 알아내는 것과 complementary 하지만, 전반적으로 AI security를 다루는 주제.
* 그래도 SIFT feature를 얻을 수 있다는 가정이 있기 때문에, '아주' realistic한 attack 상황을 가정한 것은 아니라고 생각함 (특히 end user의 입장에서는)

**Task**: Feature inversion (output -> input)
* From SfM Output (point cloud & SIFT features)
* performance increases with additional cues (depth, colour)

**Method**: 3 encoder-decoder NNs for visibility estimation, corase image reconstruction and final refinment step
* UNet structure as encoder-decoder NNs

1. Visibility Estimation
  * Not all points in the point clouds would be visible from a certain view if rendered on a 2D image.
  * Use a neural network to classify each input point as either 'visible' or 'included'
2. Coarse image reconstruction
   * Nearest neighbour upsampling followed by standard convolutions 
   * transposed convolutions are not used (known to produce artifacts)
3. Refinement 
   * conditional discriminator was used to distinguish between real source images and synthesized (predicted) images.

**Loss**: Using GT visibility / Colour (pixel loss) / Perceptual loss + Discriminator loss for refinement

**Results**: Qualitatively similar output image as the actual input image
* better results qualitatively and quantitatively (MAE, SSIM) when using more cues (depth, colour)
