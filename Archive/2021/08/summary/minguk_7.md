# Denoising Diffusion Implicit Models
### Jiaming Song, Chenlin Meng, Stefano Ermon - ICLR 2021
#### Summarized by Minguk Kang
---
Task: 디퓨전 모델의 느린 inference time을 빠르게 할 수 없을까?
 
Motivation: DDPM이 high-dimensional dataset 생성을 할 수 있다는 것을 성공적으로 보였음에도 불구하고, Inference time에 있어서는 GAN보다 효용성이 많이 뒤떨어진다. 따라서, Inference를 할 때 time T를 줄여서 그 속도를 높힐 수는 없을까?
 
Method: 우선 Non-Markovian chain q(x_{1:T}|x_{0}) := q(x_T|x_0)\Pi q(x_{t-1}|x_t, x_0)과 q(x_{t-1}|x_t, x_0)을 정의하고, 이를 통해 diffusion transition q(x_t, x_0)가 DDPM의 그 녀석과 수식이 같음을 보인다. 다음으로, 위의 Non-Markovian chain에 Bayes' rule을 적용하여 forward process (Non-Markovian)을 정의한 다음 negative log-likelihood의 다른 버전인 J_sigma를 정의한다. 정의된 J_sigma는 DDPM의 L_{\gamma}과 상수를 제외하면 동치이기에 (Theorem 1), DDPM 모델을 통해 학습된 모델을 통해 reverse process과정만 바꿔서 inference가능하다는 것을 보였고, J_sigma는 p(x_t|x_0)가 주어진 conditional gaussian이면 되므로 이를 만족하는 어떠한 forward process든 reverse process로 바꿔서 사용할 수 있다는 것이 저자들의 메인 주장이자 방법이다. 따라서, 새로 정의된 단축된 forward process에서 reverse process를 정의하였고, \sigma =0 인경우 (deterministic reverse process를 가지는 경우)를 DDIM (Denoising Diffusion Implicit Model)이라고 명명하였다. DDIM은 DDPM과 달리 짧은 reverse process를 가지는 경우에도 만족할만한 이미지 생성 결과를 보여주었고, 이를 통해 계산 부담과 생성 성능사이의 trade-off 조절할 수 있는 새로운 모델을 제안하였다.
 
총평: 최근 읽은 논문 중에 재미있게 읽은 논문 Top-3안에 들어가는 논문. Non-Markovian process에서 부터 L_{\gamma} + C = J_{\alpha}를 증명하는 과정까지의 논리적 흐름이 정말 흥미로웠고, 학습된 DDPM을 inference 하는 부분만 수정하여 더욱 효율적이게 이미지 생성을 할 수 있다는게 정말 놀라웠다. 또한, 수학적 귀납법을 사용하여 증명한 Lemma 1은 저자가 정말 천재가 아닌가라는 생각을 들게 하였다.
