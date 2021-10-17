# Graph U-Nets
### Hongyang Gao, Shuiwang Ji - ICML 2019
#### Summarized by Jiye Kim

---

### **Task** : 
Node classification and graph classification


### **Main Idea** : 
-  graph pooling (gPooling), graph unpooling (gUnpool) 방법을 제안해서 graph U-Net 구조로 node classification과 graph classification을 푼 방법이다. Image 에서 pooling과 upsampling 방법을 graph에 곧바로 적용하기는 어렵기 때문에 이를 graph 특성에 맞추어서 방법을 제안한 점이 contribution 이다.





### **Method** :  
Graph pooling (gPooling)

- Graph pooling 과정은 중요한 노드들만 남기고 노드들의 숫자를 계속 줄여나가는 방법이다.
모든 노드의 feature를 projection vector를 통해서 scalar output을 얻은 후 큰 순서대로 k개를 뽑는다. 이 k개의 노드들의 feature vector와 adjacency information만을 남긴다.


Graph unpooling (gUnpool)

- graph pooling과정에서 사라진 node 들의 index 를 저장해놓고 unpooling과정에서 사용한다.
현재까지 graph node feature X^l과 index를 받아서, 사라진 노드들의 feature를 predict하도록 한다.


Graph U-Net architecture

- gPool 과 GCN을 반복하면서 graph encoding을 수행하고, gUnPool과 GCN을 반복하면서 decoding을 수행한다. low-level spatial feature를 주기위해 skip connection을 사용한다.


Graph connectivity

- graph pooling과정에서 isolated part가 생길 수 있기 때문에, adjacency matrix로 2nd graph power matrix를 사용한다. i.e. A^2





### **Experiment** :
- 여러가지 node, graph classification task에서 sota를 기록했다.


### **총평**:
- image 에서 사용되는 U-Net구조를 graph에 적용한 논문이다. U-Net구조는 기존에 제안된 방법이기 때문에 논문이 엄청 novel하진 않지만 graph에서 pooling과 unpooling이 직관적이지 않기 때문에 해당 방법을 어떻게 제안했는지가 contribution인 것 같다.
