
from src.Debug import Debug
from src.GateDictionary import GateDictionary

from src.defaultTypes import *

from copy import deepcopy


class Assembler():

    def iniAsm(nQubits):
        return '\nOPENQASM 2.0;\ninclude "qelib1.inc";\nqreg q[' + str(nQubits) + "];\ncreg c[" + str(nQubits) + "];\n\n"

    def finAsm(nQubits):
        return "\nmeasure q -> c;\n\n"    

    def comment(text, comment="//"):
        return comment + " " + str(text) + " " + comment + "\n"

    def writeStdGate(standarGate, target, nQubits):
        if standarGate == StandarGate.X:
            return "x q[" + str(nQubits-target-1) + "];\n"
        elif standarGate == StandarGate.I:
            return Assembler.comment(" Identity gate\n")
        return "ERROR BASIC GATE\n"

    def writeTurn(turnType, target, angle, nQubits):
        if turnType == TurnType.Z:
            return "u1(" + str(angle) + ") q[" + str(nQubits-target-1) + "];\n"
        elif turnType == TurnType.X:
            return "u3(" + str(angle) + ",0,0) q[" + str(nQubits-target-1) + "];\n"
        return "ERROR TURN\n"

    def writeXnot(source, target, nQubits):
        return "cx q[" + str(nQubits-source-1) + "], q[" + str(nQubits-target-1) + "];\n"


