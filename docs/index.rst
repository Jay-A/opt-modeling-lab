Opt Modeling Lab
=================

`GitHub Repository <https://github.com/Jay-A/opt-modeling-lab>`_

A structured lab for exploring mixed-integer optimization models,
solver backends, and modeling abstractions.

Core Architecture
------------------

This project is organized into three layers:

- **Chapters**: conceptual and theoretical frameworks
- **Problems**: concrete optimization models
- **Modeling Layer**: solver-agnostic abstraction (``aliases.py``)

Navigation
----------

.. toctree::
   :maxdepth: 1
   :caption: Chapters

   chapters/index

.. toctree::
   :maxdepth: 1
   :caption: Problems

   problems/index
   problems/knapsack
   problems/set_cover
   problems/set_packing
   problems/set_partitioning
   problems/maximum_coverage
   problems/capital_budgeting
   problems/vertex_covering
   problems/assignment
   problems/facility_location

.. toctree::
   :maxdepth: 1
   :caption: Modeling Layer

   modeling