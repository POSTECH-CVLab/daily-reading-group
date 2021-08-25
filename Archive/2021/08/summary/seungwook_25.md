# FastFormer: Additive Attention is All you need
### Chuhan Wu et al., MSRA - Arxiv 2021 
#### Summarized by Seungwook Kim
---

**총평**:
* Efficient Transformer 중 원형의 Transformer 구조를 최대한 많이 살린 느낌. Operator들이 많이 편했지만 (Dot product->Addition), context를 학습하고 적용하는 구조가 잘 유지됨.
* 다른 sparse transformer + vanilla transformer와의 성능 비교가 꽤나 디테일하게 되어있는데, 그 중에서 가장 우수한 성능을 보이는 것으로 보임.
* 다양한 efficient transformer (MLP mixer 등 포함) 논문을 읽어봤는데, 그 중 이해하기도 편하고 크게 거부감도 들지 않는 편.  
* 한번 현재 진행중인 연구에 적용해볼 생각입니다. 마침 Lucidrains github에서 구현을 이미 해뒀네요...빠르네 ([Link](https://github.com/lucidrains/fast-transformer-pytorch))
* residual connection이 Query vector 에서부터 이어진다 (Input vector가 아닌). 왜지?
---


**Task**: Efficient Transformer
* Most of the interactions are switched to **addition-based & element-wise product** from dot-product

**Novelties & Contributions**:
* Best efficiency in transformer-based architectures ($O(N \cdot d)$ )
* Much more efficient than many Transformer Models and can achieve competitive performance 
   * More SoTA when sequence length is longer

**Method**
1. Input -> Q, K, V 
   * Same as any other transformer
   * Weight sharing for Q & K 
2. Q (vector) -> q (scalar)
   * q = $\sum_i \alpha_i Q_i$
   * $\alpha$ is an attention weight computed using a softmax-like operation 
   * "global query vector"
3. K (vector) -> P (vector)
   * $p_i = q \times K_i$
   * element-wise product to model relations between two vectors (Q and V)
   * "Global context-aware key matrix"
4. P (vector) -> k (scalar)
   * k = $\sum_i \beta_i P_i$
   * $\beta$ is an attention weight computed using a softmax-like operation 
   * "Global key vector" 
5. V (value matrix) -> U (key-value interaction result!)
   * $U_i = k \times V_i$
6. Output = FC(U) + Q
   * 왜 + Input 이 아닌 + Q인지 잘 모르겠음
   * 기존 transformer architecture를 다시 확인해봐도 + input임

**vs. other methods**
* Longformer: Sparse attention, combines sliding window attention and global attention
* BigBird: extension of LongFormer, incorporates sparse random attention
* Linformer: low-dimensional key/value matrices to compute approx. self-attention
* Linear Transformer: use kernel functions to approximate self-attention mechanisms
* Poolingformer: sliding window self attention + pooling self attention for both short and long range context

**Result**
* 전반적으로 SoTA/comparable
* 다른 efficient trasnformer들에 비해 유의미하게 좋은듯
* **Interesting**: Layer-wise sharing (모든 layer들이 같은 param) + Q/K sharing이 더 좋은 성능을 보임
  * Avoid overfitting + less parameter usage
  * 이 또한 개인 연구에 적용해볼 예정
