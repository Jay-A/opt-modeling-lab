Mixed-Integer Programming
==========================

Abstracted slightly from Bertsimas et al. Chapter 1 definition, instances of continuous, discrete, and mixed integer optimization problems
are innumerable and range in context pervasively throughout academia, engineering, industry, finance, logistics, cybersecurity, and entertainment among many others.
The shear expanse of application space warrants further investigation into the topic for those curious. And, that is where we begin.

In concept, the optimization problems we will look at seek to find a solution :math:`x^*` in some set :math:`\mathcal{X}`
that optimizes, either minimizes or maximizes, an objective function :math:`f(x)` for all :math:`x \in \mathcal{X}`.
The path toward a solution to these problems is the topic of interest for this pseudo-course:

Mixed-integer programming (MIP) is a mathematical framework for formulating
and solving optimization problems that involve both continuous and discrete
decisions, i.e. variables.
It provides a unified way to model situations in which some decisions are
quantitative (such as quantities, flows, or allocations), while others are
discrete (such as yes/no choices, assignments, or sequencing decisions).

The central idea is simple:

> represent a decision problem as a set of variables, an objective function, and constraints, where some variables are restricted to integer values.

Once formulated in this way, powerful optimization algorithms can be used to
compute optimal or near-optimal solutions.

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
We will make every attempt to clearly state the how each problem ties back into this framework, because
the purpose of this lab is to develop intuition for modeling optimization
problems using MIP. We are not focused on a singular specific application domain, instead the goal 
is use problem class abstractions that reveal underlying and recurring modeling structures to 
approach optimization problems in a general sense.

Components of a Mixed-Integer Program
-------------------------------------

Every mixed-integer programming model consists of three fundamental components.

Decision Variables
^^^^^^^^^^^^^^^^^^

Decision variables represent the choices available to the optimizer. Within the
scope of mixed-integer programming, decision variables are defined over either
**continuous** subsets of the real numbers or **integer** subsets of the
integers. A particularly important class of integer variables are
**binary** variables, whose values are restricted to :math:`\{0,1\}` and which
are widely used to model logical decisions, selection, assignment, and on-off
operating modes.

Choosing an appropriate set of decision variables is often the most important
step in constructing an effective optimization model.

Objective Function
^^^^^^^^^^^^^^^^^^

An objective function is a mapping

.. math::

   f : \mathcal{X} \rightarrow \mathbb{R}

that assigns a numerical measure of quality to each candidate solution
:math:`x \in \mathcal{X}`.

The optimization problem seeks a feasible solution

.. math::

   x^* \in X \subseteq \mathcal{X}

that minimizes or maximizes this value,

.. math::

   x^* \in
   \operatorname*{arg\,opt}_{x \in X} f(x),
   \qquad
   \operatorname{opt} \in \{\min,\max\}.

The objective function encodes the criterion by which feasible solutions are
evaluated. Selecting an appropriate objective is a modeling decision, and
different objectives applied to the same feasible region can produce different
optimization problems and computational behavior.

Constraints
^^^^^^^^^^^

Constraints are conditions imposed on the decision variables that define the
feasible solutions of an optimization problem. Collectively, the constraints
determine the set of solutions that are considered feasible.

Mathematically, constraints define the feasible region

.. math::

   X = \{x \in \mathcal{X} : g_i(x) \le 0,\; h_j(x) = 0\},

where the functions :math:`g_i` and :math:`h_j` represent inequality and
equality constraints, respectively. In mixed-integer programming, these
constraints are most commonly linear or quadratic, giving rise to important
problem classes such as mixed-integer linear programming (MILP),
mixed-integer quadratic programming (MIQP), and mixed-integer nonlinear
programming (MINLP).

Regardless of type, all constraints encode the physical, logical, or
operational rules that every feasible solution must satisfy. Typical examples
include

- resource limitations,
- assignment requirements,
- logical relationships,
- precedence conditions, and
- flow conservation equations.

Selecting an appropriate set of constraints is a modeling decision. Different
formulations may describe the same feasible region while exhibiting
dramatically different computational behavior. Consequently, effective
optimization modeling requires more than mathematical correctness—it also
requires an understanding of how formulations influence the algorithms used to
solve them.

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

Assignment models determine how one collection of entities is matched to
another.

Representative examples include

- assignment,
- transportation,
- generalized assignment, and
- facility allocation.

Scheduling Models
^^^^^^^^^^^^^^^^^

Scheduling models determine when activities occur while respecting resource
availability and temporal relationships.

Representative examples include

- machine scheduling,
- job shop scheduling,
- flow shop scheduling, and
- workforce scheduling.

Network Models
^^^^^^^^^^^^^^

Network models describe how flow, information, or resources move through a
graph or transportation system.

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

Many practical optimization models naturally combine multiple structures. For
example,

- facility location combines selection and assignment,
- vehicle routing combines assignment, scheduling, and network structure,
- production planning combines scheduling, network flow, and inventory
  management.

Accordingly, each optimization problem presented in this lab is classified
according to its dominant modeling pattern, while recognizing that many
real-world models span multiple categories.

Chapters
---------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   selection_problems
   assignment_problems
   scheduling_problems
   network_problems
   advanced_problems