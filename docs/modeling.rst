Modeling Interface (aliases.py)
===============================

This module defines the core abstraction layer used throughout the lab.

It provides a Gurobi-style interface on top of ``python-mip`` to support:

- consistent modeling syntax across backends
- pedagogical clarity in optimization formulation
- easy migration from Gurobi-style code

Core Concept
------------

Instead of interacting directly with solver-specific APIs, all models in this
lab are built using:

- ``Model()``
- ``add_binary_var()``
- ``add_constraint()``
- ``set_objective()``
- ``solve()``

This allows the same mathematical formulation to be expressed independently of
the backend solver.

Implementation Reference
------------------------

.. automodule:: optilab.aliases
   :members:
   :undoc-members:
   :show-inheritance: