Problem Library
===============

Core optimization problems implemented in this lab.

Selection Problems
------------------

- :doc:`knapsack` — Select a subset of items to maximize value while satisfying
  a capacity constraint.

- :doc:`set_cover` — Select a minimum-cost collection of sets such that every
  element in a universe is covered at least once.

- :doc:`set_packing` — Select a maximum-profit collection of sets such that no
  element is contained in more than one chosen set.

- :doc:`set_partitioning` — Select a collection of sets such that every element
  in a universe is covered exactly once.

- :doc:`maximum_coverage` — Select up to a fixed number of sets to maximize the
  number of covered elements.

- :doc:`capital_budgeting` — Select a subset of projects subject to budget and
  logical constraints to maximize total return.

- :doc:`vertex_cover` — Select a minimum-size subset of vertices such that every
  edge in a graph is incident to at least one selected vertex.

Assignment Problems
-------------------

- :doc:`assignment` — Assign resources to tasks while minimizing total
  assignment cost.

- :doc:`transportation` — Allocate continuous flows from supply nodes to demand
  nodes at minimum cost.

- :doc:`generalized_assignment` — Assign tasks to agents with capacity-limited
  resources and coupled assignment decisions.

- :doc:`multiassignment` — Assign multiple agents to multiple tasks under
  capacity and coverage constraints.

- :doc:`facility_location` — Decide which facilities to open and assign clients
  to open facilities while minimizing fixed and assignment costs.

Facility Location Problems
--------------------------

- :doc:`facility_location` — Decide which facilities to open and assign clients
  to open facilities while minimizing fixed and assignment costs.

Problem Subsections
--------------------

.. toctree::
   :maxdepth: 1

   knapsack
   set_cover
   set_packing
   set_partitioning
   maximum_coverage
   capital_budgeting
   vertex_cover
   assignment
   transportation
   generalized_assignment
   multiassignment
   facility_location