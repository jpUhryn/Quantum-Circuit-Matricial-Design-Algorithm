
# PROGRAM
This program allows to probe empirically the use of the Quantum Circuit Matricial Design - QCMD algorithm.
This algorithm generate an assembler file with the quantum circuit required that fixed with a given matrix as input.
All the scripts to use (root directory and loadAsm directory) have a --help command to know the arguments required.

## Use IBM-Q cuantum computer
To use this program, it is needed the installation of the Python API QISKit. (https://github.com/QISKit/qiskit-tutorial/blob/master/INSTALL.md)

Some of this scrips need a direct connection with the IBM quantum computer, and a login is required.
In order to log in in the IBM-Q you need to get an IBM account (explained in: https://qiskit.org/documentation/quickstart.html) and set the TOKEN that you get in account/Qconfig.py -> APItoken.

## LOAD ASSEMBLER
There are 3 scripts in loadAsm directory that allows to send a .qasm file to the QISKit Python API to get the results of the circuit inside.
In this directory it is found a .qasm example.

### load_qasm
This script allows to get a simulated result of the circuit.

### load_qasm_matrix
This script return by raw text the matrix solution of the circuit.

### load_real_qasm
This script allows to send the circuit to the IBM-Q 5 qubits IBM quantum computer and get the results.

## TEST
This 2 scripts test the funcionallity of the algorithm, using it to generate a .qasm file with the circuit specified.

### aqp_matrix_test
This script test all the implemented gates in QCMD algorithm and compare the matrix solution with the real matrix that the circuit generates in QISKit simulator

### aqp_real_test
This script execute two kind of this gates (generate matrix and rowReverse) in a real quantum computer, and compares the results with the expected and theorical ones.


# AUTHOR: 
Javier París Uhryn - 
Universidad Autonoma de Madrid, Escuela Politécnica Superior