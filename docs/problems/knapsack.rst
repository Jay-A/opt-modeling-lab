Knapsack Problem
================

Overview
--------

The knapsack problem is one of the fundamental optimization problems in
mixed-integer programming. It models the task of selecting a subset of items
to maximize total value while satisfying a limited capacity constraint.

Despite its simple formulation, the knapsack problem appears in many practical
applications, including resource allocation, budgeting, cargo loading,
portfolio selection, and project planning. It is also the basis for many more
advanced optimization models.

Problem Statement
-----------------

Given a collection of items, each with

- a value :math:`v_i`, and
- a weight :math:`w_i`,

select a subset of items that maximizes total value without exceeding the
capacity of the knapsack.

Decision Variables
------------------

Let

.. math::

   x_i =
   \begin{cases}
   1 & \text{if item } i \text{ is selected}, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary, indicating whether an item is included in the
solution.

Mathematical Formulation
------------------------

Objective:

.. math::

   \max \sum_{i=1}^{n} v_i x_i

Subject to:

.. math::

   \sum_{i=1}^{n} w_i x_i \le C

and

.. math::

   x_i \in \{0,1\},
   \qquad i = 1,\ldots,n.

where

- :math:`v_i` is the value of item :math:`i`,
- :math:`w_i` is the weight of item :math:`i`,
- :math:`C` is the capacity of the knapsack.

Discussion
----------

The knapsack problem illustrates several core ideas in optimization:

- binary decision variables,
- linear objective functions,
- linear inequality constraints,
- trade-offs between competing objectives and limited resources.

Because of its simplicity, it is often the first problem used to introduce
mixed-integer programming and optimization modeling.

Implementation
--------------

The Opt Modeling Lab provides implementations of the knapsack problem using
multiple solver backends through a common modeling interface. Comparing these
implementations helps illustrate how different optimization libraries expose
similar mathematical concepts.

See Also
--------

See :doc:`../chapters/selection_problems` for the broader discussion of
selection-style optimization models.