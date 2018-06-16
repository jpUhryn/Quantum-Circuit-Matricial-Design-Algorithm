
from src.defaultTypes import *

from time import gmtime, strftime
import inspect


class Debug():

    _fileName = "standarDebugFile.dbg"
    _fileOutputLevel = DebugLevel.Schedule
    _stdOutputLevel = DebugLevel.Error
    _autoDebugLevel = True
    _autoTime = True
    _outClasses = []
    _outFunction = []


    def startDebug(reset=False, fileName="standarDebugFile.dbg", fileOutputLevel=DebugLevel.Schedule, stdOutputLevel=DebugLevel.Error, autoDebugLevel=True, autoTime=True, outClasses=[], outFunctions=[]):
        
        Debug._fileName = fileName
        Debug._fileOutputLevel = fileOutputLevel
        Debug._stdOutputLevel = stdOutputLevel
        Debug._autoDebugLevel = autoDebugLevel
        Debug._autoTime = autoTime
        Debug._outClasses = outClasses
        Debug._outFunctions = outFunctions
        
        if reset:
            Debug.resetFile()

    def setFileName(fileName):
        Debug.fileName = fileName

    def setFileOutputLevel(fileOutputLevel):
        Debug.fileOutputLevel = fileOutputLevel

    def setStdtdOutputLevel(stdOutputLevel):
        Debug.stdOutputLevel = stdOutputLevel

    def setAutoDebugLevel(autoDebugLevel):
        Debug.autoDebugLevel = autoDebugLevel

    def setAutoTime(autoTime):
        Debug.autoTime = autoTime

    def resetFile():
        file = open(Debug.fileName,'w')
        file.close()

    def debug(text, level=DebugLevel.Schedule, color=None):

        function = inspect.stack()[1][3]
        classParam = inspect.stack()[1][1].split("/")[-1].split(".")[0]

        if classParam in Debug._outClasses:
            return

        if function in Debug._outFunctions:
            return

        #write in file
        if level.value <= Debug._fileOutputLevel.value:
            file = open(Debug._fileName,'a')
            if Debug._autoTime:
                file.write(strftime("%H:%M:%S", gmtime()) + ": ")

            file.write(classParam + "::" + function + ": ")

            if Debug._autoDebugLevel:
                file.write(level.name + ": ")
            file.write(str(text) + "\n\n")
            file.close()

        #write in stdout
        if level.value <= Debug._stdOutputLevel.value or level == DebugLevel.StdOut:

            st = (classParam + "::" + function + ": ") 

            #if Debug.__instance.autoDebugLevel:
            #    st += (level.name + ": ")
            st += str(text)

            #print in color
            if color:
                print(color + st + DebugColors.ENDC.value)
            elif level == DebugLevel.Warning:
                print(DebugColors.WARNING.value + st + DebugColors.ENDC.value)
            elif level == DebugLevel.Error:
                print(DebugColors.FAIL.value + st + DebugColors.ENDC.value)
            elif level == DebugLevel.Result:
                print(DebugColors.OKGREEN.value + st + DebugColors.ENDC.value)    
            elif level == DebugLevel.Debug:
                print(DebugColors.OKBLUE.value + st + DebugColors.ENDC.value)      
            else:
                print(st)
            print()

    def jump(file=False):

        jump = ("\n" +
                "-----------------------------------------------------------------------------" +
                "-----------------------------------------------------------------------------\n" +
                "-----------------------------------------------------------------------------" +
                "-----------------------------------------------------------------------------\n\n\n")
                

        if file:
            file = open(Debug.fileName,'a')
            file.write(jump)
            file.close()

        print (jump)