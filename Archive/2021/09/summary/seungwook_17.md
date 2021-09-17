# MyTraces: Investigating Correlation and Causation between User's Emotional States and Mobile Phone Interaction
## Abhinav Mehrotra et al., UCL - ACM 2017
#### Summarized by Seungwook Kim
---

**총평**: 
* Coursework에서 발표해야 해서 읽었습니다 (지능형모바일시스템)
* 딥러닝과의 관련은 전혀 없습니다.
* Mobile Interaction과 Mood가 가진 Correlation & Causality에 대한 분석을 진행한 논문으로, 실제로 mobile interaction과 mood가 correlation&causation관계를 가지고 있다는 게 인상깊은 결론이었습니다.
* 21페이지여서 읽느라 쉽지 않았습니다.
* Correlation과 Causation에 대한 기본적인 설명이 잘 되어있긴 합니다.

**Task**: Causality Analysis between Users' behaviour and mood and mobile phone interaction

**Contributions**
* Examine how phone usage and user's interactions associates with emotional states
* First in-depth study, investigating a series of causal relationships between users' emotional states and mobile phone interactiosn

Motivation: profound implications for design of interactive mobile systems

**Method outline**
Emotional states: The Circumplex mood model
* Activeness, Happiness, Stress level 
* 5 point-based Likert scale

Phone interaction: Grouped into 
* Notification, Phone Usage, Application Usage, and Communication

Data collection:
* Android App called MyTraces
* runs in the background to unobtrusively and continuously collect users' mobile phone interaction logs and context information
* Data collected for 6 months.
* Considers 28 users who ran application for at least 20 days, and responded to at least 50% of mood questionnaires 

Correlation Analysis:
* Calculate Kendall's rank correlation coefficients per individual
* The average is computed for the coefficient values
* Fisher's method is used to combine p-values of individual-based correlation analysis

Causation Analysis:
* Only between variables that are significantly correlated
* Consider temporal precedence
* Uses the widely used "matching design approach"

**Evaluation / Results**
* People's activeness level has a significant association with the seen and decision time of notifications
* In stressful situations people become more attentive - reduction of notification response time
* increase in activeness level positively impacts users' phone usage, number of apps launched and clicks on the screen
* The happier people report to be, the less inclined they are to use their phone
* User's activeness level has a positive impact on the music app usage.
* Increase in the stress level of users significantly reduces the usage of communication apps
* People reported being less stressed when their usage of travel apps increases


**Limitations**
* Data collected from only 28 users - may not be sufficient
* SMS count - how is this related to communication apps? Not specified
* Uses raw sensor data to derive high-level info (location, activity) -> subject to limitations and inaccuracies of inference method
* self-reported states may be in themselves inaccurate (biased self-represetnation in questionnaires)
* In extreme cases (streseed, unhappy, sleepy) , users may not want to answer any questionnaires
* Not practically possible to control all confounding variables in observational studies
    * Causality studies may not be accurate
* Increasing number of prompts will be more accurate, but this will annoy the users
    * lab-based experiments on the other hand lack realism.
