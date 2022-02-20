# Einops: Clear and Reliable Tensor Manipulations with Einstein-like Notation 
## Alex Rogozhnikov, Yandex - ICLR 2022 (Oral)
#### Summarized by Seungwook Kim
---

**Short-sentences summary**
* The paper proposes einops notation, a uniform and generic way to manipulate tensor structure, that significantly improves code readability and flexibility by focusing on structure of input and output tensors.
* Einops solves many problems in existing pipelines ex) not suited to write readable, reliable, or easy-to-modify code for multidimensional tensor manipulations, no checks provided, discrepancies between APIs. 
* While this library was open to the public for a long time (and I have tried using it) (@lucidrains also enjoys using einsum), this was the first time einops was submitted as a conference paper. There are no notable technical details (w.r.t deep learning) in the paper, but the readability & flexibility of einops is indeed great.
