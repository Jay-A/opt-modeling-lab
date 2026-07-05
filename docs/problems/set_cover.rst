Set Cover Problem
=================

Overview
--------

The set cover problem is a fundamental optimization problem in
mixed-integer programming. It models the task of selecting a collection of
sets such that every element in a universe is covered by at least one chosen
set, while minimizing the total selection cost.

Despite its simple formulation, the set cover problem appears in many practical
applications, including facility placement, sensor deployment, crew scheduling,
network monitoring, and resource allocation. It is also a canonical example of
a covering problem in combinatorial optimization.

Problem Statement
-----------------

Given

- a universe of elements :math:`i = 1,\ldots,m`, and
- a collection of sets :math:`S_j \subseteq \{1,\ldots,m\}` each with an
  associated cost :math:`c_j`,

select a subset of sets that covers every element in the universe at least
once while minimizing total cost.

Decision Variables
------------------

Let

.. math::

   x_j =
   \begin{cases}
   1 & \text{if set } j \text{ is selected}, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary, indicating whether a set is included in the solution.

Mathematical Formulation
------------------------

Objective:

.. math::

   \min \sum_{j=1}^{n} c_j x_j

Subject to:

Coverage constraints:

.. math::

   \sum_{j:\, i \in S_j} x_j \ge 1,
   \qquad i = 1,\ldots,m.

Binary constraints:

.. math::

   x_j \in \{0,1\},
   \qquad j = 1,\ldots,n.

where

- :math:`c_j` is the cost of selecting set :math:`j`,
- :math:`S_j` is the subset of elements covered by set :math:`j`.

Discussion
----------

The set cover problem illustrates several important ideas in optimization:

- binary decision variables over sets,
- covering constraints expressed as linear inequalities,
- sparse constraint structure,
- trade-offs between cost and coverage.

It is one of the canonical examples of a covering problem and forms the basis
for many more advanced models, including facility location, crew scheduling,
and network design problems.

Implementation
--------------

The Opt Modeling Lab provides implementations of the set cover problem using
multiple solver backends through a common modeling interface. Comparing these
implementations helps illustrate how different optimization libraries expose
covering constraints in a unified way.

See Also
--------

See :doc:`../chapters/selection_problems` for the broader discussion of
selection-style optimization models.