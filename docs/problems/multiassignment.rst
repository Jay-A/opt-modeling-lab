Multi-Assignment Problem
=========================

Overview
--------

The multi-assignment problem is a classical extension of assignment models in
mixed-integer programming, where elements from one set may be assigned to
multiple elements in another set subject to capacity and structural constraints.

Unlike the classical assignment problem, which enforces a one-to-one matching,
the multi-assignment model allows **one-to-many relationships**, making it a
natural framework for modeling distributed allocation, redundancy, and
resource replication.

In this lab, the multi-assignment structure is used to model **security
monitoring allocation in enterprise networks**, where monitoring agents may
observe multiple services, and services may be observed by multiple agents.

This introduces redundancy and robustness into the monitoring architecture,
reflecting real-world cybersecurity systems.

Connection to Optimization Framework
-------------------------------------

As defined in the foundational chapter, an optimization problem consists of

- decision variables,
- an objective function, and
- a feasible region defined by constraints.

In the multi-assignment model, these components specialize as follows:

- **decision variables** represent assignment relationships between agents and services,
- **objective function** measures total deployment or monitoring cost,
- **constraints** regulate capacity of agents and coverage requirements of services.

This fits directly into the mixed-integer linear programming framework:

.. math::

   \operatorname{opt}_{x \in X} c^T x
   \quad \text{subject to} \quad Ax \le b,\; x \in \{0,1\}^{|A|\times|S|}.

Problem Structure
-----------------

We define two index sets:

- :math:`i \in A` : security agents (monitors)
- :math:`j \in S` : services (network endpoints)

Each agent has a monitoring capacity :math:`u_i`, representing the maximum number
of services it can observe. Each service has a coverage requirement :math:`r_j`,
representing the minimum number of agents that must monitor it.

Decision Variables
------------------

Let

.. math::

   x_{ij} =
   \begin{cases}
   1 & \text{if agent } i \text{ monitors service } j, \\
   0 & \text{otherwise}
   \end{cases}

Each binary variable represents an assignment decision between an agent and a service.

Unlike classical assignment models, these variables do not enforce exclusivity,
allowing multiple simultaneous assignments across both rows and columns of the
assignment matrix.

Objective Function
------------------

Each assignment is associated with a cost :math:`c_{ij}`, representing monitoring
overhead, latency, or operational burden.

The objective is to minimize total monitoring cost:

.. math::

   \min \sum_{i \in A} \sum_{j \in S} c_{ij} x_{ij}.

This captures the system-level goal of deploying a monitoring structure that
is both efficient and sufficiently redundant.

Constraints
-----------

The model is governed by two fundamental constraint classes.

Agent Capacity Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each agent can monitor only a limited number of services:

.. math::

   \sum_{j \in S} x_{ij} \le u_i
   \qquad \forall i \in A.

These constraints limit the workload of each monitoring agent.

Service Coverage Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each service must be monitored by at least a minimum number of agents:

.. math::

   \sum_{i \in A} x_{ij} \ge r_j
   \qquad \forall j \in S.

These constraints ensure redundancy in the monitoring system.

Binary Constraints
^^^^^^^^^^^^^^^^^^

.. math::

   x_{ij} \in \{0,1\}
   \qquad \forall i \in A,\; j \in S.

This enforces discrete assignment decisions.

Why This is a Multi-Assignment Problem
--------------------------------------

This model generalizes classical assignment structures in two directions:

1. **One-to-many allocation**

   - each agent can be responsible for multiple services

2. **Many-to-one coverage**

   - each service can be monitored by multiple agents

This dual relaxation distinguishes the model from:

- **Classical assignment**, which enforces one-to-one matching
- **Transportation models**, which allow continuous flow but no discrete assignment
- **Set covering models**, which enforce coverage without structured pairing

The multi-assignment model occupies the intersection of assignment and covering
structures.

Modeling Interpretation
-----------------------

From a systems perspective, this model represents a **redundant monitoring
architecture** in a distributed enterprise network.

Unlike vertex cover, which selects endpoints of communication links, the
multi-assignment model explicitly encodes **who monitors what**, allowing
fine-grained control over redundancy, workload balancing, and resilience.

This is particularly relevant in cybersecurity settings where:

- multiple monitoring agents may observe the same service for fault tolerance
- services may require multiple independent observers for anomaly detection
- monitoring load must be balanced across a distributed infrastructure

Feasibility Structure
---------------------

Feasibility depends on the balance between:

- total agent capacity
- total service coverage requirements

Unlike vertex cover, feasibility is **not guaranteed by construction**, and
may require careful parameter design or relaxation strategies.

Structural Properties
---------------------

The multi-assignment problem exhibits the following structural features:

- **bipartite decision structure**: assignments occur between two disjoint sets
- **row constraints**: agent capacity limits
- **column constraints**: service redundancy requirements
- **matrix-based decision space**: variables form a structured assignment matrix
- **coupled feasibility conditions**: row and column constraints interact globally

These properties make the model significantly richer than classical assignment
and closely related to covering and network flow formulations.

Relationship to Other Models
----------------------------

The multi-assignment model bridges several fundamental optimization classes:

- **Classical assignment**, as a special case with unit capacities
- **Set cover**, when viewed from the perspective of service coverage
- **Transportation problems**, when integrality is relaxed
- **Facility location**, when interpreted as assignment with activation costs

It serves as a foundational building block for more complex models involving
resource allocation and redundancy design.

Discussion
----------

The multi-assignment problem demonstrates how relaxing structural constraints
in classical assignment models leads to richer and more realistic system
representations.

In cybersecurity applications, it captures the essential trade-off between:

- monitoring cost
- redundancy for resilience
- workload balancing across agents

Unlike vertex cover, which focuses on **monitoring edges in a graph**, the
multi-assignment model explicitly represents **assignment decisions between
agents and services**, providing a more direct representation of operational
deployment.

Implementation
--------------

The Opt Modeling Lab implements the multi-assignment model using a unified
alias-based interface built on top of mixed-integer linear programming tools.

The implementation demonstrates:

- construction of a bipartite agent-service structure
- binary assignment variables
- capacity and redundancy constraints
- visualization of assignment density in a bipartite graph

See Also
--------

See :doc:`../assignment_problems` for the classical assignment formulation,
:doc:`../transportation` for the continuous relaxation, and
:doc:`../vertex_cover` for graph-based covering structures.