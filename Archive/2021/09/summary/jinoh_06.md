Swapping Autoencoder for Deep Image Manipulation (Taesung Park et al., UC Berkely) - NeurIPS 2020

Overview : 

They intended to seperate the latent code of input image as two parts: structure code and texture code. To achieve this, they swap the latent codes from two input images and trained with Vanilla Reconstruction Loss, GAN loss with reconstructed images, GAN loss with swapped images, and Co-occurrent patch statistics loss which encourage texture code to imply the texture information.

Task : Image Manipulation

Motivation : Deep generative models have achieved astonishing results when generating realistic images from the random noise vectors. However, using those models to manipulate the existing images are still challenging.  Method & Exp: 

Entire Architecture can be divided as three parts: Classic Autoencoder, Discriminator for realistic image generation, and co-occurrence patch discriminator.


 0. Loss Function: Recon loss + Recon Image Gan Loss + Hybrid Image GAN Loss + Co-ocurrence patch GAN Loss

 1. Method : “How they disentangle the structure codes and texture codes?”

	(1) They differ the design of layers.

		(a) The texture code(1 by 1 by 2048) is designed to be agnostic to positional information by using convolution layer 	followed by average pooling layer. 

		(b) On the other hand, each location of the structure code(32 by 32 by 8) has a strong inductive bias to encode information in its neighborhood, due to its fully convolutional architecture and limited receptive field.

	(2) They swap the texture codes and structure codes from the two input images.

		(a) 일반적인 오토인코더와 같이 reconstruction loss를 통해서 인코더에서 추출한 structure and texture code가 인풋 이미지를 복원하기에 충분한 information을 담고 있도록 하였음. 허나, 이 로스만으로는 structure information과 texture information이 disentangle되지 않음.

		(b) 두 이미지를 준비하고, 이 두 이미지로 부터 각각 texture code와 structure code를 추출한다. 추출한 code들을 swapping을 하여 hybrid image를 generate한다. Hybrid image와 각 원본 입력 이미지에서 patch들을 crop하고 Hybrid image에서 뽑은 patch가 texture code를 추출한 원본 이미지의 patch들과 구분이 되지 않도록 하는 co-occurence patch discriminator loss를 이용한다. 이를 통해서 texture code가 texture information을 가지고 있도록 supervison을 준다. 이 로스는 Julesz’s theory of texture perception에서 similar marginal and joint feature statistics를 가지고 있는 두 이미지는 texture가 같게 인식된다는 것에 영감을 받아 디자인 되었음.

2. Experiment: 

Training 된 autoencoder로 시도 할 수 있는 다양한 application(Texture와 Structure Swapping generation 결과, Image Editing, Vector Arithmetic)과 다양한 SOTA 베이스 라인과의 비교 실험 결과를 보여주고 있음.

Single Image FID(SIFID)는 Style을 capture, Self Similarity Distance는 Structure를 평가하는데 적합하다는 실험도 appendix에 있음.  

총평: 
	
Technical하게 굉장히 Novel하다는 느낌보다는, 다양한 평가 지표들을 사용해서 제안한 method가 우수하다는 것을 다양한 실험에서 입증하고 있음. Writing도 이해하기 쉽게 명확하게 써져있는 것 같다는 느낌을 받음.
