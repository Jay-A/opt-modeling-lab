Assignment-Style Optimization Problems
======================================

Overview
--------

Assignment problems are a central class of mixed-integer programming (MIP)
models in which the primary decision is:

> how to assign one set of entities to another in an optimal way

Unlike selection problems, where the decision is whether to include an item,
assignment problems introduce a relational structure between two (or more)
sets of entities.

These models form the foundation for resource allocation, logistics matching,
and many real-world planning systems.

Connection to the General MIP Framework
----------------------------------------

As introduced in the foundations chapter, every optimization model consists of
decision variables, an objective function, and a feasible region defined by
constraints.

Assignment models specialize this structure by introducing **two-dimensional
decision variables**:

- decision variables represent relationships between entities
- feasibility is defined by consistency constraints across both sets

Formally, assignment models typically use variables of the form:

.. math::

   x_{ij} \in \{0,1\}

where:

- :math:`i` indexes one set of entities (e.g., workers, facilities, vehicles)
- :math:`j` indexes another set (e.g., tasks, customers, jobs)

A value of 1 indicates that entity :math:`i` is assigned to entity :math:`j`.

The general objective takes the form:

.. math::

   \min / \max \sum_{i}\sum_{j} c_{ij} x_{ij}

subject to assignment feasibility constraints.

Modeling Characteristics
------------------------

Assignment models are characterized by the following structural properties:

- **two-dimensional decision structure**: variables represent relationships
- **mutual exclusivity constraints**: assignments must be consistent
- **balance constraints**: each entity is typically assigned exactly once
- **cost or profit matrices**: objective depends on pairwise relationships

These features make assignment models a natural extension of selection models,
where decisions are no longer independent but relational.

Canonical Structure
-------------------

Most assignment problems follow a common modeling template:

1. Define two sets of entities (sources and targets)
2. Define a cost or profit for each possible pairing
3. Introduce binary variables for assignments
4. Enforce feasibility constraints (e.g., one-to-one or many-to-one rules)
5. Optimize total assignment cost or profit

This structure appears across logistics, scheduling, and resource allocation
problems.

Representative Problems
-----------------------

The following problems illustrate the assignment modeling paradigm, ranging
from classical one-to-one matching to more complex allocation structures.

Classical Assignment Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The classical assignment problem assigns each agent to exactly one task while
ensuring each task is assigned to exactly one agent.

This is the foundational assignment model and has efficient solution structure
in the linear programming relaxation.

Transportation Problem
^^^^^^^^^^^^^^^^^^^^^^

The transportation problem generalizes assignment by allowing supply and demand
quantities.

Instead of binary assignments, flows are assigned between sources and
destinations, often with capacity constraints.

Generalized Assignment Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In generalized assignment problems, each assignment consumes resources and
agents have limited capacities.

This introduces coupling between assignment decisions, making the model
significantly more complex.

Facility Location (Assignment Component)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Facility location models combine selection and assignment:

- selection determines which facilities are opened
- assignment determines which facility serves each client

This hybrid structure will be studied in the advanced models chapter.

Discussion
----------

Assignment models extend selection models by introducing **structured
relationships between decision variables**.

Instead of choosing a subset of independent items, the optimizer must determine
a consistent mapping between two sets of entities under feasibility constraints.

This additional structure significantly increases modeling power and appears in
many real-world systems, including logistics, workforce planning, and network
design.

In the remainder of this section, we focus on implementing classical assignment
and transportation models using a unified mixed-integer programming framework.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/assignment
   ../problems/transportation
   ../problems/generalized_assignment
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