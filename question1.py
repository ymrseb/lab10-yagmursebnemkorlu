import numpy as np

#Create an empty array to be filled.
x = np.array([])

for i in np.arange (11,120,1):
    if (np.remainder(i,3) == 0) & (np.remainder(i,9)!=0):
        x = np.append(x, i)
print (x)
