부록 B: 물리 상수 및 단위계
=============================

원자 단위계 (Atomic Units)
---------------------------

Week 11 시뮬레이션은 모두 원자 단위계를 사용합니다 (:math:`\hbar = m_e = e = 1`):

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20

   * - 물리량
     - 원자 단위 기호
     - SI 값
     - 코드 값
   * - 작용
     - :math:`\hbar`
     - :math:`1.055 \times 10^{-34}` J·s
     - ``hbar = 1.0``
   * - 질량
     - :math:`m_e`
     - :math:`9.109 \times 10^{-31}` kg
     - ``m = 1.0``
   * - 에너지
     - Hartree
     - 27.211 eV
     - 수치 에너지 단위
   * - 길이
     - Bohr (:math:`a_0`)
     - 0.529 Å
     - 수치 거리 단위

SI 단위로 변환 예시
~~~~~~~~~~~~~~~~~~~~

무한 우물 (L=10 Bohr, 전자):

.. math::

   L_\text{SI} = 10 \times 0.529 \text{ Å} = 5.29 \text{ Å}

.. math::

   E_1 = \frac{\pi^2\hbar^2}{2m_e L^2}
   = \frac{(1.055\times10^{-34})^2\pi^2}{2(9.109\times10^{-31})(5.29\times10^{-10})^2}
   \approx 1.34 \text{ eV}

수소 원자 에너지 (n=1):

.. math::

   E_1 = -0.5 \text{ Hartree} = -0.5 \times 27.211 \text{ eV} = -13.6 \text{ eV} \checkmark

자주 사용하는 물리 상수
------------------------

.. code-block:: python

   # SI 단위
   hbar_SI = 1.054571817e-34   # J·s
   m_e = 9.10938356e-31        # kg
   e_charge = 1.602176634e-19  # C
   a0 = 0.529177210903e-10     # m (보어 반지름)
   E_h = 4.3597447222071e-18   # J (하트리 에너지)
   eV = 1.602176634e-19        # J (1 eV)
