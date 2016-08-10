#! /usr/bin/env python
import sys
import numpy as np

def evaluateEnergy(J, configuration):
    """
    calculate the energy of a given configuration.

    Parameters:
        >>> J: 
        nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
        >>> configuration: 
        nSpin*1 vector, configuration[i] stores the spin at site i.

    Returns:
        the total energy of this configuration.
    """
    return 0.5*np.dot(configuration,np.dot(J,configuration))


def energyChange(J,oldConfiguration,iSite):
    """
    calculate the energy change when flip one spin at site i.

    Parameters:
        >>> J:
            nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
        >>> oldConfiguration:
            the configuration before flip.
        >>> iSite:
            the site that the spin flips

    """
    pass



def readCoupling(nSpin):
    """
    read spin-spin coupling strength from the file(example.txt).
    
    Parameters:
        >>> nSpin:
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




def getConfiguration(nSpin, J, nFlip):
    """
    Random flip spin and accept the configuration if the energy is lower.

    Parameters:
        >>> nSpin: spin number in the system.
        >>> nFlip: random flip spin times.
        >>> J: the coupling matrix read from the file

    Returns:
        minConfiguration: the minimum energy spin configuration.
        minEnergy: the corresponding minimum energy.
    """
    minEnergy = 0
    #Flip mSites' spins a time
    mSites = 1
    #generate a random configuration first
    newConfiguration = np.random.randint(0,2,nSpin)*2 -1
    for iFlip in range(nFlip):
        randomSites = np.random.randint(0,nSpin,mSites)
        newConfiguration[randomSites] = -newConfiguration[randomSites]
        newEnergy = evaluateEnergy(J, newConfiguration)
        if newEnergy < minEnergy:
            minEnergy = newEnergy
            minConfiguration = newConfiguration

    return minEnergy, minConfiguration



nSpin = 300
nFlip = nSpin*50
J = readCoupling(nSpin)
np.random.seed()
minEnergy, minConfiguration = getConfiguration(nSpin, J, nFlip)
print minEnergy
print 'v '+' '.join(map(str, minConfiguration))
