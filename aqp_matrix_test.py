
from qiskit.wrapper import load_qasm_file
from qiskit import QISKitError, available_backends, execute

from src.Debug import Debug
from src.QuantumMath import QuantumMath
from src.AQP import AQP
from src.DictionarySearcher import DictionarySearcher
from src.Visualizer import Visualizer
from src.Assembler import Assembler
from src.WriterAsm import WriterAsm

from src.defaultTypes import *

import numpy as np

import sys

import math





def generateGate(index, nQubits, dic):
    Debug.debug(str(index) + " ; " + str(nQubits), DebugLevel.Function)

    array = []
    for i in range(nQubits):
        array.append(i)

    if index == 0:
        return AQP.generateBasic(standarGate=StandarGate.X, targets=array, dic=dic)

    elif index == 1:
        return AQP.generateXnot(source=0, target=nQubits-1, dic=dic)

    elif index == 2:
        return AQP.generateBasicTurn(target=nQubits-1, angle=math.pi/2, turnType=TurnType.X, dic=dic)

    elif index == 3:
        return AQP.generateCondTurn(turnType=TurnType.X, target=nQubits-1, source=nQubits-2, angle=math.pi/2, dic=dic)

    elif index == 4:
        return AQP.generateMultipleTurn(turnType=TurnType.X, target=nQubits-1, sources=array[:-1], angle=math.pi/2, dic=dic)  

    elif index == 5:
        return AQP.generateToffoli(target=nQubits-1, sources=array[:-1], dic=dic)

    elif index == 6:
        return AQP.generateSpecialTurn(a=1j, b=-1, dic=dic)

    elif index == 7:
        return AQP.generateRowReverse(target1=1, target2=2**nQubits-2, dic=dic)

    elif index == 8:
        matrix = QuantumMath.getOracleMatrix(nQubits=nQubits, targets=[0, nQubits, 2**nQubits-1])
        return (AQP.generateSpecial(name="oracle", matrix=matrix, dic=dic), matrix)

    elif index == 9:
        matrix = QuantumMath.getAmplitudAmplifier(nQubits=nQubits)
        return (AQP.generateSpecial(name="aa", matrix=matrix, dic=dic), matrix)


def generateMatrix(filename, nQubits, index, compress):
    Debug.debug(filename + " ; " + str(nQubits) + " ; " + str(index), DebugLevel.Function)

    # inicializa un diccionario para 4 qubits
    dic = DictionarySearcher(nQubits=nQubits)

    # genera una puerta de giro condicionado multiple y las subpuertas necesarias
    #id = AQP.generateMultipleTurn(sources=[0,1,2], target=3, angle=math.pi, turnType=TurnType.Z, dic=dic)
    gate = generateGate(index, nQubits, dic)

    if isinstance(gate, tuple):
        matrix = gate[1]
        gateId = gate[0]
    else:
        gateId = gate

    # genera el fichero .qasm para crear esta puerta
    numberGates = WriterAsm.writeAsm(gateId, dic, filename, reset=True, compress=compress)

    print(Colors.BOLD.value + "\nAssembler written with " + str(numberGates) + " gates\n" + Colors.ENDC.value)

    if gate is tuple:
        return matrix
    else:
        return dic.getGate(gateId).getMatrix()

    return dic.getGate(gateId).getMatrix()


def areEqual(matrix1, matrix2):
    return np.array_equal(matrix1, matrix2)

def areClose(matrix1, matrix2):
    return np.allclose(matrix1, matrix2)

def probeMatrix(filename, nQubits, index, viewMatrix, compress):
    #Debug.debug(filename + " ; " + str(nQubits) + " ; " + str(index) + " ; " + str(viewMatrix), DebugLevel.Function)

    matrix1 = generateMatrix(filename, nQubits, index, compress)

    try:
        qc = load_qasm_file(filename)

        job_sim = execute(qc, "local_unitary_simulator")
        sim_result = job_sim.result()
        matrix2 = sim_result.get_unitary(qc)
        
        if (viewMatrix):
            print(Colors.ORANGE.value + "\nGenerated matrix\n" + str(matrix1) + "\n" + Colors.ENDC.value)
            print(Colors.PURPLE.value + "\nSimulated matrix\n" + str(matrix2) + "\n" + Colors.ENDC.value)

        if areEqual(matrix1, matrix2):
            print(Colors.GREEN.value + "\n EQUAL \n\n" + Colors.ENDC.value)
            res = 0
        elif areClose(matrix1, matrix2):
            print(Colors.BLUE.value + "\n CLOSE \n\n" + Colors.ENDC.value)
            res = 1
        else:
            print(Colors.RED.value + "\n ERROR \n\n" + Colors.ENDC.value)
            res = 2

    except QISKitError as ex:

        print ("EXCEPCION Error = {}".format(ex))


