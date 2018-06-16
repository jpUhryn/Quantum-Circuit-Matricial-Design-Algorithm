
from src.QuantumMath import QuantumMath
from src.Debug import Debug
from src.Assembler import Assembler


from src.defaultTypes import *

class Gate():

    def __init__(self, id, matrix, nQubits):
        self.id = id
        self.matrix = matrix
        self.nQubits = nQubits
        

    def getMatrix(self):
        return self.matrix
        
    def getNQubits(self):
        return self.nQubits 

    def getPath(self):
        pass

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def __str__(self):
        return "<" + str(type(self)) + " id:" + str(self.id) + " path:" + str(self.getPath()) + ">"
        
    #all strings same length
    def getStringPerQubit(self):
        l = []
        for i in range(self.nQubits):
            l.append("[?]")
        return l
        
    #tuple (maxString, [(type, string),...])
    #all strings same length (only if type is QubitStringType.Target)
    def getStringTypedPerQubit(self):
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Target, "?"))
        return (1,l)
        
    

class Standar(Gate):

    def __init__(self, id, matrix, nQubits):
        Gate.__init__(self, id=id, matrix=matrix, nQubits=nQubits)
    
    def getPath(self):
        return []

    def getAsm(self, compress=False):
        return ""

        
#final class
class Basic(Standar):

    def __init__(self, id, matrix, nQubits, standarGate, targets):
        Standar.__init__(self, id=id, matrix=matrix, nQubits=nQubits)
        self.standarGate = standarGate
        self.targetsCode = QuantumMath.codingQubits(targets)
        
    def getStringTypedPerQubit(self):
        l = []
        targets = QuantumMath.decodingQubits(self.targetsCode)
        for i in range(self.nQubits):
            if i in targets:
                l.append((QubitStringType.Target, self.standarGate.name))
            else:
                l.append((QubitStringType.Empty, ""))
        return (len(self.standarGate.name),l)


    def getAsm(self, compress=False):
        stCom = Assembler.comment("Std Gate - " + self.standarGate.name + " targets: " + str(self.targetsCode))
        st = ""
        for i in QuantumMath.decodingQubits(self.targetsCode):
            st += Assembler.writeStdGate(standarGate=self.standarGate, target=i, nQubits=self.nQubits)

        if compress:
            return st
        else:
            return stCom + st + stCom + "\n"
        

#final class
class BasicTurn(Standar):

    def __init__(self, id, matrix, nQubits, target, angle, turnType):
        Standar.__init__(self, id=id, matrix=matrix, nQubits=nQubits)
        self.target = target
        self.angle = angle
        self.turnType = turnType
        
    def getStringTypedPerQubit(self):
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Empty, ""))
        st = printTurn(self.turnType, self.angle)
        l[self.target] = (QubitStringType.Target, st)
        return (len(st),l)


    def getAsm(self, compress=False):
        stCom = Assembler.comment("Basic Turn - " + self.turnType.name + " target: " + str(self.target) + " angle: " + str(self.angle))
        if compress:
            return Assembler.writeTurn(turnType=self.turnType, target=self.target, angle=self.angle, nQubits=self.nQubits)
        else:
            return stCom + Assembler.writeTurn(turnType=self.turnType, target=self.target, angle=self.angle, nQubits=self.nQubits) + stCom + "\n"
        

#final class
class Xnot(Standar):

    def __init__(self, id, matrix, nQubits, target, source):
        Standar.__init__(self, id=id, matrix=matrix, nQubits=nQubits)
        self.target = target
        self.source = source
    
    def getStringTypedPerQubit(self):
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Empty, ""))
        l[self.target] = (QubitStringType.Target, "(X)")
        l[self.source] = (QubitStringType.Source, "")

        return (int(3),l)

    def getAsm(self, compress=False):
        stCom = Assembler.comment("X-NOT - source: " + str(self.source) + " target: " + str(self.target))
        if compress:
            return Assembler.writeXnot(source=self.source, target=self.target, nQubits=self.nQubits)
        else:
            return stCom + Assembler.writeXnot(source=self.source, target=self.target, nQubits=self.nQubits) + stCom + "\n"


class Builded(Gate):

    def __init__(self, id, matrix, nQubits, path):
        Gate.__init__(self, id=id, matrix=matrix, nQubits=nQubits)
        self.path = path
        
    def getPath(self):
        return self.path

