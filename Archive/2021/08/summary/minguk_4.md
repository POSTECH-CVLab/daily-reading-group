# Omni-GAN: On the Secrets of cGANs and Beyond
### Author Information 
#### Summarized by Minguk Kang
---

OmniGAN에서 기존의 conditional GAN 모델이 가지고 있는 단점: 

1) instable한 학습 특정

2) full-supervision의 부제 (정확히 이해하지는 못 했지만, 밀고 당니는 힘으로 생각하고 있음)

을 극복한 새로운 conditional GAN framework을 제안하였는데, metric learning에서 유명한 Circle loss에서 영감을 받은 (거의 같은) omni-loss를 차용한 Omni-GAN을 제안합니다. 

 

하지만, 바로 classifier-based conditional GAN인 omni-GAN을 바로 학습했을 하면, 학습이 불안정하여 조기 무너짐이 생기는 문제가 있는데, 저자는 이를 단순한 weight decay를 사용하여 학습 안정화로 해결합니다. 

 

실험 결과가 정말 인상적인데, ImageNet에서 train dataset (IS 233)보다는 낮고 validation dataset (IS 162)보다는 높은 IS: 190.23 값을 보여주고 있으며, FID는 예상과는 반대로 기존 BigGAN benchmark과 별 차이 없는 8.3의 값을 보여주고 있습니다. 

 

또한, implicit neural representation과 결합하면 더욱 좋은 생성 성능을 보여주는데, 해당 논문들을 공부를 해보면 더 좋을 것 같습니다.

 

단점으로는, weight decay를 사용하면 classifier-based GAN이 무너지지 않는 이유를 실험적으로만 보여주었다는 것, IS, FID 값을 봤을 때 Omni-GAN이 학습 데이터를 암기하여 분류되기 쉬운 이미지들을 생성하는게 아닌가라는 의문이 있는 것 같습니다. 또한, Omin-loss 자체가 저자가 고안한 새로운 목적함수가 아니기에 novelity의 limitation이 있는 것 같습니다.