# Neural Discrete Representation Learning 
### Aaron van den Oord et al., DeepMind - NeurIPS 2017
### Summarized by Woohyeon Shim

**Task:** learning discrete latent codes/representations in variational auto-encoder(VAE) using vector quantization(VQ).
	
**Why discrete representations?**
* a natural fit for many of modalities - language: sequence of symbols, image/speech/planning/predictive learning: can be described concisely by language.
* to pair with a powerful autoregressive decoder - have been developed for modeling distributions over discrete variables (e.g., wavenet; self-citation).
* to circumvent issues of "posterior collapse" - where latents are ignored in later synthesis.
	
**VQ-VAE**
* **An encoder network - parameterizes a posterior distribution q(z|x)**
	* outputs continuous embedding vector z_e.
	* discretize these embeddings by a nearest neighbor z_q from look-up table e ∈ R K×D (= the size of the discrete latent space x dimensionality of each latent vector).
	* posterior distribution is deterministic and defined as one-hot; q(z=k|x) = (whether nearest neighbor or not)
* **A decoder network - a distribution p(x|z) over input data.**
	* feed nearest embeddings z_q as input.
* **Training losses**
	* **for encoder and decoder: reconstruction loss of log p(x|z_q(x))** with straight-through estimator, which copies gradients from decoder input z_q to encoder output z_e.
  	* **for look-up table (vector quantization): l2 loss** between the encoder outputs z_e and corresponding dictionary item e_i. (z_e is stop-gradiented)
	* **additional regularizer for encoder (commitment loss not to alter arbitrarily the dictionary item): the same loss of** look-up table learning, but here, e_i is stop-gradiented.
* **Log likelihood of the complete model**
	* **log p(x) = log [Sum_k p(x|z_k)p(z_k)],** summations over dictionary items.
	* **A prior distribution p(z): categorical distribution,** set to a simple uniform distribution.
		* **z can be made auto-regressive by depending on other z in the feature map:** after training, the authors use the auto-regressive models, PixelCNN for images and WaveNet for audio, to generate x via ancestral sampling.
		* **Training prior and VQ-VAE jointly is left as future work.**
			
**Experiments**
* **Image generation:** not collapsed even with powerful auto-regressive PixelCNN decoder (CIFAR10/ImageNet/DeepMind Lab)
* **Audio:** can conserves the content of original waveform with 64x compression rate, but has drawbacks that the waveform is quite different and prosody is altered.
* **Speaker conversion:** can decodes using other speaker id after factoring out speaker-specific information!
* **Quality of discrete codes:** gets 49.3% accuracy of learned latents to be associated with 41 possible phoneme values.
* **Video:** synthesizes sequence of frames conditioned on initial frames and an action. this is purely based on manipulation of latent vectors, which were created using prior model.
	
**총평:** embedding을 discretize하여 auto-regressive decoder로 long-term sequence 생성을 가능하게 한 논문. 저자는 개념적인 접근으로 discrete representation의 당위성을 일반화시키려 하지만 보통의 테스크에서의 성능은 continuous counterpart가 더 좋기 떄문에 납득은 되지 않음. 하지만 auto-regressive decoder를 붙임으로써 long-term modeling, conditional synthesis등 활용성이 높아지고 그것을 실제로 실험으로 다양하게 보려주려 했던 것은 높이 평가하고 싶음.