#final class
class Special(Builded):

    def __init__(self, id, matrix, nQubits ,path, name):
        Builded.__init__(self, id=id, matrix=matrix, nQubits=nQubits, path=path)
        self.name = name
    
    def getStringTypedPerQubit(self):
        st = ""
        for i in range(len(self.name)+2):
            st += "*"
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Target, st))
        l[self.nQubits//2] = (QubitStringType.Target, "*" + self.name + "*")
        return (len(self.name),l)

class Conditional(Builded):

    def __init__(self, id, matrix, nQubits, path, target):
        Builded.__init__(self, id=id, matrix=matrix, path=path, nQubits=nQubits)
        self.target = target


class Individual(Conditional):

    def __init__(self, id, matrix, nQubits, path, target, source):
        Conditional.__init__(self, id=id, path=path, target=target, nQubits=nQubits, matrix=matrix)
        self.source = source



#final class
class CondTurn(Individual):

    def __init__(self, id, matrix, nQubits, path, target, source, angle, turnType):
        Individual.__init__(self, id=id, matrix=matrix, path=path, target=target, source=source, nQubits=nQubits)
        self.angle = angle
        self.turnType = turnType
        
    def getStringTypedPerQubit(self):
        l = []
        st = printTurn(self.turnType, self.angle)
        for i in range(self.nQubits):
            l.append((QubitStringType.Empty, ""))
        l[self.source] = (QubitStringType.Source, "")
        l[self.target] = (QubitStringType.Target, st)
        return (len(st),l)


class Multiple(Conditional):

    def __init__(self, id, matrix, nQubits, path, target, sources):
        Conditional.__init__(self, id=id, matrix=matrix, path=path, target=target, nQubits=nQubits)
        self.sourcesCode = QuantumMath.codingQubits(sources)

#final class
class MultipleTurn(Multiple):

    def __init__(self, id, matrix, nQubits, path, target, sources, angle, turnType):
        Multiple.__init__(self, id=id, matrix=matrix, path=path, target=target, sources=sources, nQubits=nQubits)
        self.angle = angle
        self.turnType = turnType
        
    def getStringTypedPerQubit(self):
        l = []
        st = printTurn(self.turnType, self.angle)
        sources = QuantumMath.decodingQubits(self.sourcesCode)
        for i in range(self.nQubits):
            if i in sources:
                l.append((QubitStringType.Source, ""))
            else:
                l.append((QubitStringType.Empty, ""))
        l[self.target] = (QubitStringType.Target, st)
        return (len(st),l)


#final class
class Toffoli(Multiple):

    def __init__(self, id, matrix, nQubits, path, target, sources):
        Multiple.__init__(self, id=id, matrix=matrix, path=path, target=target, sources=sources, nQubits=nQubits)
        
    def getStringTypedPerQubit(self):
        l = []
        sources = QuantumMath.decodingQubits(self.sourcesCode)
        for i in range(self.nQubits):
            if i in sources:
                l.append((QubitStringType.Source, ""))
            else:
                l.append((QubitStringType.Empty, ""))
        l[self.target] = (QubitStringType.Target, "(X)")
        return (3,l)


#final class
class SpecialTurn(Builded):

    def __init__(self, id, matrix, nQubits, path, a, b):
        Builded.__init__(self, id=id, matrix=matrix, nQubits=nQubits, path=path)
        self.a = a
        self.b = b
        
    def getStringTypedPerQubit(self):
        stMain = ".ST:" + str(self.a) + "-" + str(self.b) + "."
        st = ""
        for i in range(len(stMain)):
            st += "."
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Target, st))
        l[self.nQubits//2] = (QubitStringType.Target, stMain)
        return (len(stMain),l)


#final class
class RowReverse(Builded):

    def __init__(self, id, matrix, nQubits, path, target1, target2):
        Builded.__init__(self, id=id, matrix=matrix, nQubits=nQubits, path=path)
        self.target1 = min(target1, target2)
        self.target2 = max(target1, target2)
        
    def getStringTypedPerQubit(self):
        stMain = "+RR:" + str(self.target1) + "-" + str(self.target2) + "+"
        st = ""
        for i in range(len(stMain)):
            st += "+"
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Target, st))
        l[self.nQubits//2] = (QubitStringType.Target, stMain)
        return (len(stMain),l)

def printTurn(turnType, angle, decimals=2):
        return turnType.name + str(QuantumMath.round(angle, decimals))



#final class
class Oracle(Special):

    def __init__(self, id, matrix, nQubits ,path, targets):
        Special.__init__(self, id=id, matrix=matrix, nQubits=nQubits, path=path, name="Oracle" + str(nQubits) + "_" + str(QuantumMath.codingQubits(targets)))
        self.targets = QuantumMath.codingQubits(targets)
    
    def getStringTypedPerQubit(self):
        st = ""
        for i in range(len(self.name)+2):
            st += "/"
        l = []
        for i in range(self.nQubits):
            l.append((QubitStringType.Target, st))
        l[self.nQubits//2] = (QubitStringType.Target, "/" + self.name + "/")
        return (len(self.name),l)