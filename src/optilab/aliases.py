"""
aliases.py

Gurobi-style thin wrapper over python-mip.
"""

from mip import Model as _Model
from mip import xsum as _xsum
from mip import BINARY, INTEGER, CONTINUOUS, MAXIMIZE, MINIMIZE


class Model(_Model):
    def __init__(self, backend="mip", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.backend_name = backend
        self._vars = []   # optional tracking

    def add_binary_var(self, name=None):
        v = self.add_var(var_type=BINARY, name=name)
        self._vars.append(v)
        return v

    def add_int_var(self, name=None):
        v = self.add_var(var_type=INTEGER, name=name)
        self._vars.append(v)
        return v

    def add_continuous_var(self, name=None):
        v = self.add_var(var_type=CONTINUOUS, name=name)
        self._vars.append(v)
        return v

    def add_constraint(self, expr):
        self += expr

    def set_objective(self, expr, sense):
        self.objective = expr
        self.sense = sense

    def solve(self):
        return super().optimize()


GRB_BINARY = BINARY
GRB_INTEGER = INTEGER
GRB_CONTINUOUS = CONTINUOUS

GRB_MAXIMIZE = MAXIMIZE
GRB_MINIMIZE = MINIMIZE


def quicksum(exprs):
    return _xsum(exprs)


xsum = _xsum


class GRB:
    BINARY = BINARY
    INTEGER = INTEGER
    CONTINUOUS = CONTINUOUS

    MAXIMIZE = MAXIMIZE
    MINIMIZE = MINIMIZE