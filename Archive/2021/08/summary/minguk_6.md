# Diffusion Models beat GANs on Image Synthesis
### Prafulla Dhariwal, Alex Nichol - Neurips 2021 (submitted)
#### Summarized by Minguk Kang
----

**Task**: 디퓨전 모델이 적대적 생성 신경망에 비해 이미지 생성 성능이 떨어지는 이유를 규명
 
**Motivation**: DDPM, DDIM과 같은 디퓨전 모델이 CIFAR10 데이터세트에서는 GAN의 생성 성능을 이겼는데, LSUN, ImageNet과 같은 large-scale 데이터셋의 생성 실험에서는 좋은 결과를 보여주지 못 했습니다. 본 논문의 저자들은 이는 (1) GAN의 architecture가 수년동안 엄청나게 가다듬어 졌다는 점과 (2) Conditional GANs과 같이 class label을 사용하여 이미지 생성을 보조하는 방법이 Diffusion model에는 없다는 것을 지적하고, 이에 대한 조사를 통해 large-scale image generation에서 성공적인 이미지 생성 결과를 보여주고 있습니다.
 
**Method**: 먼저 5개의 범주 내에서 아키텍처 서치를 합니다. 이를 나열하면 아래와 같습니다. 
(1) depth와 width를 늘려보기
(2) attention head의 수를 늘려보기
(3) 32 x 32, 16 x 16, 8 x 8 해상도에서 MHA을 적용하기
(4) BigGAN에서 사용하는 upsampling and downsampling 방법을 사용하기
(5) Residual output에 1/root(2)를 곱하기
 
아키텍처 서치결과 이 중 (2), (3), (4)에서 많은 효과를 보았고 Diffusion model에도 도입하기로 합니다 ((1)은 연산량을 너무 증가시켜 moderate size로 통합했습니다). 
다음으로는 미리 학습된 classifier를 통해 sampling guidance를 해주는데, 이를 통해 denoised image를 샘플링 할 때 mean을 \sigma*g만큼의 벡터로 biasing해주게 됩니다. 그 결과 BigGAN-deep 및 StyleGAN의 생성 성능을 모두 이기는 새로운 Generative model을 학습 시킬 수 있었고, Recall을 기준으로 봤을 때 GAN보다 더욱 다양한 이미지를 생성할 수 있었습니다.
 
**총평**: GAN에서 Diffusion Model로 페러다임 체인지를 할 것 같다는 생각을 하게 만드는 논문이었습니다. 실험 논문이었으나 그 결과가 정말 놀라웠으며, 앞으로 해당 모델을 기준으로 Generative model의 baseline이 구축되지 않을까 기대되는 논문이었습니다. 단점으로는 Model의 크기가 GAN에 비해 얼마나 큰지에 대한 설명이 없었고, 아직 inference time이 길기 때문에 넘어야 할 산은 남아 있는 것 같습니다.
