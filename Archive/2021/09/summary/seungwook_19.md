# SonicPrint: A Generally adoptable and secure fingerprint biometrics in Smart Devices
## Aditya Singh Rathore et al., University of Buffalo - MobiSys2020 best paper
#### Summarized by Seungwook Kim
---

**총평**: 
* Coursework에서 Paper critique 해서 읽었습니다 (지능형모바일시스템)
* 딥러닝과 관련 되어있지만, 새로운 학습적 novelty를 제안한 것은 아닙니다.
* 일반적인 지문인식을 통한 authentication이 아니라, 손가락과 휴대폰의 상호작용을 통해 발생하는 소리를 통해 사용자를 identify/authenticate하는 논문입니다. 신기한 내용이어서 재미있게 읽었습니다.
* 음성 전처리/후처리 부분은 잘 몰라서 제대로 읽지 못했습니다.
* best paper를 받을만한 innovation/실험 설정 / 실험 결과 라고 생각합니다.

**Task**: Biometric system for user identification

**Contributions**
* Hypothesizes that the FiSe(finger-induced sonic effect) from "finger" swiping on "phone" contains intrinsic fingerprint information
* Design SonicPrint: a biometric system applicable to smart devices using this FiSe
* Shows up to 97% accuracy on mobile phones, and resilience against fake-finger and replay attacks
* Note that since this method uses the 'sound' input, it does not require touch sensors - and is (in theory) applicable to all smart devices

Motivation: Adopting touch sensors in small smart devices in infeasible (hardware constraints)

**Method outline**
1. Background isolation
    * Pre-process sound input (high pass filter)
    * Sonic effect enhancement using Multi-band spectral subtraction
    * Denoising-aware wavelet reconstruction

2. Friction event detection
    * Adaptive detection via Hidden Markov Model (acoustic event detection)
    * phase-based detection & duration verificatino for robustness

3. Acoustic fingerprint analysis
    * Identify fingerprint features (by level) -> then determine fingerprint-induced sonic features
    * ex) Arch, Line-Unit, Pores are fingerprint features
    * ex) Temporal centroid, Mel-frequency cepstral coefficients are fingerprint-induced sonic features
4. Ensemble classification
    * Uses ensemble of the following models for final identification:
        * Logistic Regression
        * SVM
        * Random Forest
        * Linear Discriminant Analysis
        * Gaussian Mixture Model


**Evaluation / Discussions**
* based on data & reponses from 31 users

* Balanced accuracy around 80% ~ 90% based on the type of interaction (type of swipe)
* Reaches up to 97% when the surface is rough, and the sound is more distinguishable
* Successfully eliminates alien fingers (untrained fingers) at test time
    * FP rate around 2%

    ---
* As the number of subjects increase, performance decreases
    * But usually do not register a lot of subjects in one phone
    * After 15 subjects, learns more accurate features for better identification! (performance bounces)
* more suitable for rough spaces vs smooth spaces
* The more curved the surface, lower performance
    * since only partial fingerprint is in contact with the surface
* Performance is proportional to complexity of swipe pattern
    * more complex -> longer length -> more user-specific information for identification
* Performance also depends on position of swipe w.r.t microphone position
* Resilient against fingerprint phantom attack (fake finger) and replay attack (record sound and replay)
    * due to different surface characteristics & small sound
* May be vulnerable to inaudible ultrasound signals
* Not robust when trained only in controlled environment (with controlled noise)
