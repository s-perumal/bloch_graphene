
#Sathya S R R Perumal
#!/bin/python3


import numpy as np
a = 1.42
r_cc = np.sqrt(3) * a
b1 = ( 2 * np.pi / r_cc) * np.array([1,0])
b2 = ( 2 * np.pi / r_cc) * np.array([1/2, np.sqrt(3)/2])

k_points = [ np.array([0,0]),
             np.array([1/3,0]),
             np.array([1/2,0]),
             np.array([0,0])]

def energycal(k,a1,a2)
    

