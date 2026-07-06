Selection-Style Optimization Problems
=====================================

Overview
--------

Selection problems are a fundamental class of mixed-integer programming models
in which the primary modeling decision is determining which elements of a
finite set should be included in a solution.

These models arise whenever a decision maker must choose a subset of options
subject to constraints, and they form one of the most basic structures in
discrete optimization.

In all cases, selection decisions are represented using binary variables that
indicate whether each element is included in the solution.

Formulation Structure
---------------------

Selection models are typically expressed using binary decision variables

.. math::

   x_i \in \{0,1\}, \quad i = 1,\dots,n

where :math:`x_i = 1` indicates that item :math:`i` is selected.

A typical selection model takes the form

.. math::

   \max / \min \sum_{i=1}^n c_i x_i

subject to problem-specific constraints, commonly written in linear form as

.. math::

   Ax \le b,

or more structured combinatorial constraints depending on the application.

Modeling Characteristics
------------------------

Selection models exhibit several common structural features:

- binary decision structure representing inclusion or exclusion
- additive or near-additive objective functions over selected items
- coupling constraints that impose global feasibility conditions
- exponentially large sets of possible solutions

Despite their simplicity, these models capture a wide range of practical
decision problems in logistics, finance, and network design.

Canonical Modeling Pattern
--------------------------

Most selection problems follow a common modeling pattern:

1. Define a finite set of candidate items
2. Associate values, costs, or utilities with each item
3. Introduce binary variables representing selection decisions
4. Define constraints restricting feasible subsets
5. Optimize total value or cost over feasible selections

This structure appears throughout all selection-based optimization models.

Representative Problems
-----------------------

The following problems illustrate the selection modeling paradigm, ranging from
basic resource allocation to structured combinatorial optimization problems.

Knapsack Problem
^^^^^^^^^^^^^^^^

The knapsack problem is the canonical selection model.

Given items with values and weights, the objective is to select a subset of
items that maximizes total value without exceeding a capacity constraint.

.. toctree::
   :maxdepth: 1

   ../problems/knapsack

Capital Budgeting
^^^^^^^^^^^^^^^^^

In capital budgeting problems, each project has an associated cost and return.
The objective is to select a subset of projects that maximizes total return
subject to a budget constraint.

Set Covering
^^^^^^^^^^^^

In set covering problems, each item corresponds to a subset of elements, and
the goal is to select a minimum-cost collection of sets that covers all
elements.

Set Packing / Set Partitioning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These models impose structural constraints on how subsets overlap or partition
a ground set.

Maximum Coverage
^^^^^^^^^^^^^^^^

Maximum coverage problems select a subset of sets to maximize the number of
elements covered within a resource limit.

Multi-Knapsack Variants
^^^^^^^^^^^^^^^^^^^^^^^

Multi-knapsack models extend the classical knapsack structure by introducing
multiple resource constraints simultaneously.

Facility Location (Selection Component)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Facility location models combine selection with assignment decisions.

The selection component determines which facilities are opened, making it a
direct extension of the selection modeling paradigm.

Discussion
----------

Selection models represent the simplest non-trivial class of mixed-integer
programming formulations. Despite their simplicity, they capture the core
difficulty of combinatorial optimization: selecting an optimal subset from an
exponentially large set of possibilities.

They serve as the foundation for more complex modeling patterns, including
assignment, scheduling, and network optimization models introduced in later
chapters.

In the remainder of this section, we focus on implementing and analyzing
canonical selection problems, beginning with the knapsack model.

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
