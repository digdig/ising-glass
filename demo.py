#! /usr/bin/env python
import sys
import numpy as np

def evaluateEnergy(J, configuration):
    """
    calculate the energy of a given configuration
    Args:
    J: 
        N*N matrix, J[i,j] is the interation between  
        spins[i] and spin[j]

    configuration: 
        N*1 vector, configuration[i] stores the spin 
        at site i

    Returns:
        the total energy of this configuration
    """
    return 0.5*np.dot(configuration,np.dot(J,configuration))

def readCoupling(N):
    """
    read spin-spin coupling strength from the file(example.txt)
    
    Args:
        N:
            the number of spins, in example.txt is 300

    Returns:
        the symmetric matrix J with J[i,j] represent 
        the coupling strength of spin[i] and spin[j]

    """
    J = np.zeros((N,N)) #zero if not defined in the file
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.split()
            J[int(line[0]),int(line[1])] = float(line[2])
            J[int(line[1]),int(line[0])] = float(line[2])
    return J

N = 300
J = readCoupling(N)
minEnergy = 0

for i in range(10):
    #generate a new configuration by random guessing
    newConfiguration = np.random.randint(0,2,N)*2 -1
    newEnergy = evaluateEnergy(J, newConfiguration)
    if newEnergy < minEnergy:
        minEnergy = newEnergy
        minConfiguration = newConfiguration
print minEnergy
print 'v '+' '.join(map(str, minConfiguration))
