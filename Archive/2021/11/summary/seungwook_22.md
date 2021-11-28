# Differentiating Higher and Lower Job Performers in the Workspace Using Mobile Sensing
## Shayan Mirjafarih et al., ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 2019
#### Summarized by Seungwook Kim
---

**총평**:
* AIGS700D 수업의 일환으로 읽게 됨
* Mobile device / wearable device / bluetooth beacon에서 얻어진 데이터를 바탕으로 high-performing/low-performing employee를 구분하는 연구
* 개념은 참신하고 재미있으나, 정확도가 크게 높지는 않음
* ML-based방법을 사용하여 interpretable한 결과를 바탕으로 high- & low-performer를 나누는 기준을 알 수 있게 됨
    * 당연한 결과들이 많음 (핸드폰을 덜 볼 수록... 덜 돌아다닐수록...)
    * 그러나 직업군에 따라서 다른 패턴이 존재함을 보임
* Objective 한 assessment를 지향하지만, subjective한 label을 사용하여 bias가 그대로 존재할 수 있다고 생각함.

**Task**: Differentiating high-and low-job performers

**Motivation**:
* Existing methods for performer assessment is subjective (peer reviews, etc)
* Aims to propose an OBEJCTIVE, UNOBSTRUSIVE method for employee assessment

**Dataset**: Collected through mobile device (app: phone monitoring), wearable device (watch: heart rate and physical activity), and bluetooth beacon within the company (identify position within company)

**Method**:
* Creates features from data collected in a human-interpretable way
    * Number of times a phone was unlocked...
    * Amount of physical activity...
* Use K-mean clustering for unsupervised divison of high-and low-performers
    * Initialize with human-given 'best' labels on high- and low- performers
