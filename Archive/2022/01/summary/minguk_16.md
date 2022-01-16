# Ensembling Off-the-shelf Models for GAN Training
### Nupur Kumari, Richard Zhang, Eli Shechtman, Jun-Yan Zhu
#### Summarized by Minguk Kang
---



총평:



* Off-the-shelf recognition models들을 사용하여 GAN을 효율적이고 빠르게 학습할 수 있는 방법을 제안하였음.



* 생각보다 Computation overhead가 있고, training 시간이 길어지는 단점이 있음.



* StyleGAN2와 ADA, DiffAugment 어그멘테이션을 통해 data-limited situation에서 differentiable augmentation의 필요성을 보여주었고, 명확한 베이스라인을 잡아줬다고 생각함.



* Twitter에서 해당 논문의 인기도에 비해 새로운 알고리즘을 제시하거나 엄청난 성능 향상을 보여준 논문은 아닌 것 같음. 오타가 조금 있지만 전체적으로 글은 잘 적은 것 같고 라지스케일 학습을 어떻게 하는지에 대해서 궁금하다면 빠르게 읽어보는 것도 좋은 것 같습니다.



Motivation:



* 사전학습된 최신 모델, ViT, DINO, Swin-T, VGG을 사용하여 data-efficient GAN training을 할 수 있는 방법이 없을까?



* 다른 tasks들은 사전학습을 사용하는데, GAN만 스크레치에서 학습을 시작하고 있음.



Method:



* N개의 pre-trained SOTA models을 준비한다.


* 우선 Naive GAN을 특정 iteration동안 학습한다.


* Naive GAN을 통해 생성한 이미지와 실제 이미지를 통해 Top-accuracy model을 선정한다.


* The top-accuracy model을 freeze한 다음 non-linear projector를 통해 adversarial training을 한다.


* 위의 과정을 반복한다.



Data:



* FFHQ dataset, AFHQ(512 res.), LSUN-church, LSUN-Cat



Results:



* 제안하는 방벙을 사용하면, discriminator의 overfitting의 발생을 늦출수 있다는 것을 실험적으로 증명



* DINO, CLIP, Swin-T 순으로 Top model이 선정되었음.



* ADA, DiffAugment와 잘 조화되서 사용될 수 있음을 정량적으로 확인하였음.



* 다만 학습시간에 대한 실험 및 비교가 있었으면 더 좋았을 것 같고, StyleGAN architecture에서만 실험한게 아쉬움.
