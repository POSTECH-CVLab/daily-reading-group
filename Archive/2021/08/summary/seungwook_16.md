# How to avoid machine learning pitfalls: A guide for academic researchers
## Michael A. Lones, Heriott-Watt University (Associate Professor) - Arxiv
#### Summarized by Seungwook Kim
---

개요: ML 테크닉을 사용할 때 발생할 수 있는 실수와, 이를 피할 수 있는 방법
* 연구를 하는 학생들을 위함
* Academic research에서 중요한 issue 위주
* ML의 5가지 과정을 커버함
1. What to do before modeling
2. How to reliably build models
3. How to robustly evaluate models
4. How to compare models fairly
5. How to report results

(시간이 지남에 따라서 업데이트 될 수도 있다고 함)

## 1. Before you start to build models
#### Do take the time to understand your data
* 데이터가 reliable source에서 오는 게 / reliable한 method로 만들어진 게 / 좋은 퀄리티인 게 좋음
* 데이터를 사용하기 전에 위 사항들을 확인하고, 저자들이 데이터의 한계를 서술했는지 확인
* 데이터가 여러 논문에서 쓰였다고 해서 좋지 않을 수 있음 (실제로 많은 데이터셋에 문제가 많음)
    * 이미지넷도 사실 multi-label classification 라벨들이 있는 게 더 좋다는 최근 평이 있음
    * PF-PASCAL evaluation에서도, test set에 train/valid set과의 overlap이 있음.
* Exploratory Data Analysis (EDA)등을 통해 데이터를 확인
* Missing/inconsistent 한 기록들이 있는지 확인 

> 실제 논문작성 때 도움이 될지는 모르겠지만, 데이터를 새로 구성하거나 / 저널 extension을 할 때 유용해보임

#### Don't look at all your data
* 데이터를 보다보면 modeling에 도움이 되는 pattern/insight를 얻을 수 있음
* 하지만 test set의 데이터를 보고 가정을 만들기 시작하면, 결국 전반적으로 generalize가 안 되는 모델에 그칠 수 있음

#### Do make sure you have enough data
* Data가 부족하면 generalize가 잘 되는 모델을 얻기 어려움
* 데이터가 부족하면 cross validation/augmentation으로 더 잘 활용할 수는 있음
* Data가 부족하면 모델의 complexity도 그에 맞게 제한하는 것이 좋을 것
    * 개인적 논문견해) Noise가 없는 clean데이터일시에는 더욱 더 그럼
* 이런 이슈가 있는지 없는지를 **미리 파악하고 어떻게 해결할지 고민해두는 것이 좋음**
    * PF-PASCAL과 SPair-71k 에서 semantic matching을 할 때, 최근까지 augmentation을 하지 않다가 augmentation을 해주니 성능이 많이 오르는 것을 알 수 있었음.
    * 당연한 결론이고, 연구적인 contribution은 아니지만, 더 좋은 모델을 구축했다는 것 또한 사실인듯

#### Do survey the literature
* 무엇이 이전이 시도되었고 시도되지 않았는지 파악하는 게 중요함
* 누군가 이미 비슷한 아이디어를 시도해보았을 수는 있지만, 웬만하면 더 연구해볼만한 가치가 있는 부분들은 남겨져있을 것임 (plenty of avenues of investigation still open)
    * 따라서 오히려 비슷한 아이디어의 이전 연구가 새로운 연구의 justification으로 사용되기 좋음
* 이 부분을 늦게 한다면 왜 이미 진행된 연구를 하는지 / 이미 확인된 사실을 바탕으로 연구를 진행하지 않는지에 대한 설명이 요구될 수 있음

#### Do think about how your model will be deployed
* 많은 연구들은 실제 상황을 딱히 고려하지 않는 경우가 많음
    * 모델 자체를 build & analyse하는 과정이 중요할 수 있으니 그럴 수 있음
* 하지만 결국 deploy될 environment를 고려하여 모델을 구축하는 것이 좋음
    * 실제로 많은 논문들이 이런 부분을 지적하는 것으로 보임
    * 주로 속도/메모리 constraint를 deploy환경에 맞게 제안하는 것이 좋음
    * 제안되지 않은 분야가 있다면 이를 제안하고, 이에 맞는 첫 아키텍쳐를 보이는 것 자체가 contribution일 수 있음
* MLOps가 풀고자 하는 부분 중 하나

## 2. How to reliably build models
#### Don't allow test data to leak into the training process
* mean/variance를 사용할 때도 train data내에서만 사용할 것
* (tabular data의 경우) data partitioning 전에 feature selection은 하지 말 것
    * 위에서 언급했듯 PF-Pascal evaluation에 있던 문제
