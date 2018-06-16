
from src.DictionarySearcher import DictionarySearcher
from src.QuantumMath import QuantumMath
from src.Debug import Debug

from src.defaultTypes import *
from src.gate import *

import numpy as np
import math
import cmath



class AQP():

    # GENERATE MATRIX
    def generateBasicMatrix(standarGate, targets, nQubits):
        
        matrixIdentity = QuantumMath.getStdMatrix("I")
        matrixGate = QuantumMath.getStdMatrix(standarGate.name)
        matrixList = []
        
        for i in range(nQubits):
            if i in targets:
                matrixList.append(matrixGate)
            else:
                matrixList.append(matrixIdentity)
                
        return QuantumMath.tensorDot(matrixList)

    def generateXnotMatrix(source, target, nQubits):

        array = []
        o2 = 2**(nQubits-source-1)
        t2 = 2**(nQubits-target-1)
        q2 = 2**nQubits
        for i in range(q2):
            #buscamos los bits que nos conciernen en este caso
            bo = (i//o2)%2
            if bo == 1:
                to = (i//t2)%2
                if to == 0:
                    n = i + t2
                else:
                    n = i - t2
            else:
                n = i

            newArray = np.zeros(q2, dtype=complex)
            newArray[n] = 1

            array.append(newArray)

        return QuantumMath.generateMatrixFromBasicEquations(nQubits, array)

    def generateBasicTurnMatrix(target, angle, turnType, nQubits):
        
        matrixIdentity = QuantumMath.getStdMatrix("I")          
        matrixGate = QuantumMath.getStdTurnMatrix(turnType, angle)
        matrixList = []
        
        for i in range(nQubits):
            if i == target:
                matrixList.append(matrixGate)
            else:
                matrixList.append(matrixIdentity)
                
        return QuantumMath.tensorDot(matrixList)

        
    def generateMatrixFromPath(path, dic):

        matrixList = []
        
        for i in path:
            matrixList.append(dic.getGate(i).getMatrix())
        matrixList.reverse()
        return QuantumMath.matrixDot(matrixList)


    # GENERATE PATH

    def generateRowReversePath(target1, target2, dic):
            
        nQubits = dic.getNQubits()

        if target1 == target2:

            #identity matrix
            basicId = AQP.generateBasic(standarGate=StandarGate.I, targets=[0], dic=dic)

            return [basicId]

        #convert targets to binary
        targetList1 = QuantumMath.toBinary(2**nQubits-target1-1, nQubits)
        targetList2 = QuantumMath.toBinary(2**nQubits-target2-1, nQubits)

        allsources = []
        for i in range(nQubits):
            allsources.append(i)

        idList = []

        for i in range(nQubits):

            if targetList1[i] == targetList2[i]:
                continue

            # create X gate to set all to 1
            targets = []
            sources = []
            for j in range(nQubits):
                if i == j:
                    continue
                if targetList1[j] == 1:
                    targets.append(j)
                sources.append(j)

            setTrueId = AQP.generateBasic(standarGate=StandarGate.X, targets=targets, dic=dic)

            # create toffoli
            toffoliId = AQP.generateToffoli(sources=sources, target=i, dic=dic)
            
            idList.append([setTrueId, toffoliId, setTrueId])

            targetList1[i] = targetList2[i] 
        
        # generate the last path concatenating all
        path = []

        for i in idList:
            path += i

        for i in reversed(idList[:-1]):
            path += i

        return path


        
    def generateCondTurnPath(turnType, target, source, angle, dic):
        
        # xnot
        xnotId = AQP.generateXnot(source=source, target=target, dic=dic)

        # turn
        inverseTurnId = AQP.generateBasicTurn(target=target, angle=QuantumMath.inverseAngle(angle/2), turnType=turnType, dic=dic)
        turnId = AQP.generateBasicTurn(target=target, angle=angle/2, turnType=turnType, dic=dic)
        

        # with Z turn it need a recalculation
        if turnType == TurnType.Z:
            turnIdSource = AQP.generateBasicTurn(target=source, angle=angle/2, turnType=turnType, dic=dic)
            return [xnotId, inverseTurnId, xnotId, turnId, turnIdSource]

        else:
            #return [xnotId, inverseTurnId, xnotId, turnId]
            return [turnId, xnotId, inverseTurnId, xnotId]

        
    def generateMultipleTurnPath(turnType, target, sources, angle, dic):
        
        # if there is just one source, is like a condTurn
        if len(sources) == 1:
            return [AQP.generateCondTurn(turnType=turnType, target=target, source=sources[0], angle=angle, dic=dic)]

        # if there is two sources the implementation in automatic
        elif len(sources) == 2:

            nAngle = angle/2

            # conditional turn
            condTurnId = AQP.generateCondTurn(turnType=turnType, target=target, source=sources[1], angle=nAngle, dic=dic)

            # xnot
            xnotId = AQP.generateXnot(source=sources[0], target=sources[1], dic=dic)

            # conditional turn inverse
            condTurnInvId = AQP.generateCondTurn(turnType=turnType, target=target, source=sources[1], angle=QuantumMath.inverseAngle(nAngle), dic=dic)

            # conditional turn from above
            condTurnAboveId = AQP.generateCondTurn(turnType=turnType, target=target, source=sources[0], angle=nAngle, dic=dic)

            #added to path
            return [condTurnId, xnotId, condTurnInvId, xnotId, condTurnAboveId]

        else:

            nAngle = angle/2

            path = []

            # multiple n-1 sources
            multipleId = AQP.generateMultipleTurn(turnType=turnType, target=target, sources=sources[1:], angle=nAngle, dic=dic)

            path.append(multipleId)


            # create xnot to every qubit source from first source
            pathXnot = []
            for qubitAux in sources[1:]:

                # xnot
                xnotId = AQP.generateXnot(source=sources[0], target=qubitAux, dic=dic)

                #added to path
                pathXnot.append(xnotId)

            
            path += pathXnot


            # multiple n-1 sources
            multipleInvId = AQP.generateMultipleTurn(turnType=turnType, target=target, sources=sources[1:], angle=QuantumMath.inverseAngle(nAngle), dic=dic)

            path.append(multipleInvId)


            # redo xnots
            path += pathXnot


            # negate last qubit
            negateId = AQP.generateBasic(standarGate=StandarGate.X, targets=[sources[-1]], dic=dic)

            path.append(negateId)


            # x not from last qubit
            pathInverseXnot = []
            for qubitAux in sources[1:-1]:

                # xnot
                xnotId = AQP.generateXnot(source=sources[-1], target=qubitAux, dic=dic)

                #added to path
                pathInverseXnot.append(xnotId)

            path += pathInverseXnot

            # create the new multi conditional
            multiLowId = AQP.generateMultipleTurn(turnType=turnType, target=target, sources=sources[:-1], angle=nAngle, dic=dic)

            path.append(multiLowId)


            # redo the negation
            path += pathInverseXnot
            path.append(negateId)

            return path

        
    def generateSpecialTurnPath(a, b, dic):
        
        module = QuantumMath.vectorModule([a,b])

        # normalizing parameters
        a /= module
        b /= module

        # calculating theta x and y
        theta = math.asin(QuantumMath.complexModule(b))
        y = cmath.phase(b)
        x = cmath.phase(a)

        lastQubit = dic.getNQubits()-1
        sourceQubits = []
        for i in range(lastQubit):
            sourceQubits.append(i)

        firstGateId = AQP.generateMultipleTurn(turnType=TurnType.Z, target=lastQubit, sources=sourceQubits, angle=(-y+x+math.pi), dic=dic)

        secondGateId = AQP.generateMultipleTurn(turnType=TurnType.X, target=lastQubit, sources=sourceQubits, angle=theta*2, dic=dic)

        thirdGateId = AQP.generateMultipleTurn(turnType=TurnType.Z, target=lastQubit, sources=sourceQubits, angle=(y+x), dic=dic)

        lastCondId = AQP.generateMultipleTurn(turnType=TurnType.Z, target=lastQubit, sources=sourceQubits, angle=QuantumMath.inverseAngle(x), dic=dic)

        # is the same with Toffoli or last qubit X
        #allToffoliId = AQP.generateToffoli(target=lastQubit, sources=sourceQubits, dic=dic)
        allToffoliId = AQP.generateBasic(standarGate=StandarGate.X, targets=[lastQubit], dic=dic)

        return [firstGateId, secondGateId, thirdGateId, lastCondId, allToffoliId, lastCondId, allToffoliId]


    def generateToffoliPath(target, sources, dic):

        if len(sources) == 1:
            xnotId = AQP.generateXnotMatrix(source=sources[0], target=target, nQubits=dic.getNQubits())
        
        #X turn
        xId = AQP.generateMultipleTurn(turnType=TurnType.X, target=target, sources=sources, angle=math.pi, dic=dic)

        #Z turn
        zId = AQP.generateMultipleTurn(turnType=TurnType.Z, target=target, sources=sources, angle=math.pi, dic=dic)   

        return [zId, xId] 
        
     
    def generateSpecialPath(name, matrix, dic):
        
        nRows = 2**dic.getNQubits()
        step = AQP.getNextStep(matrix=matrix, step=[-1, -1], nRows=nRows)

        lastRow = nRows-1
        penLastRow = nRows-2

        idPath = []

        while(step):

            #print(matrix)
            #print(step)

            a = 0
            b = 0

            if step[0] == step[1]:
                #diagonal

                if step[0] == penLastRow:
                    #last special turn

                    # create the special turn matrix with the conjugate values
                    a = QuantumMath.conjugate(matrix[step[0], step[0]])

                    specialTurnId = AQP.generateSpecialTurn(a=a, b=0, dic=dic)


                    #added to path
                    idPath = [specialTurnId] + idPath

                else:
                    rowRevertPenLastId = AQP.generateRowReverse(target1=step[0], target2=penLastRow, dic=dic)


                    # create the special turn matrix with the conjugate values
                    a = QuantumMath.conjugate(matrix[step[0], step[0]])

                    specialTurnId = AQP.generateSpecialTurn(a=a, b=0, dic=dic)


                    #added to path
                    idPath = [rowRevertPenLastId, specialTurnId, rowRevertPenLastId] + idPath


            else:
                # create the row reversion
                rowRevertPenLastId = AQP.generateRowReverse(target1=step[0], target2=penLastRow, dic=dic)

                rowRevertLastId = AQP.generateRowReverse(target1=step[1], target2=lastRow, dic=dic)


                # create the special turn matrix with the conjugate values
                a = QuantumMath.conjugate(matrix[step[0], step[0]])
                b = QuantumMath.conjugate(matrix[step[1], step[0]])

                specialTurnId = AQP.generateSpecialTurn(a=a, b=b, dic=dic)


                #! IS IMPORTANT THE ORDEN OF THE REVERSER
                #added to path
                idPath = [rowRevertLastId, rowRevertPenLastId, specialTurnId, rowRevertPenLastId, rowRevertLastId] + idPath


            matrix = AQP.nextMatrix(matrix=matrix, step=step, a=a, b=b, nRows=nRows)
            #print(matrix)
            #print("\n\n")


            step = AQP.getNextStep(matrix=matrix, step=step, nRows=nRows)


        # Last binary matrix should be a Z 

        #get phase for last value
        phase = QuantumMath.getPhase(matrix[nRows-1,nRows-1])

        if phase != 0:

            sources = []
            for i in range(dic.getNQubits()-1):
                sources.append(i)

            # added last turn Z
            turnId = AQP.generateMultipleTurn(turnType=TurnType.Z, target=dic.getNQubits()-1, sources=sources, angle=phase, dic=dic)

            idPath = [turnId] + idPath

        return idPath


    # AUXILIAR FUNCTIONS TO SPECIAL GATES
    def getNextStep(matrix, step, nRows):

        while(True):
            step = AQP.calculateNextStep(step, nRows)
            if not step:
                return None
            elif step[0] == step[1]:
                if not np.isclose(matrix[step[0],step[0]],1):
                    return step

            elif matrix[step[1],step[0]] != 0:
                return step


    def calculateNextStep(step, nRows):

        if step[0] == step[1]:
            step[0] += 1
            step[1] += 2

            if step[0] == nRows - 1:
                return None

            return step

        step[1] += 1

        if step[1] >= nRows:
            step[1] = step[0]
            return step

        return step


    def nextMatrix(matrix, step, a, b, nRows):

        module = QuantumMath.vectorModule([a,b])

        if step[0] == step[1]:

            #diagonal
            matrix[step[0],step[0]] = 1

            matrix[nRows-1,nRows-1] *= -QuantumMath.conjugate(a)

            return matrix

        else:
            #! mejorar para no hacer la multiplicacion

            newMatrix = np.eye(nRows, dtype=complex)

            newMatrix[step[0],step[0]] = a/module

            newMatrix[step[1],step[1]] = -QuantumMath.conjugate(a)/module

            newMatrix[step[0],step[1]] = b/module

            newMatrix[step[1],step[0]] = QuantumMath.conjugate(b)/module

            #print (newMatrix)


            return np.dot(newMatrix, matrix)
 

    # GENERATE ID

    def generateBasic(standarGate, targets, dic):
        #Debug.debug("standarGate:" + str(standarGate) + " targets" + str(targets), DebugLevel.Function)
        
        idRes = dic.getIdBasic(standarGate=standarGate, targets=targets)
        if not idRes == NO_ID:
            return idRes

        gate = gate=Basic(id=NO_ID, matrix=AQP.generateBasicMatrix(standarGate=standarGate, targets=targets, nQubits=dic.getNQubits()), nQubits=dic.getNQubits(), standarGate=standarGate, targets=targets)
        return dic.addIdBasic(gate, standarGate=standarGate, targets=targets)


    def generateXnot(source, target, dic):
        
        idRes = dic.getIdXnot(source=source, target=target)
        if not idRes == NO_ID:
            return idRes

        gate = Xnot(id=NO_ID, matrix=AQP.generateXnotMatrix(target=target, source=source, nQubits=dic.getNQubits()), nQubits=dic.getNQubits(), target=target, source=source)
        return dic.addIdXnot(gate=gate, source=source, target=target)


    def generateBasicTurn(target, angle, turnType, dic):
        
        idRes = dic.getIdBasicTurn(angle=angle, turnType=turnType, target=target)
        if not idRes == NO_ID:
            return idRes

        gate = BasicTurn(id=NO_ID, matrix=AQP.generateBasicTurnMatrix(target=target, angle=angle, turnType=turnType, nQubits=dic.getNQubits()), nQubits=dic.getNQubits(), angle=angle, turnType=turnType, target=target)
        return dic.addIdBasicTurn(gate=gate, angle=angle, turnType=turnType, target=target)



    def generateRowReverse(target1, target2, dic):
        
        t1 = target1
        target1 = min(target1, target2)
        target2 = max(t1, target2)

        idRes = dic.getIdRowReverse(target1=target1, target2=target2)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateRowReversePath(target1=target1, target2=target2, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = RowReverse(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, target1=target1, target2=target2)
        return dic.addIdRowReverse(gate=gate, target1=target1, target2=target2)

        
    def generateCondTurn(turnType, target, source, angle, dic):

        idRes = dic.getIdCondTurn(turnType=turnType, target=target, source=source, angle=angle)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateCondTurnPath(turnType=turnType, target=target, source=source, angle=angle, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = CondTurn(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, target=target, source=source, angle=angle, turnType=turnType)
        return dic.addIdCondTurn(gate=gate, target=target, source=source, angle=angle, turnType=turnType)

        
    def generateMultipleTurn(turnType, target, sources, angle, dic):
        
        idRes = dic.getIdMultipleTurn(turnType=turnType, target=target, sources=sources, angle=angle)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateMultipleTurnPath(turnType=turnType, target=target, sources=sources, angle=angle, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = MultipleTurn(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, target=target, sources=sources, angle=angle, turnType=turnType)
        return dic.addIdMultipleTurn(gate=gate, target=target, sources=sources, angle=angle, turnType=turnType)

        
    def generateSpecialTurn(a, b, dic):
        
        idRes = dic.getIdSpecialTurn(a=a, b=b)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateSpecialTurnPath(a=a, b=b, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = SpecialTurn(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, a=a, b=b)
        return dic.addIdSpecialTurn(gate=gate, a=a, b=b)


    def generateToffoli(target, sources, dic):

        idRes = dic.getIdToffoli(target=target, sources=sources)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateToffoliPath(target=target, sources=sources, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = Toffoli(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, target=target, sources=sources)
        return dic.addIdToffoli(gate=gate, target=target, sources=sources)    
        
     
    def generateSpecial(name, matrix, dic):
        
        idRes = dic.getIdSpecial(name=name)
        if not idRes == NO_ID:
            return idRes

        path = AQP.generateSpecialPath(name=name, matrix=matrix, dic=dic)

        matrix = AQP.generateMatrixFromPath(path=path, dic=dic)

        gate = Special(id=NO_ID, matrix=matrix, nQubits=dic.getNQubits(), path=path, name=name)
        return dic.addIdSpecial(gate=gate, name=name)    

    
    
        
        
        