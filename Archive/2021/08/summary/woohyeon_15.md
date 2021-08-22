# Few-Shot Unsupervised Image-to-Image Translation
### Ming-Yu Liu et al., NVIDIA - ICCV 2019
### Summarized by Woohyeon Shim

**Task:** translating images of seen classes to analogous images of unseen classes in limited-shot setting.
	
**Motivation**
* **Human:** can form a vivid mental picture of a new object in a different pose given a lifetime of experience of other animals.
* **Machine:** can simulate the images of unseen classes using a dataset containing images of many different object classes.

**Assumtion**
* **source data -** images of various object classes; being capable of multi classes translation
* **target data -** few images for a novel class and only available at test time
* **unstructured datasets;** no paired images given for image translation
	
**Training - translate images between source object classes**
* **Translator: x' = G(x, {y_1, ..., y_K }) = Fx(zx, zy) = Fx(Ex(x), Ey({y1,...,yK})).**
	* **overview**
		* x: a content image of object class c_x
		* y_1, ..., y_k: a set of K images of object class c_y
		* x': translated image analogous to the images in class c_y.
	* **content encoder Ex**
		* output content latent code z_x from the content image x.
		* z_x is a spatial feature map.
		* aim at extracting class-invariant latent representation (e.g., object pose)
	* **class encoder Ey**
	  * output class latent code z_y with a mean operation along the sample axis
		* aim at extracting class-specific latent representation (e.g., object appearance)
		  * at test time, this generalizes to images of previously unseen classes.
		  * the generalization capability depends on the number of source object classes seen during training
	* **decoder Fx**
	  * several adaptive instance normalization residual blocks.
	  * affine tranformation parameters are adaptively computed using z_y via a two-layer fully connected network.
	    * class images control the global look (e.g., object appearance).
	    * content image determines the local structure (e.g., locations of eyes).
    * followed by a couple of upscale convolutional layers
	* **Objective:** GAN loss + content image reconstruction loss - when using the same image for both input content image and input class image
* **Discriminator - D^c(x)**
	* **Multi-task discriminator:** class-wise discrimination for source classes without interaction with other classes. ⇒ this was much better than training with classifier.
	* **Objective:** GAN loss + the feature matching loss - minimizing the difference of feature representations between translation output and class images.
		
**Details**
* use hinge version of GAN loss with λRecon = 0.1 and λFeatmat = 1.
* use real gradient penalty regularization
* apply exponential moving average for generator (update weight = 0.001)
* evaluate performance under K=1, 5, 10, 15, 20.
	
**Experiments**
* **Dataset (classes):** Animal Faces (149), Birds (555), Flowers(102), Foods (256)
	* Animal faces: from Imagenet of 149 carnivorous animal classes, manually label bounding boxes and train detector to crop them, resulting in 117574 animal faces.
* **Evaluation:** distinguish settings depending on whether the target classes are available during training or not.
	* Translation accuracy: measure whether a translation belongs to the target class.
	* Preservation of class-invariant content: measure domain-invariant perceptual distance (L2 distance between two normalized VGG Conv5 features)
	* Photorealism: with IS and FID, measured with classifier after trained using target classes.
* **SoTA for all datasets on all metrics**
  * Work well even when only one target class image is available.
  * Positively correlated with number of available target images K at test time.
* **Latent interpolation:** keeping the content code fixed while interpolating the class code between two source class images
  * sometimes generate a target class that the model has never observed
* **Few-shot classification** by data augmentation: outperform a method based on feature hallucination.
	
**총평:** multi-class translation과 few-shot setup, 그리고 unstructured dataset에서 generation을 처음으로 시도함. 실험 셋업은 few-shot classification 방식과 아주 비슷함. 이런 시도가 처음이기 때문에 베이스라인을 같은 셋업으로 구성하거나, 제안한 방식을 다른 일반적인 셋업으로 맞추는데 애를 먹은 것 같음. 전반적으로 논문 구성이 좋으며 실험도 알차고 결과도 좋으며 제안한 방식이 상당히 도전적인 것 만큼 임팩트도 큰 것 같음.
