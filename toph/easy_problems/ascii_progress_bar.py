""" ASCII Progress Bar """
from math import floor
rate = float(input())
# Round numbers down to the nearest integer
near = int(floor(rate))
tm = int(rate/10)

data = ["["]
data.extend("+" for _ in range(tm))
data.extend("." for _ in range(10, tm, -1))
data.extend(("]", f" {near}%"))
print("".join(data))
