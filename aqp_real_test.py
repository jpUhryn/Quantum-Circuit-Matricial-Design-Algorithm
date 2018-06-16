
from qiskit.wrapper import load_qasm_file
from qiskit import QISKitError, available_backends, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register

from src.Debug import Debug
from src.QuantumMath import QuantumMath
from src.AQP import AQP
from src.DictionarySearcher import DictionarySearcher
from src.Visualizer import Visualizer
from src.Assembler import Assembler
from src.WriterAsm import WriterAsm

from src.defaultTypes import *

from account.Qconfig import *


import numpy as np

import sys

import math

import matplotlib.pyplot as plt




def generateGate(index, rowReverse, nQubits, dic):
    Debug.debug(str(index) + " ; " + str(nQubits), DebugLevel.Function)

    if rowReverse:
        return AQP.generateRowReverse(target1=0, target2=index, dic=dic)

    else:
        matrix = QuantumMath.getOracleMatrix(nQubits=nQubits, targets=[]) #generate a diagonal matrix
        matrix[0,0] = 1/math.sqrt(2)
        matrix[0,index] = 1/math.sqrt(2)
        matrix[index,0] = 1/math.sqrt(2)
        matrix[index,index] = -1/math.sqrt(2)
        return AQP.generateSpecial(name="2superpoitionGate", matrix=matrix, dic=dic)


def generateMatrix(filename, nQubits, rowReverse, index, compress):
    Debug.debug(filename + " ; " + str(nQubits) + " ; " + str(index), DebugLevel.Function)

    # inicializa un diccionario para 4 qubits
    dic = DictionarySearcher(nQubits=nQubits)

    # genera una puerta de giro condicionado multiple y las subpuertas necesarias
    #id = AQP.generateMultipleTurn(sources=[0,1,2], target=3, angle=math.pi, turnType=TurnType.Z, dic=dic)
    gateId = generateGate(index, rowReverse, nQubits, dic)

    # genera el fichero .qasm para crear esta puerta
    numberGates = WriterAsm.writeAsm(gateId, dic, filename, reset=True, compress=compress)

    print(Colors.BOLD.value + "\nAssembler written with " + str(numberGates) + " gates\n" + Colors.ENDC.value)

    return dic.getGate(gateId).getMatrix()


def areEqual(matrix1, matrix2):
    return np.array_equal(matrix1, matrix2)

def areClose(matrix1, matrix2):
    return np.allclose(matrix1, matrix2)

