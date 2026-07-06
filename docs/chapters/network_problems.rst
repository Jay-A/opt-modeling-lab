Network-Style Optimization Problems
===================================

Overview
--------

Network problems are a fundamental class of mixed-integer programming models
in which the primary modeling decision is how to route, distribute, or connect
flow through a network in an optimal way.

Unlike scheduling problems, which introduce an explicit temporal dimension,
network models focus on the movement of resources through a graph consisting of
nodes and edges. These resources may represent goods, information, energy,
vehicles, or communication traffic.

These models form the foundation of transportation systems, logistics,
telecommunications, and infrastructure planning.

Formulation Structure
---------------------

Network models define decision variables on the edges (or arcs) of a graph.

Typical variables represent:

- flow along edges
- selection of edges in a network
- capacity decisions on links
- routing decisions between origins and destinations

Flow variables are often continuous:

.. math::

   x_{ij} \ge 0,

although many models also include binary variables for routing or network
design decisions.

A typical network objective takes the form:

.. math::

   \min \sum_{(i,j)\in E} c_{ij} x_{ij}

representing transportation cost, or related objectives such as maximizing
throughput or connectivity.

These objectives are optimized subject to structural constraints imposed by the
network.

Modeling Characteristics
------------------------

Network models are characterized by several defining structural features:

- **graph-based decision structure**: variables are associated with nodes and edges
- **flow conservation constraints**: inflow and outflow must balance at nodes
- **capacity constraints**: edges or nodes have limited throughput
- **connectivity structure**: feasible solutions must respect network topology

These properties distinguish network models from selection, assignment, and
scheduling formulations by explicitly leveraging graph structure.

Canonical Structure
------------------

Most network problems follow a common modeling pattern:

1. Define a graph of nodes and edges
2. Assign costs, capacities, or distances to edges
3. Introduce decision variables on edges representing flow or selection
4. Enforce flow conservation and capacity constraints
5. Optimize a global objective such as cost, flow, or connectivity

This structure appears broadly in transportation, communication, energy, and
supply chain systems.

Representative Problems
-----------------------

The following problems illustrate the network modeling paradigm, ranging from
classical flow models to more complex routing and design problems.

Shortest Path
^^^^^^^^^^^^^

The shortest path problem determines the minimum-cost route between two nodes
in a graph.

It is one of the foundational models in network optimization.

Maximum Flow
^^^^^^^^^^^^

The maximum flow problem determines the largest feasible flow from a source to
a sink subject to capacity constraints.

Flow conservation is the defining structural property of this model.

Minimum-Cost Flow
^^^^^^^^^^^^^^^^^

Minimum-cost flow combines flow conservation, capacity constraints, and
transportation costs in a unified framework.

It generalizes both shortest path and transportation models.

Transshipment
^^^^^^^^^^^^^

Transshipment models extend minimum-cost flow by allowing intermediate
transfer nodes, enabling multi-stage distribution systems.

Vehicle Routing
^^^^^^^^^^^^^^^

Vehicle routing problems determine optimal routes for vehicles serving a set of
customers under capacity and routing constraints.

These models combine assignment, sequencing, and network structure.

Network Design
^^^^^^^^^^^^^^

Network design problems determine which edges or infrastructure components
should be built or upgraded in order to satisfy demand.

These models combine selection decisions with network flow structure.

Traveling Salesman Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^

The traveling salesman problem determines the minimum-cost tour visiting each
node exactly once.

It is a canonical combinatorial optimization problem with strong structural
connections to routing and network design.

Discussion
----------

Network models extend earlier optimization paradigms by introducing
**graph-structured decision variables** and **flow conservation constraints**.

Rather than selecting items, assigning entities, or scheduling activities, the
optimizer determines how resources move through an interconnected system while
respecting capacity and connectivity constraints.

This modeling framework underlies many large-scale optimization applications in
transportation, logistics, telecommunications, and infrastructure systems.

In the remainder of this section, we focus on implementing canonical network
optimization models using mixed-integer programming formulations that exploit
graph structure while remaining compatible with general-purpose solvers.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/shortest_path
   ../problems/maximum_flow
   ../problems/minimum_cost_flow
   ../problems/transshipment
   ../problems/vehicle_routing
   ../problems/network_design
   ../problems/traveling_salesman

.. Network Models
.. ├── Shortest Path
.. ├── Maximum Flow
.. ├── Minimum-Cost Flow
.. ├── Transshipment
.. ├── Vehicle Routing
.. ├── Traveling Salesman Problem
.. └── Network Design