# On the evaluation of conditional generation (FJD)


### Terrance DeVries, Adriana Romero, Luis Pineda, Graham W. Taylor, Michal Drozdzal (Facebook) - submitted to ICLR 2020
#### Summarized by Jiye Kim

---

### **Task** : 
Evaluation metric for conditional image generation




### **Main Idea** : 
-  기존의 FID는 real images와 generated images의 distribution 차이를 비교하는 방법인데 condition에 맞춰서 image를 생성했는지 비교하지 못하기 때문에 image quality와 conditioning 정보를 같이 고려하는 Frechet joint distance를 제안했다. 단순하게, image embedding과 condition embedding을 concatenation하여 Frechet distance 를 재는 방법이다.


### **Method** :  
- Embedding function f를 통해 image embedding을 구하고, condition embedding function h를 통해 condition embedding을 구한다. condition modality는 여러가지가 있는데, class/ attribute labels 같은 경우 one-hot encoding을 captions/dialogue 같은 경우는 sentence-bert를 이용하는 것을 제안했다. 이렇게 구해진 image embedding과 condition embedding 을 concatentation하여 frechet distance를 구한다.
 
### **Experiment** :
conditional image generation에서 중요한 세가지 요소 image quality, conditional consistency, intra-conditioning diversity에 대해서 synthetic dataset인 dSprite-textures에 대해 실험을 진행했다.

Conditioning은 class label, bounding box, mask label 이 3가지에 대해서 진행했다.



1. image quality

- real dataset을 reference로 두고 gaussian noise를 점점 늘려가면서 주면서 FJD를 계산. FID와 같은 trend를 보임. → image quality를 잘 반영한다고 주장.



2. sensitivity to Conditional consistency

- 이미지의 여러가지 attribute 중에 하나만 바꾸면서 FID, FJD가 어떻게 바뀌는지 확인. 예를 들어서, 다른 attribute는 고정시키고 이미지의 x position만 바꿨을 때 FID, FJD with class conditioning은 constant를 유지함. 하지만 FJD with bbox, FJD with mask conditioning은 X position offset이 증가할 수록 증가함. BBOX conditioning, mask conditioning 모두 x position에 sensitive하기 때문.



3. sensitivity to Intra-conditioining diversity

- Intra conditioning diversity가 감소할 때 FJD가 증가하는 것을 보였다.



그 외에도 여러 생성모델에 대해 FJD를 평가하고 이 수치를 FID, accuracy, diversity 등 다른 metric과 비교해서 분석했다.


### **Review에서 지적된 단점** :
- FID와 FJD가 여러 생성모델에 대해 같은 Ranking을 보이는데, FID 대신 FJD를 써야하는 이유를 제대로 입증하지 못했다.
- FJD가 FID 보다 더 stable 한 metric이라고 논문에서 주장하고 있는데, FJD가 단순히 condition embedding을 concat함으로서 dimensionality가 커져서 절대적인 수치가 커져서 stable한 것이 아닌지 지적됐다.
- Real dataset이 아닌 synthetic dataset에 대해서만 실험을 진행했다.
- Novelty 부족
- condition을 embedding하는 방법, condition과 image embedding을 합치는 방법에 여러 design choice가 있는데 다른 여러 design choice외에 concatentation을 한 이유가 무엇인지 설명이 없었다.

### **총평**:
- Motivation은 좋지만 FJD를 써야하는 이유에 대한 입증을 충분히 하지 못한것 같다. 리뷰에서 지적된 대로 FID와 모든 모델에서 같은 ranking을 보이는데, FID가 condition을 고려하지 못하여 falsely model을 ranking할 때 FJD는 correctly ranking한다는 예시를 하나라도 보였어야 되는 것 같다. Synthetic dataset으로 진행한 실험도 당연한 결과를 실험적으로 보인것 같았다.
