
from qiskit.wrapper import load_qasm_file
from qiskit import QISKitError, available_backends, execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import register
import sys
sys.path.append('../')
from account.Qconfig import *

if len(sys.argv) < 2:
    print ("ONE ARGUMENT IS REQUIRED -> use --help")
    quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print ("load_qasm_matrix <fileName> <number of shots> ->\n" +
        " load the qassembler code in fileName and execute in the real quantum computer IBM-Q of 5 qubits from IBM\n" +
        " OPTIONAL use an exact number of shots in the computer (1024 default)")
    quit()

try:

    if len(sys.argv) > 2:
        shots = sys.argv[2]
    else:
        shots = 1024

    QX_TOKEN = APItoken
    QX_URL = config['url']

    register(QX_TOKEN, QX_URL)

    print('\033[93m' + "\nConnecting with Quantum Computer... It could take a moment\n" + '\033[0m')

    qc = load_qasm_file(sys.argv[1])

    job_exp = execute(qc, 'ibmqx4', shots=shots, max_credits=10)
    sim_result = job_exp.result()
    realValues = sim_result.get_counts(qc)

    print(realValues)

except QISKitError as ex:
    print ("EXCEPCION Error = {}".format(ex))
    
