# PPFL: Privacy-preserving Federated Learning with Trusted Execution Environments
## Fan Mo et al., - MobiSys 2021 Best paper
### Summarized by Seungwook Kim

**총평**
* AIGS700D 과목의 일환으로 읽게 됨.
* Component적으로 novel한 면은 없으나, 여기서 제안하는 방법을 가능하도록 하는 파이프라인을 구축하여 safety/privacy까지 챙긴 부분이 큰 novelty로 작용했다고 생각함.
* Vision area에 논문을 작성할 떄도 사용성과 안전성을 더 고려한 연구갖 진행된다면 더 좋을 것 같다는 생각이 듦.
* 하지만 TEE가 GPU-compatible하지 않다는 comment가 있었는데, 그런 명에서 해당 논문의 실 사용성이 어떻게 될지 궁금함.

**Task & Motivation**:
* Privacy-preserving federated learning
* GIven scenario: Model is trained on server, distributed to phone. The model is trained with additional data collected from the phones.
* This is not secure, as an attacker would be able to observe the photos taken from phones.
* A naive solution was to send the 'layer-wise' gradients only to the server for training, so that the model will not have direct access to the collected data.
* However, with only the gradients, they can perform 1) membership attack, 2) gradient attack to reconstruct the images which incurred those gradients. Therefore, sending the gradients alone is not safe.

**Method**:
* The main method: Exploit TEE (Trusted Execution Environments) in the hardware.
    * Main assumption: data stored/transmitted in TEEs are well encrypted, such that the data on TEEs will not be accessible to the attacker
* Therefore, send gradients (layer-wise) using TEEs!
    * However, TEEs incur high latency, and a lot of hardware only support a small storage size for TEEs
    * THe original method is not operable when using TEEs, since ALL layer-wise gradients cannot fit on the TEE.
* Therefore, propose "layer-wise training"
    * only send a "single-layer gradient" for each transmit to server
    * which is much smaller than all layer-wise gradients, and can fit into the TEE.
    * Shows that layer-wise training is almost as good as full-layer training, and sometimes even better.
        * THere is no theoretical explanation on this point, but I think it is similar to situations where few-layer finetuning is better than full-model finetuning in transfer learning.
* This paper does not handle how TEEs work, but the existence of TEEs again motivate models with lower memory/computation overheadd IMHO.
