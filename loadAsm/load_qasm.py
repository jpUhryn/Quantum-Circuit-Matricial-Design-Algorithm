
from qiskit.wrapper import load_qasm_file
from qiskit import QISKitError, available_backends, execute
import sys


if len(sys.argv) < 2:
	print ("ONE ARGUMENT IS REQUIRED -> use --help")
	quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
	print ("load_qasm <fileName> -> load the qassembler code in fileName and execute a simulator to get a simulated result")
	quit()

try:

    qc = load_qasm_file(sys.argv[1])

    job_sim = execute(qc, "local_qasm_simulator")
    sim_result = job_sim.result()
    counts = sim_result.get_counts(qc)

    print(counts)

except QISKitError as ex:
	print ("EXCEPCION Error = {}".format(ex))