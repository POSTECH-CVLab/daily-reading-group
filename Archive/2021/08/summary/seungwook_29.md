# PoinTr: Diverse Point Cloud Completion with Geometry-Aware Transformers
## Xumin Yu et al., Tsinghua U - ICCV 2021 Oral
#### Summarized by Seungwook Kim
---

**총평**: 
* Transformer를 적용하여, Transformer의 inherent characteristic (set-to-set, global context 등) 을 잘 활용하고 적용하여 Oral paper가 되었다고 생각함.
* 그 외에 formulation에는 큰 novelty가 없어보임. DGCNN / FoldingNet의 사용이 꽤나 중심적이어서, Transformer를 자연스럽게 적용한 pipeline의 제안이 가장 크게 작용했다고 생각함.
* 읽기 적당한 논문. Point Cloud Completion task에 입문하고자 하면 추천할만한 논문.


**Task**: Point Cloud Completion
* Using transformers

**Motivation / Contributions**
* **Adopt Transformers** for long-range dependency between points before completion
* Two additional datasets to cover real-world scenarios

**Method**:
1. Set-to-set translation using transformers
    * Encoder-Decoder structure
    * Given input, obtain "point proxies"
    * Refer to (2)
    * Point proxies to point proxies

2. Point Proxies
    * Using all points requires too much compute
    * By using Farthest Point Sampling to sample point centers
    * use DGCNN to extract features
    * Use MLP to compute positional encoding (addition)

3. Geometry-aware Transformer block
    * 일반적인 block: (Q,K,V -> MHSA -> FFN)
    * Geometry aware: (query coordinates, key coordinates, V -> KNN query -> FFN)
        * KNN 으로 geometry-aware하게 만든다고 주장
    * 일반적인 block & Geometry-aware block을 parallel으로 한 뒤 concat -> FFN

4.  Query Generator
    * Decoder의 Query : Initial state of predicted proxies
    * 1)Summarize Encoder outputs with FFN + Max Pooling
    * 2)Linear project results of (1) to reshape to predicted proxies
    * 3)Concat Results of (1) to each result of (2) and MLP 

5. Multi-scale point cloud generation
    * First scale: 4)의 결과를 missing point cloud의 center point를 나타내는 proxy로 사용해서 recover
    * 이후 FoldingNet을 사용하여 local detail까지 generate함

Loss function: Chamfer Distance of predicted proxies + Chamfer Distance of local details
* 굳이 분리한 이유는, Proxy / Detail이 output되는 부분이 달라서라고 생각됨

Newly introduced benchmarks:
* ShapeNet-55, ShapeNet-34
* Previous datasets: PCN, Kitti
