# Using rule-based labels for weak supervised learning: A chemnet for transferable chemical property prediction
### Garrett B. Goh, Charles Siegel, Abhinav Vishnu, Nathan O. Hodas - KDD 2018
#### Summarized by Jiye Kim

---

**Task** : Transfer learning, representation learning on molecules



**Main Idea** : 
- Chemistry에서는 data가 일반적으로 작고, sparsely labelled 되어있는 경우가 많다. chemistry domain에서 사용되는 feature extracting method를 사용하여 molecular descriptors를 뽑아내고, 이를 pseudo-label로 사용하는 weak-supervised 방법을 제안했다. 

**Details** : 
- RDkit으로 100여개의 2D descriptors that includes basic computable properties (e.g. MW,logP, etc)를 뽑아내어 이를 pseudo-label로 하여 model를 pretrain을 위한 label로 사용.
- 3개의 datasets - Tox21, HIV, Freesolv dataset에 대한 downstream performance를 계산함으로서 위의 방법이 얼마나 효과가 있는지 보였다. 기존 모델과 비교했을 때, 3개의 데이터셋 모두에서 chemnet의 방법이 효과가 있음을 보였다. 3개의 dataset은 pretrained dataset의 label과 겹치지 않기 때문에, Chemnet이 general한 chemistry-relevant feature를 학습할 수 있다고 한다.
- 위의 학습 방법이 network-agnostic한 것을 보이기 위해서, 기존 CNN-based model Chemception, RNN-based model Smiles2Vec 두가지를 사용해서 두가지 경우 모두 성능이 증가했음을 보였다.
- 다른 SOTA DNN model과 비교했을 때도 가장 좋은 성능을 내는 것을 보였다.



**총평**:
- 굉장히 간단한 방법이지만, label이 부족한 chemistry domain에서는 매우 도움이 될 수 있는 방법이라고 생각한다.
