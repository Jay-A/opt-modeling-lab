"""
aliases.py
==========

Gurobi-style thin wrapper over python-mip.

This module provides a simplified modeling interface inspired by Gurobi's
API, built on top of ``python-mip``. It is designed for experimentation
with optimization modeling abstractions and backend interchangeability.

The goal is to provide a lightweight, consistent interface for:

- variable creation
- constraint definition
- objective specification
- solver execution

It is not a full replacement for Gurobi, but a pedagogical abstraction layer
for studying mixed-integer programming workflows.
"""

from mip import Model as _Model
from mip import xsum as _xsum
from mip import BINARY, INTEGER, CONTINUOUS, MAXIMIZE, MINIMIZE


class Model(_Model):
    """
    Gurobi-style wrapper around ``python-mip.Model``.

    This class extends the base ``mip.Model`` to provide a simplified and
    more expressive modeling interface for optimization problems.

    It adds convenience methods for variable creation, constraint handling,
    and objective definition while preserving full compatibility with
    the underlying solver.

    Attributes
    ----------
    backend_name : str
        Name of the backend used (default: "mip").
    _vars : list
        Internal registry of created variables (for tracking/debugging).
    """

    def __init__(self, backend="mip", *args, **kwargs):
        """
        Initialize optimization model.

        Parameters
        ----------
        backend : str, optional
            Identifier for the solver backend in use.
        *args
            Positional arguments passed to ``mip.Model``.
        **kwargs
            Keyword arguments passed to ``mip.Model``.
        """
        super().__init__(*args, **kwargs)
        self.backend_name = backend
        self._vars = []   # optional tracking

    def add_binary_var(self, name=None):
        """
        Create a binary decision variable.

        Parameters
        ----------
        name : str, optional
            Name of the variable.

        Returns
        -------
        mip.Var
            Binary decision variable.
        """
        v = self.add_var(var_type=BINARY, name=name)
        self._vars.append(v)
        return v

    def add_int_var(self, name=None):
        """
        Create an integer decision variable.

        Parameters
        ----------
        name : str, optional
            Name of the variable.

        Returns
        -------
        mip.Var
            Integer decision variable.
        """
        v = self.add_var(var_type=INTEGER, name=name)
        self._vars.append(v)
        return v

    def add_continuous_var(self, name=None):
        """
        Create a continuous decision variable.

        Parameters
        ----------
        name : str, optional
            Name of the variable.

        Returns
        -------
        mip.Var
            Continuous decision variable.
        """
        v = self.add_var(var_type=CONTINUOUS, name=name)
        self._vars.append(v)
        return v

    def add_constraint(self, expr):
        """
        Add a constraint to the model.

        Parameters
        ----------
        expr : mip.LinExpr or constraint expression
            Constraint expression of the form ``lhs <= rhs`` or similar.
        """
        self += expr

    def set_objective(self, expr, sense):
        """
        Set the objective function.

        Parameters
        ----------
        expr : mip.LinExpr
            Objective expression.
        sense : int
            Optimization sense (MAXIMIZE or MINIMIZE).
        """
        self.objective = expr
        self.sense = sense

    def solve(self):
        """
        Solve the optimization model.

        Returns
        -------
        OptimizationStatus
            Solver result status from ``python-mip``.
        """
        return super().optimize()


# ---------------------------------------------------------------------
# Gurobi-style aliases for constants
# ---------------------------------------------------------------------

GRB_BINARY = BINARY
GRB_INTEGER = INTEGER
GRB_CONTINUOUS = CONTINUOUS

GRB_MAXIMIZE = MAXIMIZE
GRB_MINIMIZE = MINIMIZE


def quicksum(exprs):
    """
    Efficient summation of expressions (Gurobi-style alias).

    Parameters
    ----------
    exprs : iterable
        Iterable of linear expressions.

    Returns
    -------
    mip.LinExpr
        Summed linear expression.
    """
    return _xsum(exprs)


# Alias for consistency with Gurobi API
xsum = _xsum


class GRB:
    """
    Namespace for Gurobi-style constants.

    This class mimics the structure of the Gurobi ``GRB`` module to ease
    migration from Gurobi-style syntax to ``python-mip`` backend.
    """

    BINARY = BINARY
    INTEGER = INTEGER
    CONTINUOUS = CONTINUOUS

    MAXIMIZE = MAXIMIZE
    MINIMIZE = MINIMIZE