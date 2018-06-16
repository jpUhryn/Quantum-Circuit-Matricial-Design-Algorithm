
from qiskit.wrapper import load_qasm_file
from qiskit import QISKitError, available_backends, execute
import sys
import numpy as np

if len(sys.argv) < 2:
	print ("ONE ARGUMENT IS REQUIRED -> use --help")
	quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
	print ("load_qasm_matrix <fileName> -> load the qassembler code in fileName and execute a simulator to get the matrix solution")
	quit()

try:

    np.set_printoptions(precision=2, linewidth=200, suppress=True)

    qc = load_qasm_file(sys.argv[1])

    job_sim = execute(qc, "local_unitary_simulator")
    sim_result = job_sim.result()
    matrix2 = sim_result.get_unitary(qc)

    print(matrix2)

except QISKitError as ex:
    print ("EXCEPCION Error = {}".format(ex))
    
