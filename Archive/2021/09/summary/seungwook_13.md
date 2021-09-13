# ConvMLP: Hierarchical Convolutional MLPs for Vision
### Jiachen Li et al., UoOregon, UIUC - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**:
* MLP-mixer + convolution의 hybrid를 시도한 논문. ViT가 처음 제안되었을 때, Convolution과 Transformer의 hybrid가 많이 나왔던 것과 비슷한 방향으로 보인다. 나올만한 논문이 나온 느낌이지만, 큰 impact는 없다고 여겨짐.
* MLP variant와 비교하여 accuracy - parameter tradeoff를 강조하는데, MAC/memory의 경우에는 어떤지에 대한 분석이 부족하며,결국 efficientNet 계열의 model보다는 accuracy - parameter, accuracy - MAC tradeoff에서 둘 다 뒤쳐진다. 
* **convolution과 MLP를 같이 쓰면 메모리와 parameter를 덜 쓰면서 다른 MLP 기반 모델을 이길 수 있지만, 그래도 efficientnet 계열이 가장 잘 된다**가 내가 생각하는 결론.
---


**Task**:Improved MLP-Mixer architecture
* For not only image classification, but also other downstream tasks (segmentation, object detection)

**Motivation & Contributions**:
* Previous MLP-based architectures (resMLP, MLP-Mixer, gMLP...) only take inputs of fixed dimensions and are difficult to be used in downstream computer vision tasks as backbones. 
  * their single-stage design and large computation also limit applications
  * Cycle MLP and AS-MLP are concurrent work, which are more flexible for varying input sizes

Proposes **ConvMLP**: Hierarchical Convolution MLP backbone
* co-design of convolution and MLP layers
* scalable and can be deployed to downstream tasks easily

**Method**

1. Tokenizer
    * instead of direct patch tokenizer, uses a convolutional-based tokenizer
    * extracts the initial feature map to reduce computation & improve spatial connections

2. Convolution Stage
   * To "augment spatial connections"
   * 1x1 conv -> 3x3 conv -> 1x1 conv

3. Conv-MLP stage
   * Channelwise MLP -> Depthwise Conv -> Channelwise MLP -> Convolutional downsampling
   * Convolutional Downsampling: Same as in Swin Transformer
     * patch merging method based on linear layers to down-sample feature maps

**Overall**: Original MLP-mixer architecture has channelwise MLP and spatial-wise MLP
* This architecture only uses channelwise MLP, and leaves the spatialwise interaction to convolutional / downsampling operations.

**Result**

Image Classification
* Outperforms other MLP-based methods in accuracy, param and GMACs
* outperforms transformers in params and GMACs, but not in accuracy
* **Outperformed by** efficientnet families in params, GMACs and accuracy

When used as backbones vs ResNet:
* outperforms ResNet (compared model w.r.t params) when using RetinaNet, Mask R-CNN on MSCOCO
* outperforms ResNet (compared model w.r.t params) when using Semantic FPN on ADE20K.

**Overall**: Notable param/accuracy improvements among MLP models, minor MAC improvement
* but still falls behind SoTA CNN models
