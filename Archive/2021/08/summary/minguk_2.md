# Emerging Properties in Self-Supervised Vision Transformers
### Author information
#### Summarized by Minguk Kang
---

해당 논문은 DINO라는 이름으로 유명한 논문이며, facebook AI와 INRIA에서 퍼블리쉬 된 논문입니다.
 
Motivation: Vision Transformer (ViT)는 supervised learning에서 놀라운 성능을 보여주고 있으며, 특히 locality라는 inductive bias를 CNN보다 적게 사용하기에 large-scale dataset에서 generalization 성능이 좋은 것으로 알려져있습니다. 본 논문에서는 BERT와 같은 모델이 NLP에서 성공적으로 많이 사용되는 이유인 self-supervised pre-training을 vision task에도 적용해보면 어떨까라는 생각에서 출발하였습니다. 
 
Method: weight를 share하는 student와 teacher를 만듭니다. 이 때 student는 SGD를 사용하여 학습하는 모델이며 teacher는 student network를 momentum update를 해주는 모델입니다. 이 때 teacher 모델을 과거의 student model들의 앙상블로 생각하여 soft distillation을 해주는데 이를 위해 student의 probability와 teacher의 probability의 consistency를 맞춰주는 cross-entropy loss를 사용합니다. 디테일로는 SwAV에서 사용한 multi-crop을 가지고 왔으며, 또한 ViT에서 사용하는 토크나이징 방법을 그대로 사용하여 학습을 수행합니다.
 
결과는 기존 SwAV, BYOL등과 비교해서 ResNet50, ViT-s에서 더 좋은  linear-probe 성능을 보여주고 있으며, 
특징점으로는 k-NN classification을 했을 대 기존 self-supervised 방법에 비해 눈에 뛸만한 성능 향상을 보여주고 있다는 것 입니다.
그 이유에 대해서는 설명하고 있지 않은데, 후속 연구로 해볼 만 할 것 같습니다.
마지막으로 class token의 attention map을 visualization 해보면 이미지의 semantic part를 유난히 더 강조를 하게 되는데 첨부되어 있는 비디오를 보면 self-supervised ViT가 이미지의 semantic에 집중하여 instance discrimination task를 풀어나간다는 것을 알 수 있는 재미있는 논문인 것 같습니다.