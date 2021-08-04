# Putting NeRF on a Diet: Semantically Consistent Few-Shot View Synthesis 
### Author Information - ICCV 2021 Oral
#### Summarized by Yoonwoo Jeong
---

**Task**: novel view synthesis with a few inputs. 

 

**Motivation**: Although pixelNeRF has shown clear rendering qualities in few-shot view synthesis, it lacks semantically consistency of rendered images. This paper proposes a method to improve semantic consistency by adopting CLIP, unsupervised representation learning method with an Internet data collection. 

 

They have observed that **CLIP's representations are similar when the input images are capturing the same object in a different view**. 

 

**Method**: They follow the original training pipeline of NeRF with additional training process. They first augment the pose among the distribution of poses. Then they render an image from the augmented pose. Finally, they calculate the semantic similarity, viz, **the similarity of representation extracted by CLIP**. The estimated similarity is jointly optimized with the NeRF's photometric loss. 

 

**Overall**: \
    - It is quite clear that the proposed model improves the rendering quality by jointly optimizing the photometric loss with semantic consistency. \
    - Unlike the goal of NeRF, overfitting networks to the scene, this method targets to regularize the NeRF network for better generalizability on unobserved scenes. \
    - However, this method is not evaluated when sufficiently many images are provided as an input. It might be better if it were evaluated in a such condition.