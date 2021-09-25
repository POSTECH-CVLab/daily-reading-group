# Molecule attention transformer
### Łukasz Maziarka, Tomasz Danel, Sławomir Mucha, Krzysztof Rataj, Jacek Tabor, Stanisław Jastrzębski - NeurIPS workshop 2019
#### Summarized by Jiye Kim

---

**Task** : Representation learning of molecules



**Main Idea** : 
-  General하게 molecule의 feature를 뽑을 수 있는 molecule attention transformer(MAT) model을 제안했다. main contribution은 transformer의 self-attention식에 추가로 inter-atomic distance와 molecular graph structure term을 더해주는 방법을 제안한 것이다.

 

 
**Details** : 

- molecule를 sequence로 표현할 때는 보통 SMILES representation을 사용하는데, 이 논문에서는 위와 같이 augment를 해주기 위해서 각 molecule을 list of atoms으로 표현해서 input으로 넣어주었다고 한다. 각 atom은 26dim의 binary dim으로 표현되서 들어간다.
	
- Transformer의 self-attention 부분을 soft adjacency matrix between the elements of the input sequence라고 해석할 수 있고, 따라서 self-attention 항에 input의 actual structure를 반영해주는, inter-atomic distance, adjacency matrix (both n*n matrix)를 더해주는 것이 자연스럽다고 한다.
	
- self-attention term에 가중치를 다르게 해서 inter-atomic distance와 adjacency matrix를 더해준다.

**Experiment** : 
- pretraining 방법은 기존 논문의 아이디어인 atom을 masking하고 이를 prediction하는 방법으로 진행한다.
	
- Downstream task로는 Freesolv, ESOL, BBBP, Estrogen Alpha, Estrogen Beta, MetStab(high), MetStab(low)를 사용했다.
	
- Baseline으로 deep, shallow model의 성능을 모두 보여주기 위해서 GCN, Random Forest, SVM, EAGCN, Weave를 사용했다. RF, SVM의 input으로 넣어주기 위해서 molecule을 ECFP fingerprint로 numerical하게 바꿔서 넣어준다.
	
- Pretrain을 하지 않고 바로 downstream performance를 쟀을 때, gnn 기반 모델은 대부분의 task에서 좋은 성능을 보여주지 못했고, MAT는 좋은 성능을 보여주었다고 한다. dataset에 따라 fingerprint-based model이 outperform하는 경우가 있었는데 이는 particular structure의 존재가 prediction에 큰 영향을 미치는 경우였다.
	
- Pretrain을 했을 때, 2개의 다른 모델 Pretrained EAGCN, Smiles Transformer와 비교했고, 다른 모델들은 negative transfer를 보여주었지만 MAT는 더 좋은 성능을 보였다.


**총평**:
- self-attention term을 바꿨다는 것을 제외하고는 새로운 것이 거의 없는 논문이다. self-attention term을 바꿨을 때 왜 잘되는지에 대한 설명도 부족해서 아쉬웠다.
