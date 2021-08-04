# Robust Neural Routing Through Space Partitions for Camera Relocalization in Dynamic Indoor Environments
### Siyan Dong et al., Shandong University) - CVPR 2021 (Oral)
#### Summarized by Kanghee Lee
---

**Task**) \
Indoor scene의 entire map pcd가 있고 input으로는 scene의 일부에 해당하는 frame이 rgb-d로 들어올때 전체 map에서 어디에 해당하는지 6DoF를 추정하는 task이다.
	
**Motivation**) \
기존의 CNN 혹은 decision tree를 이용하여 2D/3D-3D correspondence를 찾고 localization을 수행하는 연구들은 static input img sequence에서만 잘 동작하고 
dynamic environments에서는 성능이 큰 폭으로 하락한다.

**Contribution**) \
Dynamic환경에서의 outlier들을 제대로 못 잡아내서 생기는 correspondence error를 outlier-aware module을 통해 해결했다. 
해당 모듈을 통해 input points중 outlier point는 제외시키고 training때 보았던 static points에 대해서만 correspondence를 찾아내서 정확한 localization을 수행할 수 있도록 유도했다.
	
**Method**) \
네 가지로 구성된다. \
(a) Hierarchical space partition : 3D scene map pcd를 physically 나눠서 subregion을 만드는데 이 작업을 계층적으로 계속 반복하여 각 subregion들이 tree의 node를 구성하도록 한다. 
Entire map은 tree의 root node에 해당하고 각 child node는 parent node의 subregion들이 된다. \
(b) Neural routing function : Tree에서 routing을 시작하는데 input query point와 neighborhood points를 가지고 어떤 child node로 routing해줄지 결정하는 함수이다. 
Leaf node는 Scene map pcd에서의 points set를 의미한다. 결국, input points+neighbor points를 인풋으로 하여 Tree root node부터 출발하여 점점 subregion들로 routing해가며 
최종적으로 map pcd에서 실제 points set을 의미하는 leaf node로 mapping된다. 
이때 한 가지 주목할 점은, leaf node를 선택할때 leaf node들 중 score가 가장 높은 node를 선택하는 방식이 아니라, routing과정에서 거쳤던 모든 node들의 score들을 곱하면서 accumulate probabilities를 통해 leaf node를 선택하게 된다. \

**Neighbourhood points?** \
해당하는 split node에서의 region에서 randomly sampled된다. 즉, 각 level마다 split node가 represent하는 region크기가 다르므로 sampling되는 ball query크기도 다른 것이다. 
이 방식으로 17개의 points를 sampling한다.

**Input?** \
Query points와 neighbor points 각각의 normal vector를 이용해서 위처럼 3개의 angle을 구하고 1개의 distance를 구한다. (=4D)
거기에 각 neighbor points의 color정보(3D)를 더하여 최종적으로 7D 정보가 인풋이된다.
이 과정에서 query의 geometric feature는 위에 충분히 담겼기 때문에 points에 대한 정보는 color정보 3D만 이용한다. 이렇게 7D와 3D 두개가 인풋이다.

**Routing function?** \
Routing function을 각각의 level의 split node들에 대해 따로 학습한다는건 시간, 메모리상으로 엄청 비효율적이다. 
따라서 동일 level에서는 모든 split node들이 같은 네트워크로 학습할 수 있도록 해주기 위해 Context points(7D), Query point(3D)뿐만 아니라 Node index도 들어간다. 
즉 t level tree라면 t개의 routing function을 학습시키면 된다.

(c) Outlier rejection : dynamic input points에 대해 outlier임을 알아차리지 못하면 잘못된 point correspondence를 만들게 되고 이는 결국 false 6DoF prediction을 야기시킨다. 
해당 논문에서는 Tree에서 각 node들이 subregion을 child node로 갖게 하면서 동시에 outlier node도 child node로 갖도록 한다. 
다시 말해, Map을 계층적으로 k subregion씩 나눴다면, Tree에서 각 node는 k개가 아닌 k+1(outlier node)의 child node를 갖게 된다. 
이로써 outlier point가 input으로 들어 왔을때는 leaf node로 나아가지 못하도록, outlier node에서 routing이 끊기도록 한다. \

(d) Camera pose estimation : RANSAC을 이용함.



한계 : only RGB input에 대해 동작하지 않고 또한 새로운 environments에 대해 pretrained를 이용하여 generalization test를 할 수 없다. 
(node index를 supervision으로 주고 이거를 새로운 환경에서는 완전히 다른 학습이 되어버리므로)
