"""
is a right triangle,  at .
Therefore, .
Point  is the midpoint of hypotenuse .
You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.
"""
import math
ab = int(input())
bc = int(input())

h = math.sqrt(ab**2 + bc**2)
h = h/2.0
adj = bc/2.0

resulr = int(round(math.degrees(math.acos(adj/h))))
degree_sign = u"\N{DEGREE SIGN}"
print(str(resulr)+degree_sign)