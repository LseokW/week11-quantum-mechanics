부록 A: 수치 해법 상세
========================

유한 차분법 (Finite Difference Method)
----------------------------------------

2차 미분의 중앙 차분 근사:

.. math::

   \frac{d^2\psi}{dx^2}\bigg|_i \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{(\Delta x)^2}

이것은 테일러 전개에서 유도됩니다:

.. math::

   \psi_{i+1} = \psi_i + \Delta x\psi_i' + \frac{(\Delta x)^2}{2}\psi_i'' + O(\Delta x^3)

.. math::

   \psi_{i-1} = \psi_i - \Delta x\psi_i' + \frac{(\Delta x)^2}{2}\psi_i'' + O(\Delta x^3)

더하면: :math:`\psi_{i+1} + \psi_{i-1} = 2\psi_i + (\Delta x)^2\psi_i'' + O(\Delta x^4)`

따라서: :math:`\psi_i'' = \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{(\Delta x)^2} + O(\Delta x^2)`

행렬 고유값 문제
-----------------

슈뢰딩거 방정식 :math:`\hat{H}\psi = E\psi` 를 이산화하면:

.. math::

   \sum_j H_{ij} \psi_j = E \psi_i

이것이 바로 행렬 고유값 문제입니다. N×N 해밀토니안 행렬 H의 고유값이 에너지,
고유벡터가 파동함수입니다.

``scipy.linalg.eigh`` 선택 이유:

- 해밀토니안이 **실수 대칭 행렬** (에르미트) 임을 보장하므로
- 일반 ``eig`` 보다 수치 안정성 높음
- 고유값이 실수임을 보장
- LAPACK의 ``dsyev`` 루틴 사용 → 최적화된 BLAS 연산
