#!/usr/bin/env python
# coding=utf-8
from decimal import Decimal
from decimal import ROUND_UP

# 1=====================
#rate = 1.45
#seconds = 3*60+42
#cost = rate*seconds/60
#print(cost)
#print(round(cost, 2))


# 2======================
rate = Decimal('1.45')
seconds = Decimal('222') # 3*60+42
cost = rate*seconds/Decimal('60')
print(cost)

# 3========================
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)


# 4========================
rate = Decimal('0.01')
seconds = Decimal('5')
cost = rate*seconds/Decimal('60')
print(cost)


# 5========================
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(rounded)
