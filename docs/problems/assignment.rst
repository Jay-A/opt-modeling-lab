Assignment Problem
==================

Overview
--------

The assignment problem is one of the classical optimization problems in
operations research and mixed-integer programming. It models the task of
assigning resources to tasks while minimizing total cost or maximizing total
benefit.

Common applications include assigning workers to jobs, machines to tasks,
vehicles to routes, students to projects, and crews to flights. Although it
can be formulated as a binary integer program, the assignment problem has a
special mathematical structure that allows it to be solved efficiently using
linear programming techniques.

Problem Statement
-----------------

Given

- a set of workers,
- a set of jobs, and
- an assignment cost :math:`c_{ij}` representing the cost of assigning worker
  :math:`i` to job :math:`j`,

determine an assignment so that every worker is assigned exactly one job and
every job is assigned exactly one worker while minimizing the total assignment
cost.

Decision Variables
------------------

Let

.. math::

   x_{ij} =
   \begin{cases}
   1 & \text{if worker } i \text{ is assigned to job } j, \\
   0 & \text{otherwise.}
   \end{cases}

Each variable is binary, indicating whether a particular worker-job assignment
is selected.

Mathematical Formulation
------------------------

Objective:

.. math::

   \min \sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} x_{ij}

Subject to:

Each worker is assigned exactly one job:

.. math::

   \sum_{j=1}^{n} x_{ij} = 1,
   \qquad i = 1,\ldots,m.

Each job is assigned exactly one worker:

.. math::

   \sum_{i=1}^{m} x_{ij} = 1,
   \qquad j = 1,\ldots,n.

Binary decision variables:

.. math::

   x_{ij} \in \{0,1\},
   \qquad i = 1,\ldots,m,\;
   j = 1,\ldots,n.

where

- :math:`c_{ij}` is the cost of assigning worker :math:`i` to job :math:`j`,
- :math:`x_{ij}` indicates whether the assignment is selected.

Discussion
----------

The assignment problem introduces several important concepts in optimization:

- matrix-valued binary decision variables,
- equality constraints,
- one-to-one matching between two sets,
- linear objective functions.

Unlike many mixed-integer optimization problems, the assignment problem has a
constraint matrix that is totally unimodular. As a result, its linear
programming relaxation naturally produces integer solutions, making it an
important example of a problem that can be solved efficiently without requiring
general-purpose branch-and-bound methods.

Implementation
--------------

The Opt Modeling Lab provides implementations of the assignment problem using
multiple solver backends through a common modeling interface. This example
illustrates how matrix decision variables and families of constraints are
represented consistently across optimization libraries.

See Also
--------

See :doc:`../chapters/selection_problems` for related optimization models.