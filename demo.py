#! /usr/bin/env python
import sys, random, numpy

# Evaluate the energy given a coupling matrix and configuration
def evaluate_energy(J, cfg):
    tot = 0
    for i in range(len(cfg)):
        for j in range(i+1, len(cfg)):
            tot += J[i,j]*cfg[i]*cfg[j]
    return tot

# Read coupling matrix
N = 300
J = numpy.zeros((N,N))
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.split()
        spin_a, spin_b, coupling = int(line[0]), int(line[1]), float(line[2])
        assert(spin_a != spin_b)
        if (spin_a < spin_b):
            J[spin_a,spin_b] = coupling
        else:
            J[spin_b,spin_a] = coupling

# Solve for minimum spin configuration (by random guessing)
min_energy = 1.e9
min_cfg = [1]*N
for i in range(10):
    cfg = [(2*random.randint(0,1)-1) for i in xrange(N)]
    energy = evaluate_energy(J, cfg)
    if energy < min_energy:
        min_energy = energy
        min_cfg = cfg
print min_energy
print 'v '+' '.join(map(str, min_cfg))
