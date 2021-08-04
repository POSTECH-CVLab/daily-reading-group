# On the difficulty of training Recurrent Neural Networks 
### Razvan Pascanu, Yoshua Bengio, Tomas Mikolov - ACM 2012
#### Summarized by Seungwook Kim
---

**Task**: Preventing Exploding/Vanishing gradients \
 (Gradient clipping)
 
**Motivation**: When training RNNs, exploding / vanishing gradient problem may occur. \
Exploding gradients: Large increase in norm of gradient during training. \
- caused by explosion of long term components. \


Vanishing gradients: Long term components go exponentially fast to 0, making it impossible for the model to learn correlation between temporally distant events.
 
**Method**: \
Solving exploding gradients: Gradient clipping
 
```
 if norm(g) > threshold : 
     g = g * (threshold / norm(g))
```
threshold: a hyperparameter. Can be easily chosen by looking at statistics on the average norm over a large number of updates. \
Training is not very sensitive to this hyperparameter, and algorithm behaves well even under small thresholds.
 
Solving vanishing gradients: Regularization \
-> forces the error signal not to vanish when travelling back in time \
-> forces the Jacobian matrices to preserve norm only in the relevant directions.
 
**Evaluation:** \
SoTA on pathological synthetic datasets / polyphonic music prediction
 
**총평:** \
Gradient clipping을 사용해본 적은 없지만, 많은 논문들에서 (연구실 내에서도) 사용되기에 그 시초가 되는 논문을 읽어보았습니다.
Motivation이 아주 명확하고, clipping 방법을 채용하는 배경 (valley with a single steep wall in the error surface) 또한 알 수 있어서 납득이 잘 가는 논문이었던 것 같습니다.
Writing도 군더더기 없습니다.