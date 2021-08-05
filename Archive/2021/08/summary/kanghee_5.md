# Semantic Graph Based Place Recognition for 3D Point Clouds
### Xin Kong et al. - IROS 2020
#### Summarized by Kanghee Lee
---

**Task**) \
Place Recognition with point cloud data
	
**Motivation**) \
dynamic situation을 represent하기 위해서는 segments들을 matching하는 방법으로 place를 인식해야하는데 정확하고 stable한 segment feature를 얻는 것 자체가 힘들고 
기존 method들은 segment간의 relation은 무시하고 있다. 그러나 segment의 relation들이 scene expression의 핵심이다.

**Contribution**)
1) propose a novel semantic graph representation for 3D pcd scenes which captures semantic information and models topological relations between semantic objects
2) propose an efficient network to estimate the graph matching similarity among pcd scenes
	
**Method**) \
(a) Semantic Graph representation : SemanticKITTI에 대해 pretrain되어있는 RangeNet++ network를 사용하여 semantic segmentation을 수행한다. 
Segmentation결과에서 dynamic class들을 static one으로 merge한다(사람과 같이 불필요하거나 별로 등장하지 않는 class는 제거). 동일 class끼리의 instance들끼리 graph를 구성하도록 한다. \
(b) Graph Similarity Network : DGCNN의 EdgeConv를 이용하여 spatial, semantic level features들을 얻고 두 feature를 concat하여 다시 conv를 거침으로써 embedded feature를 만든다. 
위 Node embedding network는 spatial, semantic 각각에 대해 3 Edge Conv layer로 구성되어 있다. 
두 scene에 대해 이렇게 얻어진 두 embedded feature에 대해 Neural Tensor Network를 이용하여 Graph-Graph interaction output을 도출한다. 
NTN은 source graph의 embedded feature에 weight와 target graph의 embedded feature를 곱한 후 두 feature에 다시 weight vector를 곱하고 둘을 더한다. 
해당 output은 FC layer를 통해 0~1사이의 similarity score를 갖게 된다.
