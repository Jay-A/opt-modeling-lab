Scheduling-Style Optimization Problems
======================================

Overview
--------

Scheduling problems are a fundamental class of mixed-integer programming models
in which the primary modeling decision is determining when and in what order a
set of activities should be performed.

Unlike assignment problems, which match entities to one another, scheduling
problems introduce an explicit **temporal dimension**. Decisions must account
for both resource allocation and the timing of activities.

These models arise naturally in manufacturing systems, workforce planning,
project management, and other environments where limited resources must be
coordinated over time.

Formulation Structure
---------------------

Scheduling models typically include decision variables that represent timing
and ordering relationships between activities.

Common representations include:

- start times of activities
- completion times
- sequencing relationships between jobs
- binary variables encoding temporal ordering or machine usage

Depending on the formulation, scheduling models may involve continuous,
integer, or binary decision variables.

Typical scheduling objectives include:

.. math::

   \min C_{\max}

(minimizing makespan),

.. math::

   \min \sum_j C_j

(minimizing total completion time), or

.. math::

   \min \sum_j w_j T_j

(minimizing weighted tardiness).

These objectives are optimized subject to temporal feasibility and resource
constraints.

Modeling Characteristics
------------------------

Scheduling models are characterized by several structural features:

- **temporal decision structure**: activities are embedded in time
- **resource constraints over time**: limited resources cannot process overlapping tasks
- **precedence relationships**: certain activities must occur before others
- **sequencing interactions**: competing tasks require ordering decisions

These features distinguish scheduling models from selection and assignment
problems by introducing explicit time-based coupling between decisions.

Canonical Structure
------------------

Most scheduling problems follow a common modeling pattern:

1. Define a set of jobs or activities
2. Define processing requirements and available resources
3. Introduce variables representing timing and sequencing decisions
4. Encode precedence and resource feasibility constraints
5. Optimize a performance measure such as makespan, completion time, or tardiness

This structure appears broadly in production systems, computing, transportation,
and workforce planning.

Representative Problems
-----------------------

The following problems illustrate the scheduling modeling paradigm, ranging
from basic single-machine settings to more complex multi-resource systems.

Single Machine Scheduling
^^^^^^^^^^^^^^^^^^^^^^^^^

Single machine scheduling considers a set of jobs processed on a single
resource.

The primary decision is determining the processing order that optimizes a
given objective such as makespan or total completion time.

Parallel Machine Scheduling
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parallel machine scheduling extends the single-machine case by introducing
multiple machines, requiring both assignment and sequencing decisions.

Job Shop Scheduling
^^^^^^^^^^^^^^^^^^^

Job shop scheduling models production systems where each job consists of a
sequence of operations that must be processed on specific machines.

Feasible schedules must satisfy both machine capacity constraints and operation
precedence relationships.

Flow Shop Scheduling
^^^^^^^^^^^^^^^^^^^^

Flow shop scheduling considers systems where all jobs follow the same machine
ordering, introducing structured temporal constraints.

Workforce Scheduling
^^^^^^^^^^^^^^^^^^^^

Workforce scheduling determines shift assignments over time while satisfying
labor rules, demand requirements, and availability constraints.

These models combine assignment and temporal structure in a unified framework.

Project Scheduling
^^^^^^^^^^^^^^^^^^

Project scheduling models (such as RCPSP and PERT/CPM variants) determine the
timing of interdependent activities subject to precedence and resource
constraints.

Discussion
----------

Scheduling models extend assignment models by introducing an explicit temporal
structure.

Rather than determining only which resource performs each task, the optimizer
must also determine when each activity occurs while respecting precedence and
resource constraints.

This additional dimension significantly increases modeling complexity and
leads to many of the most challenging and practically important optimization
problems.

In the remainder of this section, we focus on canonical scheduling models
formulated within the mixed-integer programming framework.

Navigation
----------

.. toctree::
   :maxdepth: 1

   ../problems/single_machine
   ../problems/parallel_machine
   ../problems/job_shop
   ../problems/flow_shop
   ../problems/open_shop
   ../problems/workforce_scheduling
   ../problems/project_scheduling

.. Scheduling Models
.. ├── Single Machine Scheduling
.. ├── Parallel Machine Scheduling
.. ├── Job Shop Scheduling
.. ├── Flow Shop Scheduling
.. ├── Open Shop Scheduling
.. ├── Workforce Scheduling
.. └── Project Scheduling (RCPSP / PERT / CPM)