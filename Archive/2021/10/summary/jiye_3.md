# Improved precision and recall metric for assessing generative models
### Tuomas Kynkäänniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, Timo Aila - NeurIPS 2019
#### Summarized by Jiye Kim

---

### **Task** : 
Evaluation metric for image generation model



### **Main Idea** : 
-  Image generative model을 평가하기 위한 improved precision and recall metric을 제안했다.





### **Summary** :  
기존 precision & recall metric이 가지고 있는 문제점으로 relative probability densities of the two distributions을 계산하기 때문에 여러 문제가 발생한다고 언급하는데 이부분은 잘 이해하지 못했다.

논문에서 Precision은 real image manifold에 들어가는 generated image의 비율, recall은 generated image manifold에 들어가는 real image의 비율로 정의했다. manifold는 image embedding을 기준으로 k-nn 을 수행하여 만들어지는 hypersphere들의 합으로 정의된다.




### **Experiment** :
1. StyleGAN과 BigGAN에 truncation trick을 사용하여 예상과 맞게 동작하는지 확인했다.

- Truncation trick을 통해 생성된 이미지가 diverse하지만 less realistic해질수록 논문의 improved p&r은 precision은 낮아지고 recall은 높아지는 것을 확인했다. 기존p&r은 이를 잡아내지 못하는 것을 확인했다. FID는 realistic 한 이미지보다 diverse한 이미지에 더 낮은 값(낮을수록 좋음)을 내보내고, realistic과 diverse의 tradeoff 를 구별하지 못하는 것을 확인했다.
2. StyleGAN의 configuration을 바꿔가면서 각 모듈을 뺏을 때 예상과 맞게 precision recall이 바뀌는지 확인했다.

Realism score:

논문에서는 realism score라는 것도 제안했는데 continuous 한 값으로, 생성된 image가 real manifold에 가까워질 수록 큰 값을 멀어질수록 작은 값을 주는 스코어이다.
여기서 trick이 하나 들어가는데, realism score의 경우 precision & recall과 다르게 하나의 샘플에 대해 계산되는 값이기 때문에 error 에 취약하다. 예를 들어 real sample이 sparse한 곳에는 knn hypersphere가 크게 생기게 될텐데 이런 manifold에 generated sample이 들어가게 되면 inaccurate score를 야기할 수 있다. 따라서 real sample중 hypersphere 의 radius가 median보다 작은 것만 남기고 나머지는 disregard한 후 realism score를 측정한다고 한다.
Experiment: interpolation을 통해 생성된 이미지를 visually inspect한 후 realism score와 일치하는지 확인했다.

### **총평**:
- 적절한 실험 설계를 통해 제안한 metric의 우수성을 잘 보인 논문인 것 같다.
