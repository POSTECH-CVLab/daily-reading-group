# A Closer Look at Memorization in Deep Networks
### Devansh Arpit, Yoshua Bengio et al., - ICML 2017
#### Summarized by Seungwook Kim
---

**Task**: Analysis on deep learning \
--> Examine the role of memorization in deep learning \
--> Differences in gradient-based optimization on noise vs real data
 
**Motivation:** \
Traditional view: A model with sufficient capacity will be able to 'memorize' each example, overfitting the training set and yielding poor generalization to the validation set. \
BUT: Models achieve excellent generalization performance with massively over-parametrized models. 
 
-----> "Investigate the intuitive notion of memorization by training DNNs to fit real&random data"
 
**Summary of findings:** \
-> There are qualitative differences in DNN  optimization behaviour on real vs noise => DNNs do not just memorize real data. \
-> DNNs learn simple patterns first, before memorizing \
-> Regularizations can hinder memorization in DNNs while preserving their ability to learn about real data.
 
**Experiments & Findings:**


	
* Expressiveness of DNNs grows **exponentially** with depth (from prev work)
	
* For 100 differently initialized models, many real data are consistently classified (in)correctly after a single epoch.
	* Different examples are significantly easier/harder
	* Noise data are fit more independently (much lower consistency in correct/incorrect classification)
	
* Check loss-sensitivity (gradient of loss w.r.t train data)
	* Real data: only a subset of training set has high loss sensitivity
	* Random data: loss sensitivity is high for all examples
		* When training on real data, the neural network probably does not memorize.
	
* Optimal validation performance requires higher capacity model **in presence of noise examples**
	
* No relationship between model capacity and val performance in noise datasets.
	* 원래 capacity를 restrict해서 가장 중요한 pattern만을 학습함으로서 generalization 성능을 높여야한다고 생각했음.
	* 그러나 Higher capacity가 있다면 real data 학습을 방해하지 않는 선에서 noise example까지 fit할 수 있음을 보임.
	* 결국 noise 가 없이 전부 다 clean, real data만 있다면 lower capacity model이 가장 좋을 것.
	
* Reducing capacity/Increasing size of dataset slows down training for real/noise data.
	
* Increasing number of hidden units (capacity) decreases number of training iterations to fit the data (up to some limit)
	
* Increasing number of data also increases the time needed to memorize the training set.
	
* Time to convergence is longer on noise data
	* Networks are learning to **extract patterns in the data, rather than memorizing.**

Building on the intuitions that : **Number of different decision regions** into which an input space is partitioned reflects the **complexity of the learned hypothesis**


	
* Critical sample (there exists at least one adversarial example in neighborhood)이 많을수록 complex한 hypothesis를 학습했다는 뜻
	
* Models trained on noise data: Much higher number of critical samples
	* Training on noise data leads to much more complex hypothesis (당연한 결론)
	
* Critical Sample ratio increases gradually with epochs and then stabilizes
	* 모델이 서서히 더 complex한 hypothesis를 학습한다는 것을 의미함
	* "Model first learns the simple and general patterns of real data before fitting the noise"
	* Noise를 설명하기 위해서 모델이 복잡해지는 것

Regularization이 학습에 끼치는 영향


	
* Regularizer를 사용하면 모델의 real data 학습 능력을 저하시키지 않으면서 noise를 memorize하는 효과를 방해할 수 있음!
	* Adversarial training + dropout이 가장 효과적
	
* 따라서 regularization을 쓰면 noise를 어느정도 알아서 처리해주는 효과를 얻게 되는 것 (성능 하락 없이)
	 

**총평:** \
Cite가 600번 이상 된 유명한 논문입니다. \
간단한 실험들로 구성되어 있지만, 그 결론들과 discussion들이 전반적으로 딥러닝과 모델들에 대한 직관에 크게 도움이 되는 것 같아서 재미있게 읽었습니다. 실제로 도움이 되는 경우도 많을 것 같습니다 (언제 큰 모델이 좋은지, 언제 작은 모델이 좋은지, noise가 있을 때 어떻게 하는게 좋을지 등...) \
앞으로 이 논문을 cite한 논문들을 천천히 따라가면서, 딥러닝에 대한 직관을 키우기 위해 주기적으로 이런 논문들을 읽을 예정입니다.