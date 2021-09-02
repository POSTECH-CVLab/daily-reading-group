# RoFormer: Enhanced Transformer with Rotary Position Embedding
## Jianlin Su et al., Zhuiyi Technology Co. Ltd - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**: 
* Positional encoding이 맞는지 positional embedding이 맞는지 헷갈린다
* 기존에 feature들에 더해지는 positional encoding들보다는 조금 더 intuitive하게 다가온다
    * 본 논문 방법은 곱해지는 방법
* "Rotary" position encoding을 통해 위치정보가 보다 중요한 상황에 더 적합할 것으로 보임
* Writing이 깔끔하지 않고, 실험이 부족하지만 transformer 를 사용한다면 (특히 위치정보가 중요한 경우) 참고할만한 논문이라고 생각.
* Attention/transforemr계열을 누구보다 빠르게 재현하는 lucidrains에서도 rotary PE를 많이 사용하는 것으로 확인.

**Task**: Positional Embedding for Transformers


**Motivation / Contributions**
* Previous positional encodings have limitations
    * abs positional encoding may not generalize
    * Existing methods do not work with efficient transformers
* Favorable properties of newly presented Rotary Positional Embedding:
    * flexibility of being expand to any sequence lengths
    * paper provided for 1D positional encoding (NLP), but can be easily expanded to higher dimensions
    * decaying inter-token dependency with increasing relative distances
    *  capability of equipping the linear self-attention with relative position encoding

**Details & Mathematical derivation**

Previous absolute / relative positional encodings : Refer to main paper
* [Link](https://arxiv.org/pdf/2104.09864.pdf)
* Writing이 깔끔하진 않지만, 수식의 전개와 PE의 흐름을 잘 볼 수 있도록 정리되어있다.

Details & Derivatino of Rotary PE
* [Blog link](https://blog.eleuther.ai/rotary-embeddings/)
* 본 논문보다도 상세히, 그리고 깔끔한 writing으로 정리되어있다.

**Results**
* 논문에서는 중국어 dataset에 대해서만 실험. SoTA compared to Absolute / Relative PE
* 블로그에서 더 다양한 실험을 진행해보는데, 실제로 rotary PE가 우수한 것을 나타냄.
