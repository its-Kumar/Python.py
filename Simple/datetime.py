from datetime import *

from _datetime import *

ldates = []
d1 = date(2018, 6, 6)
d2 = date(2019, 6, 6)
d3 = date(2017, 6, 6)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.sort()

for date in ldates:
    print(date)
