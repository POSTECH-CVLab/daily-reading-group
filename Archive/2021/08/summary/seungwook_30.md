# Deformable DETR: Deformable Transformers for End-to-end Object detection
## Xizhou Zhu et al., Sensetime Research - ICLR 2021 Oral
#### Summarized by Seungwook Kim
---

**총평**: 
* DETR의 베이스가 되는 Transformer에 의해 발생하는 한계점을 잘 파악하여, 이를 해결하는 구조를 제안한다. 그 과정에서 efficiency / train time / performance를 모두 챙기는, 아주 이상적인 논문이다.
* Main idea는 매우 간단하나, 그 간단함이 heuristic하지 않도록 learning pipeline에 잘 녹아들어있으며, 존재하는 deformable convolution의 개념을 들고 와서 적용하기에 더욱 잘 동작한다고 여겨진다.
* efficiency를 챙김으로서 performance를 올릴 수 있는 추가적인 technique (multi-scale feature maps)를 적용하는, sparse-NCNet과 비슷한 흐름의 novelty 전개도 있다.
* DETR - Deformable DETR은 꼭 읽어봐야 하는 논문이라고 생각한다.


**Task**: End-to-end object detection
* Using transforemrs


**Motivation / Contributions**

Preliminary : [DETR](https://github.com/POSTECH-CVLab/daily-reading-group/blob/main/Archive/2021/08/summary/seungwook_6.md)
* Suffers from slow convergence & limited feature resolution
* Limited feature resolution -> weak at identifying small objects

Deformable DETR: attention modules only attend to a **small set of sampling points around a reference**
* Mainly inspired by deformable convolutions
* Better performance than DETR
* 10X less training epochs
* Use multi-scale deformable attention modules 

Also tries:
* Simple & Effective iterative Bbox refinement
* Two-stage Deformable DETR
    * Region proposal -> used as object proposals in decoder

**Method**
1. Deformable attention module (Refer to paper for precise formulation)
    * Small fixed number of keys for each query
    * How are the keys sampled?
        * Query feature is projected linearly to 3MK channels (M=num of heads, K=num of keys)
        * From 3MK, 
            * 2MK: encodes the key sampling offsets (not necessarily integer: bilinearly interpolated)
            * MK: fed to softmax operator to obtain attention weights

2. Multi-scale Deformable Attention module
    * Extend single-scale deformable attention module for multi-scale
    * i.e. Attend to multiple keys from multiple scales

3. Deformable Transformer Encoder
    * Unnecessary to build like FPN, because the multi-scale formulation already allows for top-down information exchange
    * Fixed positional encoding + Learned **scale encoding**

4. Deformable Transformer Decoder
    * Cross attention) key: output of encoder <-- multi-scale deformable 
    * Self attention) key: Object proposals themselves
    * 2D normalized coordinate of refernece point predicted by FFN + Sigmoid
        * input: object proposal
        * USed as initial guess for bbox center
        * Final predictor predicts the **relative offset w.r.t the reference point coordinate**

Iterative bounding box refinement?
* Each decoder layer refines bbox predictions from the previous layer

Two-stage deformable DETR?
* First stage: Region proposal (encoder-only architecture)
* Second stage: Region proposal fed as **object queries** to decoder (full architecture)

Note: Iterative bbox refinement, two-stage DETR, and multi-scale attention is possible because computation has been decreased due to deformable attention

