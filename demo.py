#! /usr/bin/env python
import sys
import numpy as np

def totalEnergy(J, configuration):
    """
    calculate the energy for a given configuration.

    Parameters:
        >>> J: 
        nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
        >>> configuration: 
        1*nSpin vector, configuration[i] stores the spin at site i.

    Returns:
        the total energy of this configuration.
    """
    # 0.5 for double counting
    return 0.5*np.dot(configuration,np.dot(J,configuration))


def energyChange(J,configuration,randomSite):
    """
    calculate the energy change when flip one spin at one randomSite.

    Parameters:
        >>> J:
            nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
        >>> configuration:
            the configuration before flip the spin.
        >>> randomSite:
            the site number that the spin flips
    Returns:
        the energy difference when flip one spin
    """
    # energy after - energy before, double counting considered
    return -configuration[randomSite]*np.dot(J[randomSite,:],configuration)



def getJ(nSpin):
    """
    read spin-spin coupling strength from the file (example.txt).
    
    Parameters:
        >>> nSpin:
            the number of spins, in example.txt is 300.

    Returns:
        the symmetric matrix J, with J[i,j] represent the coupling strength 
        between spin[i] and spin[j].
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
    Random flip one spin and accept the configuration if the energy is lower.

    Parameters:
        >>> nSpin: spin number in the system.
        >>> nFlip: number of random one spin flip.
        >>> J: the coupling matrix read from the file

    Returns:
        configuration: the minimum energy spin configuration.
        energy: the corresponding minimum energy.
    """
    #generate a random configuration first
    configuration = np.random.randint(0,2,nSpin)*2 -1
    for iFlip in range(nFlip):
        randomSite = np.random.choice(nSpin)
        if energyChange(J,configuration,randomSite) < 0:
            configuration[randomSite] *= -1

    return totalEnergy(J,configuration), configuration



nSpin = 300
nFlip = nSpin*300
J = getJ(nSpin)
np.random.seed()
energy, configuration = getConfiguration(nSpin, J, nFlip)
print energy
print 'v '+' '.join(map(str, configuration))
