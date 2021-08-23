# E(n) equivariant normalizing flow
### Victor Garcia Satorras, Emiel Hoogeboom, Fabian B. Fuchs, Ingmar Posner, Max Welling
#### Summarized by Jiye Kim
---

**Task** : generative model


 

**Motivation** : 예를 들어, molecules과 이 molecules의 mirrored version이 있을 때 이들의 data likelihood는 똑같아야 함으로 Euclidean symmetries 에 equivariant 하게 likelihood estimation을 할 수 있는 모델이 필요하다.

 

**Method** :


	
목표: input x가 Euclidean symmetries(rotations, reflections, translations)에 대해 변해도 resulting data likelihood는 변하지 않도록 하고 싶음. 이를 위해 normalizing flow + EGNN을 합친 모델을 제안.

normalizing flow의 transformation f의 조건:


	
1) f needs to be invertible → normalizing flow의 조건
	
2) f needs to be equivariant → data likelihood를 Euclidean symmetries에 대해 invariant 하게 만들 조건. (base distribution p_z를 function f를 통해 transform 시킨 resulting distribution이 p_x라고 할 때, f가 equivariant이고 p_z가 invariant 하면 p_x가 invariant 함이 이전 논문에서 밝혀졌음. → p_x를 invariant distribution으로 만들 수 있음)


하지만 이 두 조건을 모두 충족시키는 f의 space는 작기 때문에, 1번 invertibility 조건을 mild 하게 바꿔주기 위해서 continuous-time normalizing flow를 사용함. continuous-time normalizing flow의 경우 neural network에 대한 constraint가 상대적으로 mild 함. (only need to be high order differentiable and Lipschitz continuous with possibly large Lipschitz constant.)

또한, 이 continuous-time normalizing flow의 differential을 EGNN을 통해 predict함으로서 f가 equivariant하게 됨.

기타 details:


	
-data likelihood P_x가 translation에 invariant하다는 조건을 만족시키려면 P_x가 distribution이 될 수 없음. 왜냐하면, p(x+t) = p(x)를 만족시켜야하고 이렇게 되면 p는 sum to 1이 안되기 때문. 따라서, p를 subspace로 restrict시켜서 연산한다는 내용이 있는데 이해를 잘 못했음.
	
-기존 EGNN form을 사용하면 기존 term이 easily explode하는 문제가 발생해서 stability를 위한 normalized form을 제시함.
	
-base distribution p_z는 Standard Gaussian으로 함. (Standard Gaussian은 reflection과 rotation에 대해 invariant하기 때문. 위의 base distribution이 invariant해야한다는 조건 만족.)
	
-Normalizing flow는 continuous distribution을 modeling하는 방법인데, node feature의 경우 ordinal(ex. charge of an atom), categorical (ex. atom type)한 경우가 있음. 이를 continuous 로 바꿔주기 위해서 ordinal feature에는 variational dequantization방법을 적용하고, categorical feature는 argmax flows방법을 적용하여 continuous variable로 바꿔줌. 이렇게 계산된 continuous-version likelihood가 discrete-version likelihood의 lowerbound가 된다는 사실을 이용해 continuous-version을 optimize 시킴.



**Experiment**:

-Particle systems (DW4, LJ13), Molecules (QM9) dataset에 대해서 평가.

-이전의 non-equivariant normalizing flow 모델, equivariant normalizing flow 모델과 NLL을 기준으로 비교했을 때 더 성능이 좋은 것을 확인함.


 



**총평**:

-normalizing flow와 EGNN을 합친 모델을 제안한 논문.

-generative model이 E(n) equivariant해야된다는 motivation은 좋은 것 같은데, 이것이 generation에서 필요한 이유와 성능 향상이 될 수 있었던 이유를 잘 모르겠다.

-내용이 많고 어려워서 이해하기 힘들었던 논문.
