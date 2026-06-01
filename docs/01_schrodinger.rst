01schrodinger.py — 슈뢰딩거 방정식 수치 풀기
==============================================

**생성 출력 파일**:

- ``outputs/01_infinite_square_well.png``
- ``outputs/01_finite_square_well.png``
- ``outputs/01_harmonic_oscillator.png``

.. contents::
   :local:
   :depth: 2

----

핵심 알고리즘: 유한 차분법 + 행렬 대각화
------------------------------------------

이 파일은 **시간 독립 슈뢰딩거 방정식**을 풉니다:

.. math::

   \hat{H}\psi = E\psi, \quad \hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)

Step 1: 공간 격자 생성
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   x = np.linspace(0, L, N)   # N개 점으로 [0, L] 분할
   dx = x[1] - x[0]           # 격자 간격

연속 공간을 이산 격자로 바꿉니다. :math:`N = 1000` 이면 :math:`dx = L/999`.

Step 2: 해밀토니안 행렬 구성
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

운동에너지 항의 2차 미분을 **유한 차분법**으로 근사합니다:

.. math::

   \frac{d^2\psi}{dx^2}\bigg|_i \approx \frac{\psi_{i+1} - 2\psi_i + \psi_{i-1}}{dx^2}

이를 행렬로 표현하면:

.. math::

   T = \frac{\hbar^2}{2m \cdot dx^2}
   \begin{pmatrix}
    2 & -1 &  0 & \cdots \\
   -1 &  2 & -1 & \cdots \\
    0 & -1 &  2 & \cdots \\
   \vdots & & & \ddots
   \end{pmatrix}

포텐셜 에너지는 대각 행렬:

.. math::

   V = \text{diag}(V(x_0),\, V(x_1),\, \ldots,\, V(x_{N-1}))

전체 해밀토니안: :math:`H = T + V`

.. code-block:: python

   def create_hamiltonian(x, V):
       N = len(x)
       dx = x[1] - x[0]
       T = np.zeros((N, N))
       for i in range(N):
           if i > 0: T[i, i-1] = -1
           T[i, i] = 2
           if i < N-1: T[i, i+1] = -1
       T = T * hbar**2 / (2 * m * dx**2)
       return T + np.diag(V)

Step 3: 고유값 문제 풀기
~~~~~~~~~~~~~~~~~~~~~~~~~

:math:`H\psi = E\psi` 를 :math:`\text{eigh}(H)` 로 풉니다.

.. code-block:: python

   from scipy.linalg import eigh
   eigenvalues, eigenvectors = eigh(H)
   # eigenvalues[i] → i번째 에너지 준위
   # eigenvectors[:, i] → i번째 파동함수

``eigh`` 는 **실수 대칭 행렬**의 고유값 분해에 특화된 함수입니다.
일반 ``eig`` 보다 수치적으로 안정적이고 빠릅니다.

Step 4: 정규화
~~~~~~~~~~~~~~

파동함수는 확률 해석을 위해 정규화합니다:

.. math::

   \int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1

이산 버전:

.. math::

   \text{norm} = \sqrt{\sum_i |\psi_i|^2 \cdot dx}

.. code-block:: python

   norm = np.sqrt(np.sum(eigenvectors[:, i]**2) * dx)
   eigenvectors[:, i] /= norm

----

그래프 1: ``01_infinite_square_well.png``
------------------------------------------

무엇을 보여주는가
~~~~~~~~~~~~~~~~~~

6개 서브플롯으로 구성:

- **[0,0] ~ [1,1]**: n=1 ~ n=5 상태의 파동함수 :math:`\psi_n(x)` (파란 실선)와
  확률 밀도 :math:`|\psi_n(x)|^2` (빨간 점선)
- **[1,2]**: 에너지 준위 다이어그램

왜 이런 모양인가
~~~~~~~~~~~~~~~~~

무한 우물에서 파동함수는 정현파입니다:

.. math::

   \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)

