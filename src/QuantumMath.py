
from src.defaultTypes import *

from src.Debug import Debug

import numpy as np
import math
import cmath


class QuantumMath():

    # number of qubits depending on matrix size
    def qubitsNumberMatrix(matrix):
        return int(math.log2(np.shape(matrix)[0]))

    # size of matrix depending of number of qubits
    def matrixSize(nQubits):
        return int(math.pow(2,nQubits))

    # round the number to "decimals" number of fraction decimals
    def round(npObject, decimals=None):
        Debug.debug(str(npObject) + " ; " + str(decimals), DebugLevel.Function)
        
        if decimals is not None:
            return np.round(npObject, decimals=decimals)
        else:
            return npObject

    # get the conjugate of a complex number
    def conjugate(n):
        return np.conjugate(n)

    # normalize the size of a vector (convert module to 1)
    def normalizeVector(array):
        return array/np.linalg.norm(array)

    def vectorModule(array):
        return np.linalg.norm(array)

    def complexModule(n):
        return np.absolute(n)
        
    def inverseAngle(angle):
        #return 2*math.pi-angle
        return -angle

    def codingQubits(qubits):
        Debug.debug(qubits, DebugLevel.Function)

        code = 0
        for i in qubits:
            code += 2**i

        return code


    def decodingQubits(code):
        Debug.debug(code, DebugLevel.Function)

        ind = 0
        qubits = []

        while code > 0:

            if code % 2 == 1:
                qubits.append(ind)

            code //= 2
            ind += 1

        return qubits

    def getStdMatrix(name):
        return QuantumOriginalGates[name]

    def getStdTurnMatrix(turnType, angle):
        if turnType is TurnType.Z:
            return (np.matrix([[1, 0],[0, cmath.rect(1, angle)]], dtype=complex))
        elif turnType is TurnType.X:
            return (np.matrix([[math.cos(angle/2), -math.sin(angle/2)],[math.sin(angle/2), math.cos(angle/2)]], dtype=complex))


    def tensorDot(matrixArray):
        Debug.debug(matrixArray, DebugLevel.Function)
        m = matrixArray[0]
        for i in matrixArray[1:]:
            m = np.kron(m, i)
        return m

    def matrixDot(matrixArray):
        Debug.debug(matrixArray, DebugLevel.Function)
        m = matrixArray[0]
        for i in matrixArray[1:]:
            m = np.dot(m, i)
        return m


    def generateMatrixFromBasicEquations(qubitsNumber, solutionArray):
        size = 2**qubitsNumber
        matrix = np.zeros((size, size), dtype=complex)
        for column, s in enumerate(solutionArray):
            for row, v in enumerate(s):
                matrix[row,column] = v
        return np.matrix(matrix, dtype=complex)

    def toBinary(number, digits):
        Debug.debug("number:" + str(number) + " digits:" + str(digits), DebugLevel.Function)

        binary = []
        for i in range(digits):
            if number % 2 == 0:
                binary.append(0)
            else:
                binary.append(1)
            number //= 2

        binary.reverse()
        return binary

    def getPhase(complex):
        return cmath.phase(complex)

    def matrixDeterminant(matrix):
        return np.linalg.det(matrix)


    def getOracleMatrix(nQubits, targets):
        Debug.debug("nQubits:" + str(nQubits) + " targets:" + str(targets), DebugLevel.Function)
        
        matrix = np.eye(2**nQubits, dtype=complex)
        for i in targets:
            matrix[i][i] = -1
        return matrix


    def getAmplitudAmplifier(nQubits):

        leng = 2**nQubits
        val = 1/(leng/2)
        matrix = np.zeros((leng,leng), dtype=complex)
        for i in range(leng):
            for j in range(leng):
                matrix[i][j] = val

        for i in range(leng):
            matrix[i][i] -= 1

        return matrix
