# Speaker sensitive response evaluation model
### JinYeong Bak, Alice Oh (KAIST) - ACL 2020
#### Summarized by Jiye Kim

---

### **Task** : 
Evaluation method of dialogue response generation



### **Summary** : 
-  Open-domain dialogue response generation을 평가하기 위한 방법을 제안했다. 기존의 evaluation 방법들은 generated responses들을 ground truth와 비교해서 appropriate response였음에도 불구하고 inappropriate으로 평가하는 경우가 많았다. 이를 위해서 conversational context와 similarity를 고려하여 평가하는 방법을 사용했고, 이러한 방법은 기존 연구에 있었지만 이 논문의 주요 contribution은 학습할 때 twitter에서 추출한 speaker sensitive response를 사용하여 hard negative examples들을 고려하여 학습을 진행했다는 것이다. Twitter conversation corpus에서 학습을 했지만 다른 dataset으로 옮겨도 잘 되는 것을 확인했다.
 

 
### **기존 method** : 

- BLEU, ROUGE: based on overlap of word between the two responses → cannot identify synonyms, ground truth와 벗어나는 response는 inappropriate하다고 판단함.

- Liu et al: evaluation metric based on the distributed word representation → shows low correlation with human judgements, embedding based method이지만 여전히 gt와의 similarity를 보기 때문에 gt와 다른 response에 대해서는 inappropriate하다고 평가함.

- ADEM, RUBER: compute the similarity between a context and a generated response.
	
  - ADEM - require human-annotated scores to train and thus cannot be applied to new datasets and domains.(use pretrained VHRED to encode the texts and compute the score by mixing similarities among the context, generated response and ground truth)
	
  - RUBER - overcome ADEM's limitation by using "random response" as negative sample, but random sample cannot provide sufficient information about appropriate and inappropriate responses.


기존 method와 비교하여 이 논문에서 제안한 Speaker sensitive response evaluation model(SSREM)은 RUBER와 유사하지만, random response를 negative로 사용하는 RUBER와 달리 SSREM은 twitter에서 추출한 response들의 similarity의 정도를 고려하여 hard negative response를 추출하여 학습에 사용했다는 것이 차이점이다.


### **Method** :  Speaker sensitive response evaluation model (SSREM)
1. Motivation

- 4 type의 response를 정의했다. 1) Random, 2) Same speaker, 3) Same partner, 4) Same conversation

- 4번으로 갈수록 utterance(말)들의 similarity가 높을 것이라고 판단하고 실제로 그렇다는 것을 실험을 통해 보였다.

 
2. Model

- c: context, r_hat: generated response, r: ground truth response

- SSREM(c,r,r_hat) = h(f(c,r_hat), g(r_hat, r)) 으로 정의됨.

  - f: measure the similarity between c and r_hat → contain parameters to train

  - g: meausre the similarity between r_hat and r → use sentence mover's similarity

  - h: mix the values of f and g

→ 따라서 gt와 r_hat의 similarity, context와 r_hat의 similarity 둘다 고려해줌

 
3. Training

- To train the f, define a classification problem to identify gt r from a set of candidate responses R_cand. R_cand는 gt r와 위에서 정의된 4가지 타입의 response를 포함한다. 4가지 타입 response들은 negative sample 역할을 한다.

### **Experiment**:
- the evaluation score shows high correlation with human scores
	
- outperform other metrics in terms of identifying the ground truth responses given a context
	
- can be applied to evaluate a new corpus in a different domain

### **총평**:
- Text generation evaluation 방법을 제안했다. 단순히 gt와의 유사도 비교가 의미가 없는 상황에서 어떻게 generation 평가를 하면 좋을지에 대해 생각해볼 수 있는 논문이다. 논문에서는 conversational context와 비교하는 방법을 사용했다. 궁금한 점은 f를 위와같이 classification problem을 디자인해서 학습하면 r_hat과 context의 유사도가 어떻게 학습이 되는 것인지 궁금하다.
