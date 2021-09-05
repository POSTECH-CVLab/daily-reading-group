# Deep Learning on Lie Groups for Skeleton-based Action Recognition
### Zhiwu Huang et al., ETH Zurich - CVPR 2017
### Summarized by Woohyeon Shim

- **Task:** skeleton-based human action recognition
- **총평:** skeleton을 Lie group representation으로 변환하여 deep network를 학습하는 방식 제안. Liegroup으로 변환하여 푸는 알고리즘은 이미 존재하며 그 효과가 있음이 검증 되었으며, 본 논문은 해당 representation을 deep network로 학습하는 것을 main novelty로 가져감. 메인 이슈는 weight이 3x3 rotation matrix로 제한되기 때문에 backprop 이후에도 그 그룹에 속해야 한다는 점인데, tangent space를 이용하여 유지되도록 하였음. 또한 Liegroup manifold의 output을 Euclidean manifold의 output으로 변환해야 했는데 이것을 위해 logmapping layer란걸 제안함. 하지만 최종 결과는 그렇게 효과적이지 않았는데 그 이유는 1) pooling이 temporal dim.에 대해 적용되기 때문에 clip length에 따라 쌓을 수 있는 layer가 제한됨, 2) 중간중간 non-linearity layer를 붙이기 힘듦이지 않을까 싶음. 아, 그리고 한가지 인상적이었던 것은 deep network라 제안된 것임에도 불구하고 모든 실험 결과가 cpu로 학습된 것임.
- **A body skeleton (V,E)**
    - V = {v1,...,vN} = the set of body joints
    - E = {e1 , . . . , eM } = oriented rigid body bones (parts)
    - R_m,n = rotation matrix that models relative geometry from e_m to the local coordinate system of e_n.
    - local coordinate system of e_n = minimum rotation that takes the starting joint as the origin and coincide the edge with x-axis.
- **Lie Group representation?**
    - A moving skeleton at the time instance t is represented with a curve on the Lie group SO3 × . . .×SO3 : (R1,2(t), R2,1(t) . . . , RM−1,M (t), RM,M−1(t))
        - R_m,n forms special orthogonal group SO_n, which is actually a matrix Lie group.
        - R_m,n has a Riemannian manifold structure that is differentiable.
- **RotMap Layer**
    - Lie group feature learning often suffer from temporal misalignment
    - This layer performs transformations on input rotation matrices to generate new rotation matrices for more reliable matching.
        - f_r ((R1ˆ{k-1} ,R2ˆ{k-1} ...,RMˆ{k-1} );W1ˆ{k} ,W2ˆ{k} ...,WMˆ{k})
        = (W1^{k}R1^{k-1} , W2^{k}R2^{k-1},..., WMˆ{k}RMˆ{k-1})
        = (R1ˆ{k},R2ˆ{k} ...,RMˆ{k})
        - transformation matrix Wi^{k} ∈ R3×3 should also be rotation matrices.
        - both the data and the weight spaces correspond to a Lie group.
    - To update the weight matrices while keeping it on the Lie Group, one should compute Riemannian gradient on the manifold SO3 by transporting the euclidean gradients onto the corresponding tangent space
        - Substract the normal component at W_k^{t+1} when transporting the gradient from a point W^t_k to another point W_k^{t+1}; Searching along the tangential direction takes the update in the tangent space of the SO3 manifold.
        - Then, such update is mapped back to the SO3 manifold with a retraction operation.
- **RotPooling Layer**
    - Lie group representations tend to be extremely high-dimensional, thus needs dimensionality reduction.
    - spatial pooling (grouping features on each pair of basic bone): max({Rm,n, Rn,m})
    - temporal pooling (for a motion sequence): (max({R1,2^{1} ...,R1,2^{p} })...,max({RM−1,M ^{1} ...,RM−1,M^{p}})) ; p is the number of frames for pooling
- **LogMap Layer (penultimate layer)**
    - Lie group representations is in non-Euclidean domains
    - We design the logarithm map (LogMap) layer to flatten the Liegroup SO3 ×...×SO3 to its Lie algebra so3 ×...× so3: (log(R1^{k−1}), log(R2^{k−1}) . . . , log(RM^{k−1}))
    - we can explore the relationship between the logarithm map and the axis-angle representation as: log(R) = 0, if θ(R)=0 ; θ(R)/(2 sin(θ(R)))(R − RT )  otherwise.
    - After LogMap layer, the outputs can be concatenated directly frame by frame within one sequence due to Euclidean nature, and add any regular layers (ReLU and FC) upon it. We can also employ LSTM over temporal outputs to learn temporal features.
    - Finally, they append a FC and softmax layer to output class probabilities.
- **Experiments**
    - three standard 3D human action datasets: G3D-Gaming, HDM05, NTU
    - baseline: manifold-based approaches; special euclidean group (SE), special orthogonal group (SO)
    - result: not so interesting since it is not SoTA and the gain of appending layers is highly-dependent on temporal length of a clip.
