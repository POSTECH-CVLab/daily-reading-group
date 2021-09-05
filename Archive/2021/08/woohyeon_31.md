# Transforming Auto-Encoder
### G. E. Hinton et al., University of Toronto - ICANN 2011
### Summarized By Woohyeon Shim

- **Task:** recognizing objects in image with capsule.
- **총평:** capsule이란 개념을 처음 도입한 논문. feature encoding 할 때 invariance를 넘어 equivariance가 필요함을 보이고 간단한 생성 실험을 통해 그것의 활용성을 보였음. 아쉬운 점은 서두에 제안한 동기는 representation learning 중심으로 서술되어있는데 실험은 연관이 크게 없는 테스크에서 한 것임. 하지만 개념적으로 equivariance와 capsule의 관계, 이후 논문에서 capsule을 사용하는 이유 등의 기반 지식을 얻는덴 좋은 논문인 것 같음.
- **Why capsule?**
    - aiming for viewpoint invariance using a single scalar output in the activities of "neuron" is not sufficient to recognize object correctly; high-level features have a lot of uncertainty in their poses.
    - replicated copies of exactly the same weight kernel are far from optimal for extracting the pose of a visual entity over a limited domain, especially if the replication must cover scale and orientation as well as position.
    - hand-engineered features (SIFT) produces a whole vector of outputs including an explicit representation of the pose of the feature, but using NN is more promising since it provides an efficient way of adapting features to the domain.
    - for object recognition, it requires knowledge of the precise spatial relationships between high-level parts.
- **What is capsule?**
    - perform quite complicated internal computations on their inputs that output a whole vector of instantiation parameters.
    - encapsulate the results of these computations into a small vector, not a scalar, which contains,
        - invariant information: the probability of visual entity being present within a limited domain of viewing condition.
        - equivariant information: a set of "instantiation parameters" that may change as the entity moves over the appearance manifold with respect to the viewing condition. The instantiation parameters represent the intrinsic coordinate of the entity on the appearance manifold.
    - capsule provide a simple way to recognize whole by recognizing their parts.
        - suppose two active capsule, A and B, have the right spatial relationship to activate a higher-level capsule, C.
        - given pose of capsule A as matrix of T_A and capsule B as T_B, which specifies the transform between the canonical visual entity and the actual instantiation of that entity, each can predict the pose of C (T_C) by the part-whole coordinate transform T_AC or T_BC, respectively, which relates the canonical visual entity A or B to the canonical visual entity of C.
        - If the predictions from A and B are a good match, the instantiations found by capsules A and B are in the right spatial relationship to activate capsule C and the average prediction of T_C tells us how the larger visual entity is transformed relative to the canonical visual entity of C.
- **How to compose capsule (or part-whole hierarchy)?**
    - Learn from pairs of transformed images and auto-encoder.
    - Case 1: output shifted images with desired shift ∆x and ∆y.
        - Suppose a single-hidden layer architecture where a number of capsules locate before the final layer.
        - Each capture outputs x, y, and p using logistic "recognition units".
        - The capsule has also its own "generation units" that computes the capsule's contribution to the transformed image.
        - The contributions that the capsule's generation units make to the output image (x + ∆x and y + ∆y) are multiplied by p.
    - Case 2: more complex 2-D transformation - Each capsule output a full 2-D affine transformation and predict the target output image by generation units after applying known transformation matrix.
    - Case 3: modeling changes in 3-D viewpoint
        - modeling viewpoint using matrix multiplication should make it far easier to cope with 3-D.
        - make ground-truth stereo images of various types of cars used computer graphics.
        - the network consist of 900 capsules, each with 11 x 11 pixel receptive fields and arranged on a 30 x 30 grid over 96 x 96 image. (no weight sharing)
        - each capsule outputs 3x3 matrix representation of the 3-D orientation of the feature as well as a probability. this 3x3 matrix is then multiplied by the real transformation matrix between the source and target images, and the result is fed into the capsule's single layer of 128 generative units.
        - The generation unit activities are multiplied by the probability and the result is used to increment the intensities in a 22 x 22 patch of the reconstructed image centered at the center of the capsule's 11x11 receptive field.
