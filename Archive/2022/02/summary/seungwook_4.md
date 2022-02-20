# KPConv: Flexible and Deformable Convolution for Point Clouds
## Hugues Thomas Yu et al., Mines ParisTech/FAIR(Meta AI)/Stanford U -  ICCV 2019
#### Summarized by Seungwook Kim
---

**Short-sentences summary**
* The paper proposes KPConv, a flexible and deformable convolution for point clouds. In works in a convolution-like sense, where each point is processed using a fixed, predefined kernel(rigid kernel) OR a deformable kernel, which shows better results/generalizability for certain datasets with varying density and harder geometrics for processing.
* KPConv enables the usage of point-wise calculation for large-scale point clouds, not using voxelization for efficiency / speed. Since FCGF was also introduced in ICCV 2019, KPConv / FCGF would be an important comparison to make when deciding on the usage of points vs voxels.
* Results outperform existing SoTA methods at the moment (DGCNN, SubSparseCNN, PointCNN, PointNet variants...)
* Deformable kernel works better under constrained number of kernel points K. Also, the effective receptive field of deformable kernels are more focused on the objects of interest, unlike rigid kernels where the effective receptive field focuses on other parts of the object as well.
