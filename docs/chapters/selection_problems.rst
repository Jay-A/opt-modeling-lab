Selection-Style Optimization Problems
=====================================

Overview
--------

Selection problems are a fundamental class of mixed-integer programming (MIP)
models in which the primary decision is:

> which subset of available items should be selected to optimize a given objective while satisfying constraints.

These models form the foundation of discrete optimization, as many more
complex formulations can be interpreted as generalized or structured selection
problems.

In all cases, the decision is represented through binary variables indicating
whether each item is included in the solution.

Connection to General MIP Framework
-----------------------------------

As introduced in the foundations chapter, every optimization model consists of
decision variables, an objective function, and a feasible region defined by
constraints.

Selection models specialize this structure as follows:

- **Decision variables**: binary indicators of item selection
- **Objective function**: typically additive over selected items
- **Constraints**: resource limitations or logical dependencies on selections

Formally, selection models take the form:

.. math::

   x_i \in \{0,1\}, \quad i = 1,\dots,n

with objective

.. math::

   \max / \min \sum_{i=1}^n c_i x_i

subject to problem-specific constraints of the form

.. math::

   Ax \le b

or more structured combinatorial restrictions.

Modeling Characteristics
------------------------

Selection models are characterized by the following structural properties:

- **binary decision structure**: each item is either selected or not
- **additive or near-additive objectives**: total value is typically a sum over selected items
- **global coupling through constraints**: feasibility depends on shared resource limits
- **combinatorial explosion of feasible subsets**

These properties make selection problems both expressive and computationally
challenging.

Despite their simplicity, selection models already capture many important
practical decision problems in logistics, finance, and network design.

Canonical Structure
-------------------

Most selection problems follow a common modeling template:

1. Define a set of candidate items
2. Associate value and/or cost with each item
3. Introduce binary decision variables for selection
4. Encode constraints limiting feasible subsets
5. Optimize total value or cost over feasible selections

This template will recur throughout all models in this chapter.

Representative Problems
-----------------------

The following problems illustrate the selection modeling paradigm, ranging from
simple additive structures to more complex combinatorial interactions.

Knapsack Problem
^^^^^^^^^^^^^^^^

The knapsack problem is the canonical selection model.

Given items with values and weights, the goal is to select a subset of items
that maximizes total value without exceeding a capacity constraint.

.. toctree::
   :maxdepth: 1

   ../problems/knapsack

Capital Budgeting
^^^^^^^^^^^^^^^^^

In capital budgeting, each project has an associated cost and expected return.
The objective is to select a subset of projects that maximizes total return
subject to a budget constraint.

(This will be introduced in a subsequent notebook.)

Set Covering
^^^^^^^^^^^^

In set covering problems, each item corresponds to a subset of elements, and
the goal is to select a minimum-cost collection of sets such that every element
is covered at least once.

Set covering introduces structured constraint interactions beyond simple
resource limits.

Multi-Knapsack Variants
^^^^^^^^^^^^^^^^^^^^^^^

Multi-knapsack problems extend the classical knapsack model by introducing
multiple resource constraints simultaneously.

These models capture more realistic allocation settings where multiple limited
resources must be considered jointly.

Facility Location (Selection Component)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Facility location models combine selection with assignment structure.

The selection component determines which facilities are opened, making it a
natural extension of the selection modeling paradigm.

Discussion
----------

Selection models represent the simplest non-trivial class of MIP formulations,
yet they already capture the core difficulty of combinatorial optimization:
choosing an optimal subset from an exponentially large solution space.

They serve as the foundation for more complex modeling patterns, including
assignment, scheduling, and network optimization models introduced in later
chapters.

In the remainder of this section, we focus on implementing and analyzing
canonical selection problems, beginning with the knapsack model as the
prototypical example.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/knapsack
   ../problems/set_cover
   ../problems/set_packing
   ../problems/set_partitioning
   ../problems/maximum_coverage
   ../problems/capital_budgeting
   ../problems/vertex_cover
