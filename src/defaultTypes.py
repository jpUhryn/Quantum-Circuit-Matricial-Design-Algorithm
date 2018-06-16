
from enum import Enum
import numpy as np
import math


class DebugLevel(Enum):
    Nothing = 0
    Error = 1
    Warning = 2
    Result = 3
    Schedule = 4
    Info = 5
    Function = 6
    Debug = 7
    All = 8
    StdOut = 9

class DebugColors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Colors(Enum):
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class QubitStringType(Enum):
    Empty  = 1
    Source = 2
    Target = 3

class StandarGate(Enum):
    I = "I"
    X = "X"
    H = "H"

class TurnType(Enum):
    X = "X"
    Z = "Z"

class GateType(Enum):
    Basic			  = 1
    BasicTurn         = 2
    Xnot              = 3
    Special           = 4
    RowReverse        = 5
    CondTurn          = 6
    Toffoli           = 7
    MultipleTurn      = 8
    SpecialTurn       = 9
    Oracle            = 10
    AmplitudAmplifier = 11

class GateDominio(Enum):
    Open = 1
    Close = 2

QuantumOriginalGates = {
        "I" : (np.matrix([[1, 0],[0, 1]], dtype=complex)),
        "X" : (np.matrix([[0, 1],[1, 0]], dtype=complex)),
        "Y" : (np.matrix([[0, -1j],[1j, 0]], dtype=complex)),
        "Z" : (np.matrix([[1, 0],[0, -1]], dtype=complex)),
        "H" : (np.matrix([[1, 1],[1, -1]], dtype=complex)*(1/math.sqrt(2))),
        "S" : (np.matrix([[1, 0],[0, 1j]], dtype=complex)),
        "Si" : (np.matrix([[1, 0],[0, -1j]], dtype=complex)),
        "T" : (np.matrix([[1, 0],[0, math.sqrt(2)/2 + math.sqrt(2)*1j/2]], dtype=complex)), #math.exp(1j*math.pi/4)
        "Ti" : (np.matrix([[1, 0],[0, math.sqrt(2)/2 - math.sqrt(2)*1j/2]], dtype=complex)),
    }

NO_ID = -1
FIRST_ID = 0

#dic
#   basic*
#       standar gate
#           targets
#   basic turn*
#       turn type
#           target
#               angle
#   xnot*
#       source
#           target
#######################################
#   builded
#       special*
#           name
#       row reverse*
#           target1
#               target2
#       conditional
#           conditional turn*
#               turn type
#                   target
#                       source
#                           angle
#           multiple
#               special turn*
#                   theta
#                       phi
#               multiple turn*
#                   turn type
#                       target
#                           source
#                               angle
#           toffoli*
#               target
#                   sources
