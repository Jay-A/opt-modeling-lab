Set Partitioning Problem (Crew Scheduling)
==========================================

Overview
--------

The set partitioning problem is a fundamental mixed-integer programming model
in which a collection of elements must be assigned to exactly one subset from a
family of candidate sets.

Unlike set covering problems, where elements must be covered at least once,
set partitioning enforces a stricter requirement:

every element must belong to exactly one selected set.

This makes set partitioning a core model for structured allocation problems,
particularly in scheduling and assignment systems.

A canonical application is **crew scheduling**, where flights must be assigned
to exactly one valid crew duty schedule.

Problem Statement
-----------------

Given:

- a set of elements (e.g., flights)
- a family of candidate sets (e.g., feasible crew schedules)
- a cost associated with selecting each set

select a subset of sets such that every element is covered exactly once, while
minimizing total cost.

In the crew scheduling interpretation:

- each flight must be assigned to exactly one crew schedule
- each schedule covers a subset of flights
- schedules have different operational costs

Decision Variables
------------------

Let

.. math::

   x_j =
   \begin{cases}
   1 & \text{if schedule } j \text{ is selected}, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary and indicates whether a candidate schedule is included
in the final roster.

Mathematical Formulation
------------------------

Objective:

.. math::

   \min \sum_{j=1}^{m} c_j x_j

Subject to:

.. math::

   \sum_{j=1}^{m} a_{ij} x_j = 1
   \qquad \forall i = 1,\ldots,n

and

.. math::

   x_j \in \{0,1\},
   \qquad j = 1,\ldots,m.

where:

- :math:`a_{ij} = 1` if flight :math:`i` is covered by schedule :math:`j`
- :math:`c_j` is the cost of schedule :math:`j`
- each flight :math:`i` must be covered exactly once

Modeling Interpretation
-----------------------

This formulation enforces a **hard partition structure** over the set of
flights:

- every flight must belong to exactly one selected schedule
- schedules compete to explain the same set of flights
- feasibility depends on a structured generation of candidate schedules

In this lab, feasibility is guaranteed by construction:

- flights are first grouped into a latent partition
- schedules are generated from this structure
- therefore at least one valid partition always exists

Alternative Solutions and Structural Diversity
----------------------------------------------

A key insight explored in the implementation is that:

> multiple feasible partitions may exist with different total costs

To illustrate this, we construct and compare:

- a baseline partition (derived from structured grouping)
- an alternative partition generated from a different assignment strategy
- a resampled feasible partition constructed via stochastic assignment

All alternatives satisfy the exact coverage constraint, but differ in cost.

This highlights that set partitioning is not only a feasibility problem, but
a combinatorial optimization over a space of valid decompositions.

Discussion
----------

The set partitioning problem illustrates several key ideas in optimization:

- strict assignment constraints (exact coverage)
- combinatorial feasibility structures
- multiple competing feasible solutions
- sensitivity of objective value to structural decomposition

Unlike selection problems such as knapsack, feasibility here is not inherent in
individual variables, but emerges from the interaction between sets.

Implementation
--------------

The Opt Modeling Lab implements set partitioning using multiple solver
backends through a unified modeling interface.

The crew scheduling notebook demonstrates:

- guaranteed feasibility via structured construction
- generation of alternative valid partitions
- comparison of multiple feasible solutions
- diagnostic visualization of coverage structure

See Also
--------

See :doc:`../chapters/selection_problems` for selection-style models and
:doc:`../chapters/assignment_problems` for related assignment structures.