#### Do try out a range of different models
* **There's no such thing as a single best ML model**
* 풀고자 하는 문제에 가장 적합한 ML model을 찾는 것이 중요함
* 가끔 다른 related work를 참고하면 a priori가 있을 수 있음
* 결론적으로 다양한 모델을 사용해보는 것이 좋다는 뜻
    * CNN vs Transformer
    * LSTM vs GRU 등의 의미
    * 어떻게 optimize/use하냐에 따라 task마다 best model이 다를 수 있음

#### Don't use inappropriate models
* 예) Categorical feature를 예상하는 model을 numerical feature에 사용
* 예) variable사이의 dependency를 고려하지 않는 모델을 time-series에 사용
* 예) Unncessarily complex models 
* 이런 잘못된 사용은 reviewer들에게 부정적인 인식을 줄 수 있음
* "Don't use recency as a justification for choosing a model"
    * 최근에 나왔다는 것을 motivation으로 삼지 말라는 말
        * transformer 사용 자체가 motivation이 되는 것은 별로라는 말인듯 (공감)
#### Do optimise your model’s hyperparameters
* Hyperparameter는 data에 알맞게 설정해야 모델의 최대 성능을 끌어낼 수 있음
* 이것저것 막 시도해보는 방법보다 hyperparameter optimization approach가 좋음
    * random search / grid search
    * AutoML techniques
    * [[Yang and Shami, 2020](https://www.sciencedirect.com/science/article/pii/S0925231220311693?via%3Dihub)]에 더 많은 방법들이 survey되어있다고 함

#### Do be careful where you optimise hyperparameters and select features
* 위에서 언급된 내용과 큰 차이 없음
* Nested (Double) cross-validation 을 쓰는 것을 추천
    * Hyperparameter optimization & Feature selection as an extra loop inside the main cross-validation
    * training 자체를 시작하게 전에 optimization/feature selection을 하지 말라는 의미

## 3. How to robustly evaluate models

#### Do use an appropriate test set
* Training set성능은 거의 의미 없다고 봐도 된다
    * generalization ability없이 train set 성능이 나올 수 있음
    * 간혹 적은 training set에 대해서 train set 성능이 100이 찍히는지 확인해보는 건 좋다고 생각함. 
        * 모델 자체가 해당 데이터에 쓸만한지 판단하기 위함
* 다른 언급된 부분들은 test set을 직접 만들지 않는 이상 해당사항 없음
    * train set보다 더 넓은 환경에서 collect되는 것이 좋음
    * Single equipment로 collect된 데이터보다 다양한 equipment사용이 좋음
    * train/test set의 "성질"이 겹치면 그 성질만 overlearn할 수 있다는 의미 (equipment, weather..)

#### Do use a validation set
* test set을 validation에 쓰면, test set이 training 과정의 일부가 되어버림
* validation set으로 early stopping을 하기 위함


#### Do evaluate a model multiple times
* 많은 ML 모델은 unstable해서 데이터가 바뀌거나 / 여러번 학습함에 따라서 결과가 유의미하게 바뀔 수 있음
* Cross-validation을 사용하는 것이 대중적
* 여러 결과의 mean 과 std를 report하는 것이 좋음
* 이후의 statistical test를 통한 model comparing을 위해 개별적인 결과도 남겨두는 것이 좋음


#### Do save some data to evaluate your final model instance
* Cross validation을 통해 가장 점수가 높은 fold를 쓰는 것도 단지 easiest fold를 들고 있어서 그럴 수 있음
* 데이터가 충분하다면 아예 train/valid/test를 나누는 CV과정 외에 따로 unbiased test set을 두는 게 좋을 수 있음
* 우리한테 해당되는 사항이 많을지는 모르겠음

#### Don’t use accuracy with imbalanced data sets
* Imbalanced data set의 경우 accuracy가 misleading할 수 있음
    * 예) 99:1의 데이터 비율일 경우 (극단적), 전부 다 class 1으로 예측해도 99% accuracy임
* Balance를 고려한 metric을 쓰는 것이 좋음
    * Cohen's kappa coefficient
    * Matthew's Correlation Coefficient
    * 경험적) F1 score

## 4.  How to compare models fairly
#### Don’t assume a bigger number means a better model
* 다른 data partition에 학습/평가되었을 수도 있음
* hyperparameter optimization시도의 차이가 있을 수 있음
* "정말" 공평한 평가를 위해서는 비교할 다른 모델들을 직접 구현하여, 비슷한 수준의 parameter optimization을 진행한 뒤 해야함 (multiple evaluation, statistical test까지)
    * (too much work 아닐까요)


