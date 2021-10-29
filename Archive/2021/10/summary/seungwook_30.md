# Infinite Nature: Perpetual View Generation of Natural Scenes from a Single Image
## Andrew Liu et al., Google Research - ICCV 2021 (Oral)
### Summarized by Seungwook Kim
---

**총평**:
* 연구 주제를 볼 때 "이거 novel하다", "이거 잘 되겠다" 라는 생각으로 설계된 주제를 많이 봐왔는데, "이거 재미있겠다"라는 motivation이 뚜렷해보이는 논문이었습니다. 
* Qualitative results가 엄청 impressive하고, 재미를 위해 상상한 주제를 구현하기 위해 여러 SoTA method를 도입한 모습 또한 인상깊었습니다. 새로운 task 자체가 얼마나 유의미한지는 모르겠지만, 여러 조건만 갖춰진다면 꽤나 인기 있는 분야가 될 수 있지 않을까 생각합니다.
* 이 논문의 main motivation이 2010년 논문 (Infinite Images)입니다. 요새 옛날 논문들이 많이 읽고싶어지네요
* 다음주 세미나에 더 자세하게 소개드릴 예정입니다.

**Task**: Perpetual view generation (Video synthesis)
* Single image -> novel views for a camera trajectory covering a long distance
* Unlike Nerf-based methods, which cover limited viewpoints (not long-distance camera trajectories)

**New dataset**: ACID - Aerial Costline Image dataset
* nature scenes, as GANs show promising results on GAN texture
* 765 videos collected online using keywords ('coastal','aerial footage'...)
* 13000 sequences with 2.1million frames

**Method**: Render - Refine - Repeat

Render:
* Given initial image
* Get disparity map from image using MiDAS (monocular depth estimation)
* Use differentiable mesh renderer (Genova et al.,) for rendering next step image & disparity map
  * uses camera pose, obtained using SfM on the input video data
* Note that this new rendering introduces new views which were occluded / out of view.

Refine:
* There are needs for: superresolution (if trajectory moves forward), inpainting (occlusion), outpainting (out of view).
* Uses SPADE (image-to-image translation) to ouput refined disparity map & image

Repeat:
* repeat the above process to synthesize a series of images -> video!

Loss:
* L1 reconstruction loss on RGB, Disparity map
* VGG Perceptual loss on RGB
* hinge-based adversarial loss with discrimnator for synthesized frames
* feature matching loss using synthesized frames
* KL divergence loss on image encoder.
  * not really sure what this is for?
