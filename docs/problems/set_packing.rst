Set Packing Problem
===================

Overview
--------

The set packing problem is a fundamental optimization problem in
mixed-integer programming. It models the task of selecting a collection of
sets such that no element in the underlying universe is covered more than once,
while maximizing total profit.

Despite its simple formulation, the set packing problem appears in many
practical applications, including scheduling, resource allocation, conflict-free
selection problems, and combinatorial design. It is one of the canonical
examples of a *conflict-constrained selection problem*.

In the language of general optimization, set packing defines a feasible region
through *mutual exclusivity constraints* that restrict overlapping selections.

Problem Statement
-----------------

We consider a collection of sets :math:`S_j \subseteq \{1,\ldots,m\}` each
with an associated profit :math:`p_j`.

The goal is to select a subset of these sets such that no element in the
universe is contained in more than one chosen set, while maximizing total
profit.

This can be interpreted as a selection problem over a constrained feasible
region where conflicts arise from overlapping set membership.

Decision Variables
------------------

Let

.. math::

   x_j =
   \begin{cases}
   1 & \text{if set } j \text{ is selected}, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary, representing whether a set is included in the
solution.

These variables define the decision vector :math:`x \in \{0,1\}^n`, which
parameterizes the feasible region.

Mathematical Formulation
------------------------

Following the general optimization framework:

.. math::

   \mathrm{opt}_{x \in X} f(x)

we define:

Objective function:

.. math::

   f(x) = \sum_{j=1}^{n} p_j x_j

Feasible region:

.. math::

   X = \{ x \in \{0,1\}^n \mid Ax \le 1 \}

where the matrix :math:`A \in \{0,1\}^{m \times n}` encodes set membership:

- :math:`A_{ij} = 1` if element :math:`i` is contained in set :math:`j`,
- :math:`A_{ij} = 0` otherwise.

Thus, the optimization problem is:

.. math::

   \max_{x \in X} \sum_{j=1}^{n} p_j x_j

Subject to:

.. math::

   \sum_{j:\, i \in S_j} x_j \le 1,
   \qquad i = 1,\ldots,m,

and

.. math::

   x_j \in \{0,1\},
   \qquad j = 1,\ldots,n.

Optimization Interpretation
---------------------------

In the general framework of mixed-integer programming:

- **Optimization variables**: :math:`x \in \{0,1\}^n`
- **Objective function**: linear profit maximization :math:`c^T x`
- **Feasible region**: linear constraints defining conflict structure

The constraint system enforces *pairwise exclusion through shared resources*
(elements), making this a structured selection problem over a conflict graph.

MIP Problem Decomposition
-------------------------

Within the classification used in this lab, set packing belongs to the
family of **selection problems**, where the primary decision is choosing a
subset of discrete objects.

It differs from other selection models as follows:

- Knapsack: resource-constrained selection
- Set Cover: coverage requirement (≥)
- Set Packing: conflict avoidance (≤)
- Set Partitioning: exact assignment (=)

Thus, set packing represents a *mutual exclusivity structure* within the
selection class.

Discussion
----------

The set packing problem illustrates several core ideas in optimization:

- binary decision variables over combinatorial sets,
- linear objective functions,
- sparsity and structure in constraint matrices,
- modeling of conflicts via linear inequalities.

It is closely related to the **maximum independent set problem** in graphs,
where each set corresponds to a node and overlaps define edges.

Understanding set packing provides a foundation for more advanced models in
scheduling, assignment, and network optimization.

Implementation
--------------

The Opt Modeling Lab provides implementations of the set packing problem using
multiple solver backends through a common modeling interface. This allows
direct comparison of how different optimization engines handle conflict
structures in binary decision spaces.

See Also
--------

See :doc:`../chapters/selection_problems` for the broader discussion of
selection-style optimization models.