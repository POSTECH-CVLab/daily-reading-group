# Infinite Memory Transformers
## Pedro Henrique Martins et al., DeepMind - Arxiv 2021
#### Summarized by Seungwook Kim
---

**총평**: 
* Continuous attention의 개념을 처음 알게 되어 신기했다. 어쩌면 vision task에도 적용할 수 있을 것 같다.
* 비교된 베이스라인은 Transformer-XL 과 Compressive Transformer인데, 더 다양한 (특히 efficient한) baseline과 비교하면 좋았을 것 같다.
* 결국 long + discrete sequence 를 fixed length + continuous sequence로 "approximate"하여 문제를 푸는 것이 main novelty로 보이며, 따라서 sequence length가 크게 길지 않은 경우에는 Transformer-XL이 더 잘 동작하는 것이 자연스러운 결과인 것 같다.
* Continuous attention을 제안한 몇 안 되는 논문이기 때문에, 어쩌면 발전가능성이 많을 것 같다.
* Sequence modeling을 다루거나, vanilla transformer를 사용하기엔 메모리 부담이 큰 경우 읽어볼만 할 것 같다.

**Task**: Transformer Architecture
* For long sequences


**Motivation / Contributions**
* Transformer have computational limitations (memory)
* Previous approaches to this problem: Sparse attention, Reducing complexity...
    * Still depends on context length
    * **cannot deal with unbounded context**
* Proposes Infinite-former
    * Transformer extended with **unbounded** long-term memory (LTM)
    * allows model to attend to arbitrarily long contexts
    * Introduce "sticky memories" so that important information will persist (stay) in LTM

**Method outline**

Represent input sequence as a "continuous signal"
* expressed as linear combination of RBFs
    * coefficients can be obtained with closed-form solution (multivariate ridge regression)
* the number of basis RBFs can be fixed -> fixed memory requirements!

Attend over continuous signal
* Previously: discrete probaility ditribution over the input sequence
* Now: Probability **density** -> modelled as Gaussian

NOTE: Up to this point has been proposed in NeurIPS 2020, "Sparse and Continuous Attention mechanisms"

Infinite Memory Transformer
* Vanilla transformer + LTM (Long term memory)
    * LTM: stores input embeddings / hidden states of previous steps
    * May also consider STM for short-term memory (as in Transformer-XL)
* Overall Q,K,V projection and residual connection is similar
    * BUT of course, formulated differently
* Unbounded memory?
    * Input: Existing vectors from LTM, New vectors coming from STM
    * sample & contract vectors from LTM , concat with new vectors from STM
    * Recalculate the coefficient matrix
* No need for positional encoding, memory vectors represent basis coefficients in a predefined continuous space

Wouldn't this approach lose resolution for old memories?
* introduce "sticky memory"
* Attribute larger space in the LTM's new signal to relevant regions in the previous signal
* better capture long context, prevents losing relevant information


**Evaluation / Results**
Synthetic task: Sorting (based on frequency of appearance)
* To ensure decision is not made on the 'recent tokens' only, the frequency distribution is set to change over time
* Transformer XL > Infinite Transformer >=Compressive for short lengths
* Infinite Transformer > Compressive >> Transformer XL for longer lengths
    * How does Compressive transformer work?

Language Modeling task
* From scratch, Wikitext-103 dataset
    * Infinite Transformer > Compressive > Transformer XL
    * Infinite Transformer with Sticky Memory > Infinite Transformer

Visualization shows that sticky memory indeed helps.