- n=1: 반파장 → 노드 0개, 최솟값 1개 봉우리
- n=2: 전파장 → 노드 1개, 봉우리 2개
- n=k: (k-1)개 노드, k개 봉우리

에너지 준위 다이어그램에서 :math:`E_n \propto n^2` 이므로 준위 간격이 점점 넓어집니다.

실제 세계와의 대응
~~~~~~~~~~~~~~~~~~

이것은 **나노 구조의 전자 구속** 을 모델링합니다:

- 반도체 양자점(Quantum Dot)에서 전자의 에너지 준위
- 형광 나노입자의 발광 파장 결정 ← :math:`E \propto 1/L^2` 이므로 크기가 작을수록 에너지(파장)가 달라짐
- CdSe 양자점의 색깔이 크기에 따라 달라지는 이유!

----

그래프 2: ``01_finite_square_well.png``
-----------------------------------------

무엇을 보여주는가
~~~~~~~~~~~~~~~~~~

- 위 패널: 포텐셜 :math:`V(x)` 와 속박 상태들의 파동함수 (에너지 준위에 오프셋)
- 아래 3개 패널: 각 속박 상태의 파동함수와 확률 밀도 개별 표시

파라미터: :math:`V_0 = 10.0` (우물 깊이), :math:`a = 5.0` (우물 너비)

왜 이런 모양인가
~~~~~~~~~~~~~~~~~

유한 우물에서 파동함수는 우물 밖으로 **지수적으로 감쇠**합니다:

.. math::

   \psi(x) \sim e^{-\kappa|x|}, \quad x > a/2
   \quad \text{where} \quad \kappa = \sqrt{2m(V_0 - E)/\hbar^2}

- 에너지가 낮을수록 (:math:`E \ll V_0`) → :math:`\kappa` 가 크므로 → 꼬리가 짧음
- 에너지가 높을수록 (:math:`E \to V_0`) → :math:`\kappa \to 0` → 꼬리가 길어짐

무한 우물과의 차이:

- 에너지 준위가 약간 낮음 (파동함수가 밖으로 퍼지므로)
- 속박 상태 개수가 유한함 (:math:`V_0` 에 의해 제한)

실제 세계와의 대응
~~~~~~~~~~~~~~~~~~

- 반도체 헤테로 접합(Heterostructure)의 전자 구속 모델
- GaAs/AlGaAs 양자 우물: 전자가 GaAs 층에 구속되어 LED/레이저 동작
- 핵 속 핵자(양성자, 중성자)의 구속

----

그래프 3: ``01_harmonic_oscillator.png``
------------------------------------------

무엇을 보여주는가
~~~~~~~~~~~~~~~~~~

- 위 패널: 포물선 포텐셜과 n=0~5 파동함수 (에너지 준위 오프셋)
- 아래 3개 패널: n=0, 1, 2 파동함수와 확률 밀도

왜 이런 모양인가
~~~~~~~~~~~~~~~~~

조화 진동자의 파동함수는 **에르미트 다항식** 으로 표현됩니다:

.. math::

   \psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}
   \frac{1}{\sqrt{2^n n!}} H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right)
   \exp\left(-\frac{m\omega x^2}{2\hbar}\right)

- n=0: 가우시안 형태 (노드 없음)
- n=1: 1개 노드, 선형 × 가우시안
- n=2: 2개 노드, 이차 × 가우시안

**에너지가 등간격**: :math:`E_{n+1} - E_n = \hbar\omega` (모두 동일)

이것이 무한 우물의 :math:`E_n \propto n^2` (불균등)과 다른 핵심 차이입니다.

실제 세계와의 대응
~~~~~~~~~~~~~~~~~~

조화 진동자는 양자역학에서 가장 중요한 모델입니다:

- **분자 진동**: HCl, CO₂ 분자의 적외선 흡수 스펙트럼
- **고체의 포논(Phonon)**: 결정격자의 진동 양자
- **양자 광학**: 광자장의 양자화 (광자 = 조화 진동자의 들뜸 상태)
- **양자 컴퓨터**: 초전도 큐비트의 회로 양자전기역학
