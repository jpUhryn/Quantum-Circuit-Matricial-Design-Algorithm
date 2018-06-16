
from src.Debug import Debug
from src.GateDictionary import GateDictionary
from src.Assembler import Assembler

from src.defaultTypes import *

from copy import deepcopy

class WriterAsm():

    def getPath(id, dic):
        Debug.debug("id:" + str(id), DebugLevel.Function)
        
        path = dic.getGate(id).getPath()
        if not path:
            return [id]
        
        res = []
            
        for i in path:
            res += WriterAsm.getPath(i, dic)

        return res


    def writeAsm(id, dic, fileName, reset=True, compress=False):

        Debug.debug("id:" + str(id), DebugLevel.Function)

        path = WriterAsm.getPath(id, dic)

        Debug.debug("path:" + str(path), DebugLevel.Debug)


        if reset:
            file = open(fileName, "w")
        else:
            file = open(fileName, "a")

        if not compress:
            file.write(Assembler.comment("Assembler file: " + fileName + " to id: " + str(id)))
        file.write(Assembler.iniAsm(nQubits=dic.getNQubits()))

        for i in path:
            file.write(dic.getGate(i).getAsm(compress))

        file.write(Assembler.finAsm(nQubits=dic.getNQubits()))

        file.close()

        return len(path)

