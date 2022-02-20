# CoFiNet: Reliable Coarse-to-fine Correspondences for Robust Point Cloud Registration
## Hao Yu et al., MunichU - NeurIPS 2021
#### Summarized by Seungwook Kim
---

**Short-sentences summary**
* The paper proposes CofiNet, a point cloud registration algorithm that outperforms SoTA methods especially in ther regime of lwo overlap ratio between large-scale point clouds (3DMatch, 3DLoMatch). 
* No comparison has been made with DHVR (Junha Lee et al., ICCV 2021).
* THe overall motivation & designf follows LoFTR (and thus, SuperGlue:). CoFiNet aims to establish coarse-to-fine correspondences (like LoFTR), where it **strengthens features for better coarse-level matching** and **the coarse-level matches are finalized with a differentiable sinkhorn-based matching layer**.
* The paper uses KPConv as the overall architecture - for the encoder (for downsampling - coarse-level correspondences), and also for the decoder/upsampler when establishing fine-level correspondences.
* There are some weighting functions related with the GT overlap ratio between the coarse components for supervision, which is the only 'completely novel' component that can be found in comparison to "KPConv + LoFTR".
* In my opinion, a lot of the paper was dedicated to explaining common details in a hard, formal way ('jargon' in a way), and the paper was overall not **very** smooth to read. 
