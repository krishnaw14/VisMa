# This module contains classes for all functions
# TODO: Add exponential, logarithmic, trigonometric and hyperbolic functions
# FIXME: Fix method arguments


class Function(object):

    def __init__(self, tid, scope, coefficient, power, operand, operator):
        self.tid = ""
        self.scope = []
        self.coefficient = None
        self.power = None
        self.operand = []
        self.operator = []

    def setprop(self, operand=None, operator=None, power=None, coefficient=None, scope=None):
        if operand is not None:
            self.operand = operand
        if operator is not None:
            self.operand = operator
        if power is not None:
            self.power = power
        if coefficient is not None:
            self.coefficient = coefficient
        if scope is not None:
            self.scope = scope

    def inverse(self, RHS):
        RHS.coefficient = (RHS.coefficient /
                           self.coefficient)**(1 / self.power)
        RHS.power /= self.power
        self.operand = RHS
        self.coefficient = 1
        self.power = 1

    def differentiate(self):
        self.power = 1
        self.coefficient = 1

    def level(self):
        return (int((len(self.tid)) / 2))


###################
# Mixed Functions #
###################
# For example: sec(x)*tan(x) or sin(x)*log(x) or e^(x)*cot(x)
# Will be taken care by function 'Token ID'ing/tokening module