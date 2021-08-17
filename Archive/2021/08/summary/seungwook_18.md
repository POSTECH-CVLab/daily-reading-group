# Generating Long Sequences with Sparse Transformers (a.k.a Sparse Transformer)
### Rewon Child et al., OpenAI - Arxiv2019
#### Summarized by Seungwook Kim
---

**Task**: Efficient Transformers
* basically focused on autoregressive tasks
* becomes similar to local self attention but seems applicable to visual transformers.

**Main Idea**: Approximating global attention using sparse attention between multiple heads
**Motivation**: The memory & computational requirements of transformer networks grow quadratically with sequence length
* cannot be easily used on long sequences


**Contributions & Novelty + Methods** \
사실상 1번의 main contribution을 제외하고는 minor technical addition


1. introduce several sparse factorizations of the attention matrix
* scale as $O(n\sqrt[p](n))$ with sequence length without loss in performance
* done by separating full attention to several faster operations to "approximate" dense attention **when combined**
    * **Factorized self attention**: $p$ separate attention heads, attending to **different subset of indices of attention matrix**
      * previous attention: the head (or multi-head) attended to all indices of attention matrix
    * **Two-dimensional factorized attention**
      * 1)One head attend to **previous N** locations
      * 2)Second head attend to **every Nth** locations
        * stride N * coverage N --> approximate dense attention!

2. Restructured residual block and weight initialization to improve training of very deep networks
* Restructured residual block: Pre-activation (layernorm 이후에 attention을 태우는 방식)
* Weight initialization: Head를 나눠 attention을 주기 때문에, 나눈 개수에 따라서 initialization 당시 normalization을 추가하는 것.
* 둘 다 기존에 있던 방법/trivial 한 novelty 

3. A set of sparse attention kernels which efficiently compute subsets of the attention matrix
* 1번에서 소개된 방식을 GPU kernel의 형태로 구현했다는 말
* tensorflow로 구현된 코드를 보니 CUDA coding을 한 건 아니고, 단순히 코드 구현을 의미하는 듯
* Autoregressive인지라 lower part of the attention matrix만 학습
  * visual transformer에 적용시에는 사용하기 어려운 듯한 성질

4. Recomputation of attention weights during the backwards pass to reduce memory usage
* (Chen et al., 2016)에서 제안된 Gradient checkpointing을 통해, compute를 올리는 대신 memory절약이 가능하다.
* Sequence가 길어서 memory usage가 높을 때 특히 더 효과적이라고 한다.
  * High-dimension tensor에 attention을 시도하는 제 입장에서 도움이 되는 코멘트였습니다.

**Results**: Density modeling task에서 SoTA.
* Density modeling task 가 정확히 뭔지 모르겠지만 PixelCNN과 비교한 것으로 보아 sequence generation과 관련이 있는 듯 함.
* 이 외에도 google research 에서 efficient transformer들의 성능 비교를 위한 **Long Range Arena(LRA)**에서도 거의 2번쨰로 높은 성능을 보여주고 있음.
    * SoTA는 BigBird
    * 최근에 H-Transformer-1D 라는 모델이 LRA 전체 SoTA를 갱신했다고 함

총평:
* Writing이 어렵게 되어있습니다. 쉽게 할 수 있는 설명을 굳이 어렵게 한 것 같진 않지만, 더 쉽게 풀어서 쓸 수 있었을 것 같아서 시간이 생각보다 오래 걸렸습니다.
* 다 이해하고 나면 꽤나 technically/theoretically 훌륭한 논문이라는 생각이 듭니다. Efficiency를 살리며 dense attention을 approximate하는 novelty와, 이를 더불어 long sequence/many layers를 가능하게 하는 engineering이 둘 다 유의미한 contribution 같습니다.