def probeAll(filename, nQubits, index, viewMatrix, compress):
    Debug.debug(filename + " ; " + str(nQubits) + " ; " + str(index) + " ; " + str(viewMatrix), DebugLevel.Function)

    array = [0,0,0]

    for i in range(index+1):
        print(Colors.BOLD.value + "\n\n******************************************\n TEST " + str(i) + "\n" + Colors.ENDC.value)
        array[probeMatrix(filename, nQubits, i, viewMatrix, compress)] += 1
        print(Colors.BOLD.value + "\n\n******************************************\n END TEST " + str(i) + "\n\n" + Colors.ENDC.value)

    print(Colors.BOLD.value + "\n\n******************************************\n ALL TEST UNDER " + str(index) + "\n" + Colors.ENDC.value)
    print(Colors.GREEN.value + " EQUAL:" + str(array[0]) + "\n" + Colors.ENDC.value)
    print(Colors.BLUE.value + " CLOSE:" + str(array[1]) + "\n" + Colors.ENDC.value)
    print(Colors.RED.value + " ERROR:" + str(array[2]) + "\n" + Colors.ENDC.value)
    print(Colors.BOLD.value + "******************************************\n END ALL TEST\n\n" + Colors.ENDC.value)

if __name__ == "__main__":

    np.set_printoptions(precision=2, linewidth=200, suppress=True)

    Debug.startDebug(fileOutputLevel=DebugLevel.Nothing, stdOutputLevel=DebugLevel.Nothing, autoDebugLevel=True, autoTime=True)
    
    if "-h" in sys.argv[1:] or "--help" in sys.argv[1:]:
        print("This script test every kind of gate generated with QCMD in a theorical way with the IBM-Q simulator.")
        print(" The test use the numy functino 'allclose' to avoid the float precision error")
        print(" Every argument is OPTIONAL and they do not need to be sorted")
        print("-f <filename> : filename where the qasm will be generated -> default = 'prueba.qasm'")
        print("-n <qubits> : number of qubits -> default = 2")
        print("-i <index> : index of the probe to generate (maximum 9) -> default = 0")
        print("-v : active to view the matrix solutions")
        print("-c : active to write the qasm in a compress way (compress the out file, not the number of gates)")
        print("-a : active to probe all the probes under this index (included)")
        print()
        print("The gates to test are:")
        print(" 0 -> X gate for every qubit")
        print(" 1 -> XNOT from first qubit to last one")
        print(" 2 -> Y turn of angle pi/2")
        print(" 3 -> conditional turn Y from penultimate to last qubit of angle pi/2")
        print(" 4 -> conditional multiple turn Y from all qubits to last of angle pi/2")
        print(" 5 -> Toffoli gate from all qubits to last")
        print(" 6 -> special turn with arguments a=i and b=-1")
        print(" 7 -> Reverse gate from second row to penultimate row")
        print(" 8 -> Generate the oracle matrix for qubits 0, n and (2**n)-1")
        print(" 9 -> Generate AmplitudAmplifier matrix")
        quit()

    if not "-f" in sys.argv[1:]:
        filename = "prueba.qasm"
    else:
        filename = sys.argv[sys.argv.index("-f") + 1]

    if not "-n" in sys.argv[1:]:
        nQubits = 2
    else:
        nQubits = int(sys.argv[sys.argv.index("-n") + 1])

    if not "-i" in sys.argv[1:]:
        index = 0
    else:
        index = int(sys.argv[sys.argv.index("-i") + 1])

    if "-v" in sys.argv[1:]:
        viewMatrix = True
    else:
        viewMatrix = False

    if "-c" in sys.argv[1:]:
        compress = True
    else:
        compress = False

    if "-a" in sys.argv[1:]:
        probeAll(filename, nQubits, index, viewMatrix, compress)
    else:
        probeMatrix(filename, nQubits, index, viewMatrix, compress)

    
    
