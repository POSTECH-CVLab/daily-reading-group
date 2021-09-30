# Dynamic Convolution: Attention over Convolution Kernels
### Yipeng Chen, Xiyang Dai, Mengchen Liu, Dongdong Chen, Lu Yuan, Zicheng Liu - CVPR 2020
#### Summarized by Yoonwoo Jeong

---

**Motivation**

Simply stacking convolution kernels result in large computational budgets. They propose a method that increases model complexity without increasing the network depth or width in an efficient way.
Within the reasonable cost of model size, dynamic kernel aggregation provides an efficient way to boost representation capability.

**Method**

Since training DYConv is much more difficult than the static-Conv, they provide two keys for optimization strategies.

- Constraining the attention output to satisfy sum-to-one to facilitate the learning of the attention model. (Adopted SoftMax)
- Flattening attention in early training epochs to facilitate the learning of convolution kernels. (Done by annealing the temperature in the SoftMax operation)

**Task & Result**

- Image classification (ImageNet) and Human Pose Estimation (COCO2017)
- For both tasks, the proposed dynamic convolution module enhances previous convolutional modules, resulting in improved performance

**Comment**
- The idea is quite simple and intuitive. In my opinion, the reason why this paper is accepted is its meticulous ablation studies. Its ablation studies strongly support the authors' arguments.
- However, demonstrating CNN model's behavior with two tasks is not sufficient. The authors should provide more experiments that attempt to solve other tasks.
