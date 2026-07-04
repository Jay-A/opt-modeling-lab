Facility Location Problem
=========================

Overview
--------

The facility location problem is a fundamental optimization model in
mixed-integer programming. It captures the decision of selecting which
facilities to open and how to assign clients to those facilities in a cost-
optimal way.

This problem introduces the interaction between *fixed costs* (opening a
facility) and *variable costs* (serving clients from opened facilities). It
is widely used in logistics, supply chain design, service system planning,
and network design.

Unlike simpler selection models, facility location combines both selection
and assignment decisions in a single integrated optimization problem.

Problem Statement
-----------------

Given

- a set of potential facilities,
- a set of clients, and
- assignment costs :math:`c_{ij}` representing the cost of serving client
  :math:`i` from facility :math:`j`,
- fixed opening costs :math:`f_j` for each facility,

determine which facilities to open and how to assign each client to an open
facility such that total cost is minimized.

Decision Variables
------------------

Let

.. math::

   y_j =
   \begin{cases}
   1 & \text{if facility } j \text{ is opened}, \\
   0 & \text{otherwise.}
   \end{cases}

and

.. math::

   x_{ij} =
   \begin{cases}
   1 & \text{if client } i \text{ is assigned to facility } j, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary, representing either an opening decision or an
assignment decision.

Mathematical Formulation
------------------------

Objective:

.. math::

   \min \sum_{j=1}^{m} f_j y_j +
        \sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} x_{ij}

Subject to:

Each client must be assigned to exactly one facility:

.. math::

   \sum_{j=1}^{m} x_{ij} = 1,
   \qquad i = 1,\ldots,n.

A client can only be assigned to an open facility:

.. math::

   x_{ij} \le y_j,
   \qquad i = 1,\ldots,n,\; j = 1,\ldots,m.

Binary constraints:

.. math::

   x_{ij}, y_j \in \{0,1\}.

where

- :math:`f_j` is the fixed cost of opening facility :math:`j`,
- :math:`c_{ij}` is the cost of assigning client :math:`i` to facility
  :math:`j`.

Discussion
----------

The facility location problem illustrates several important ideas in
mixed-integer programming:

- interaction between different types of binary decisions,
- linking constraints between variables,
- trade-offs between fixed and variable costs,
- modeling of logical implications using linear constraints.

This makes it a foundational example of *network design* and *logistics
optimization* problems, and a natural extension beyond pure selection and
assignment models.

Implementation
--------------

The Opt Modeling Lab provides implementations of the facility location
problem using multiple solver backends through a common modeling interface.
This allows direct comparison of how different optimization solvers handle
linked binary decision structures.

See Also
--------

See :doc:`../chapters/selection_problems` for related optimization model
structures.