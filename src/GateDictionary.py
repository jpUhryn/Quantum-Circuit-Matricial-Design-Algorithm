
from src.Debug import Debug
from src.defaultTypes import *

class GateDictionary():

    #genera la instancia
    def __init__(self, nQubits):
        self.nQubits = nQubits
        self.idActual = FIRST_ID
        self.stDic = {}
        self.idDic = {}

    def __str__(self):
        return "stDic:" + GateDictionary.printCascadeDictionary(self.stDic) + "\n" + "idDic:" + GateDictionary.printCascadeDictionary(self.idDic)


    def getNQubits(self):
        return self.nQubits

    def getGate(self, id):
        Debug.debug(id, DebugLevel.Function)
        return self.idDic[id]

    def getId(self, gateType, params):
        Debug.debug("gateType:" + str(gateType) + " params" + str(params), DebugLevel.Function)
        if gateType in self.stDic.keys():
            return GateDictionary.getIdRecursive(self.stDic[gateType], params)
        else:
            return NO_ID

    def getIdRecursive(dic, params):
        if not params:
            if isinstance(dic,dict):
                return NO_ID
            else:
                return dic
        elif not params[0] in dic.keys():
            return NO_ID
        else:
            return GateDictionary.getIdRecursive(dic[params[0]], params[1:])

    #return id
    def addGate(self, gate, gateType, params):
        idExist = self.getId(gateType, params)
        if idExist != NO_ID:
            return idExist
        else:
            Debug.debug("Adding gate [" + str(self.idActual) + "]<" + str(gateType.name) + ">: " + str(params), DebugLevel.Debug)
            gate.setId(self.idActual)
            self.idDic[self.idActual] = gate
            GateDictionary.addGateRecursive(self.idActual, self.stDic, [gateType] + params)
            self.idActual += 1
            return self.idActual - 1

    def addGateRecursive(id, dic, params):
        if len(params) == 1:
            dic[params[0]] = id
        else:
            if not params[0] in dic.keys():
                dic[params[0]] = {}
            GateDictionary.addGateRecursive(id, dic[params[0]], params[1:])


    def printCascadeDictionary(dic):
        st = "{"
        for k in dic.keys():
            st += " " + str(k) + ": "
            if isinstance(dic[k], dict):
                st += GateDictionary.printCascadeDictionary(dic[k])
            else:
                st += str(dic[k]) + " ;"
        st += "}"
        return st