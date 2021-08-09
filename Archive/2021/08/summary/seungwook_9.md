# IDM: An intermediate Domain Module for Domain Adaptive Re-ID
## Yongxing Dai et al., Peking University|Singapore university of Technology and Design| NUS | Megvii Tech | Penc Cheng Laboratory - ICCV 2021 Oral
#### Summarized by Seungwook Kim
---
**Task**: Unsupervised domain adaptive person re-identification (UDA re-ID)
* Identify person across non-overlapped cameras

**Main Idea**: 
1. Generate appropriate intermediate domains to bridge the source and target domains.
2. Train the source, target, and intermediate domains at the same time
3. Network will adaptively characterize the distribution of source & target domains
    * This smoothly adapt between two extreme domains (source & target)
    * Better transfer the source knowledge to improve model's performance on target domain

**Methods summary**
* Architecture: 일반적인 re-ID setup (혹은 metric learning): Feature extraction backbone (ResNet50)
* IDM Module: 중간에 어디든 낄 수 있지만, ablation상 conv layer 1 다음이 가장 성능이 좋았음
    * Feature -> AvgPool / Maxpool -> concat Avg/Max pool results -> FC layer -> output
    * Repeat for source domain / target domain image
    * Add outputs of source/target domain -> MLP -> predict domain factor for source & target domain
    * OUTPUT: 
        *  Source/Target domain features (IDM 전후로 차이 없음) 
        *  Intermediate domain feature (domain factor * domain feature의 합)

**"Intermediate Domain?"**:
* 논문에서의 정의: located on shortest geodesic path (geodesic이 찾아봐도 정확히 뭔지 모르겠지만 별 의미 없는듯..)
* intermediate domain이 2개의 property를 만족해야 한다고 제안
    1. Distance should be proportional (shortest path위에 있다고 가정하면 당연함)
    * 그렇지 않으면 intermediate domain이 너무 많아질 수 있으며, 오히려 noise로 작용할 수 있음
        * 현재 intermediate domain= sum(domain factor * domain feature)를 사용
        * 한 domain으로 치우치지 않도록 loss를 제안.
        * feature space & prediction space에 각각 적용되는 loss (i.e. feature/prediction space 둘 다 에서 intermediate space를 찾겠다는 의미. smooth adaptation을 위함)
    2. Intermediate domains should be as diverse as possible
    * 2개의 extreme domain (source/target)사이의 intermediate domain이 끊기는 것을 방지하기 위함
        * 단점) 이게 왜 중요한지에 대한 과정이 자세히 서술되어있지 않다. "avoid overfitting to either of the domains" 라고 다른 곳에 나와있지만, 엄청 theoretically sound한 부분은 아닌듯 함. 
        * 다만 intermediate domain이 너무 diverse하지 않게 정의되어있으면 오히려 편협한 knowledge transfer밖에 가능하지 않을 것이라는 생각은 듦.
        * source/target의 domain factor들의 variance가 크도록 loss를 제안. 따라서 다양한 domain factor들 -> 다양한 intermediate domain의 결과로 이어짐.

**전체 Loss:**
1. ReID loss (source/target domain의 feature/prediction space에 적용)
* ReID loss는 a(classification loss) + (1-a)(triplet loss)로, 일반적인 ReID loss이다. 
2. Bridge Loss (intermediate domain의 feature/prediction space에 적용)
3. Diversity Loss (source/target domain에 적용)

> Note: Unsup인데, target domain에 대해 어떻게 ReID loss를 줄 수 있을까?
> 논문에서 강조되지는 않았지만 (supple에 있음), target domain에 pseudo label을 만든다.
> DBSCAN algorithm + clustring으로 pseudolabel 생성.
> 조금 naive해 보이지만 제안된 intermediate domain방법이 꽤나 효과적인 것으롭 보인다.

**Results**:
* SoTA on real --> real UDA re-ID tasks
* SOTA on synthetic --> real UDA re-ID tasks

**총평**:
1. 굉장히 이해하기 어렵게 써있는 느낌이다. 아마 비슷한 domain의 연구를 하는 사람이라면 잘 납득되는 paper일 수 있겠지만, 나로서는 이해하기 어려웠으며, 전반적으로 정보의 배치가 들쑥날쑥하고 writing이 엄청 clear하지 않은 점도 확실히 있었다.
2. "intermediate domain"을 "re-ID"에 적용한 사례는 처음이 맞다.
    * 하지만 geodesic path를 바탕으로 한, "traditional domain adaptation" method는 존재함. 
        * learning-based model에 apply되지 않았었음!
    * 다른 domain을 mix하는 mixup / manifold mixup 은 존재함.
        * 다만 위에서는 model의 generalizability를 위해 random interpolation ratio를 사용
    * **따라서 기존에 존재했던 motivation에, 다른 분야의 idea를 따와서 하나로 합친 후, 실험적으로 간단하면서도 효과적인 framework를 제안했기에 oral paper가 된 것으로 보인다.**
    * learning-based method로 넘어오기 전의 motivation들을 잘 적용한 사례가 accept되는 경우가 많은 것 같다. 옛날 논문들이라도 공부해야 하나...
3. 실험이 굉장히 많다. 대충봐도 20개가 넘는 다른 방법들이랑 비교한듯. Ablation은 딱 필요한 만큼만 있다.
4. 딱히 읽어보라고 추천하지는 않을 논문. 이 정리글을 읽고, 총평의 (2)번에서 얘기하고자 하는 포인트만 얻어가면 좋을 것 같다.
