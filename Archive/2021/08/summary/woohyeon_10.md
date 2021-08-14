# End-to-End Object Detection with Transformers 
### Nicolas Carion and Francisco Massa et al., Facebook AI - ECCV 2020 (Oral)
### Summarized by Woohyeon Shim 

**Task:** solving object detection as a direct set prediction with transformer.
	
**Previous approaches:** indirect (surrogate regression and classification)
* **large set of proposals (two-stages), anchors or centers (one-stage)** that encode prior knowledge ⇒ this is replaced by direct set prediction (box is defined w.r.t the input image rather than an anchor).
* **post-processing** (non-maximum suppression) ⇒ this is removed by bipartite matching after modeling all pairwise interactions using transformer.
* **bipartate-matching losses with encoder-decoder architectures based on CNN Stewart**, R.J., Andriluka, M., Ng, A.Y.: End-to-end people detection in crowded scenes. In: CVPR (2015) ⇒ developed for a specific task and not evaluated against modern baselines, also this work is based on RNN (auto-regressive model).
	
**Intuition**
* **Set prediction:** global inference scheme, permutation invariance
* **Transformer:** aggregating information from the whole sequence, parallel decoding
	
**Method:**
* **Encoder-decoder architecture based on transformer**
	* **transformer encoder**
		* reduce channel dimension by 1x1 convolution given CNN features.
		* collapse spatial dimensions into one dimension to make input sequence.
		* **pass through a multi-head self-attention module** and linear layer.
		* supplement with **fixed** spatial positional encodings, shared and added to the input of each attention layer
	
  * **transformer decoder**
		* **decode N objects in parallel** at each decoder layer
		* add **learnt** positional encoding (refered as object queries) to the input for each attention layer, similarly to the encoder, to make different output for permutation-invariant input.
	
  * **Output:** class labels and box coordinates that are independently decoded for each object, resulting in N final predictions. (3-layer MLP with ReLU + Linear projection layer)

* **Bipartite matching that assigns a prediction uniquely to a ground truth box.**
	* **Hungarian algorithm** (optimal assignment)
		* N = # of predictions >> # of objects in images
		* GTs are padded with (no object) to have the same number of predictions.
		* the optimal assignment = highest class probability and the similarity of predicted and ground truth boxes.
	* **Loss computation:** NLL loss for class prediction + l1 loss and geralized IoU loss for Box prediction
		* down-weight the term for (no-object) by a factor 10
		* resolve relative scaling issue of box by IoU loss
			
**Experiments:**
  * **Comparable results with** FasterRCNN with **extra-longer training schedule** (lower AP_s [-5.5], but improved AP_L [+7.8]),
	* **No need of NMS:** incurring small loss when adding NMS at last layer of decoder.
	* **Need of positional encoding:** Removal of spatial positional encoding drops 1.3 AP and only one output encoding at input leads to 1.4 AP drop, removing both of them results in 7.8 AP drop.
	* **Need of GIoU loss:** Without L1 loss → losing only 0.7 AP. Without GIoU → poor results.
	* **Extension to panoptic segmentation,** which is similar to the extension of Faster R-CNN to Mask R-CNN with a simple segmentation head on top of a pre-trained DETR.

**총평:** 승욱씨가 리뷰한대로 set prediction의 novelty는 이전웍이 있었기에 없다고 봐야함. 결국 기여한 것은 transformer를 인식 문제에 적용해서 그럴듯한 성과를 보여주고 minor하게 보이긴 하지만 적용 방식을 계산량/시간 이슈로 sequential하게 계산 하던 방식에서 parallel방식으로 바꾼 것에 있는 것 같음. 하지만 혁신적인 것은 분명하며 직관적인 아키텍쳐 제안, 실험적 검증이 모두 동기를 반영하여 전체가 매끄럽게 이어져서 재미있게 읽은 논문.
