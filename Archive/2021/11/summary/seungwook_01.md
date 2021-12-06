# EagleEye: Wearable Camera-based Person Identification in Crowded Urban Spaces
## Juheon Yi et al., SNU, Samsung Research - Mobicom2020
### Summarized by Seungwook Kim

**총평**
* AIGS700D 과목의 일환으로 읽게 됨.
* Component적으로 novel한 면은 없으나, task가 image를 다룰 때 해당 image의 spatial consistency가 필요없다는 점을 활용하여 spatial pipelining을 진행하여 latency를 획기적으로 줄인 것이 인상깊었음.
* Vision task에서도 series of model을 사용해야 할 떄, spatial pipelining과 같은 방법을 사용할 수 있으면 좋겠다고 생각함.

**Task**:
* Person detection within a crowd
* HUmans are not very good at detecting a desired person within a large crowd
* DNNs are not good at detecting Low resolution faces

**Method**:
* Given photo (of many people)
* First remove photo areas with no faces using heuristic edge detection + thresholding
    * questionable, as this step may remove faces as well.
* Then perform face detection using RetinaNet with MobileNetV1 backbone
* According to the type of face detected, face recognition is done seprately:
    * High resolution, frontal face: LIghtweight face recognition on phone 
    * High resolution, profile face: Heavyweight face recognition on server
    * Low resolution: ICN (to reconstruct high-resolution face from LR face) + heavyweight face recognition on server
        * Lightweight face recognition: MobileFaceNet
        * Heavyweight face recognition: ArcFace with ResNet50 bacbone
* Spatial pipelining: Split photo into blocks (with padding to prevent faces being cropped)
    * Then pipeline the process of face detection / ICN / face recognition for each block
    * Improves latency by ~9 times
