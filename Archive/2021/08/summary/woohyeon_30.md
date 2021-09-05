# Learning to Diversify for Single Domain Generalization
### Zijian Wang et al., University of Queesland - ICCV 2021
### Summarized by Woohyeon Shim

- **Task:** single domain generalization
- **총평:** sample generation 기반의 generalization 논문. MI를 도입하여 generation에서는 MI를 낮추는 쪽으로 학습하여 sample diversity를 높이고 classifier에서는 반대로 MI를 높이는 쪽으로 학습하여 생성된 image에 대한 compact한 feature를 얻도록 함. generation은 간단하게 conv-transposed conv pair로 구성하였고 중간에 AdaIN과 비슷한 transformation으로 style을 바꾸는 방식을 채택함. 이때 transformation을 여러개 두어 multiple style를 적용가능하도록 하였음. 결과는 generalization 모든 벤치마크에서 가장 좋은 성능을 보였으며 ablation도 잘 되어있음. 글도 군더더기 없이 깔끔하게 작성되어 있음. 이쪽 분야를 한다면 참고하기 아주 좋은 논문임.
- **Diverse sample generation (out-of-distribution, unseen styles)**
    - **Style-complement module G(·; θ_G ) : x → x+**
        - Generate K versions of x+ with different styles {μ_k , σ_k} from x.
        - with transformation layers (convolution + style modulation + transposed convolution).
            - Convolutional layer: outputs an feature map f_k \in R^{h*w*c} given x
            - Style-learning layer: T(f_k ; θ_G ) = σ_k ∗ (f_k − μ_k) / σ + μ_k
            - Transposed convolutional layer: reconstruct to the original image dimensions of x.
        - Final outcome: linear combination of the augmented images x+_k with randomly sampled scalars from a normal distribution.
    - **MI is minimized between the source and the generated images to diversfy images**
        - **Compute MI in the latent feature space.**
            - first transforms images x and x+ to latent vectors z and z+ with feature extractor F (·; θF )
            - I(z;z+) = E_p(z,z+) [log p(z+|z)/p(z+)] 
            ≤ Ep(z,z+) [log p(z+ |z)] - Ep(z)p(z+)[log p(z+|z)]
        - Since the conditional distribution p(z+|z) is intractable, we **adopt a variational distribution q(z+|z)**, that **employs a neural network parameterized by θq to** approximate the upper bound I^(z; z+) of mutual information
            - I(z; z+) = 1/N Sum_i=1^N [log q**θ**(z+_i | z_i) - 1/N Sum_j=1^N log q**θ**(z+_j | z_i)]
    - **Semantic consistency loss**
        - the module may introduce noise or generate images with distorted semantic information from original source images. (e.g., when the variance shift σ_k equals to 0, the generated images will become meaningless)
        - thus limit the conditional distribution shift from the source distribution by the class-conditional maximum mean discrepancy (MMD) in the latent space.
- **Discriminative style-invariant representation learning**
    - **MI among samples belonging to the same category is maximized;** use supervised contrastive loss for maximizing MI.
    - **Task loss** with cross-entropy loss on both the source image X and the generated images X+
    - **Minimizing difference ∆ between I(z; z ) and the upper bound of I(z; z+) by KLD**
        - ∆ = KLD(p(z+, z) ∥ qθ(z+, z)) = Ep(z,z+)[log(p(z+|z)p(z)) − log(qθ(z+|z)p(z))] = Ep(z,z+)[log p(z+|z)] − Ep(z,z+)[log qθ(z+|z)].
        - ∆ is supposed to be only affected by qθ(z+|z) since p(z+|z) is not related to θ; thus minimizing the negative log-likelihood qθ(z+|z) between z_i and z+_i.
- **Experiments**
    - **L2D achieves the highest average performance on all datasets and is generally more robust on larger domain shift.**
    - **Digit** - MNIST, SVHN, MNIST-M, SYN, USPS
        - each one is different from the rest of the domains in font style, background, and stroke color.
        - use MNIST as the source domains and test on the others
        - ranked 2nd on USPS since USPS and MNIST share very similar stroke styles.
    - **Corruptted CIFAR-10** - 15 corruptions from 4 main categories (weather, blur, noise, and digital) and has 5 levels severities
        - train on the training split and test on the corrupted test split.
        - the gain is small under severity level one, but gradually increases when the level goes up.
    - **PACS** - photo, art painting, cartoon, sketch
        - use photo images as the source domain and evaluate models on the rest.
        - achieve large performance margin on sketch domain, which has the largest domain shift.
    - **Ablation on PACs**
        - w/o style complement module (just having variational approximation of z in backbone model): 10% of decline showing the importance of image generation.
        - w/o style modification (mean & var change): 1.35% decline
        - w/o Min MI (tends to generate images following source distribution): 1.26% decline
        - w/o Max MI (mapping diverse styled images from the same class not to closer in the embedding space): 3.76% decline due to the lace of generalization.
        - K - gradually increasing as the style-component module combines more transformations. (stablized at around k=5)
    - **tSNE visualization:** form discriminative clusters for target domains, but still shows the large intra-class variations.
