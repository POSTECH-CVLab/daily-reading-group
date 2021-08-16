# How to train your ViT? Data, Augmentation, and Regularization in Vision Transformers
## Andreas Steiner, Ross Wightman et al., Google Brain, Timm - Submitted to NeurIPS 2021
#### Summarized by Seungwook Kim
---

**Task**: Systematic study on Vision Transformers (ViTs only)
* amount of training data
* AugReg (Augmentation, Regularization)
* Model size
* Compute budget

**Motivation / Contributions**
* No comprehensive study of trade-offs between AugReg, training data size, compute budget in ViTs.
* Fills this gap by conducting empirical studies
* Jax/Flax를 사용
    * Matrix 관련 계산에는 PyTorch/TF 보다 유의미하게 빠르다고 함
* timm library 사용
    * 요새 torchvision에서 제공하는 모델보다 더 많이 사용됨 (pretrained 모델)

**Experimental Setup**:
Pretraining datasets: ILSVRC-2012, ImageNet-21K \
Finetuning datasets: CIFAR-100, Oxford IIT Pets, Resisc45, Kitti-distance
    * used original (224) and higher (384) resolutions for finetuning

used 4 variants of ViT: ViT-Ti, ViT-S, ViT-B, ViT-L
* patch size 16
* patch size 32 also for -S and -B
* Note: dropped the hidden layer in head
    * does not lead to more accurate models
    * often results in optimization instabilities
* Also trained hybrids (ResNets + ViT)
    * patch size of ViT altered to match "effective patch size" of 16 / 32

Total of 28 configurations, a combination of:
* Dropout (or not)
* Stochastic Depth (or not)
* 7 different RandAugment settings 
* Weight decay (0.1 or 0.03)

> 2 * 7 * 2 = 28 setups

1. With good use of Aug&Reg, one can (pre)train a model to **similar accuracy as by increasing the dataset by an order of magnitude (~10x)**
    * Does not hold for arbitrarily small datasets
2. Finetuning is almost always better than training from scratch on tiny datasets
    * regardless of **how much time is spent**
3. Pretraining on more data yields more transferable models on average (more generic models)
4. Significantly more cases where augmentation >>> regularization
    * for mid-sized ImageNet-1k dataset, all RegAug helps
    * for larger-sized ImageNet-21k dataset
        * keeping compute fixed (ex 30 epochs): any AugReg hurts performance except for largest model
        * increasing budget (ex 300 epochs) : smaller models still hurt performance
    * as data increases, AugReg hurts performance when **budget is fixed & model is smaller**
5. When choosing which pretrained model to transfer:
    * Choice 1: validate all pretrained models on downstream task, choose one with best val performance
    * Choice 2: choose model with best pretrained validation performance (cheaper option)
    * **Cheaper strategy works equally well on majority of the cases**
        * But not always
        * Use the more expensive option of trying all pretrained models if budget is within check
6. **Important Note**: ImageNet21k contains ImageNet1k data
    * large models pretrained on ImageNet21k may "memorize" ImageNet1k data
    * **so using validation set from ImageNet1k data when finetuning is NOT RELIABLE**
    * solution: use ImageNetV2 data as validation set (independently collected!)
        * This resolves the issue
        * **All researchers transferring from ImageNet21k to 1k are advised to follow this strategy**
7. Increasing patch size >> Shrinking model size
    * Roughly equal in throughput, but increasing the patch size shows better results


**총평**:
* Pretrain은 Adam으로 하고, finetune 은 SGD로 하던데 theoretical / empirical background가 있는지 궁금하다
* ImageNet21k에서 1k로 finetuning할 때의 issue를 발견하고 address한건 유의미한 것 같다
* 사실 그 외의 결론들은 모두 다 실험적 결론이며, 그렇게 놀라운 결과는 없다
    * Bag of tricks for Image Classification 논문에 비하면 얻어갈 점도 별로 없다
* 뭔가 당연하고 놀랍지 않은 결론들을 extensive 실험들로 입증한 느낌인데... 어느정도의 novelty라고 봐야할지 궁금하다. 과연 붙을까
