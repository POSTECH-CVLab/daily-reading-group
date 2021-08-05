# StarGAN v2: Diverse Image Synthesis for Multiple Domains 
### Yunjey Choi et al., Clova AI - CVPR 2020
### Summarized by Woohyeon Shim
	
**Task**: Synthesizing diverse images over multiple domains using a single generator

**Background**: Domain and Style?
* domain implies a set of images that can be grouped as a visually distinctive category.
* style is an unique appearance/characteristic of an image in the domain, e.g., makeup, beard and hairstyle where the domain is set to person.
	
**Main Contribution**
* replace domain label with domain-specific style code so as to represent diverse styles of a specific domain.
* inject domain-specific style code into generator to diversify the synthesized images within the designated domain.
	
**Method**: Generating domain specific images with variety of style code
* **Style-code generation** \
⇒ mapping network - given latent code: transforms a latent code into style codes for random image synthesis. \
⇒ style encoder - given image: extracts the style code from an image to perform reference-guided image synthesis. \
⇒ both networks have multiple output branches, each of which provides style codes for a specific domain.

* **Image-to-image translation** \
⇒ inject domain-specific style code using adaptive instance normalization (adaIN). \
⇒ synthesize images of all domains using a single generator.
		
* **Discriminator** \
⇒ distinguishes between real and fake images for each domain (multi-task discriminator).
				
* **Training:** adversarial loss for latent-guided synthesis, style reconstruction loss between latent code and the outputs of corresponding synthesized image from the style encoder, diversity sensitive loss that enforces the different codes to produce different outputs, cycle consistency loss that takes the style code of an image and reconstructs it from once-translated one by changing the code to the original.
		
**Other Contribution** : new animal face dataset (AFHQ) for three domains (cat, dog, wildlife)

**Experiments** : the components were effective in following order (latent code injection ⇒ style code embedding ⇒ reconstruction & cycle-consistency loss ⇒ multi-task discriminator ⇒ diversity regularization)
	
**총평** : StyleGAN을 image-to-image translation에 early-adopt한 논문. 이미지 생성을 latent-code와 reference-image 기반으로 하는 것이 application 측면에서 아주 흥미로웠지만 학습 과정이 복잡한 것이 아쉬웠음.
