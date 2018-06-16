
from src.Debug import Debug
from src.GateDictionary import GateDictionary

from src.defaultTypes import *

from copy import deepcopy

class Visualizer():

    def printPath(id, dic, deepEnd=True, deep=0, printGate=False):
        Debug.debug("id:" + str(id) + " dic:" + str(dic) + " deepEnd:" + str(deepEnd) + " deep:" + str(deep), DebugLevel.Function)
        
        if deepEnd and deep < 0:
            return ""
            
        if printGate:
            st = "[" + str(dic.getGate(id)) + ": "
        else:
            st = "[" + str(id) + ": "
        
        for i in dic.getGate(id).getPath():
            st += Visualizer.printPath(id=i, dic=dic, deepEnd=deepEnd, deep=deep-1)
            
        return st + " ]"
        
    
    def printCompress(id, dic, deepEnd=True, deep=0, autoReference=False, interLineSpace=False, typed=True):
        Debug.debug("id:" + str(id) + " dic:" + str(dic) + " deepEnd:" + str(deepEnd) + " deep:" + str(deep) + " autoReference:" + str(autoReference) + " interLineSpace:" + str(interLineSpace) + " typed:" + str(typed), DebugLevel.Function)

        nq = dic.getNQubits()
        nSt = []
        
        for i in range(nq):
            nSt.append("")
        
        path = Visualizer.getLimitedPath(id, dic, deepEnd, deep, autoReference)
        
        Debug.debug("path:" + str(path), DebugLevel.Debug)

        

        for i in path:


            #autoref close
            if autoReference and isinstance(i,(tuple,)) and i[0] == GateDominio.Close:
                
                stAux = str(i[1])
                
                nSt[0] += " " + stAux + ")"
                for j in range(nq-1):
                    for k in range(len(stAux)+2):
                        nSt[j+1] += "-"

                continue

            
            #initial chain
            for j in range(nq):
                nSt[j] += "-"
            
            #autoref open
            if autoReference and isinstance(i,(tuple,)) and i[0] == GateDominio.Open:
                
                stAux = str(i[1])
                
                nSt[0] += "(" + stAux + " "
                for j in range(nq-1):
                    for k in range(len(stAux)+2):
                        nSt[j+1] += "-"

                i = i[1]

            
            #string
            if typed:
                maxS, l = dic.getGate(i).getStringTypedPerQubit()

                Debug.debug("maxS:" + str(maxS) + " l:" + str(l), DebugLevel.Debug)

                maxS += 2

                for j, value in enumerate(l):
                    type = value[0]
                    
                    if type is QubitStringType.Empty:
                        for k in range(maxS):
                            nSt[j] += "-"
                        
                    elif type is QubitStringType.Source:
                        for k in range((maxS-1)//2):
                            nSt[j] += "-"
                        nSt[j] += "O"
                        for k in range((maxS)//2):
                            nSt[j] += "-"
                            
                    elif type is QubitStringType.Target:
                        nSt[j] += "[" + value[1] + "]"
                            
            else:
                for j, value in enumerate(dic.getGate(i).getStringPerQubit()):
                    nSt[j] += value
                    
            #final chain
            for j in range(nq):
                nSt[j] += "-"
            
        st = "\n"
        for i in nSt:
            st += i
            if interLineSpace:
                st += "\n"
            st += "\n"
        
        return st


    def getLimitedPath(id, dic, deepEnd=True, deep=0, autoReference=False):
        Debug.debug("id:" + str(id) + " deep:" + str(deep) + " autoReference:"  +str(autoReference), DebugLevel.Function)
        
        if deepEnd and deep == 0:
            if autoReference:
                return [(GateDominio.Open,id), (GateDominio.Close,id)]
            else:
                return [id]
        
        path = dic.getGate(id).getPath()
        if path is []:
            if autoReference:
                return [(GateDominio.Open,id), (GateDominio.Close,id)]
            else:
                return [id]
        
        res = []
        if autoReference:
            res.append((GateDominio.Open,id))
            
        for i in path:
            res += Visualizer.getLimitedPath(i, dic, deepEnd, deep-1, autoReference)
        
        if autoReference:
            res.append((GateDominio.Close,id))

        return res

    
    
    def printIntegerMatrix(matrix):
        return str(np.around(matrix, decimals=0).astype(int))



    def getPath(id, dic):
        Debug.debug("id:" + str(id), DebugLevel.Function)
        
        path = dic.getGate(id).getPath()
        if not path:
            return [id]
        
        res = []
            
        for i in path:
            res += Assembler.getPath(i, dic)

        return res


    def writeAsm(id, dic, fileName):

        path = Assembler.getPath(id, dic)

        file = open(fileName)

        file.write(writeComment( "## Assembler file: " + fileName + " to id: " + str(id) + " ##\n"))

        for i in path:
            file.write(dic.getGate(id).getAsm())

        file.close()

