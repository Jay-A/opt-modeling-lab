Generalized Assignment Problem (Cloud HPC Scheduling)
=====================================================

Overview
--------

The generalized assignment problem (GAP) is a fundamental extension of the classical assignment model in which assignments consume limited resources.

In this formulation, a set of computational jobs must be assigned to a set of GPU clusters in a way that respects cluster capacity constraints while minimizing a global scheduling cost.

Unlike the classical assignment problem, where each assignment is structurally uniform, the generalized assignment problem introduces **resource-dependent feasibility**, making assignment decisions coupled through capacity constraints.

This model is widely used as an abstraction of workload scheduling in cloud and high-performance computing (HPC) systems.

Connection to Optimization Framework
-------------------------------------

As defined in the foundations chapter, an optimization problem consists of

- decision variables,
- an objective function, and
- a feasible region defined by constraints.

In the generalized assignment model:

- **decision variables** represent assignment of jobs to clusters,
- **constraints** enforce both exclusivity and resource limits,
- **objective function** captures the cost of executing a job on a given cluster.

This structure fits into the mixed-integer linear programming framework:

.. math::

   \min c^T x \quad \text{subject to} \quad Ax \le b,\quad x \in \{0,1\}^n.

Problem Structure
-----------------

We define:

- :math:`i \in I` : GPU clusters (agents)
- :math:`j \in J` : computational jobs (tasks)

Each cluster has a finite processing capacity :math:`b_i`, expressed in GPU-hours.
Each job requires a resource consumption :math:`a_{ij}` when executed on cluster :math:`i`.

Decision Variables
------------------

Let

.. math::

   x_{ij} \in \{0,1\}

where:

- :math:`x_{ij} = 1` if job :math:`j` is assigned to cluster :math:`i`
- :math:`x_{ij} = 0` otherwise

Each job must be assigned to exactly one cluster.

Constraints
-----------

Job Assignment Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each job is assigned to exactly one cluster:

.. math::

   \sum_{i \in I} x_{ij} = 1 \quad \forall j \in J.

This enforces exclusivity of execution.

Cluster Capacity Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each cluster has a limited computational budget:

.. math::

   \sum_{j \in J} a_{ij} x_{ij} \le b_i \quad \forall i \in I.

This introduces coupling between assignment decisions: assigning one job to a
cluster reduces available capacity for others.

Non-Negativity and Binary Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. math::

   x_{ij} \in \{0,1\}.

Objective Function
------------------

The objective function captures the **expected scheduling cost** of executing
a job on a given cluster.

In cloud and HPC systems, this cost is typically a composite measure derived
from:

- queueing delay at the cluster,
- job priority or service class,
- and resource intensity of the job.

We model this via a cost coefficient :math:`c_{ij}` assigned to each possible
assignment.

The optimization objective is:

.. math::

   \min \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}.

Interpretation of the Cost Function
-----------------------------------

The cost term :math:`c_{ij}` represents an **aggregate scheduling penalty**
associated with executing job :math:`j` on cluster :math:`i`.

In practical cloud and HPC scheduling systems, this penalty is not purely
geometric or physical but is typically derived from multiple interacting
factors:

- **Queueing latency**: expected delay due to congestion at cluster :math:`i`
- **Job priority**: lower priority jobs incur higher effective cost
- **Resource intensity**: larger jobs are more expensive to schedule under contention

A conceptual decomposition of the cost is:

.. math::

   c_{ij}
   =
   \alpha \cdot \text{latency}_{ij}
   +
   \beta \cdot \text{resource}_{j}
   -
   \gamma \cdot \text{priority}_{j}.

This does not represent a literal system implementation, but rather a
**linear surrogate model** capturing how scheduling decisions are influenced by
system-level service objectives.

Modeling Interpretation
-----------------------

The generalized assignment problem introduces a key structural feature absent
in classical assignment:

> assignments are no longer independent; they are coupled through shared
resource constraints.

Each cluster behaves like a knapsack, and each job contributes a resource
consumption that depends on the chosen assignment.

Thus, the model can be interpreted as:

> a collection of knapsack constraints coupled through a global assignment
structure.

This coupling significantly increases computational complexity and is a key
reason why the generalized assignment problem is NP-hard.

Feasibility by Construction
---------------------------

In this implementation, feasibility is ensured by design:

- job demands are scaled relative to total cluster capacity
- thus a feasible assignment always exists
- or, in extended systems, overflow capacity clusters may be introduced

This ensures that the model focuses on optimization behavior rather than
feasibility repair.

Discussion
----------

The generalized assignment problem occupies a central position in mixed-integer
modeling because it connects two fundamental structures:

- **assignment structure**, governing exclusivity of decisions
- **knapsack structure**, governing resource limitations

This combination appears naturally in cloud computing, workforce scheduling,
and distributed processing systems.

In the cloud HPC interpretation, the model represents a simplified view of
priority-aware scheduling, where jobs are assigned to computational resources
based on both system load and service-level considerations.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/generalized_assignment