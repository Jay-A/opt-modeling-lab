Maximum Coverage Problem
========================

Overview
--------

The maximum coverage problem is a classical combinatorial optimization model
in which a limited number of candidate sets are selected in order to maximize
the coverage of a universe of elements.

Unlike set covering, which requires all elements to be covered, maximum coverage
focuses on **partial but optimal coverage under a budget constraint**.

This makes it a fundamental model for resource allocation problems where full
coverage is infeasible or too expensive.

A canonical application is **sensor placement**, where a limited number of
sensors must be deployed to monitor the largest possible number of critical
locations.

Problem Statement
-----------------

Given:

- a universe of elements (e.g., geographic regions, users, events)
- a family of candidate sets (e.g., sensor locations, service zones)
- a budget limiting the number of sets that can be selected

select at most k sets such that the number of covered elements is maximized.

In the sensor placement interpretation:

- each location can observe a subset of regions
- each region is considered covered if at least one selected location observes it
- only k sensors can be installed due to cost constraints

Decision Variables
------------------

Let

.. math::

   x_j =
   \begin{cases}
   1 & \text{if location } j \text{ is selected}, \\
   0 & \text{otherwise}
   \end{cases}

for candidate locations, and:

.. math::

   y_i =
   \begin{cases}
   1 & \text{if element } i \text{ is covered}, \\
   0 & \text{otherwise}
   \end{cases}

where coverage is induced by the selected sets.

Mathematical Formulation
------------------------

Objective:

.. math::

   \max \sum_{i=1}^{n} y_i

Subject to:

Budget constraint:

.. math::

   \sum_{j=1}^{m} x_j \leq k

Coverage linking constraints:

.. math::

   y_i \leq \sum_{j=1}^{m} a_{ji} x_j
   \qquad \forall i = 1,\ldots,n

and

.. math::

   x_j \in \{0,1\}, \quad y_i \in \{0,1\}

where:

- a_{ji} = 1 if location j covers element i
- k is the maximum number of selectable sets

Modeling Interpretation
-----------------------

This formulation introduces a **two-layer decision structure**:

- the upper layer selects candidate sets (locations)
- the lower layer determines induced coverage of elements

Unlike set partitioning or set covering, feasibility is always guaranteed:

- selecting zero sets yields a valid solution
- partial selection is allowed and does not violate constraints

Therefore, the model always has a feasible baseline solution.

Structural Properties
---------------------

The maximum coverage problem exhibits several important structural features:

- **diminishing returns**: each additional selected set may overlap with prior selections
- **overlapping coverage**: elements may be covered by multiple sets
- **non-additive value structure**: marginal gain depends on current selection
- **budget-driven combinatorics**: solution quality is constrained by k

These properties distinguish it from knapsack-style additive objective models.

Feasibility and Construction
-----------------------------

In this lab, feasibility is guaranteed by construction:

- every element is made coverable by at least one candidate set
- the empty selection (selecting no sets) is always feasible
- coverage relationships are generated such that the model is never infeasible

This ensures that the solver focuses entirely on optimization rather than
feasibility repair.

Alternative Solutions and Greedy Structure
-------------------------------------------

A key aspect of maximum coverage is that:

> greedy heuristics often perform well but are not guaranteed to be optimal

To illustrate this, one may compare:

- a greedy selection strategy (iteratively choosing the most beneficial set)
- the optimal integer programming solution
- randomized or perturbed selection strategies

These approaches may produce different coverage outcomes even under the same
budget constraint.

Discussion
----------

The maximum coverage problem is a canonical example of:

- constrained combinatorial optimization
- submodular objective maximization under cardinality constraints
- interaction-driven value structures

It provides an important bridge between:

- additive models (knapsack)
- strict assignment models (set partitioning)
- full coverage models (set covering)

Unlike partitioning problems, maximum coverage does not require full allocation,
and unlike knapsack, value is not directly additive across decisions.

Implementation
--------------

The Opt Modeling Lab implements maximum coverage using a unified modeling
interface supporting multiple solver backends.

The sensor placement notebook demonstrates:

- construction of a random but structured coverage matrix
- enforcement of cardinality constraints
- introduction of coverage-inducing auxiliary variables
- comparison of selected vs unselected coverage outcomes

See Also
--------

See :doc:`../knapsack` for additive selection problems and
:doc:`../set_cover` for full coverage formulations with strict feasibility
requirements.