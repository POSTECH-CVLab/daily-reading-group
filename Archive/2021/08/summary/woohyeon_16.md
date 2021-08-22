# Diverse Image Generation via Self-Conditioned GANs
### Steven Liu et al., MIT CSAIL - CVPR 2020
### Summarized by Woohyeon Shim

**Task:** clustering-based self-conditional image synthesis

**Clustering the dataset with discriminator features**
* use the k-means++ algorithm.
* initial clustering and re-clustering based on the last hidden layer of discriminator.
* online k-means clustering can be done at each iteration based on gradient descent, but performs worse on real image datasets.
	
**Conditional GAN training w.r.t cluster labels**
* class-conditional generator G(z,c)
	* use DCGAN architecture for MNIST and CIFAR10; add conditioning by a fully connected layer before the input layer of the generator.
	* use conditional architecture proposed in Mescheder et al. for Place365 and ImageNet datasets.
* class-conditional discriminator D(x,c)
	* conditioning is done like the multi-task discriminator.
	* the output logits amount to the number of clusters (k).
	* vanilla GAN loss is applied for each cluster(class) without interaction between them
	* the loss is weighted for each cluster proportional to its true size in the training set. (does not need to generate clusters with no elements, thus is scalable with the number of clusters)
		
**Experiments**
* (-) not SOTA, but shows improvement from the baseline.
* (-) no ablation on the number of clusters on real datasets
* (-) the model is highly sensitive to clustering techniques (FID variation: 9.76 → 19.85 without cluster initialization step, 9.76 → 20.42 without cluster rematching)
* (+) qualitatively shows the highest-scoring images from the pre-trained classifier as an evidence of synthesizing high-quality and diverse images.
* (+) perform gan inversion with additional encoder to visualize the omissions of modes from the generator by reconstruction of training set images, and measure LPIPS similarity score between their reconstruction and 50,000 gt images. ⇒ can reconstruct distinctive features that are not present in baseline model!
	
**총평:** 데이터 분포를 clustering으로 분리시킴으로써 각각의 cluster마다 생성문제를 풀게하여 다양성을 높인 논문. 제안한 방법이 단순하고 성능향상은 보장된다는 강점은 있지만, clustering을 할 수 있는 한계가 있으므로 scalability가 떨어진다는 점과, 학습 중간에 kmeans를 다시 돌려야하는 부담이 따른다는 것, 그리고 그것을 어떻게 돌리는지에 따라 성능이 크게 변하는 단점이 있었음. 이러한 단점은 있지만 핵심 아이디어인 '생성 모델에 clustering이 필요하다'는 것을 보이기 위해 다양한 검증(classification, reconstruction)은 아주 좋게 평가하고 싶음.
