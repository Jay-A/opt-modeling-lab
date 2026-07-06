Opt Modeling Lab
----------------

`GitHub Repository <https://github.com/Jay-A/opt-modeling-lab>`_

Note that this is a work in progress, and that although it is quickly becoming quite
lengthy, there are still a lot of changes, edits, rewrites, and examples to make. 
I do hope to get to the point where we can look at runtime performance and memory metrics of 
standard and strong formulations for some of the more interesting problems soon at the
very least ... fingers crossed. For now, the only baked-in backend is python-mip, but 
the cross backend comparison is something that I am quite interested in. Far out into the 
not-to-distant future, it may be fun to hijack some routines with custom C/C++ routines 

A structured lab for exploring mixed-integer optimization models,
solver backends, and modeling abstractions.

Core Architecture
------------------

This project is organized into three layers:

- **Chapters**: conceptual and theoretical frameworks
- **Problems**: concrete optimization models
- **Modeling Layer**: solver-agnostic abstraction (``aliases.py``)

Navigation
----------

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Chapters

   chapters/index

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :caption: Problems

   problems/index

.. toctree::
   :titlesonly:
   :maxdepth: 1
   :caption: Modeling Layer

   modeling