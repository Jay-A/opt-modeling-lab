Assignment-Style Optimization Problems
======================================

Overview
--------

Assignment problems are a fundamental class of mixed-integer programming models
in which the primary modeling decision is to match elements of one set to
elements of another in an optimal way.

Unlike selection problems, where the decision concerns which elements to
include, assignment problems introduce a **relational structure** between two
(or more) sets of entities.

These models arise naturally in resource allocation, logistics, scheduling, and
many structured matching problems.

Formulation Structure
---------------------

Assignment models are typically expressed using binary decision variables of
the form

.. math::

   x_{ij} \in \{0,1\}

where :math:`x_{ij} = 1` indicates that entity :math:`i` is assigned to entity
:math:`j`.

Here:

- :math:`i` indexes one set of entities (e.g., agents, machines, facilities)
- :math:`j` indexes another set (e.g., tasks, jobs, customers)

A typical assignment model takes the form

.. math::

   \min / \max \sum_{i}\sum_{j} c_{ij} x_{ij}

subject to assignment feasibility constraints that enforce consistency across
both sets.

Modeling Characteristics
------------------------

Assignment models exhibit several defining structural features:

- **relational decision structure**: variables represent pairwise assignments
- **consistency constraints**: assignments must satisfy structural rules across sets
- **balance conditions**: entities are typically assigned exactly once or within capacity limits
- **cost or profit matrices**: objective depends on pairwise interactions

These features make assignment models a natural extension of selection models,
where decisions are no longer independent but interconnected.

Canonical Structure
-------------------

Most assignment problems follow a common modeling pattern:

1. Define two sets of entities (sources and targets)
2. Define a cost or profit for each possible pairing
3. Introduce binary variables representing assignment decisions
4. Impose feasibility constraints to ensure valid mappings
5. Optimize total assignment cost or profit

This structure appears broadly across allocation, scheduling, and matching
problems.

Representative Problems
-----------------------

The following problems illustrate the assignment modeling paradigm, ranging
from classical matching to more general allocation structures.

Classical Assignment Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The classical assignment problem assigns each agent to exactly one task while
ensuring each task is assigned to exactly one agent.

This model is notable for its strong linear programming relaxation.

Transportation Problem
^^^^^^^^^^^^^^^^^^^^^^

The transportation problem generalizes assignment by introducing supply and
demand quantities.

Instead of binary assignments, decision variables represent flows between
sources and destinations, often subject to capacity constraints.

Generalized Assignment Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In generalized assignment problems, each assignment consumes limited resources
and agents have capacity restrictions.

This introduces coupling between assignment decisions and significantly
increases modeling complexity.

Facility Location (Assignment Component)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Facility location models combine selection and assignment structures:

- selection determines which facilities are opened
- assignment determines how demand is allocated to open facilities

This hybrid structure will be studied in the advanced modeling chapter.

Discussion
----------

Assignment models extend selection models by introducing structured
relationships between decision variables.

Rather than selecting independent elements, the optimizer constructs a
consistent mapping between two sets of entities subject to feasibility
constraints.

This additional structure significantly increases modeling expressiveness and
appears in many real-world applications including logistics, workforce
planning, and network-based allocation systems.

In the remainder of this section, we focus on implementing classical assignment
and transportation models within the mixed-integer programming framework.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/assignment
   ../problems/transportation
   ../problems/generalized_assignment
   ../problems/multiassignment
   ../problems/balanced_unbalanced
   ../problems/matching_problem
   ../problems/facility_location

.. Assignment Models
.. ├── Classical Assignment
.. ├── Transportation (continuous extension)
.. ├── Generalized Assignment
.. ├── Multi-Assignment (capacitated matching)
.. ├── Balanced / Unbalanced Assignment
.. ├── Matching Problems
.. └── Quadratic Assignment (nonlinear interaction structure)
.. 
.. Hybrid / Extensions
.. ├── Facility Location (selection + assignment)
.. └── Scheduling (assignment over time preview)