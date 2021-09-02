# Co-Attention for Conditioned Image matching
## Olivia Wiles et al., Oxford (VGG group) - CVPR 2021
#### Summarized by Seungwook Kim
---

**총평**: 
* Attention 개념을 matching / stylization에 적용한 논문이다. Neighbourhood consensus를 사용하는 최근 흐름과는 꽤나 다른 양상을 보이며, Descriptor 자체를 image pair에 condition하기 위해 transformer를 사용한다. Co-attention module이기는 하지만 transformer처럼 encoder/decoder 형태거나, Q,K,V 등을 사용하지는 않는다.
* Main idea가 매우 간단하며, full-sup과 self-sup에서 둘 다 사용될 수 있음을 보인다.
* 여러 task (Image matching, 3D recon...)에 대해 evaluation을 진행하는데, 왜 특정 dataset은 제외되었는지, 왜 특정 baseline과는 비교되지 않았는지에 대한 의문이 있다. 특히 SuperGlue와는 비교하지 않는 논문들이 꽤나 많던데, 왜인지 잘 모르겠다.
* Test-time의 이미지 크기가 
* 무난한 논문.


**Task**: Image Matching


**Motivation / Contributions**
* Previous methods learn descriptors for each image **without** knowledge of the other image.
    * Descriptors become more invariant -> become more ambiguous to match
    * instead, condition the descriptors on **both images**
* Proposes 1) Coattention Module to generate conditioned decriptors, and 2) Distinctiveness score to select best matches
* Eschews techniques used by other matching methods, such as:
    * High dimensional descriptors (paper uses 64-dim)
    * Multiple scales (paper uses only single scale)
        * Why though, using multi scale may increase performance?

**Method**
1. Overall: Unet encoder-decoder with CoAM (Coattention Module)
* Encoder -> Conditioned Features -> Decoder 
* Only one of the images in a pair is output
    * need to be run twice for each image pair

2. CoAM attention module
* attention mechanism to model long range dependencies
* learns "where to attend"

3. Decoder: Conditioned features
* Regress a distinctiveness score [0,1] for each pixel (i,j) using MLP
    * approximates its 'matchability'
    * used at test time to select the best matches for downstream tasks
    * approximates "how often the descriptors is confused ith negatives in the other image"
        * nearer to 1 if descriptor is uniquely matched
* Test time: Distinctiveness scores * Similarity scores
    * top-K used as final matches
    * may select only the mutual nearest neighbours as well

Training:
* Sample positive correspondences from GT 
* Sample fixed number of large negatives for each positive correspondence (for supervision)
* Contrastive Hinge Loss for feature discriminability
* Distinctiveness Loss to learn score properly
* Trained on MegaDepth

Self-sup training:
- Use CapsNet, integrate CoAM

**Results**
* SoTA or on-par on HPatches (correspondence), Aachen-Benchmark (Localization) SfM(3D recon).
* Stylization도 했다고 하지만 supple에 있는듯
* Self-sup : SoTA / On-par with CapsNet on MegaDepth (camera pose prediction)

