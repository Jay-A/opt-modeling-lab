Mixed Integer Optimization
---------------------------

Overview
--------

Mixed-integer programming (MIP) provides a flexible mathematical framework for
modeling discrete decision problems arising in engineering, logistics,
cybersecurity, finance, manufacturing, and operations research. Despite the
diversity of these applications, many share a common mathematical structure.

The purpose of this lab is to develop intuition for constructing optimization
models by studying a collection of canonical problem classes. Rather than
focusing on a particular application domain, the emphasis is placed on the
underlying modeling patterns that recur across many practical optimization
problems.

Definition: Optimization Problem
---------------------------------

An optimization problem consists of

- a collection of decision variables,
- an objective function,
- and a feasible region defined by a set of constraints.

More formally, let :math:`x \in \mathcal{X}` denote the optimization variables
and let :math:`X \subseteq \mathcal{X}` denote the feasible region. The goal is
to compute

.. math::

   \operatorname{opt}_{x \in X} f(x),
   \qquad
   \operatorname{opt} \in \{\min,\max\},

where :math:`f : \mathcal{X} \rightarrow \mathbb{R}` is the objective function.

In the case of a linear mixed-integer program, the objective is linear and the
feasible region is defined by linear constraints:

.. math::

   \operatorname{opt}_{x \in X} c^T x

subject to

.. math::

   Ax \le b,
   \qquad
   x \in X \subseteq \mathcal{X},

where :math:`A \in \mathbb{R}^{m \times n}`,
:math:`b \in \mathbb{R}^m`, and
:math:`c \in \mathbb{R}^n`.

Although individual optimization models may differ substantially in appearance,
every model developed throughout this lab is an instance of this general
framework.

Components of a Mixed-Integer Program
-------------------------------------

Every mixed-integer programming model consists of three fundamental components.

Decision Variables
^^^^^^^^^^^^^^^^^^

Decision variables represent the choices available to the optimizer. Depending
on the application, variables may be

- binary,
- integer, or
- continuous.

Choosing an appropriate set of decision variables is often the most important
step in constructing an effective optimization model.

Objective Function
^^^^^^^^^^^^^^^^^^

The objective function measures the quality of a feasible solution. Common
objectives include

- maximizing profit,
- minimizing cost,
- maximizing coverage,
- minimizing completion time, and
- minimizing resource utilization.

Throughout this lab we primarily study single-objective optimization models,
although many practical problems involve multiple competing objectives.

Constraints
^^^^^^^^^^^

Constraints define the feasible region by restricting the allowable values of
the decision variables. They encode the physical, logical, or operational rules
that every admissible solution must satisfy.

Typical constraints include

- resource limitations,
- assignment requirements,
- logical relationships,
- precedence conditions, and
- flow conservation equations.

The objective function determines which feasible solution is preferred, while
the constraints determine which solutions are admissible.

Standard and Strong Formulations
--------------------------------

Different mathematical formulations may represent the same optimization
problem.

A **standard formulation** correctly describes the feasible solutions of the
problem.

A **strong formulation** describes the same feasible region while providing a
tighter linear programming relaxation.

Because modern mixed-integer programming solvers repeatedly solve linear
relaxations during branch-and-bound, stronger formulations often

- reduce the size of the search tree,
- improve computational performance, and
- produce stronger bounds throughout the solution process.

Accordingly, the goal of this lab is not only to formulate optimization models
correctly, but to formulate them strongly whenever possible.

Modeling Patterns
-----------------

The optimization problems studied throughout this lab are organized according
to their dominant modeling structure.

Selection Models
^^^^^^^^^^^^^^^^

Selection models determine which objects should be chosen from a collection of
candidates while satisfying resource or logical constraints.

Representative examples include

- knapsack,
- capital budgeting,
- set cover,
- maximum coverage,
- set packing,
- set partitioning, and
- vertex cover.

Assignment Models
^^^^^^^^^^^^^^^^^

Assignment models determine how one collection of entities should be matched to
another.

Representative examples include

- assignment,
- transportation,
- generalized assignment, and
- facility allocation.

Scheduling Models
^^^^^^^^^^^^^^^^^

Scheduling models determine when activities should occur while respecting
resource availability and temporal relationships.

Representative examples include

- machine scheduling,
- job shop scheduling,
- flow shop scheduling, and
- workforce scheduling.

Network Models
^^^^^^^^^^^^^^

Network models determine how flow, information, or resources move through a
graph or transportation network.

Representative examples include

- shortest path,
- maximum flow,
- minimum-cost flow,
- routing, and
- network design.

Advanced Models
^^^^^^^^^^^^^^^

Advanced models combine multiple modeling structures or introduce richer
decision processes.

Representative examples include

- facility location,
- production planning,
- robust optimization,
- stochastic programming, and
- decomposition methods.

Relationships Between Modeling Patterns
---------------------------------------

The modeling patterns introduced in this lab should not be viewed as a
partition of mixed-integer programming problems.

Instead, they provide a useful **covering** of the modeling landscape.

Many practical optimization models naturally combine several modeling
structures. For example,

- facility location combines selection and assignment,
- vehicle routing combines assignment, scheduling, and network optimization,
- production planning combines scheduling, network flow, and inventory
  management.

Accordingly, each optimization problem presented in this lab is classified
according to its dominant modeling pattern while recognizing that many
real-world models span multiple categories.

Chapters
---------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   selection_problems
   assignment_problems