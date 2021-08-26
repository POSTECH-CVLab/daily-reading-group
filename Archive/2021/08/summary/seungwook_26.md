# PonderNet: Learning to ponder
### Andrea Banino., DeepMind - ICML2021 Workshop
#### Summarized by Seungwook Kim
---

**총평**:
* "Number of computational steps" 를 학습한다는 컨셉이 신기했다. 필요한 만큼의 계산량만 사용한다는 점에서 특이했는데, 이런 motivation을 가진 work이 처음은 아니지만 (Adaptive Computation Time, Adaptive Early Exit Networks) 아직 발전의 여지가 많아 보인다.
* 설명하는 이론과 개념은 이해가 되지만 이게 어떻게 구현 가능한 네트워크로 이어지는지에 대한 이해를 잘 못 한 것 같다. 그래도 전반적인 '개념'을 이해하는데 문제는 없었는데, 구현해보라고 하면 바로 하지는 못 할 것 같다.
* 진행중인 / 진행할 연구에 도움이 될 지는 모르겠으나, 이전에 리뷰했던 Recurrent Parameter Generator와 같이 학습한다면 1. 정해진 weight들을 바탕으로, 2. task에 알맞은 computation만을 사용하는 네트워크를 만들 수 있지 않을까 하는 생각이 들었다. 연구실 내에서 해볼 수 있는 연구일까
* Lucidrains가 구현중인 Ponder-transformer도 결국 PonderNet에 해당된다. 본 논문에서도 transformer architecture를 사용하여 pondernet을 구현한 실험이 있기 때문.
* evaluation에 사용된 데이터셋이나 task 자체가 생소한 감이 있었음.
---


**Task**: Learning to achieve effective compromise between training prediction accuracy, computational cost and generalization
* "Learning to ponder"
* **Pondering**: Adjusting computational budget based on the complexity of the task they are learning to solve
  * previously done by ML practitioners

**Novelties & Contributions**:
* Fully differentiable with low-variance gradient estimates without bias (unlike previous works)
* Reformulate halting policy as a **probabilistic model**

**Method** \
Considers supervised setting

PonderNet architecture requires a **step function**
* pred_y, next state, probability of halting = step_function(x, current_state)
* step function can be any neural network (MLPs, LSTMs, Transformers...)
* Step function is applied **recurrently** up to N times
  * N is a hard upper limit
  * Output is from a dynamic nuymber of steps n <= N
  * probability of halting: follows a Markov Process i.e. P(halt) = P(halt now | prev didn't halt)
  * final prediction: prediction made at step n when it halts

Maximum number of pondering steps, N
* sum of probabilities should sum up to 1
   * unrolling the step function is only possible for a limited number of iterations
* Most effective / interpretable way: minimum cumulative probabilirt of halting
  * N is the smallest value of n such that **sum of probabilities up to n > 1 - e**
      * e is positive near 0 (0.05 in the paper)
* Therefore, compute up to N steps, where N is predefined using the above steps.

Loss functions
* Reconstruction Loss
  * expectation of pre-defined reconstruction loss (cross entropy, MSE...depends on the task) across halting steps.
* Regularization loss
  * KL divergence between distribution of halting probabilities and the geometric prior distribution on the halting policy (using hyper-parameter)
* Need to fulfill original task, while being similar to prior distribution on the halting policy.

**Result**
* Parity Task
  * explained in previous work, 읽어보진 않음
  * 어쨌든 baseline (ACT) 보다 higher accuracy, with more efficient use of thinking time.
* bAbI question-answering
  * SoTA results , faster, lower average error
  * main comparion: Universal Transformer using ACT.
  * The paper: Universal Transformer using PonderNet. 
* Paired associative inference (PAI) task
  * on par with MEMO (specifically designed for the PAI task)
  * outperform UT (previous work?) while using same architecture.
 
