Week 11: 양자역학 시뮬레이션 매뉴얼
=====================================

이 매뉴얼은 Week 11 양자역학 시뮬레이션 코드의 **출력(output)이 실제 양자역학 이론과
얼마나 잘 일치하는지 검증**하고, 각 시뮬레이션이 어떻게 만들어졌으며 왜 그러한 결과가
나오는지를 체계적으로 설명합니다.

.. admonition:: 핵심 검증 결과

   ✅ 무한 사각 우물 에너지: 수치해 오차 < 0.01% (해석해와 사실상 일치)

   ✅ 조화 진동자 에너지: 수치해 오차 < 0.001% (매우 정확)

   ✅ 터널링 투과 계수: 해석적 공식과 수치 결과 일치

   ✅ 수소 원자 에너지: :math:`E_n = -13.6 \text{ eV}/n^2` 패턴 재현

.. toctree::
   :maxdepth: 2
   :caption: 목차

   overview
   validation
   01_schrodinger
   02_wavefunction
   03_tunneling
   04_wells_oscillator
   physics_background

.. toctree::
   :maxdepth: 1
   :caption: 부록

   numerical_methods
   constants_units

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
