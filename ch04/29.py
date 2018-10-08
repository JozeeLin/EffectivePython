#!/usr/bin/env python
# coding=utf-8

class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


# first==========
#r1 = Resistor(50e3)
#r1.ohms = 10e3
#print(r1.ohms)

# second=================
#class VoltageResistance(Resistor):
#    def __init__(self, ohms):
#        super().__init__(ohms)
#        self._voltage = 0
#
#    @property
#    def voltage(self):
#        return self._voltage
#
#    @voltage.setter
#    def voltage(self, voltage):
#        self._voltage = voltage
#        self.current = self._voltage/self.ohms
#
#r2 = VoltageResistance(1e3)
#print('Before: %5r amps' % r2.current)
#r2.voltage = 10
#print('After: %5r amps' % r2.current)


# third===================
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms<=0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


r3 = BoundedResistance(1e3)
#r3.ohms = 0
r3.ohms = 10
print(r3.ohms)
