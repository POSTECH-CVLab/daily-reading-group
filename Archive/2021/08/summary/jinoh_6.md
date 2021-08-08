# Contrastive Learning for Unpaired Image to Image Translation
### Taesung Park et al.(University of California, Berkeley) - NeurIPS 2020
#### Summarized by Jinoh Cho
	
# Task: Image to Image Translation
	
# Motivation:
	 
  기존의 Image to Image Translation Task에서 인풋 이미지의 Content를 유지하기 위해서 Cycle Consistency Loss를 사용해왔었으나, 이 방법은 input 도메인과 output 도메인 사이의 relationship이 양방향성이라는 가정을 하고 있음, 이는 굉장히 restrictive하다. 이 논문에서는 bijection translation의 제한을 없엔 one-side translation을 위해 multi-layer, patch wise contrastive loss를 제안함.

  다른 여러 Unsup Task들에서 Contrastive Learning Approach가 효과적으로 작동을 해왔었는데 이를Image to Image Translation에서 Contrastive Learning을 어떻게 Effective하게 사용할 것인가에 대해서 깊이 고민을 해본 논문. 

# Method:

  로스는 크게 3개로 이루어져 있음.

  첫번째 로스는, Input Domain의 이미지로부터 새롭게 생성한 이미지가 Target Domain과 Appearance가 유사하도록 Adversarial Loss(생성 이미지와 Target Domain이미지 사이에)를 부과함. 

  두번째 로스는, Input Domain과 Output Domain사이의 Mutual Information Maximization을 위한 Multi Layer, Patch Wise Contrastive Learning Loss를 주었다. 여기서 특이한 점은 Query(Anchor)에 대한 Positive Sample과 Negative Sample을 모두 Input Image에서 Sampling한다. 예를 들어서, 말 -> 얼룩말 task를 생각해보면 생성된 얼룩말 이미지에서 얼굴 부분 patch를 Query라고 하면 Positive Sample은 말 이미지(인풋 이미지)의 얼굴 부분 patch를 Positive, 말의 다리, 산, 풍경, 백그라운드 부분의 patch를 Negative로 보는 것이다. 이를 통해서 이미지 전체에서 추출한 컨텐츠 정보를 이용해서 인풋 이미지와 생성된 이미지 사이의 content를 유지하는 것이 아니라 입출력이미지의 동일한 위치에 있는 patch 사이의 content를 유지함을 통해서 더 좋은 signal을 준다.

  마지막 로스는 identity 로스이다. 생성된 이미지와 Target Domain의 이미지 사이에서 Multi Layer, Path Wise Contarstive Learning Loss를 준다. (두번째 로스와 유사) 이를 통해서 generator가 unnecessary change를 만드는 것을 막아준다. 이는 기존의 unpaired translation methods에서 사용되었다고 함. 

  위 세 가지 로스를 통해서 contrastive learning을 통해서 input 이미지와 output 이미지 사이에서 content consistency를 달성함을 통해서 더 좋은 퀄리티의 Image To Image Translation 이미지 생성을 달성하였음.

# Strong Point :
	
1. image to image translation task에서 어떻게 하면 contrastive loss를 디자인 해야 content를 잘 유지 할 수 있을까에 대한 고찰과 이에 대한 실험적 결과가 근거로 잘 제시된 논문이다.

2. 일반적으로 contrastive loss를 image set단위로 하나 이 논문에서는 patch단위로 contrastive loss를 사용함으로서 single image pair만으로도 contrastive loss를 사용할 수 있어 메모리를 줄일 수 있다는 장점이 있음. 
	 
	
# Weak Point :
	
1. Failure Case에서 볼 수 있듯이 unfamiliar pose of the horse를 보게 되면 texture를 background에 추가하는 경우가 있으며, 고양이->개 task에서는 없던 혀를 생성하는 문제 등이 발생하는 것을 볼 수 있음.
	 
# Experiments:

  각 로스의 디자인 초이스에 대한 ablation도 잘 진행하여 보여주고 있으며, cat->Dog, Horse -> Zebra, Cityscape 세가지 데이터 셋에 대한 실험 결과도 디테일하게 보여주고 있음.
	 	
# 총평:

  논문도 깔끔하게 writing되어 있어 이해하기 쉬웠고, contrastive learning을 이 태스크에 어떻게 사용해야 효과적인지 잘 보여주고 있는 논문이다. 
