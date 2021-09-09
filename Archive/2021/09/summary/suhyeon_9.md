End to End object detection with Transformers- Nicolas Carion et al. (ECCV 2020 oral)
    






**Overview** : DETR 로 유명한 논문. Transformer architecture 를 그대로 들고와 bbox regression 과 object classficaiton 을 한꺼번에 진행하도록 모델을 구성하였음. end-to-end detection model.

**task** : object detection

**Method** : CNN encoder -> transformer encoder -> transformer decoder -> FFN(feed-forward network) 로 구성된 end-to-end model. N 개의 fixed-number object 를 predict 하며, classification label 중 no-object label 이 있어서 fixed output 으로 생기는 background detection 들을 처리할 수 있다. ground truth object 들도 N size 를 맞추기 위해 no-object 로 padding 한다. loss 는 total loss 를 최소화하는 prediction - GT 간의 bipartite matching 을 구해 계산한다. 각 match 마다 class prediction loss + bbox loss 를 계산하는데, bbox loss 는 L1 loss 와 scale invariant 한 GIoU loss 의 linear combination 이다. 
+ auxilary decoding losses : decoder layer 마다 FFN prediction 생성, 각 loss 를 계산하여 sum함. FFN 의 parameter 는 share 하고 있음


DETR architecture

1) CNN encoder 로 dxHxW lower-resolution embedding 을 생성한다. + 1*1 convolution 을 이용하여 channel dimension reduce
2) 1) 에서 생성된 image feature 를 d dimension 을 가진 HW 개의 vector set 으로 하여 transformer encoder 에 넘긴다. (with fixed positional encoding)
3) transformer decoder 의 input 으로는 N learnable positional encodings (object queries) 와 encoder output 을 넣어 주게 된다. 이 positional encoding 들이 decoder 를 거치면서 N개의 object 들을 represent 하는 feature 로 바뀌게 된다. 기존 transformer 의 decoder 처럼, DETR 의 decoder layer 는 object query 의 self attention + encoder output 을 key 와 value 로 한 attention 으로 구성된다.
4) FFN 을 거쳐 decoder output 에서 normalized center coordinate, height, width, 그리고 class label 을 predict 하게 된다. 

**Results** : 


	
* optimized Faster R-CNN에 comparable 한 result 달성
	
* panoptic segmentation task 에서도 좋은 성능을 보임
	
* large object 는 잘 detect 했지만 small object 에서는 성능이 떨어짐


