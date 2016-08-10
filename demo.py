#! /usr/bin/env python
import sys
import numpy as np

def evaluateEnergy(J, configuration):
    """
    calculate the energy of a given configuration.

    Parameters:
    J: 
        nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
    configuration: 
        nSpin*1 vector, configuration[i] stores the spin at site i.

    Returns:
        the total energy of this configuration.
    """
    return 0.5*np.dot(configuration,np.dot(J,configuration))



def readCoupling(nSpin):
    """
    read spin-spin coupling strength from the file(example.txt).
    
    Parameters:
        nSpin:
            the number of spins, in example.txt is 300.

    Returns:
        the symmetric matrix J with J[i,j] represent the coupling strength 
        of spin[i] and spin[j].
    """
    J = np.zeros((nSpin,nSpin)) #zero if not defined in the file
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.split()
            J[int(line[0]),int(line[1])] = float(line[2])
            J[int(line[1]),int(line[0])] = float(line[2])
    return J




def guessConfiguration(nSpin, J, nGuess):
    """
    random generate spin configuration nGuess times and keep the best.

    Parameters:
        nSpin: number of spins in the system.
        J: the coupling matrix read from the file
        nGuess: number of random guess of the spin configuration.

    Returns:
        minConfiguration: the minimum energy spin configuration.
        minEnergy: the corresponding minimum energy.
    """
    minEnergy = 0
    for i in range(nGuess):
        newConfiguration = np.random.randint(0,2,nSpin)*2 -1
        newEnergy = evaluateEnergy(J, newConfiguration)
        if newEnergy < minEnergy:
            minEnergy = newEnergy
            minConfiguration = newConfiguration

    return minEnergy, minConfiguration


nSpin = 300
J = readCoupling(nSpin)
minEnergy, minConfiguration = guessConfiguration(nSpin, J, nGuess=20)
print minEnergy
print 'v '+' '.join(map(str, minConfiguration))
