Opt Modeling Lab
=================

Overview
--------

To dive in as quickly as possibly, we first define a generic optimization
problem to be

Definition: Optimization Problem
=================================

An optimization problem consists of optimization variables :math:`x \in \mathcal{X}`, an objective function :math:`f : \mathcal{X} \to \mathbb{R}`, and a feasible region :math:`X \subseteq \mathcal{X}` defined by a set of constraints.

The goal is to compute:

.. math::

   \mathrm{opt}_{x \in X} f(x), \quad \mathrm{opt} \in \{\min, \max\}.

In the case of a linear mixed-integer program, this takes the form:

.. math::

   \mathrm{opt}_{x \in X} c^T x

subject to:

.. math::

   Ax \leq b, \quad x \in X \subseteq \mathcal{X},

where :math:`A \in \mathbb{R}^{m \times n}`, :math:`b \in \mathbb{R}^m`, and :math:`c \in \mathbb{R}^n`.

This course explores how mixed-integer programming (MIP) models can be
structured, decomposed, and implemented through a unified modeling layer.

The goal is to build intuition for:

- how optimization problems are classified,
- how strong formulations are constructed,
- and how modeling abstractions map onto solver backends.

MIP Problem Decomposition
-------------------------

Most discrete optimization problems studied in this lab fall into four
broad structural categories:

**1. Selection problems**
   Choose a subset of items under constraints (e.g., knapsack).

**2. Scheduling problems**
   Assign tasks over time subject to resource and ordering constraints.

**3. Covering problems**
   Ensure all requirements are satisfied using a minimal or optimal subset
   of resources (e.g., set cover, facility location).

**4. Assignment / network structure problems**
   Match entities or route flow through a structured graph (e.g., assignment,
   transportation, routing).

These categories share a common structure:
binary or integer decision variables, linear constraints, and a global
optimization objective.

Strong Formulations
-------------------

A *strong formulation* is one that tightly represents the feasible region of
the problem using linear constraints.

In practice, stronger formulations:

- reduce the size of the branch-and-bound tree,
- improve solver performance,
- and avoid weak relaxations.

The modeling goal of this lab is not only to express problems correctly,
but to express them *strongly*.

Modeling Interface (aliases.py)
-------------------------------

All models in this lab are built using a lightweight abstraction layer defined
in ``aliases.py``.

This layer provides:

- a Gurobi-style ``Model`` interface,
- simplified variable creation (binary, integer, continuous),
- linear expression helpers (``quicksum``),
- and solver-agnostic constants (``GRB`` namespace).

It acts as a pedagogical bridge between mathematical formulations and solver
implementations.

Current Focus
-------------

The current implementation focuses on **selection problems**, particularly
the knapsack family, as the foundational example for all subsequent modeling
patterns.

Navigation
----------

.. toctree::
   :maxdepth: 2
   :caption: Chapters

   chapters/selection_problems