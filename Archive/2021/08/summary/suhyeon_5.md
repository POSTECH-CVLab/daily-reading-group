# PackIt: A virtual Environment for Geometric Planning 
### Akit Goyal at al.  - ICML 2020
#### Summarized by Suhyeon Jeong
---

**Overview** : novel way to generate dataset for packing problem 을 제안하고, 이를 푸는 모델을 구성하였으며, 모델과 비교할 heuristic method 들을 설계하고 성능을 측정하였다.

**task** :  3d Geometric Planning | 3D interactive environments(?)

 

**Motivation** : 많은 interactive environments 가 연구되어 왔으나 geometric planning task 에 대해서는 연구되어지지 않았다. 그리하여 geometric planning 중 packing task 를 푸는 environment 를 디자인하였다.

**Method** : Reinforcement Learning 과 관련된 environment (Section 4) 말고, Section 5. Model 에서 설명된 learning- based model 의 내용을 요약하겠다. 
논문에서 제시한 모델은 세 파트로 나뉘어진다. 
1) Shape Selection : 다음에 쌓을 Shape 를 선정한다. Learning-based model 의 본체
2) Location Selection : heuristic 하게 Shape 를 쌓을  location 을 선정하는데, 가능한 location 중 가장 bottom-most , left-most, back-most 한 곳 부터 선정한다. preference 는 bottom > left >back 순이다.
3) Rotation Selection : 마찬가지로 heuristic 하게 선정한다. shape 의 모양에서 smallest dimension 이 top-down direction 으로 align 하도록, second smallest dimension 이 left-right direction 으로, 마지막 largest dimension 이 front-back 으로 align  하도록 rotation 을 맞춘다.

Learning based model for Shape Selection : 
1) feature extraction : voxels of each candidate shape, voxels of the box with already placed shape 를 3 residual blocks of fully connected layer 에 통과시켜 box 로부터 feature b 를, candidate shape 들로부터 feature s_0, s_1, s_2 ... 를 뽑아낸다. 
2) candidate shapes 의 feature 들을 max-pool 하여 모든 candidiate shape 의 information 을 담은 하나의 feature s_bar 로 만든다.
3) n 개의 모든 candidate shape 마다 s_x, b, s_bar 를 합친 concatenated feature 를 생성하여, 이를 각각 sequence of 4-FC residual block 에통과시켜 output a_x 를 얻는다. final probability distribution 은 Softmax(a_0, a_1, a_2 ... _a_n) 이다. 

위의 learning based model 은 Proximal Policy Optimization 으로 학습된다.


**총평** : Reinforcement learning 에 대해 알지 못해 아직 Section 5.Model 과 Section 4. Environment 의 관계에 misunderstanding 이 있을 수도 있다.  본인이 이해한 바로는 위에서 요약한 대로 location/rotation 은 heuristic 하게 선정하고,위의 learning based shape selection 을 reward 를 이용해  Proximal Policy Optimization 으로 학습한다는 것 같은데, 정확하지 않을 수도 있다. 
