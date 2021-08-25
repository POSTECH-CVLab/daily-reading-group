# Density Estimation using RealNVP
### Laurent Dinh et al., Montreal Institute for Learning Algorithm - ICLR 2017
### Summarized by Woohyeon Shim

- **Task:** develop tractable yet expressive density estimation model for high-dimensional data with real-valued non-volume preserving (realNVP) transformation
- **총평:** NICE를 기반으로 여러가지 CNN과 관련한 기법들을 접목시켜 처음으로 real image에서 그럴듯한 생성 결과를 보여준 논문. NICE의 가벼운 확장이라 볼 수 있지만 NICE가 나온지 2년후에 출판된 걸 보면 중간에 시행착오를 많이 겪은 것으로 보임. NICE를 읽은 후에 가볍게 읽을 수 있는 논문.
- **Novelty: applying following components to NICE**
    - Powerful bijective function; affine coupling layer
    - Partitioning for convolution
    - Multi-scale architecture
    - Batch normalization
- **Powerful bijective function; affine coupling layer**
    - split x into two part x[1:d] and x[d+1:D]
    - forward computation (encoding)
        - y[1:d] = x[1:d]
        - y[d+1:D] = x[d+1:D] * exp(s(x[1:d])) + t(x[1:d])
    - inverse computation (sampling)
        - x[1:d] = y[1:d]
        - x[d+1:D] = (y[d+1:D] − t(y[1:d])) * exp(− s(y[1:d]))
    - s(.) and t(.) stands for scale and translation, and are functions from R[d] → R[D−d].
    - ∂y / ∂x^T = [Id, 0; ∂y[d+1:D] / ∂x^T[1:d], diag(exp(s(x[1:d]))]
    - **Jacobian determinant: exp(sum_j s(x[1:d])_j); does not involve computing the Jacobian of s or t, so those functions can be arbitrarily complex. (hidden layers of s and t can have more features than their input and output layers)**
- **Partitioning for convolution**
    - y = b * x + (1 − b) * (x * exp (s(b * x)) + t(b * x))
    - here, both s(·) and t(·) are rectified convolutional networks
    - b: spatial checkerboard patterns or channel-wise masking. (the half is masked / the other not)
    - composed multiple masking consecutively with the same type in an alternating fashion (one that masked before becomes activated) to uniformly use every component.
- **Multi-scale architecture**
    - squeezing spatial dim. to the channel: n × n × c  ⇒ n / 2 × n / 2 × 4c
    - at each scale: applied three coupling layers with alternating checkerboard masks, a squeezing function, and finally three more coupling layers with alternating channel-wise masking. (the channel-wise masking is chosen so that the resulting partitioning is not redundant with the previous checkerboard masking)
    - for final scale: applied four coupling layers with alternating checkerboard masks.
    - at the intermediate layers, factor out half of channels from output to reduce computational and memory cost. this is done at regular interval at each level.
    - all variables which have been factored out at different scales are concatenated to obtain the final transformed output. As a consequence, the model must Gaussianize units both at a finer scale (in an earlier layer) and a coarser scale (in a later layer). This has the practical benefit of distributing the loss function throughout the network, following the philosophy similar to guiding intermediate layers using intermediate classifiers.
- **Batch normalization**
    - use deep residual networks with batch normalization and weight normalization in s and t.
    - also use apply batch normalization to the whole coupling layer output. Jacobian and its determinant can be easily updated by re-scaling batch statistics on each channel dimension.
    - alleviated the instability problem that practitioners often encounter when training
    conditional distributions with a scale parameter through a gradient-based approach.
- **Experiments on CIFAR10, CelebA, ImageNet(64x64), LSUN**
    - the generated samples look not only globally coherent but also more sharper than VAE;  real NVP does not rely on fixed form reconstruction cost like an L2 norm which tends to reward capturing low frequency components more heavily than high frequency components.
    - shows smooth transition when interpolating on latent variables.
    - still lag behind for generating ImageNet and LSUN datasets.
