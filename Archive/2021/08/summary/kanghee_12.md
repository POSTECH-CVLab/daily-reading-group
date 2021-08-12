# NeuroMorph : Unsupervised Shape Interpolation and Correspondence in One Go
### Marvin Eisenberger et al., Facebook AI Research - CVPR 2021
#### Summarized by Kanghee Lee
---

**Task**) \
source mesh와 target mesh사이의 correspondence를 찾아 source mesh의 identity는 유지하면서 target mesh의 shape으로 서서히 변형시키는 task
	
**Motivation**) \
기존 Method들은 complexity때문에 source, target mesh사이의 Correspondence를 찾거나 target shape으로 interpolation을 하거나 둘 중 하나만 수행하고 sparse shape correspondence같은 supervision이 필요했다.

**Contribution**)
1) 다른 unsupervised manner과 large margin으로 SOTA를 찍었고 supervised manner와 비슷한 성능을 보였다.
2) Interpolation과 Correspondence를 동시에 수행한다.
	
**Method**) \
Source, target mesh사이의 correspondence를 구하는 과정과 계산된 correspondence를 이용하여 interpolation을 수행하는 과정으로 이루어져있다.
Correspondence 
1) Feature extractor
Input mesh에서 EdgeConv layer를 통해 local feature를 뽑고 max pooling을 통해 만든 global feature를 local feature뒤에 concat하는 방식으로 feature를 만든다. 이때 source, target mesh모두 shared extractor를 통해 feature가 계산된다.
2) Correspondence matrix
각각 계산된 source feature, target feature사이의 cosine similarity를 구하고 softmax를 취하여 nxm size correspondence matrix를 만든다. 
Interpolator
nxm size Correspondence matrix에 target mesh를 곱하면 source mesh와 비슷한 mesh들이 남을텐데 여기에 source mesh를 뺀 것(offset vector)과 source mesh와 t(0~1값을 갖는데 interpolation된 정도를 나타낸다) 세 값을 담은 feature vector Z를 만든다. 이 Z를 feature extractor와 동일한 구조의 네트워크(weight가 공유된 것은 아니다) 를 사용하여 delta를 만든다. X(t) = X + delta로 update된다. 이때 X(1) = correspondence matrix에 target mesh를 곱한 matrix 이다. 즉 X를 서서히 변형시키다가 최종 변형된 결과는 target mesh에서 source와 대응되는 mesh들만 남긴 결과가 되어야 한다.
