
from src.GateDictionary import GateDictionary
from src.QuantumMath import QuantumMath

from src.defaultTypes import *


class DictionarySearcher(GateDictionary):


    def getIdBasic(self, standarGate, targets):
        
        return self.getId(GateType.Basic, [standarGate, QuantumMath.codingQubits(targets)])


    def getIdBasicTurn(self, turnType, target, angle):
        
        return self.getId(GateType.BasicTurn, [turnType, target, angle])


    def getIdXnot(self, source, target):
        
        return self.getId(GateType.Xnot, [source, target])


    def getIdSpecial(self, name):

        return self.getId(GateType.Special, [name])


    def getIdRowReverse(self, target1, target2):
        
        return self.getId(GateType.RowReverse, [target1, target2])
        

    def getIdCondTurn(self, turnType, target, source, angle):
    
        return self.getId(GateType.CondTurn, [turnType, target, source, angle])


    def getIdToffoli(self, target, sources):
        
        return self.getId(GateType.Toffoli, [target, QuantumMath.codingQubits(sources)])


    def getIdMultipleTurn(self, turnType, target, sources, angle):
        
        return self.getId(GateType.MultipleTurn, [turnType, target, QuantumMath.codingQubits(sources), angle])


    def getIdSpecialTurn(self, a, b):
        
        return self.getId(GateType.SpecialTurn, [a, b])


    def getIdOracle(self, targets):
        
        return self.getId(GateType.Oracle, QuantumMath.codingQubits(targets))


    def getIdAmplitudAmplifier(self):
        
        return self.getId(GateType.AmplitudAmplifier)    

###################################################################################################################
###################################################################################################################


    def addIdBasic(self, gate, standarGate, targets):
        
        return self.addGate(gate, GateType.Basic, [standarGate, QuantumMath.codingQubits(targets)])


    def addIdBasicTurn(self, gate, turnType, target, angle):
        
        return self.addGate(gate, GateType.BasicTurn, [turnType, target, angle])


    def addIdXnot(self, gate, source, target):
        
        return self.addGate(gate, GateType.Xnot, [source, target])


    def addIdSpecial(self, gate, name):

        return self.addGate(gate, GateType.Special, [name])


    def addIdRowReverse(self, gate, target1, target2):
        
        return self.addGate(gate, GateType.RowReverse, [target1, target2])
        

    def addIdCondTurn(self, gate, turnType, target, source, angle):
    
        return self.addGate(gate, GateType.CondTurn, [turnType, target, source, angle])


    def addIdToffoli(self, gate, target, sources):
        
        return self.addGate(gate, GateType.Toffoli, [target, QuantumMath.codingQubits(sources)])


    def addIdMultipleTurn(self, gate, turnType, target, sources, angle):
        
        return self.addGate(gate, GateType.MultipleTurn, [turnType, target, QuantumMath.codingQubits(sources), angle])


    def addIdSpecialTurn(self, gate, a, b):
        
        return self.addGate(gate, GateType.SpecialTurn, [a, b])


    def addIdOracle(self, gate, targets):
        
        return self.addGate(gate, GateType.Oracle, QuantumMath.codingQubits(targets))


    def addIdAmplitudAmplifier(self, gate):
        
        return self.addGate(gate, GateType.AmplitudAmplifier)    