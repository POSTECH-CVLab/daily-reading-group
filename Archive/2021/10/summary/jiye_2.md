# A Simple Unified Framework for detecting out-of-distribution samples and adversarial attacks
### Kimin Lee, Kibok Lee, Honglak Lee, Jinwoo Shin - NIPS 2018
#### Summarized by Jiye Kim

---

### **Task** : 
Abnormal detection


### **Main Idea** : 
-  Abnormal detection을 하기 위해 generative classifier기반으로 feature space에서 mahalanbis distance를 사용하여 abnormal detection을 하는 방법을 제안했다.


### **Summary** :  
out-of-distribution, adversarial sample을 detect하기위한 방법론을 제시했다. 기본적으로 classification 문제에 OOD, adversarial sample이 들어왔을 때 softmax classifier는 어느 클래스에도 해당되지 않는 균등한 output을 내보내야하는데, 특정 class를 예측하도록 학습시켰기 때문에 다른 이미지가 들어와도 confident하게 특정 class로 예측하는 문제가 발생한다. 이를 해결하기 위해 OOD 문제는 OOD detection과 classification으로 나뉘는데, OOD sample일 경우 detect하고 OOD sample이 아닐 경우 classification을 수행하도록 한다. 기존에는 softmax output에 threshold를 넣어서 max값이 threshold를 넘지 않으면 OOD sample로 간주하는 등의 discriminative classifer에 기반한 방법이 있었는데, 이 논문은 image의 class 별 embedding이 gaussian distribution(class-conditional gaussian distribution)을 따른다는 가정에서 시작해서 feature space에서 abnormal sample을 detect하는 방법을 제안했다(generative classifier에 기반한 방법). 구체적으로, 한 sample의 embedding을 계산하고 이 embedding과 다른 class-conditional gaussian distribution사이의 Mahalanobis distance를 계산하여, closest class와의 거리가 특정 threshold를 넘으면 abnormal sample로 간주하는 방법이다.

기존 방법과 비교해서 장점은 softmax output으로 abnormal detection을 하는 것보다 feature space에서 abnormal sample이 better characterized 된다고 하는데, 이유는 softmax output 은 decision boundary만 학습하기 때문에 decision boundary에 엄청 떨어져있는 sample도 쉽게 high confident sample이 되기 때문이다.

추가적인 contribution은 다음과 같다.

- 일반적으로 generative classifier의 classification accuracy가 softmax classification accuracy보다 떨어진다고 알려졌었는데, 위의 mahalanobis distance 기반 generative classifier는 여러 classification task에서 softmax 를 따라잡았다.
- 기존 연구에 있는 input calibration techinique을 사용했다.
- OOD detection performance가 마지막 feature가 아닌 그 전 feature를 사용했을 때 더 좋다는 것을 실험적으로 확인하고, 여러 layer feature를 합쳐서 사용하는 feature emsemble 방법을 사용했다.
- class incremental learning 방법도 제안했다.



### **총평**:
- writing이 잘되어있고 motivation이 좋은 논문인 것 같다. gaussian discriminant analysis를 통해 class conditional image들의 embedding이 gaussian distribution을 따른다는 점도 읽어볼만 한 것 같다.
