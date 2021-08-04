# GIRAFFE : Representing Scenes as Compositional Generative Neural Feature Fields
### Author information - CVPR 2021 best paper)
#### Summarized by Jinoh Cho
---

**Task** : Controllable image synthesis pipeline which can be trained from raw image collection without additional supervision


 

**Motivation** : Previous works is not enough to controll the attributes(camera pose, object poses, shape, appearance) of synthesized images. Further, only few works consider the compositional nature of the scenes.

key limitation of NeRF and GRAF is that the entire scene is represented by a single model. Authors were interested in disentangling different entities in the scene.


 

**Method** :


	
1. N개의 shape code와, appearance code 그리고 각 entity에 대한 affine transform 정보까지 sampling함.
	
2. 해당 정보들을 통해서 N개의 conditional radiance field를 estimate함. (기존 NeRF는 volume density와 color를 output하지만 여기서는 color 대신 feature를 output으로 함.)
	
3. 그리고 composition operator를 통해서 combination feature를 생성하고 이를 feature를 Rendering하는 encoder에 태워서 이미지를 생성(Neural Rendering)하게 됨.
	
4. 생성된 이미지와 real image에 gan loss만으로 학습을 진행함.



**Question point**:

section 3.1에 object representation part에 k inverse를 하는 이유를 모르겠음..

Strong Points:


	
1. Color가 아닌 resolution이 작은 feature를 volume rendering을 하고 이를 neural rendering 방법을 이용하여 이미지를 생성하기에 기존의 NeRF의 computational cost를 확연히 줄일 수 있었음.
	
2. Compositional Operator를 통해서 single object가 아닌 composition을 통한 n object image를 생성할 수 있었음.


 

**Weak Points**:


	
1. Struggle to disentangle factors if there is an inherent bias in the data.(이건 대부분 다른 방법도 그러지 않나유?)


 

**GRAF와 다른점**:


	
1. the composition operator를 사용함으로써 compositional conditional radiance fields를 학습할 수 있었음.
	
2. Color 대신 feature를 생성한 이 후에 neural rendering으로 image를 합성하기 때문에 기존 GRAF나 NeRF의 computational cost를 확연하게 줄일 수 있었음.