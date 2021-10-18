# Detecting Wireless Spy Camera via Stimulating and Probing
## Tian Liu et al., Peking University - Ubicomp 2018
### Summarized by Seungwook Kim
---

**총평**:
* 지능형 모바일 시스템의 Paper critique을 위해 읽음.
* 소위 "몰카 탐지"를 위한 논문으로, 사회적으로 중요한 이슈 중 하나라고 생각해서 재미있게 읽었음.
* 전반적으로 이해가 아예 안 되지는 않지만 신호처리 (Wireless, video format...) 등에 사전지식이 풍부하면 더 이해하기 편할 것 같음. 얼핏 보면 Heuristic해 보이는 전/후처리가 많음.

**Task**: Identifying the presence of spy cameras
* Live-streaming cameras, or
* Progressive downloading cameras (not real-time!)

**Method**: **Stimulate** and **Probe**

**Stimulate**: variation in light stimuli (user turns light on/off)
* The spy camera is "stimulated" by the different lighting conditions
  * ie the picture size to be transmitted increases when brighter
  * thus, something on the wifi-transmitted data packages should 'change' in accordance with the lighting in the presence of spy cmaeras

**Probe**: Identify the data rate variation of packet flow under light stimuli

Specific details are omitted for brevity

**Results**: Very accurate (90%< , nearly 100 on some cases)
* given multiple runs
  * account for jittering and noise
  * facilitates statistical testing
