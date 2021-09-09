# Sparse-MLP: A Fully-MLP Architecture with Conditional Computation
### Yuxuan Lou et al., NUS - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**:
* MLP-Mixer + Mixture of Experts를 시도한 논문. 이 외에 새로운 architecture/formulation에서 오는 novelty는 없어 보이며, 'novel combination of existing work'에 해당되는 논문으로 보임.
* 기존에 Mixture of Experts가 제안되었을 때 얻는 것으로 알려진 이점 (Large parameter scaling, negligible compute increase) 에 따른 성능 향상 외에는 크게 눈에 띄는 부분은 없음.
* MLP-Mixer와 Mixture of Experts 논문을 읽었다면 굳이 안 읽어도 될 논문이지만, 그렇지 않았다면 저 두 논문에 대해 한 번에 이해할 수 있는 논문이지만, 연구적으로 추천하는 논문은 아님. 
* Mixture of Experts를 사용하는 건데, **Sparse**-MLP 라고 부르는 건 조금 misleading할 수 있다고 생각
---


**Task**: MLP Architecture with Mixture of Experts (MoE)
* evaluated on classification tasks

**Novelties & Contributions**:
* Scales MLP-Mixer model with sparse MoE layers
  * (I think it's called sparse because) not all "Experts" are used for each input

> **What is MoE?**: involves decomposing predictive modeling tasks into sub-tasks, training an expert model on each, developing a gating model that learns which expert to trust based on the input to be predicted, and combines the predictions.

* Re-representation layer
  * Simple **Linear projection layers** (FC layers) for "balanced computational cost" 
    * MLP-Mixer attends spatial-wise and channel-wise in sequence
    * usually, channel-wise dim >> spatial-wise dim

**Method** \
* MLP-Mixer baseline
  * Replace certain MLP-Mixer blocks with proposed block.

Proposed block:
1. Re-represent layer 1
   * CxS -> C1 x S1 (C1 = C/2, S1 = 2S)
2. Token-mixing (spatial-wise) MoE
   * Equal to token mixing in MLP-Mixer, but MoE

3. Channel-mixing (channel-wise) MoE
   * Equal to channel mixing in MLP-Mixer, but MoE
   
4. Re-represent layer 2
   * S1 x C1 = S x C

MoE specifications (with choices from ablation tests)
* again, MoE: training multiple different versions of same architecture, and choosing up to K (hyperparameter) versions at test-time for inference
* each different version becomes an "expert" for different input data
* 4/8/16 experts depending on architecture size
* K= 1 or 2 (if K > 1, weighted sum of results from different experts)

Not all MLP-Mixer blocks are replaced, but the last few
* Replacing First N blocks resulted in worse results
* Replacing Last N blocks (N = 2, 4) gave best results

**Result**
* MoCov3 pretraining, finetuned on ImageNet/Cifar10/Cifar100
* Outperforms MLP-Mixer baseline on all datasets
