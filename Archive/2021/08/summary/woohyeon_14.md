# Pixel Recurrent Neural Networks
### Aaron van den Oord et al., DeepMind - ICML 2016
### Summarized by Woohyeon Shim

**Task:** Sequential prediction of pixels along x and y direction using RNN.
	
**Joint distribution of the pixels = Product of a sequence of conditional distribution**
* model the pixels as discrete values → easy to learn and produce better performance.
* multinomial distribution implemented with softmax layer.
* predict the next pixel given all the previously generated pixels.
	* ordering of pixels: from the top left to the bottom right
	* ordering of colors: R→G→B
* desired properties; tractable, scalable, expressive
  
**RNN**
* shared parameterization across all pixel positions in the image.
* can model highly-nonlinear and long-range correlations between pixels and the complex conditional distribution.
	
**PixelRNNs (Two-dimensional RNN)**
* **Two types of LSTM, each has**
	* input-to-state component (Kis)
	* recurrent state-to-state component (Kss)
	* four gates vectors: output, forget, input, and content
	* hidden and cell states for previous and current step (h, x)
	* adopt a convolution to compute at once all the states along one of the spatial dimensions of the data.
* **Row LSTM layer**
	* row-by-row, from top to bottom
	* [output, forget, input, content]=σ(Kss * hi−1 +Kis * xi)
		* k x 1 convolution (Kss, Kis) for each component
		* four gates vectors: 4h x n x n / n: image size
	* cell state update: forget ⊙ previous cell + input ⊙ content
	* hidden state update: output ⊙ tanh(content)
	* has triangular receptive field (due to convolution) → unable to capture the entire available context.
* **Diagonal BiLSTM layer
	* take two paths (left → down, down → left) along a diagonal
	* skew input map for each row to have one more offsets than previous row, resulting in n x (2n-1) size of map.
	* use 1 x 1 convolution for Kis, columnwise 1x2 convolution for Kss
	* update four gates and states with the same process of RowLSTM
	* output is skewed back into n x n map by removing offset position
  * two directional outputs are added into one.
* **Multi-scale RNN**
	* first generate small scale image; s x s
	* upsample s x s feature map to n x n by deconv layer
	* perform 1 x 1 conv to produce 4h x n x n map
	* adds it to input-to-state map of corresponding layer, then generate n x n image as usual
		
**PixelCNN**
* unbounded → bounded dependency range, but parallelization.
* simplified architecture which shares the same core components as PixelRNN
* fifteen layers of fully convolutional network that preserves the spatial resolution of the input
* outputs a conditional distribution at each location
* the process is sequential; the output needs to be given as input back into the network.
* masks are adopted in the convolutions to avoid seeing the future context.

**Details**
* **Residual connections around LSTM layer**
	* connection from one LSTM layer to the next.
	* help increase depth of the model up to twelve layers.
* **Masked Convolution**
	* restrict connections to implement dependencies (that admits left and above pixels can be used as context).
	* can be implemented by zeroing out the corresponding weights in input-to-state convolutions.
* **Training with log-likelihood loss** coming from a discrete distribution
* **Evaluation with negative log-likelihood** in bits per dimension.
	* the total discrete log-likelihood is normalized by the dimensionality of the images (e.g., 32 × 32 × 3 = 3072 for CIFAR10)
	* related to compression scheme to compress every RGB color value
* **Results: Diagonal BiLSTM has the best performance, followed by the Row LSTM and the Pixel-CNN.**
	* This coincides with the size of the respective receptive fields: Diagonal BiLSTM has a global view, the Row LSTM has a partially occluded view and the Pixel- CNN sees the fewest pixels in the context.
* **Shown application: image completions**

**총평:** auto-regressive 계열의 생성 모델의 초기 논문. image distribution을 pixel sequence의 conditional distribution의 곱으로 나타낼 수 있다는 것에 영감을 받아 sequential model인 RNN 기반한 모델을 제안함. 단순한 모델부터 복잡한 것까지 다양한 모델을 제안하였고 각각을 알기 쉽게 설명해주며 실험에서 불필요한 것이 없이 효과가 있음을 보인 것이 좋았음.
