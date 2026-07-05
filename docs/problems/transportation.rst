Transportation Problem
=======================

Overview
--------

The **Cloud Resource Allocation** problem is a canonical example of a **transportation
model** in mixed-integer programming (MIP), where divisible resources are
distributed from a set of supply nodes to a set of demand nodes at minimum cost.

In this formulation, compute capacity from distributed data centers must be
allocated to satisfy workload demand across multiple regions while minimizing
latency or communication cost.

Although the application is motivated by modern cloud computing systems, the
underlying mathematical structure is the classical transportation problem.

Connection to Optimization Framework
-------------------------------------

As defined in the root documentation, an optimization problem consists of

- decision variables,
- an objective function, and
- a feasible region defined by constraints.

In the cloud transportation model, these components specialize as follows:

- **decision variables** represent continuous flows of compute resources,
- **objective function** measures total allocation cost (e.g., latency),
- **constraints** enforce supply and demand balance across the system.

This structure fits directly into the linear MIP framework introduced in the
foundations chapter:

.. math::

   \min c^T x \quad \text{subject to} \quad Ax = b, \; x \ge 0.

Problem Structure
-----------------

We define two index sets:

- :math:`i \in I` : data centers (supply nodes)
- :math:`j \in J` : workload regions (demand nodes)

Each data center has a fixed supply capacity :math:`s_i`, and each workload
region has a fixed demand requirement :math:`d_j`.

To ensure feasibility, the system is constructed such that:

.. math::

   \sum_{i \in I} s_i = \sum_{j \in J} d_j.

This balance condition guarantees that all supply can be allocated exactly to
satisfy all demand.

Decision Variables
------------------

Let

.. math::

   x_{ij} \ge 0

denote the amount of compute capacity allocated from data center :math:`i`
to workload region :math:`j`.

Unlike selection or assignment models, these variables are **continuous flow
variables**, representing divisible resource allocation rather than discrete
decisions.

Objective Function
------------------

Each possible allocation has an associated cost :math:`c_{ij}`, representing
latency, bandwidth usage, or communication overhead between a data center and
a workload region.

The objective is to minimize total allocation cost:

.. math::

   \min \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}.

This captures the system-level goal of minimizing total communication cost
while satisfying all demand.

Constraints
-----------

The model is governed by two classes of equality constraints.

Supply Constraints
^^^^^^^^^^^^^^^^^^

Each data center must distribute all available capacity:

.. math::

   \sum_{j \in J} x_{ij} = s_i \quad \forall i \in I.

These constraints enforce that supply is fully allocated across workloads.

Demand Constraints
^^^^^^^^^^^^^^^^^^

Each workload region must receive exactly its required compute capacity:

.. math::

   \sum_{i \in I} x_{ij} = d_j \quad \forall j \in J.

These constraints ensure that all computational demand is satisfied.

Non-Negativity
^^^^^^^^^^^^^^

.. math::

   x_{ij} \ge 0 \quad \forall i \in I, j \in J.

This ensures flows are physically meaningful.

Why This is a Transportation Problem
-------------------------------------

This formulation is classified as a **transportation problem** because it
satisfies the defining structural properties:

1. **Two-layer bipartite structure**

   - one set of supply nodes (data centers)
   - one set of demand nodes (workloads)

2. **Flow-based decision variables**

   - variables represent quantities transported between nodes

3. **Linear cost structure**

   - total cost is additive over individual arcs

4. **Conservation constraints**

   - supply is fully distributed
   - demand is fully satisfied

5. **Balanced system**

   - total supply equals total demand by construction

These properties distinguish transportation problems from:

- **assignment problems**, which use binary matching variables,
- **selection problems**, which choose subsets of items, and
- **network flow problems**, which generalize this structure to arbitrary graphs.

Modeling Interpretation
-----------------------

From a systems perspective, the model represents a **load balancing problem
over a bipartite network**, where compute resources are routed from
distributed infrastructure to demand centers.

Unlike assignment models, decisions are not discrete pairings but **continuous
allocation quantities**, allowing partial distribution of resources across
multiple destinations.

This flexibility is essential in cloud computing systems, where workloads can
be split across multiple data centers.

Feasibility by Construction
---------------------------

In this lab, feasibility is guaranteed by design:

- supply values are randomly generated
- demand values are rescaled to match total supply
- thus a balanced transportation system is always ensured

This removes feasibility as a modeling concern and focuses attention on
optimization structure and solution quality.

Discussion
----------

The transportation model serves as a fundamental bridge between:

- **assignment models** (discrete matching structure), and
- **network flow models** (generalized routing on graphs)

It introduces the idea of **continuous decision flows over structured
networks**, which becomes central in later chapters on:

- minimum-cost flow,
- facility location,
- and large-scale logistics optimization.

In the cloud computing interpretation, the model captures how distributed
compute resources are allocated efficiently across a network of demand
regions, subject to cost and capacity constraints.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/transportation