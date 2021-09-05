# Harmonic Networks: Deep Translation and Rotation Equivariance
### Daniel E. Worrall et al., University College London - CVPR 2016
### Summarized by Woohyeon Shim

- **Task:** Make a CNN exhibiting equivariance to patch-wise 360-rotation by replacing regular CNN filters with circular harmonics.
- **총평:** Circular filter bases를 통해 rotation equivariant를 달성하고자 한 논문. 이전 논문이 작고 정해진 그룹(90도 회전, 반전)에서만 rotation equivariant를 만족하는 것이 문제라고 제안하였지만 본 논문도 그룹 크기에 의해 계산량이나 메모리가 quadratic하게 증가하기 때문에 그룹 크기를 늘리는 것에 제한이 있고 근본적인 문제는 풀지 못함. 실험에서도 오히려 더 작은 그룹(order=2)만 사용했는데 이에 대한 ablation이 없는 것이 아쉬웠음. 이런 이유로 결과 또한 그렇게 인상적이지 않은데 방법에서 circular harmonic을 제안했다는 것 말고는 크게 새로운 점이 없는 것 같음. 이쪽 분야를 한다면 한 번쯤 읽어볼 수 있는 논문.
- **Circular harmonics (∈ steerable filters)?**
    - **Filter representation: W_m(r,φ;R,β) = R(r)e^{i(mφ+β)}**
        - r,φ are the spatial coordinates of image/feature maps
        - m ∈ Z is known as the rotation order.
        - During training, we learn the radial profile and phase offset terms.
            - R : R+ → R is a function, called the **radial profile**, which controls the overall shape of the filter.
            - β ∈ [0,2π) is a **phase offset term**, which gives the filter orientation-selectivity.
        - can represent all rotated versions of a filter, using just a finite, linear combination of steering bases.
    - **Filter response**
        - Let counter-clockwise rotation of an image F(r,φ) about the origin by an angle θ be F(r,πθ[φ]) = F(r,φ−θ). As a shorthand we denote Fθ :=F(r,πθ[φ]).
        - [W_m*Fθ]=e^{imθ}[W_m*F0]; The response to a θ-rotated image **F**θ with a circular harmonic of order m is equivalent to the cross-correlation of the unrotated image F0 with the harmonic, followed by multiplication by e^{imθ}.
        - Filters are complex-valued filters, so all filter responses are complex-valued.
    - **Response properties by rotation order m.**
        - The phase of the response rotates with the input at frequency m, we say that the response is an *m-equivariant feature map.*
        - The rotation order m=0 defines invariance and m = 1 defines linear equivariance.
            - For m=0, ψθ[f_m]=e^{i·0θ}·fm=fm.
            - For m=1, ψθ[f_m] =e^{i·1θ}fm - as the input rotates, e^{iθ}fm is a complex-valued number of constant magnitude fm, spinning round with a phase equal to θ.
        - Chained cross-correlation of m1 and m2 produces a response with the order of m1 + m2.
        - Summation of two responses of the same order m remains of order m.
    - **Construction of Equivariant-CNN**
        - The sum of rotation orders along any path should be equal to M.
        - Typical nonlinearities can be adapted since they act solely on the magnitudes and maintain rotational equivariance.
- **Implementation Issue**
    - Discretization to 2D-grid; need anti-aliasing input. worked with a simple Gaussian Blur.
    - Sampling stratege on pooling; introduces multiple origins for equivariance. We use average pooling, since it uniformly shift the center of equivariance.
    - Set i_z (channels of regular CNN) = 2f (rotation orders) * i_h (channels of H_NN) to match the size of parameters.
- **Experiments;** two experiments - rotation invariant task (classification on rotated-MNIST) and rotation equivariant task (boundary detection)
    - The results is not that impressive and only slightly better than the baseline.
    - No ablation is provided on rotation order. (only used 2 rotation orders for all experiments)
    - But, it was nice attempt to test on rotation equivariant task.
