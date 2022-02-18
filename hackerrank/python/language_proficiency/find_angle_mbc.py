"""
is a right triangle,  at .
Therefore, .
Point  is the midpoint of hypotenuse .
You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.
"""
import math

AB = int(input())
BC = int(input())

H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0

Output = int(round(math.degrees(math.acos(adj/H))))
Output = str(Output)
print(f'{Output}°')
