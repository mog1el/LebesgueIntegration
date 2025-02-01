#This is not the most efficient way to integrate, but rather an intellectual exercise
import numpy as np

user_f = input("Enter a function of x (use numpy functions like np.sin, np.exp, etc.): ")
f = lambda x: eval(user_f)

minmax = [] 
bounds = []

lower = float(input("Enter the lower bound of the integral"))
higher = float(input("Enter the higher bound of the integral"))
dy = 0.1
area = float(0)

i = lower
min = float() 
max = float()
while i < higher:
    fv = float(f(i))
    if fv < min:
        min = fv
    elif fv > max:
        max = fv
    i += dy

i = lower
absmin = min
print(min, max)
#fin = []
#while min <= max:
#    while i < higher:
#        fv = float(f(i))
#        if min <= fv:
#            fin.append(i)
#        i += dy
#    area += len(fin)*(dy**2)
#    min += dy
#    fin = []
#    i = lower

#points = []
#min = absmin
#while min <= max:
#    while i < higher:
#        fv = float(f(i))
#        if min == fv:
#            points.append(i)
#    i = 0
#    if abs(min) <= abs(float(f(lower))):
#        for i in range (1, len(points), 2):
#            area += points[i] - points[i-1]
#    else:
#        for i in range (2, len(points), 2):
#            area += points[i] - points[i-1]
#        i += dy
#    min += dy

print(area)