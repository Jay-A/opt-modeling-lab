Capital Budgeting Problem
=========================

Overview
--------

The capital budgeting problem is a classical combinatorial optimization model
in which a set of investment projects must be selected under a limited capital
budget in order to maximize total expected return.

Each project requires an upfront investment and generates an expected financial
benefit. Because the available budget is constrained, only a subset of projects
can be funded.

This makes capital budgeting a fundamental model for **discrete portfolio
selection under resource constraints**.

A canonical application is **infrastructure and energy investment planning**,
where organizations must decide which projects to fund within a fixed budget.

Problem Statement
-----------------

Given:

- a set of candidate investment projects
- a capital cost associated with each project
- an expected return associated with each project
- a total available budget

select a subset of projects that maximizes total return while respecting the
budget constraint.

In the investment interpretation:

- each project represents a possible investment (e.g., solar, wind, storage)
- each project has a cost (capital requirement)
- each project has a return (expected profit or benefit)
- only a limited number of projects can be funded

Decision Variables
------------------

Let

.. math::

   x_j =
   \begin{cases}
   1 & \text{if project } j \text{ is selected}, \\
   0 & \text{otherwise}
   \end{cases}

Each binary variable represents whether a project is included in the final
investment portfolio.

Mathematical Formulation
------------------------

Objective:

.. math::

   \max \sum_{j=1}^{n} r_j x_j

Subject to:

Budget constraint:

.. math::

   \sum_{j=1}^{n} c_j x_j \leq B

and

.. math::

   x_j \in \{0,1\}, \quad j = 1,\ldots,n

where:

- :math:`r_j` is the expected return of project j
- :math:`c_j` is the capital cost of project j
- :math:`B` is the total available budget

Modeling Interpretation
-----------------------

This formulation captures a **discrete investment selection problem**:

- each decision corresponds to funding a project or not
- returns are additive across selected projects
- all projects compete for a shared budget resource

Unlike coverage-based models, there is no interaction between projects beyond
the global budget constraint.

Feasibility Structure
---------------------

The model is always feasible by construction:

- selecting no projects satisfies the budget constraint
- any subset of projects whose total cost does not exceed the budget is feasible

This ensures that the optimization focuses entirely on trade-offs between cost
and return rather than feasibility restoration.

Structural Properties
---------------------

The capital budgeting problem exhibits several key structural features:

- **additive objective structure**: total return is the sum of selected returns
- **shared resource constraint**: all decisions compete for a common budget
- **binary selection structure**: projects are indivisible
- **trade-off dynamics**: higher return projects may consume more budget

These properties make it a canonical example of a knapsack-type optimization model.

Alternative Interpretations
---------------------------

The same structure appears in many application domains:

- infrastructure investment planning (roads, utilities, energy systems)
- R&D portfolio selection in technology companies
- public sector project prioritization
- healthcare investment planning (equipment and facilities)

In all cases, the underlying decision is a discrete allocation of limited
financial resources across competing opportunities.

Comparison to Related Models
----------------------------

Capital budgeting is closely related to several other selection problems:

- **Knapsack problem**: identical mathematical structure, different interpretation
- **Set covering**: introduces coverage and feasibility coupling
- **Set partitioning**: enforces exact allocation constraints

Unlike coverage models, capital budgeting does not involve element-level
assignment or overlap structure. Unlike partitioning models, feasibility is not
structurally restrictive beyond the budget constraint.

Discussion
----------

The capital budgeting problem is a foundational model in integer optimization
because it introduces:

- economic interpretation of objective coefficients
- trade-offs between cost and benefit
- resource-constrained decision making
- binary investment choices

It serves as a bridge between abstract knapsack formulations and more complex
portfolio optimization models involving risk, correlation, and multi-period
planning.

Implementation
--------------

The Opt Modeling Lab implements capital budgeting using a unified modeling
interface supporting multiple solver backends.

The investment selection notebook demonstrates:

- generation of synthetic project costs and returns
- enforcement of a global budget constraint
- binary selection of projects
- extraction and interpretation of optimal portfolios

See Also
--------

See :doc:`../knapsack` for the foundational resource allocation model and
:doc:`../selection_problems` for related binary optimization structures.