####  Do use statistical tests when comparing models
* Statistical test는 우리 모델의 우수성을 입증하기에 좋은 도구임
* (하지만 정확히 무슨 말을 하고자하는지 모르겠네요)
    * Student's T Test
    * Mann-Whitney's U test

####  Do correct for multiple comparisons
* 무슨 말인지는 알겠지만 해당 사항은 딱히 없어 보임
    * Multiple comparison을 진행할 때는 confidence level 에 따른 false positive가 accumulate될 수 있음
    * Bonferroni correction을 사용하여 test의 개수에 따라서 significance threshold를 낮출 수 있음

#### Don’t always believe results from community benchmarks
* 다 같은 데이터셋으로 학습/평가하니까 더 투명할거라는 motivation을 가진 community benchmark
* Test set access도 풀려있어서, 다른 사람들이 어떻게 사용했을지 모름
    * over-optimistic한 결과로 이어질 수 있음
* 계속 같은 test set을 쓴다면 해당 test set에 overfit되는것
    * 해당 test set에서 가장 잘 나온다고 사실상 잘 generalize된다고 말하기 어려울 수 있음
* 따라서 작은 성능 gain이 significant하다고 생각하는 건 위험할 수 있음
* [[Paullada et al., 2020](https://arxiv.org/abs/2012.05345)]에 더 in-depth discussion이 있다고 함 
* (그래서 요새는 test set은 공개되지 않은 community benchmark들이 존재하는 것 같음)

#### Do consider combinations of models
* 서로 다른 모델을 (같은/닫른 아키텍쳐) 사용함으로서 (ensemble) 서로의 단점을 커버해줄 수 있음
    * (알긴 하지만 논문 쓸 때도 그래도 되나?)

## 5.  How to report your results
전반적으로 what worked & What didn't 가 포함되어 있는 게 좋음 \
ML은 주로 trade-off가 엮여있기 때문에 (한 모델이 다른 모델보다 "모든 면"에서 잘나기는 어려움) 그런 부분도 잘 서술해야함

#### Do be transparent
* 투명하게 작성해야 다른 사람들이 이 논문을 바탕으로 연구를 진행하기가 수월함
* 코드 공유도 투명하게 공개하는 것이 좋음
* "코드를 공유할 것"이라고 생각하는 게 내 자신도 더 신중해지고, 실험 정리도 꼼꼼하게 하게 되고, 깔끔한 코드를 작성하도록 도움 됨
* 이후에는 코드와 workflow가 공유되고, 잘 문서화되어있지 않으면 아예 논문 출판이 어려울 수도 있음
    * (이렇게 되면 클린해지긴 할듯)

#### Do report performance in multiple ways
* 다양한 데이터셋을 사용해보는 것이 좋다
* 각 데이터셋별로 여러 metric을 사용하는 것이 좋다
    * accuracy + F1score
    * FID score + IS
* 또한 metric을 사용할 때 정확히 어떤 metric인지 서술
    * F-score라면 F1인지
    * AUC라면 PR curve/ROC curve를 사용하는지

#### Don’t generalise beyond the data
* 실험적인 면이 아니라, 결론을 내리거나 writing을 할 때 성급한 결론을 내리지 말라는 뜻
    * 담백하게 쓰고, overstatement를 작성하지 마라
    * 한 데이터셋에서 잘 됐다고 당연히 다른 데이터셋에도 잘 되는 게 아님

#### Do be careful when reporting statistical significance
* 실제로 통계적인 비교를 할 때 그 비교 자체가 필요한지를 고려하라
* statistical test마다 성질이 다르고 완벽하지 않기 때문에 오히려 성급한 결론에 도달할 수 있음
    * (사실 비전 분야에서 이런 테스트들이 사용되는지 잘 모르겠습니다)

#### Do look at your models
* 수치적 결과 뿐만 아니라, 그래서 모델이 뭘 학습했는지 보여주는 것도 중요하다
* "어떻게" 더 좋은 성과를 냈는지에 대해, 모델에 들여다 볼 필요가 있음
* Explainable AI와도 관련이 있음
    * Visualization/Ablation test등을 통해 조금 더 interpretability를 가지면 좋다는 말인 듯

### 정리하며
여기 된 것이 알아야 할 모든 것의 전부는 아니며, 틀리거나 의논이 필요한 부분이 있을 수도 있다. 또한 the best way of doing things가 어제-오늘 다를 수 있기 때문에, 항상 open-mind로 / 최근 development에 keep-up하는 자세와 / 내가 모든 것을 알지는 못한다는 겸손함을 갖추는 것이 중요하다.

