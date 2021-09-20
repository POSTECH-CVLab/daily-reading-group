# ASMR: Learning Attribute-Based Person Search with Adaptive Semantic Margin Regularizer
### Boseung Jeong, Jicheol Park, Suha Kwak - ICCV 2021
#### Summarized by Jiye Kim

---

**Task** : Person search


**Main Idea** : 
- Cross modal embedding을 더 효과적으로 학습하기 위한 새로운 loss를 제안했다. loss는 두 modality를 맞춰주는 modality alignment loss, person categories의 유사성을 고려해주는 ASMR로 구성된다.

**Details** : 
- Task는 person images와 person catergories(text)를 각각 input으로 받고 둘의 joint embedding을 학습해서 embedding space에서 query categories와 가장 가까이 embedding되어있는 image를 retrieval하는 task이다. 이 retrieval의 정확도를 test한다. 원래 person search에서는 query로 image를 넣어주는 경우가 많았는데, 실제 application에서 query image가 없는 경우가 많아 (criminal search같은 경우) text를 query로 넣어주는게 자연스럽다. 하지만, 일반적인 text의 경우 ambiguity of natural language 때문에 query를 해석하는데 어려움이 있어서 query를 카테고리화하여 (male/female, age, ..) binary vector로 넣어준다고 한다.
	
- 위 task의 어려움 점은 cross-modality의 joint embedding을 학습하기 어렵다는 것이다. 이를 해결하기 위해 본 논문은 새로운 loss를 제안하는데, loss는 modality alignment loss와 adaptive semantic margin regularizer(ASMR) 두 term으로 구성된다.
	
- Modality alignment loss는 두 modality를 align하기 위한 term이고, 이미지와 text categories가 각각 separate neural network를 통해 embedding이 계산될 때, positive 이미지-text category끼리는 당겨주고 negative pair끼리는 밀어주는 term이다.
	
- ASMR은 person categories(text) 끼리의 유사도를 계산해서 유사한 것끼리는 당겨주고 먼것끼리는 밀어주는 term이다. ASMR이 필요한 이유는 위의 modality alignment loss는 image와 categories끼리의 연관성만 고려하고, person categories가 얼마나 semantically 유사한지를 고려하지 않고 각각을 separate class라고 생각하기 때문에, 서로 다른 category가 overly close하게 embedding되는 문제가 발생하기 때문이다.



**Experiment** :
- 3개의 dataset에 대해 sota를 기록했고, ASMR을 사용한 전 후 embedding이 어떻게 바뀌는지 qualitative하게 보여줌으로서 효과를 보여줬다.

**총평**:
- writing이 이해하기 쉽게 잘 써있고, 두 개의 loss term이 필요한 이유도 잘 쓰여있는 것 같다. 간단한 구조로 좋은 성능을 낸 논문인 것 같다.
