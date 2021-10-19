# MediaPipe: A Framework for Building Perception Pipelines
## Camillo Lugaresi et al., Google Research, Arxiv 2019
### Summarized by Seungwook Kim
---

**총평**:
* 지능형 모바일 시스템의 Paper critique을 위해 읽음.
* 전반적으로 논문이라기보다, Framework 소개 document에 가깝다고 여겨짐. Documentation도 있고 코드 공개도 되어있는데 왜 arxiv에 올린건지는 의문.
* ML 개발 위주로 공부/연구한 연구자들이 바로 deployment pipeline에 적용해볼 수 있게 된다는 점이 매력적이라고 생각함.

**Task**: Framework for building pipelines to perform inference over arbitrary sensor data
* Sensor data: Image data from camera, sound data from microphone...

Overall structure:
* Packets of data
* "Calculators" to process & convey packets
* "graph" structure of the overall process

Supports GPU & multithreading (given there are no temporal dependencies) & Scheduling

Tools for evaluation performance:
* **Tracer**: records timing events -> enables recording and visualization of individual packet flows
* **Visualizer**: Helps understand the topology and overall behaviour of pipelines

Provides cross-platform support
