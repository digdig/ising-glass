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


def energyChange(J,configuration,iSpin):
    """
    calculate the energy change when flip one spin at site i.

    Parameters:
        >>> J:
            nSpin*nSpin matrix, J[i,j] is the interation between spin i and j.
        >>> configuration:
            the configuration before flip the spin.
        >>> iSpin:
            the i-th spin that flips
    Returns:
        the energy difference when flip one spin
    """
    # energy after - energy before, double counting considered
    return -configuration[iSpin]*np.dot(J[iSpin,:],configuration)



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




def getConfiguration(nSpin, J, nConfiguration):
    """
    Random generate nConfiguratin and get the lowest local minimum. 

    To get the local minimum for a random configuration, sequentially flip 
    the spins and accept the configuration if the energy is lower.

    Parameters:
        >>> nSpin: spin number in the system.
        >>> J: the coupling matrix read from the file.
        >>> nConfiguration: number of trail initial random configurations.

    Returns:
        globalConfiguration: the global minimum energy spin configuration.
        globalMinEnergy: the global minimum energy of all the trails.
    """
    globalMinEnergy = 10e10

    for iConfiguration in range(nConfiguration):
        configuration = np.random.randint(0,2,nSpin)*2 -1
        localMinEnergy = 10e9
        oneCycleMinEnergy = 10e8    #min energy after flip nSpin spins

        #this while loop get a local min energy and the configuration
        while(oneCycleMinEnergy < localMinEnergy):
            localMinEnergy = oneCycleMinEnergy
            for iSpin in range(nSpin):
                if energyChange(J,configuration,iSpin) < 0:
                    configuration[iSpin] *= -1
            oneCycleMinEnergy = totalEnergy(J, configuration)

        #while ends, localMinEnergy get
        if(globalMinEnergy > localMinEnergy):
            globalMinEnergy = localMinEnergy
            globalConfiguration = configuration

    return totalEnergy(J,globalConfiguration), globalConfiguration



nSpin = 300
J = getJ(nSpin)
np.random.seed()
energy, configuration = getConfiguration(nSpin, J, 300)
print(energy)
print('v '+' '.join(map(str, configuration)))