def probeMatrix(filename, nQubits, rowReverse, index, viewMatrix, compress, shots):
    #Debug.debug(filename + " ; " + str(nQubits) + " ; " + str(index) + " ; " + str(viewMatrix), DebugLevel.Function)

    matrix = generateMatrix(filename, nQubits, rowReverse, index, compress)

    if (viewMatrix):
        print(Colors.BLUE.value + "\nGenerated matrix\n" + str(matrix) + "\n" + Colors.ENDC.value)

    try:

        qc = load_qasm_file(filename)

        job_sim = execute(qc, "local_unitary_simulator")
        sim_result = job_sim.result()
        matrix2 = sim_result.get_unitary(qc)
        
        

        expectedValues = {}

        for i in range(2**nQubits):
            expectedValues["{0:02b}".format(i)] = np.absolute(matrix[i,0])**2


        print(Colors.PURPLE.value + "\n EXPECTED VALUES \n" + str(expectedValues) + "\n\n" + Colors.ENDC.value)

        # send the circuit to the simulator
        qc = load_qasm_file(filename)

        job_sim = execute(qc, "local_qasm_simulator", shots=shots)
        sim_result = job_sim.result()
        simuValues = sim_result.get_counts(qc)
        
        print(Colors.RED.value + "\n SIMULATED VALUES \n" + str(simuValues) + "\n\n" +  Colors.ENDC.value)


        #######################################
        # send the circuit to the real computer

        # Set your API Token.
        # You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
        # looking for "Personal Access Token" section.
        QX_TOKEN = APItoken
        QX_URL = config['url']

        print(Colors.ORANGE.value + "\nConnecting with Quantum Computer... It could take a moment\n\n" +  Colors.ENDC.value)

        # Authenticate with the IBM Q API in order to use online devices.
        # You need the API Token and the QX URL.
        register(QX_TOKEN, QX_URL)

        qc = load_qasm_file(filename)

        job_exp = execute(qc, 'ibmqx4', shots=shots, max_credits=10)
        sim_result = job_exp.result()
        realValues = sim_result.get_counts(qc)

        # Compile and run the Quantum Program on a real device backend
                
        print(Colors.GREEN.value + "\n REAL VALUES \n" + str(realValues) + "\n\n" +  Colors.ENDC.value)

        keys = []
        expectedValuesArray = []
        simuValuesArray = []
        realValuesArray = []
        for i in range(2**nQubits):
            st = "{0:02b}".format(i)
            keys.append(st)
            
            if st in expectedValues.keys():
                expectedValuesArray.append(expectedValues[st]*shots)
            else:
                expectedValuesArray.append(0)

            if st in simuValues.keys():
                simuValuesArray.append(simuValues[st])
            else:
                simuValuesArray.append(0)

            if st in realValues.keys():
                realValuesArray.append(realValues[st])
            else:
                realValuesArray.append(0)

        _keys = np.arange(len(keys))

        ax = plt.subplot(111)
        b1 = ax.bar(_keys-0.1, expectedValuesArray,width=0.1,color='b',align='center')
        b2 = ax.bar(_keys, realValuesArray,width=0.1,color='g',align='center')
        b3 = ax.bar(_keys+0.1, simuValuesArray,width=0.1,color='y',align='center')

        ax.legend((b1[0], b2[0], b3[0]), ('Expected results', 'Real results', 'Simulated results'))

        ax.set_ylabel('Counts of computer solutions')
        ax.set_xlabel('Qubit values')

        plt.xticks(_keys, keys) # set labels manually

        plt.show()

    except QISKitError as ex:

        print ("EXCEPCION Error = {}".format(ex))



if __name__ == "__main__":

    np.set_printoptions(precision=2, linewidth=200, suppress=True)

    Debug.startDebug(fileOutputLevel=DebugLevel.Nothing, stdOutputLevel=DebugLevel.Nothing, autoDebugLevel=True, autoTime=True)
    
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print("This script execute QCMD to get a determined circuit, execute this circuit in a QISKit simulator and then compares these results with an execution in a real quantum computer IBM-Q of 5 qubits.")
        print(" Every argument is OPTIONAL and they do not need to be sorted. [-m and -r] should not be active together ")
        print("-n <qubits> : number of qubits (over 3 qubits the result are almost random) -> default = 2")
        print("-f <filename> : filename where the qasm will be generated -> default = 'prueba.qasm'")
        print("-s <shots> : number of shots to execute in the computer -> default = 1000")
        print("[-m or -r] <index> -> default = -r 1")
        print("-m <index>: active: generate a matrix of superposition of two states 0 and i")
        print("-r <index>: genererate a row reverse matrix fomr 0 to i")
        print("-v : active to view the matrix generated")
        print("-c : active to write the qasm in a compress way (compress the out file, not the number of gates)")
        quit()

    if not "-f" in sys.argv[1:]:
        filename = "prueba.qasm"
    else:
        filename = sys.argv[sys.argv.index("-f") + 1]

    if not "-n" in sys.argv[1:]:
        nQubits = 2
    else:
        nQubits = int(sys.argv[sys.argv.index("-n") + 1])

    if not "-s" in sys.argv[1:]:
        shots = 1000
    else:
        shots = int(sys.argv[sys.argv.index("-s") + 1])

    if not "-m" in sys.argv[1:]:
        rowReverse = True
        index = 1
    else:
        rowReverse = False
        index = int(sys.argv[sys.argv.index("-m") + 1])

    if "-r" in sys.argv[1:]:
        rowReverse = True
        index = int(sys.argv[sys.argv.index("-r") + 1])

    if "-v" in sys.argv[1:]:
        viewMatrix = True
    else:
        viewMatrix = False

    if "-c" in sys.argv[1:]:
        compress = True
    else:
        compress = False

    probeMatrix(filename, nQubits, rowReverse, index, viewMatrix, compress, shots)

    
    
