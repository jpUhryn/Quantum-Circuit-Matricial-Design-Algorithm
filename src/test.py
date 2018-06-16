
from Debug import Debug
from QuantumMath import QuantumMath
from AQP import AQP
from DictionarySearcher import DictionarySearcher
from Visualizer import Visualizer
from Assembler import Assembler
from WriterAsm import WriterAsm


from defaultTypes import *

import numpy as np

import math

def basicGateTest():

    dic = DictionarySearcher(2)
    
    id = AQP.generateBasic(standarGate=StandarGate.X, targets=[0], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateBasic(standarGate=StandarGate.X, targets=[0, 1], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    
    id = AQP.generateBasic(standarGate=StandarGate.H, targets=[0, 1], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)




    dic = DictionarySearcher(4)
    
    id = AQP.generateBasic(standarGate=StandarGate.X, targets=[1, 2, 3], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateBasic(standarGate=StandarGate.H, targets=[2], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    
def basicTurnGateTest():



    dic = DictionarySearcher(2)
    
    id = AQP.generateBasicTurn(target=1, angle=math.pi, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateBasicTurn(target=0, angle=math.pi/2, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateBasicTurn(target=1, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    


    dic = DictionarySearcher(4)
    
    id = AQP.generateBasicTurn(target=3, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateBasicTurn(target=1, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 
    

def xnotGateTest():

    dic = DictionarySearcher(2)
    
    id = AQP.generateXnot(target=1, source=0, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateXnot(target=0, source=1, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)



    dic = DictionarySearcher(3)
    
    id = AQP.generateXnot(target=1, source=0, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateXnot(target=0, source=1, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateXnot(target=2, source=1, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    


    dic = DictionarySearcher(4)
    
    id = AQP.generateXnot(target=3, source=0, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateXnot(target=2, source=1, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateXnot(target=1, source=2, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)


    
def toffoliGateTest():

    dic = DictionarySearcher(3)
    
    id = AQP.generateToffoli(target=2, sources=[0,1], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateToffoli(target=1, sources=[0,2], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)



    dic = DictionarySearcher(4)
    
    id = AQP.generateToffoli(target=3, sources=[0,1,2], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=2, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateToffoli(target=3, sources=[0,2], dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    

def condTurnGateTest():

    dic = DictionarySearcher(2)
    
    id = AQP.generateCondTurn(source=0, target=1, angle=math.pi, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=False, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateCondTurn(source=0, target=1, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateCondTurn(source=1, target=0, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    
    Debug.debug("\n" + str(dic) + "\n\n", DebugLevel.Result)


    dic = DictionarySearcher(3)
    
    id = AQP.generateCondTurn(source=0, target=2, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateCondTurn(source=0, target=1, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateCondTurn(source=1, target=2, angle=math.pi/4, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateCondTurn(source=2, target=1, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=False, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



def multipleTurnGateTest():

    dic = DictionarySearcher(2)
    
    id = AQP.generateMultipleTurn(sources=[0], target=1, angle=math.pi, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=False, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



    dic = DictionarySearcher(3)

    id = AQP.generateMultipleTurn(sources=[0,1], target=2, angle=math.pi, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateMultipleTurn(sources=[0,1], target=2, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateMultipleTurn(sources=[0,2], target=1, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=False, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    
    Debug.debug("\n" + str(dic) + "\n\n", DebugLevel.Result)


    dic = DictionarySearcher(4)

    id = AQP.generateMultipleTurn(sources=[0,1,2], target=3, angle=math.pi/2, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)
    

    id = AQP.generateMultipleTurn(sources=[0,1,2], target=3, angle=math.pi, turnType=TurnType.Z, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateMultipleTurn(sources=[2], target=0, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)


def rowReverseGateTest():
    
    dic = DictionarySearcher(2)

    id = AQP.generateRowReverse(target1=0, target2=3, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateRowReverse(target1=2, target2=1, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateRowReverse(target1=1, target2=2, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)


    dic = DictionarySearcher(3)

    id = AQP.generateRowReverse(target1=0, target2=3, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateRowReverse(target1=1, target2=7, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    id = AQP.generateRowReverse(target1=4, target2=2, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + Visualizer.printIntegerMatrix(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)



def specialTurnGateTest():

    dic = DictionarySearcher(2)

    id = AQP.generateSpecialTurn(a=-1, b=0, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 
    
    id = AQP.generateSpecialTurn(a=(1/(math.sqrt(2))), b=(1/(math.sqrt(2))), dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



    dic = DictionarySearcher(3)

    id = AQP.generateSpecialTurn(a=1j, b=0, dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



    dic = DictionarySearcher(4)

    id = AQP.generateSpecialTurn(a=(1/(math.sqrt(2))), b=(1j*(1/(math.sqrt(2)))), dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 


    
def codingDecodingTest():
    
    aux = QuantumMath.codingQubits([0,1,2])
    Debug.debug(aux, DebugLevel.Result)
    Debug.debug(QuantumMath.decodingQubits(aux), DebugLevel.Result)
    
    aux = QuantumMath.codingQubits([1,4])
    Debug.debug(aux, DebugLevel.Result)
    Debug.debug(QuantumMath.decodingQubits(aux), DebugLevel.Result)

    aux = QuantumMath.codingQubits([6])
    Debug.debug(aux, DebugLevel.Result)
    Debug.debug(QuantumMath.decodingQubits(aux), DebugLevel.Result)
    
    
def toBinaryTest():

    Debug.debug(QuantumMath.toBinary(5,3), DebugLevel.Result)
    Debug.debug(QuantumMath.toBinary(5,5), DebugLevel.Result)
    Debug.debug(QuantumMath.toBinary(16,6), DebugLevel.Result)
    Debug.debug(QuantumMath.toBinary(31,6), DebugLevel.Result)



def specialTest():

    dic = DictionarySearcher(2)

    matrix = np.matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, -1]])
    id = AQP.generateSpecial(matrix=matrix, name="prueba1", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 


    matrix = np.matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1j]])
    id = AQP.generateSpecial(matrix=matrix, name="prueba2", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 


    matrix = np.matrix([[-1, 0, 0, 0],[0, 1, 0, 0],[0, 0, (1/math.sqrt(2))*(1+1j), 0],[0, 0, 0, 1j]])
    id = AQP.generateSpecial(matrix=matrix, name="prueba3", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 


    matrix = np.matrix([[1j, 0, 0, 0],[0, (1/math.sqrt(2)), (-1/math.sqrt(2)), 0],[0, (1/math.sqrt(2)), (1/math.sqrt(2)), 0],[0, 0, 0, -1]])
    id = AQP.generateSpecial(matrix=matrix, name="prueba4", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 

    """
    Debug.debug("\n" + str(dic.getGate(67).getMatrix()) + "\n\n", DebugLevel.Result) 
    Debug.debug("\n" + str(dic.getGate(68).getMatrix()) + "\n\n", DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(78).getMatrix()) + "\n\n", DebugLevel.Result) 
    Debug.debug("\n" + str(dic.getGate(68).getMatrix()) + "\n\n", DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(67).getMatrix()) + "\n\n", DebugLevel.Result) 
    Debug.debug("\n" + str(AQP.generateMatrixFromPath([68,67,78,67,68], dic)) + "\n\n", DebugLevel.Result)
    """

    matrix = np.matrix([[-1, 1, 1, 1],[1, -1, 1, 1],[1, 1, -1, 1],[1, 1, 1, -1]])*(1/2)
    id = AQP.generateSpecial(matrix=matrix, name="prueba5", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



    dic = DictionarySearcher(3)


    matrix = np.eye(2**3, dtype=complex)
    matrix[7,7] = -1
    id = AQP.generateSpecial(matrix=matrix, name="prueba6", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

    matrix[5,6] = 1
    matrix[6,5] = 1
    matrix[5,5] = 0
    matrix[6,6] = 0 
    id = AQP.generateSpecial(matrix=matrix, name="prueba67", dic=dic)
    Debug.debug(Visualizer.printPath(id, dic, deepEnd=False), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)



def groverMatricesTest():

    Debug.debug(QuantumMath.getOracleMatrix(2,[3]), DebugLevel.Result)
    Debug.debug(QuantumMath.getOracleMatrix(3,[3,4,5]), DebugLevel.Result)

    matrix = QuantumMath.getAmplitudAmplifier(2)
    Debug.debug(matrix, DebugLevel.Result)
    Debug.debug(QuantumMath.matrixDeterminant(matrix), DebugLevel.Info)
    
    matrix = QuantumMath.getAmplitudAmplifier(3)
    Debug.debug(matrix, DebugLevel.Result)
    Debug.debug(QuantumMath.matrixDeterminant(matrix), DebugLevel.Info)

    matrix = QuantumMath.getAmplitudAmplifier(4)
    Debug.debug(matrix, DebugLevel.Result)
    Debug.debug(QuantumMath.matrixDeterminant(matrix), DebugLevel.Info)



def q3Test():

    dic = DictionarySearcher(3)

    matrix = np.eye(2**3, dtype=complex)
    """
    matrix[0,0] = 0
    matrix[1,0] = -1
    matrix[0,1] = 1j
    matrix[1,1] = 0

    matrix[2,2] = (1/math.sqrt(2))
    matrix[3,2] = (1/math.sqrt(2))
    matrix[2,3] = (1/math.sqrt(2))
    matrix[3,3] = (-1/math.sqrt(2))
    """

    for i in range(4,8):
        for j in range(4,8):
            matrix[i,j] = 0.5

    for i in range(4,8):
        matrix[i,i] -= 1

    Debug.debug("\n" + str(matrix) + "\n\n", DebugLevel.Debug)
    id = AQP.generateSpecial(matrix=matrix, name="semiAA2", dic=dic)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)



def grover3AATest():

    dic = DictionarySearcher(3)
    matrix = QuantumMath.getAmplitudAmplifier(3)
    id = AQP.generateSpecial(matrix=matrix, name="grover3AA", dic=dic)

    Debug.debug("\n" + str(matrix) + "\n\n", DebugLevel.Debug)
    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)

def grover2AATest():

    dic = DictionarySearcher(2)
    matrix = QuantumMath.getAmplitudAmplifier(2)
    id = AQP.generateSpecial(matrix=matrix, name="grover2AA", dic=dic)

    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result)   


def grover4AATest():

    dic = DictionarySearcher(4)
    matrix = QuantumMath.getAmplitudAmplifier(4)
    id = AQP.generateSpecial(matrix=matrix, name="grover4AA", dic=dic)

    Debug.debug(Visualizer.printCompress(id, dic), DebugLevel.Result)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 


def assemblerGetPathTest():

    dic = DictionarySearcher(2)
    matrix = QuantumMath.getOracleMatrix(2, [0])
    id = AQP.generateSpecial(matrix=matrix, name="asmPath1", dic=dic)

    Debug.debug(Visualizer.printCompress(id, dic, ), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=2, autoReference=True), DebugLevel.Debug)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 

    Debug.debug(WriterAsm.getPath(id, dic), DebugLevel.Result) 


    dic = DictionarySearcher(2)
    matrix = QuantumMath.getAmplitudAmplifier(2)
    id = AQP.generateSpecial(matrix=matrix, name="asmPath2", dic=dic)

    Debug.debug(Visualizer.printCompress(id, dic, ), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=2, autoReference=True), DebugLevel.Debug)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 

    Debug.debug(WriterAsm.getPath(id, dic), DebugLevel.Result) 



def assemblerBasicAsmTest():

    file = open("testAsm.asm", "w")
    file.close()

    dic = DictionarySearcher(2)    

    id = AQP.generateBasic(standarGate=StandarGate.X, targets=[0, 1], dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)

    id = AQP.generateXnot(source=0, target=1, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)

    id = AQP.generateBasicTurn(target=1, angle=math.pi, turnType=TurnType.Z, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)

    id = AQP.generateBasicTurn(target=0, angle=math.pi/2, turnType=TurnType.X, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)


    dic = DictionarySearcher(4)

    id = AQP.generateBasic(standarGate=StandarGate.X, targets=[1, 2, 3], dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)
    
    id = AQP.generateXnot(source=2, target=1, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)

    id = AQP.generateBasicTurn(target=2, angle=math.pi/2, turnType=TurnType.Z, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)

    id = AQP.generateBasicTurn(target=0, angle=math.pi/4, turnType=TurnType.X, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm.asm", reset=False)


def assemblerTest():

    file = open("testAsm1.qasm", "w")
    file.close()
    file = open("testAsm2.qasm", "w")
    file.close()

    dic = DictionarySearcher(2)    

    id = AQP.generateCondTurn(turnType=TurnType.Z, target=0, source=1, angle=math.pi/2, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm1.qasm", reset=False)


    dic = DictionarySearcher(4)

    id = AQP.generateRowReverse(target1=0, target2=2, dic=dic)
    WriterAsm.writeAsm(id, dic, "testAsm2.qasm", reset=False)



def memoryTest():

    # inicializa un diccionario para 4 qubits
    dic = DictionarySearcher(nQubits=4)

    # genera una puerta de giro condicionado multiple y las subpuertas necesarias
    gateId = AQP.generateMultipleTurn(sources=[0,1,2], target=3, angle=math.pi/2, turnType=TurnType.Z, dic=dic)

    # imprime por pantalla el path
    print(Visualizer.printCompress(gateId, dic, deepEnd=True, deep=1, autoReference=False))

    # genera el fichero .qasm para crear esta puerta
    WriterAsm.writeAsm(gateId, dic, "multiConditionalGate.qasm", reset=True)

    Debug.debug(Visualizer.printCompress(id, dic, ), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=1, autoReference=True), DebugLevel.Result)
    Debug.debug(Visualizer.printCompress(id, dic, deepEnd=True, deep=2, autoReference=True), DebugLevel.Debug)
    Debug.debug("\n" + str(dic.getGate(id).getMatrix()) + "\n\n", DebugLevel.Result) 



if __name__ == "__main__":

    np.set_printoptions(precision=2, linewidth=200, suppress=True)

    outClasses = ["QuantumMath", "Visualizer"]
    outFunctions = ["getGate", "getId", "getPath"]
    Debug.startDebug(fileOutputLevel=DebugLevel.Nothing, stdOutputLevel=DebugLevel.All, autoDebugLevel=True, autoTime=True, outClasses=outClasses, outFunctions=outFunctions)
    
    #groverMatricesTest()
    #toBinaryTest()
    #codingDecodingTest()
    #basicGateTest()
    #basicTurnGateTest()
    #xnotGateTest()
    #toffoliGateTest()
    #condTurnGateTest()
    #multipleTurnGateTest()
    #rowReverseGateTest()
    #specialTurnGateTest()

    #specialTest()

    #grover2AATest()

    #grover3AATest()

    #grover4AATest()

    #assemblerGetPathTest()

    #assemblerBasicAsmTest()
    
    #assemblerTest()

    #memoryTest()

    ownTest()