Vertex Cover Problem
====================

Overview
--------

The vertex cover problem is a classical combinatorial optimization model defined
on an undirected graph. The objective is to select a minimum-cost subset of
vertices such that every edge in the graph is incident to at least one selected
vertex.

This makes vertex cover a fundamental **covering problem on graphs**, where the
objects requiring coverage are communication links rather than individual
elements.

A canonical application is **enterprise network security**, where monitoring
agents must be deployed on a subset of services to ensure that every permitted
communication path is observable.

Problem Statement
-----------------

Given:

- an undirected graph consisting of vertices and communication links
- a cost associated with deploying a monitoring agent to each vertex

select a minimum-cost subset of vertices such that every communication link is
incident to at least one selected vertex.

In the cybersecurity interpretation:

- vertices represent services, hosts, or network endpoints
- edges represent permitted service-to-service communication
- selecting a vertex corresponds to deploying a security monitoring agent
- every communication link must be monitored from at least one endpoint

Decision Variables
------------------

Let

.. math::

   x_i =
   \begin{cases}
   1 & \text{if monitoring is deployed at vertex } i, \\
   0 & \text{otherwise}
   \end{cases}

Each binary variable indicates whether a monitoring agent is installed at the
corresponding network service.

Mathematical Formulation
------------------------

Objective:

.. math::

   \min \sum_{i \in V} c_i x_i

Subject to:

Edge coverage constraints:

.. math::

   x_i + x_j \geq 1
   \qquad
   \forall (i,j) \in E

and

.. math::

   x_i \in \{0,1\},
   \qquad
   \forall i \in V.

where:

- :math:`V` is the set of vertices
- :math:`E` is the set of communication links
- :math:`c_i` is the deployment cost of monitoring vertex :math:`i`

Modeling Interpretation
-----------------------

This formulation specializes the general optimization problem introduced in the
course overview by defining:

- optimization variables corresponding to monitoring decisions
- a linear objective minimizing deployment cost
- a feasible region defined by edge coverage constraints

Unlike set covering, where constraints are generated from a universe of
elements, vertex cover derives its constraints directly from the topology of a
graph.

Each edge represents a communication channel that must be monitored by at least
one of its incident vertices.

Feasibility Structure
---------------------

The model is always feasible by construction:

- deploying monitoring agents at every vertex satisfies every edge constraint
- the optimization problem seeks the smallest or least-cost subset that
  preserves complete communication coverage

Thus, the solver is guaranteed to have a feasible starting point.

Structural Properties
---------------------

The vertex cover problem exhibits several important structural features:

- **graph-based constraints**: every constraint corresponds to an edge
- **local interactions**: each decision affects only neighboring vertices
- **redundant coverage**: either endpoint of an edge may satisfy its constraint
- **global optimization**: local decisions combine to minimize overall
  deployment cost

These properties distinguish vertex cover from element-based covering models.

Relationship to Other Models
----------------------------

Vertex cover is closely related to several classical optimization problems:

- **Set cover**, where each vertex covers its incident edges
- **Independent set**, whose complement is a vertex cover
- **Maximum clique**, through graph complement relationships

Together these problems form a core family of graph optimization models.

Discussion
----------

The vertex cover problem demonstrates how the generic optimization framework can
be specialized to graph-structured systems.

Rather than covering independent elements, the model covers interactions between
pairs of entities. This perspective naturally arises in cybersecurity,
telecommunications, transportation, and infrastructure monitoring, where the
primary objective is to observe or protect communication links rather than
individual nodes.

Implementation
--------------

The Opt Modeling Lab implements vertex cover using a unified modeling interface
shared across all examples.

The cybersecurity notebook demonstrates:

- construction of a synthetic enterprise communication graph
- binary deployment decisions for monitoring agents
- edge-wise coverage constraints
- visualization of the resulting monitored network

See Also
--------

See :doc:`../set_cover` for the more general covering formulation,
:doc:`../maximum_coverage` for budget-constrained coverage maximization, and
:doc:`../selection_problems` for related discrete optimization models.