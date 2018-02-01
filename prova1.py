from mpi4py import MPI
import sys
import numpy as np

# Commented line

numberRows = int( sys.argv[1])
numberColumns = int( sys.argv[2])
TaskMaster = 0

assert numberRows == numberColumns

a = np.zeros(shape=(numberRows, numberColumns))
b = np.zeros(shape=(numberRows, numberColumns))
c = np.zeros(shape=(numberRows, numberColumns))

def populateMatrix( p ):
    for i in range(0, numberRows):
        for j in range(0, numberColumns):
            p[i][j] = i+j

comm = MPI.COMM_WORLD
worldSize = comm.Get_size()
rank = comm.Get_rank()
processorName = MPI.Get_processor_name()
print ("Process %d started.\n" % (rank))
#print ("Running from processor %s, rank %d out of %d processors.\n" % (processorName, rank, worldSize))
