# Deep clustering for unsupervised learning of visual features (DeepCluster)
### Mathilde Caron, Piotr Bojanowski, Armand Joulin, Matthijs Douze - ECCV 2018 
#### Summarized by Jiye Kim

---

**Task** : Unsupervised representation learning



**Main Idea** : 처음에 train이 되지 않은 convnet을 통해 feature representation을 뽑고 이를 사용하여 clustering을 진행한 후 clustering assignment를 pseudo-label로 하여 학습을 진행. 이 두 과정을 iterative하게 반복하여 convnet이 더 좋은 feature를 뽑게 한 방법.
 


**Motivation** : 

-학습이 되지 않은 convent으로 image의 feature를 뽑아내어 성능을 평가했을 때, chance level보다 훨씬 좋은 성능을 내는 것을 밝혀냈다. (이유: convolutional structure gives a strong prior on the input signal).
 
 

**Method** :

-학습이 되지 않은 CNN으로 deep features를 뽑아내고 이를 k-means clustering(다른 것도 상관없음)을 통해 clustering을 수행함. 이 clustering assignment를 pseudo-label로 하여 classification task를 수행하여 CNN Parameter를 학습. 이 학습된 CNN을 바탕으로 다시 deep features를 뽑고 clustering을 수행하고, pseudo-label로 classification task를 하여 학습하는 일련의 과정을 반복.
-Trivial solution을 막는 방법:


	
	
1) Optimal solution 중의 하나가 모든 인풋을 하나의 cluster로 assign하는 것이다. 이를 막기 위해, empty cluster가 생기면 기존에 있는 non-empty cluster centroids에 small perturbation을 가하여 생긴 새로운 centroid를 empty cluster의 centroid로 해준다.
	
	
	
2) 예를 들어, 대부분의 image들이 하나의 cluster에 assign이 되었다고 하면, convnet은 인풋에 상관없이 같은 값을 내보낼 것이다. 이를 막기 위한 방법으로, loss function에 inverse of the size of its assigned cluster를 곱해줌으로써 input의 contribution을 다르게 해주는 방법이 있다.
	






**Experiment**:

-assignments A, B간의 normalized mutual information(NMI)을 측정해서 assignments간의 연관성을 확인


	
	
1) relation between clusters and labels: convnet이 뽑아내는 clustering assignments와 imagenet labels의 NMI를 epoch마다 계산해보니 NMI가 계속 증가. clusters과 label의 dependence가 증가한다는 뜻이고 cluster assignments가 object class의 정보를 잘 캡처한다는 것을 알 수 있음.
	
	
	
2) Number of reassignments between epochs: epoch t-1, epoch t 시점의 cluster assignments에 대해 NMI를 계산한 결과 꾸준히 증가함. 두 시점의 cluster assignments간의 dependence가 증가한다는 뜻이고 training stability를 보여줌.
	


-Alexnet으로 학습을 시켰는데, alexnet의 conv1~conv5까지 각각의 layer의 representation quality를 평가하기 위해서 각 layer에 linear classifier를 붙여 학습하고 성능을 기록함. unsupervised model들은 마지막 layer(conv5)보다 그 전 층 (conv3-4)에서 성능이 더 좋은 것을 확인. 왜냐하면 마지막 층으로 갈 수록 task specific 한 representation을 뽑아내기 때문.

-여러 downstream task (classification, detection, segmentation)을 수행했을때, unsupervised method중에서 sota를 기록함.

-deep clustering 방법이 balanced object categories에 잘 동작하도록 디자인 되었기 때문에, well-balanced class label을 가지고 있는 Imagenet으로 학습할 때 unfair advantage를 얻을 수 있다는 점을 지적하며, random Flickr images로도 unsupervised training을 진행해봄. 3-5%정도의 성능 감소는 있었지만 여전히 다른 모델과 비교했을 때 sota였다.
 


 

**총평**:
-간단한 방법으로 좋은 성능을 낸 논문.

-SwAV의 전 논문이라 읽어보았다.
