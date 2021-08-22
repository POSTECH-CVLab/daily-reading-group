# Conditional Image Generation with PixelCNN Decoders
### Aaron van den Oord et al., DeepMind - NeurIPS 2016
### Summarized by Woohyeon Shim

**Task:** conditional image generation with PixelCNN decoder
	
**Minor fixes of PixelCNN with Gated convolution (GatedPixelCNN)**
* **Adopt architectural advantages of PixelRNN**
  * the region of neighborhood - in RNN, the entire neighborhood of previous pixels affects the current pixel. ⇒ CNN has limited receptive field, but can be largely alleviated by using sufficient many layers.
  * the multiplicative unit in LSTM gate - help it to model more complex interaction. ⇒ CNN can also use gated activation unit to replace ReLU between the masked convolution.
* **Address the potential problem of PixelCNN**
	* the masked convolution - significant portion of the input image is ignored with the progressive growth of the receptive field, resulting in none of the content to the right of the current pixel would be taken into account ⇒ can be alleviated by two convolutional stacks, one for conditioning on current row so far (horizontal stack) and one for conditioning on all rows above (vertical stack)
  	* both do not need any masking, allowing the receptive field to grow in a rectangular fashion.
  	* the horizontal stack gets inputs with the output of the previous layer and that of the vertical stack (did not connect the horizontal stack to the vertical as it would be break the dependencies)
* **Summary of proposed module**
  * Stacking many layers (large model ~ 20 layers with 384 hidden unit and filter size 5x5).
  * y = tanh(Wk,f ∗ x) ⊙ σ(Wk,g ∗ x)
  * Duplicate Wk,f and Wk,g for horizontal (n x 1 convolution) and vertical (nxn convolution) stacks
		
**Conditioning**
* **Types of conditioning**
	* **Based on the latent vector (h):** 1) descriptive labels or tags - one-hot encoding, 2) latent embeddings created by other networks.
	* **Based on the location dependent representation (s):** has the same width and height as the image but may have an arbitrary number of feature maps.
* **Modeling the conditional distribution**
	* p(x|h/s) = product of conditional distribution given all the previous pixels and h/s
	* modeled by adding term of h/s:
	  * y = tanh(Wk,f ∗ x +Vk,fT h)⊙σ(Wk,g∗x+Vk,gT h)
		* y = tanh(Wk,f ∗x+Vk,f ∗s)⊙σ(Wk,g ∗x+Vk,g ∗s).
* **Application: PixelCNN Auto-Encoder**
  * can utilize PixelCNN decoders as the decoder of AE.
  * optimized by MSE loss, use 10 or 100 dimensional bottleneck.
  * expect this change to improve the reconstruction.
  * also expect the representation learned by an encoder concentrate on more high-level abstract information since low-level pixel statistics is handled by the PixelCNN.
		
**Experiments**
* **Compared with PixelRNN:** similar results on CIFAR10, better results on ImageNet, and taking less than half for the training.
* **Conditioning on imagenet classes:** not good in sample quality, but improved against the unconditional model.
* **Conditioning on Portrait Embeddings:** can generate the same person in new poses and facial features, can observe smooth transition from linear interpolations between embeddings.
* **PixelCNN Auto-Encoder on imagenet:** the quality is not good enough to analyze, but the author argues that the model manipulates the high-level sementics more than a conventional decoder.
	
**총평:** PixelRNN 저자가 발전시킨 논문. PixelRNN을 읽고 보면 기술적으로는 크게 새로운 것은 없음. 제안된 방법은 쉽지만 conditional setup이 응용할 수 있는 부분이 많기에 확장성을 보인 것 만으로 높은 평가를 받은 것 같음. 논문은 깔끔하지만 약간 부실하게 적혀져 있음. 읽는다면 conditioning 부분만 참고하는 것을 추천함. 
