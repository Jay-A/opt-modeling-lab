Matching Problem — Cybersecurity Incident Response Allocation
=============================================================

Overview
--------

The matching problem is a fundamental combinatorial optimization model in which
the goal is to select a subset of pairwise relationships between two disjoint
sets of entities such that no entity participates in more than one selected pair.

Unlike assignment models, matching does not require full participation of all
elements. Instead, it selects an optimal subset of **non-overlapping pairings**
based on cost, benefit, and structural feasibility.

In this lab, we interpret matching as a **cybersecurity incident response
allocation problem**, where detected incidents must be paired with available
defenders or analysts under limited response capacity.

Connection to Optimization Framework
-------------------------------------

As in the general mixed-integer programming framework, the model consists of:

- decision variables
- an objective function
- a feasible region defined by constraints

The decision variables are defined as:

.. math::

   x_{ij} \in \{0,1\}

where:

- :math:`i \in I` represents security incidents
- :math:`j \in D` represents defenders or response agents

A value of 1 indicates that incident :math:`i` is assigned to defender
:math:`j`.

Problem Structure
-----------------

We consider a bipartite interaction structure:

- :math:`I` : set of detected security incidents
- :math:`D` : set of defensive response agents

Each feasible pairing :math:`(i, j)` has an associated cost and benefit:

- :math:`c_{ij}`: response cost (latency, workload, overhead)
- :math:`r_{ij}`: mitigation benefit (risk reduction, effectiveness)

In implementation, these are combined into a **net utility**:

.. math::

   u_{ij} = r_{ij} - c_{ij}

Objective Function
------------------

The model maximizes total net utility:

.. math::

   \max \sum_{i \in I} \sum_{j \in D} u_{ij} x_{ij}

This formulation reflects a key modeling decision:  
only assignments that improve overall system utility are activated.

This is important because it means that matching is not forced — it is
**selected only when beneficial**.

Constraints
-----------

The defining feature of matching models is non-overlap of selected pairs.

Incident constraints:

.. math::

   \sum_{j \in D} x_{ij} \le 1 \quad \forall i \in I

Defender constraints:

.. math::

   \sum_{i \in I} x_{ij} \le 1 \quad \forall j \in D

Binary constraints:

.. math::

   x_{ij} \in \{0,1\}

Modeling Interpretation
-----------------------

In the cybersecurity interpretation, the model represents real-time allocation
of incident response resources under limited analyst capacity.

A key modeling decision in this formulation is that **participation is optional**:

- incidents may remain unassigned
- defenders may remain idle
- only high-value pairings are selected

This reflects realistic SOC behavior, where low-priority incidents may be
deferred and resources allocated to higher-impact threats.

Structural Properties
---------------------

The matching problem exhibits several key structural characteristics:

- **bipartite interaction structure**: decisions occur between two disjoint sets
- **local exclusivity constraints**: each node participates in at most one match
- **objective-driven sparsity**: only high-utility edges are selected
- **partial coverage**: not all incidents or defenders must be used
- **graph-theoretic interpretation**: equivalent to selecting a set of edges
  in a bipartite graph with no shared vertices

Optimal Sparsity and Null Matching
-----------------------------------

An important property of this model is that feasibility does not guarantee
activation.

Even when all incidents and defenders have feasible pairings, the optimal
solution may assign no matches at all if all available utilities are negative or
insufficiently attractive.

This highlights a fundamental modeling distinction:

- feasibility defines what is possible
- the objective function determines what is selected

In cybersecurity terms, this corresponds to situations where certain incidents
are deprioritized due to low expected impact or high response cost.

Relationship to Other Models
----------------------------

Matching occupies a central position in the hierarchy of assignment-style models:

- **Assignment problem**: enforces full one-to-one coverage
- **Matching problem**: selects a subset of pairings without full coverage
- **Multi-assignment problem**: allows repeated participation under capacity
- **Set packing problem**: abstract generalization of non-overlapping selection

In graph-theoretic terms, matching corresponds to selecting a set of edges such
that no two edges share a common vertex.

Discussion
----------

The cybersecurity matching model captures realistic incident response
conditions where:

- analyst capacity is limited
- response cost varies across assignments
- not all incidents are worth immediate attention
- prioritization is driven by net operational utility

This makes matching a natural model for real-time security operations systems,
where the primary objective is to allocate limited response resources
efficiently under uncertainty and overload conditions.

A key modeling decision in this formulation is the use of **net utility
maximization**, which directly determines sparsity in the solution and explains
why some defenders or incidents may remain unused.

Implementation
--------------

The Opt Modeling Lab implements the matching model using binary decision
variables over a bipartite incident–defender graph.

The notebook demonstrates:

- construction of a synthetic incident-response network
- cost and benefit generation for each feasible pairing
- selection of high-utility matches under exclusivity constraints
- visualization of a sparse bipartite matching structure

See Also
--------

See :doc:`../assignment` for full allocation models,
:doc:`../multiassignment` for capacity-expanded assignment structures, and
:doc:`../set_packing` for the abstract combinatorial generalization of matching.