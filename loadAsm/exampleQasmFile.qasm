// This file contains a simple example //
//  of a quantum assambler code for 2 qubits //
//  and represent a superposition state //


OPENQASM 2.0;
include "qelib1.inc";

h q[0];
h q[1];

measure q -> c;
