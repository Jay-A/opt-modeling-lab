Balanced / Unbalanced Assignment Problem
========================================

Overview
--------

The balanced and unbalanced assignment problem is a structural extension of
classical assignment models in which the two sides of the assignment do not
necessarily contain the same number of entities or total capacity.

In cloud infrastructure systems, this distinction is fundamental.

- In **balanced settings**, compute resources and workloads are assumed to be
  structurally matched.
- In **unbalanced settings**, workloads significantly exceed available compute
  resources, requiring selective allocation and prioritization.

This makes the model a natural representation of real-world cloud scheduling,
where demand and supply are rarely symmetric.

Connection to Optimization Framework
-------------------------------------

As defined in the foundational chapter, an optimization problem consists of

- decision variables,
- an objective function, and
- a feasible region defined by constraints.

In the assignment framework, we introduce binary decision variables:

.. math::

   x_{ij} \in \{0,1\}

where:

- :math:`i \in I` represents compute nodes (servers, clusters, or regions)
- :math:`j \in J` represents workloads (jobs, services, or user requests)

A value of 1 indicates that workload :math:`j` is assigned to compute node :math:`i`.

Balanced and unbalanced cases differ in how feasibility constraints are defined.

Problem Structure
-----------------

We define:

- :math:`I` : set of compute nodes
- :math:`J` : set of workloads
- :math:`c_{ij}` : cost of assigning workload :math:`j` to compute node :math:`i`

Each compute node may have capacity limits, and each workload requires exactly one
(or at least one) assignment depending on the system configuration.

Balanced Assignment
-------------------

In the balanced case, the system is structurally symmetric:

- number of compute nodes equals number of workloads, or
- total capacity is exactly matched across both sides

This leads to a one-to-one assignment structure:

.. math::

   \sum_{j \in J} x_{ij} = 1 \quad \forall i \in I

.. math::

   \sum_{i \in I} x_{ij} = 1 \quad \forall j \in J

This represents an idealized cloud system where every workload is matched to
exactly one compute resource, and all resources are fully utilized.

Unbalanced Assignment
---------------------

In real cloud environments, workloads typically exceed available compute capacity.

This leads to an unbalanced structure:

- :math:`|J| \gg |I|`, or
- total demand exceeds total supply

In this case, assignment constraints are relaxed:

.. math::

   \sum_{i \in I} x_{ij} \le 1 \quad \forall j \in J

or extended with penalties for unassigned workloads.

This introduces the possibility that:

- some workloads remain unserved
- workloads are prioritized based on cost or importance
- system throughput is optimized under resource constraints

Objective Function
------------------

The objective is to minimize total assignment cost:

.. math::

   \min \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}

In unbalanced settings, additional penalty terms may be introduced for:

- unassigned workloads
- overloaded compute nodes
- service degradation

Modeling Interpretation
-----------------------

From a systems perspective, this model represents cloud workload scheduling
under structural resource constraints.

- compute nodes correspond to data centers or server clusters
- workloads correspond to user requests, jobs, or containers
- assignment decisions represent scheduling and routing decisions

The balanced case corresponds to idealized batch allocation systems, while the
unbalanced case reflects realistic production environments such as:

- bursty traffic in web services
- serverless function invocation spikes
- heterogeneous job arrival patterns

Feasibility Structure
---------------------

Balanced assignment assumes feasibility by construction.

Unbalanced assignment introduces potential infeasibility unless one of the
following is used:

- relaxed constraints (allowing unassigned workloads)
- dummy compute nodes (representing backlog or virtual capacity)
- penalty variables for unmet demand

This makes unbalanced assignment significantly more expressive and realistic.

Structural Properties
---------------------

The balanced/unbalanced assignment model exhibits the following properties:

- **bipartite structure**: assignments occur between compute nodes and workloads
- **symmetry vs asymmetry**: structure depends on system balance
- **capacity sensitivity**: feasibility depends on system scale
- **relaxation behavior**: unbalanced models naturally extend to partial assignment
- **penalty modeling**: unmet demand can be explicitly priced

Relationship to Other Models
----------------------------

This model connects directly to other assignment and covering structures:

- **Classical assignment**: special case of balanced structure
- **Transportation problem**: relaxation with flow variables
- **Generalized assignment**: capacity-constrained extension
- **Multi-assignment**: redundant coverage of workloads
- **Facility location**: introduces activation decisions for compute nodes

Discussion
----------

Balanced and unbalanced assignment models highlight a key modeling principle:

> real systems are rarely structurally symmetric, and optimization models must
> explicitly account for this asymmetry

In cloud infrastructure systems, this distinction determines whether the model
represents:

- idealized scheduling (balanced case), or
- realistic production workload allocation (unbalanced case)

This makes the model particularly important as a bridge between theoretical
assignment problems and real-world cloud computing systems.

Implementation
--------------

In the Opt Modeling Lab, the balanced/unbalanced assignment model is implemented
using the same binary decision framework as classical assignment, with structural
differences encoded in the constraint system.

The accompanying notebook demonstrates:

- synthetic cloud workload generation
- comparison between balanced and unbalanced regimes
- visualization of assignment density across compute nodes
- impact of capacity imbalance on solution structure

See Also
--------

See :doc:`../assignment` for the classical formulation,
:doc:`../transportation` for continuous flow relaxation, and
:doc:`../generalized_assignment` for capacity-constrained extensions.