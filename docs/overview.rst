개요: 시뮬레이션 구조와 흐름
==============================

파일 구성
---------

Week 11 디렉토리는 다음과 같이 구성되어 있습니다::

   week11/
   ├── 01schrodinger.py          # 슈뢰딩거 방정식 수치 풀기
   ├── 02wavefunction.py         # 파동함수 시각화
   ├── 03tunneling.py            # 양자 터널링 시뮬레이션
   ├── 04wells_oscillator.py     # 우물·진동자 비교 분석
   ├── outputs/                  # 생성된 그래프 PNG 파일들
   │   ├── 01_infinite_square_well.png
   │   ├── 01_harmonic_oscillator.png
   │   ├── 01_finite_square_well.png
   │   ├── 02_gaussian_wave_packet.png
   │   ├── 02_hydrogen_orbitals.png
   │   ├── 02_superposition_states.png
   │   ├── 03_rectangular_barrier.png
   │   ├── 03_resonant_tunneling.png
   │   ├── 03_tunneling_parameters.png
   │   ├── 04_classical_vs_quantum.png
   │   ├── 04_comparison.png
   │   ├── 04_finite_well_depth.png
   │   ├── 04_finite_well_width.png
   │   └── 04_harmonic_oscillator_detailed.png
   └── week11.md                 # 학습 가이드 문서

공통 수치 해법 파이프라인
--------------------------

모든 Python 파일은 다음 4단계 파이프라인을 공유합니다:

.. code-block:: text

   [1. 격자 정의]          x = linspace(a, b, N)
          ↓
   [2. 해밀토니안 구성]    H = T(운동에너지 행렬) + V(포텐셜 대각 행렬)
          ↓
   [3. 고유값 문제 풀기]   Hψ = Eψ  →  eigh(H)
          ↓
   [4. 시각화 & 저장]      matplotlib → outputs/*.png

공통 물리 단위계
----------------

모든 시뮬레이션은 **원자 단위계(Atomic Units)** 를 사용합니다:

.. math::

   \hbar = 1, \quad m_e = 1, \quad e = 1, \quad a_0 = 1

이 단위계에서:

- 에너지 단위: Hartree (= 27.2 eV)
- 길이 단위: Bohr radius :math:`a_0` (= 0.529 Å)
- 시간 단위: :math:`\hbar/E_h \approx 24.2 \text{ as}`

.. note::

   원자 단위계는 방정식을 단순화하기 위해 표준적으로 사용됩니다.
   예: SI 단위계에서 :math:`-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi` →
   원자 단위계에서 :math:`-\frac{1}{2}\nabla^2\psi + V\psi = E\psi`

의존 라이브러리
---------------

.. code-block:: python

   import numpy as np           # 행렬 연산, 수치 계산
   from scipy.linalg import eigh  # 대칭 행렬 고유값 문제 (에너지, 파동함수)
   import matplotlib.pyplot as plt  # 시각화

- **NumPy** : 격자 생성, 행렬 구성, 정규화
- **SciPy `eigh`** : 실수 대칭 행렬(에르미트)의 고유값 분해. 일반 `eig`보다 빠르고 안정적
- **Matplotlib** : 파동함수, 확률 밀도, 에너지 준위 다이어그램 생성
