# Polygonal Building Extraction by Frame Field Learning
### Author information - CVPR 2021 (best paper candidate)
#### Summarized by Suhyeon Jeong
---

**Overview** : segmentation performance 를 향상시키고(e.g. yielding sharper corner) vectorization 시 유용한 information 을 제공하는 Frame field output 을 추가하여 polygonalization 에 도움이 되는 추가적인 geometrical information 을 제공하고, segmentation 이 더 반듯하게 output 을 추출하도록 도와 polygonal building extraction  의 성능을 높였다. 

 

**task** : 2d Image segmentation/ polygonal extraction

 

**Motivation** : geographic information system 을 요구하는 application 들은 보편적인 segmentation model 처럼 raster format output 을 필요로 하는 것이 아닌, vector polygon 형태를 필요로 하는 경우가 많다. 기존 연구들은 raster output 의 smoothed out corners 나 discretization 으로 인한 shape information lost 로 정확한 polygon shape 를 생성하기가 어려웠다. vector representation 을 output 으로 생성하는 모델들은 simple polygon 에 한정되어 있거나, polygon 내의 holes/ 집과 집 사이 공유되는 경계면 등을 잘 잡아내지 못했다. 이를 Frame Field 를 사용하는 모델을 구성하여 polygon 의 quality 를 향상시키고자 한다. 

 

**Method** : 
기존 방법들과의 차이점 : 기존 end-to-end method 들은 CNN 으로 segmentation 을 진행하고 GAN 으로 building boundary 를 regularize 하여 학습된 corner probability map 으로 vertices 를 추출하였다. 하지만 본 논문에서는 end-to-end 는 아니지만 UNet-backbone+CNN head 로부터 frame field 와 segmentation result 를 학습하고 post-processing polygonization algorithm 을 적용하였다. 

 

**model** : 모델은 image 를 input 으로 하는 U-Net backbone 과 backbone 에 달린 두 CNN head 로 이루어져 있다. 각 CNN head 는 segmentation map 과 frame field 를 output 으로 가진다. \
-> segmentation map : backbone 의 output 을 input으로 이용해 CNN head를 통과시킨다. 건물 내부를 segmentation 하는 interior segmentation map 과 건물 edge 를 segmentation 하는 contour segmentation map 을 output 의 각 channel 로 가진다.  supervised learning. \
-> frame field : backbone output 과 segmentation output 을 concat 하여 input 으로 사용해 두 번째 CNN head 를 통과시킨다. frame field 는 {u,-u, v,-v} 이 4 개의 vector 를 plane 의 각 point 에 assign 하는 field 인데, corner 의 경우 두 edge 가 다른 direction 을 가지고 있으므로 frame field 역시 2 direction 을 가진다. u,v 는 complex number 로 나타내어 지며, 학습의 편리를 위해 실제 학습은 point z 에 대해 (z^2 -u^2)(z^2 - v^2) 을 전개한 식의 coefficient (c0,c2) 를 output 으로 하여 학습한다. (z^4 + c2z^2 + c0) \
-> loss : loss 가 꽤나 복잡하다. 


	
* segmentation map 에서 interior segmentation 과 contour segmentation 의 ground truth 와의 distance loss 
	
* frame field  에서 ground truth tangents 와 normals 각각에 대한 align loss 
	
* frame field 에서 enforces smoothness of field 를 가능하게 하는 regularizer 항
	
* segmentation 에서 edge(contour) map 이 predicted interior map 의 norm of spatial gradient 와 같게 해 주는 regularizer 항, 
	
* 두 segmentation 과 frame field 의 output 이 서로 잘 align 하게 해 주는 regularizer 항

위의 모든 loss 를 combination 하여 사용하는데, loss 가 distinct unit 을 가지므로 random initialized network 에서 random subset 을 이용해 구한 loss value 로 normalization coefficient 를 계산하여 normalization 을 적용한다. 
 
**post-processing polygonization algorithm** : Active Contour Model (ACM) 에서 영감을 받아 contour 대신 skeleton grpah 를 이용해 optimization 을 진행한다(ASM 이라고 명명함). skeleton graph 가 frame field 에 align 하도록, skeleton path 가 interior segmentation map 에 잘 fitting 되도록 energy term 을 구성하여 진행한다.

 

**총평** : 저자는 다양한 result 예시들을 이미지로 첨부해 놓았는데 타 model 들에 비해 반듯한 contour 나 집과 집 사이 경계면을 잘 구분하는 등 확연히 깔끔해진 결과물을 보였다. 물론 cherry picking 일 가능성도 있지만, frame field 로 align하는 방식이 깔끔한 polygonal contour extraction 에 확실히 도움이 되는 것 같아 보였다. 깔끔한 output 이 요구되는 경우 본 논문의 idea 를 참고해볼 만한 것 같음. 하지만 loss 및 regularizer 항이 과도하다고 생각될 수 있을 정도로 많아 다른 task 에 실제로 적용 및 학습이 잘 될 수 있을지는 모르겠음.
