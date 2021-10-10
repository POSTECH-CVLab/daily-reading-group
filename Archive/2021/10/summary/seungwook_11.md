# OK Google, What am I doing? Acoustic Activity Recognition bounded by conversational assistant interactions
## Rebecca Adaimi et al., UT Austin - UbiComp 2021
#### Summarized by Seungwook Kim
---

**총평**:
* 지능형모바일 시스템의 일환으로 읽게 되었습니다. UbiComp, Chi 등의 학회는 항상 실제 use-case와 연관지어 논문을 전개해서 보는 재미가 색다르네요. 
* 컴퓨터 비전 분야에서 Ubicomp/Chi에 제출되는 논문처럼 일반인과 밀접하게 맞닿아있는 분야로는 뭐가 있을지 궁금하네요.
* Log-mel spectogram classification을 위해 Audio-set pretrained network를 쓰는데, 이전에 Naver AIRUSH대회에서 ImageNet pretrained network로 Log-mel spectogram classification에서 우승한 팀이 있습니다. 어떤 차이가 있을지 궁금하네요.

**Task**: ADL (Activities of Daily Living) Classsification
* Sound input, preprocessed to Mel-spectogram

**Motivation**:
* When Voice assistant is activated (Hi Bixby / Hello Google etc), and until the voice assistant replies, there are "background sounds"
* Propose that these "background sounds" could be used to identify ADL, and the location of the voice assistant.

**Method**
* How to only record sound during "user - assistant interaction?"
    * raspberry pi add-on with a camera to see if assistant as activated
    * record for 30 seconds during the interaction
* Recorded audio is preprocessed to Log-Mel spectogram
* VGG-like Network, pretrained on much larger dataset (AudioSet) and finetuned on collected data (14 participants)
* trained to classify ADL (predefined 17 activities) or location (living room/kitchen/toilet)

**Results / Discussions**
##### ADL Classification
* LOPO (leave-one-person-out evaluation)
    * use each individual as a 'test' set
* 84% F1 score when using entire 30 seconds
* 57% F1 score when only using mid-interaction segment(between user query and assistant answer)
* OOD classification (읽으면서 궁금했던 부분인데 실험이 있어서 좋았음) - Majority misclassified as "boiling"
    * "boiling" is usually very quiet (just the bubbling sound)
    * has low confidence score - can be thresholded to filter out OOD sounds
* 77% F1 score when using voice-interaction masking to filter voice
    * the background noises are also affected

##### Location classification
95% F-1 score 
