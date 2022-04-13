from qiskit import QuantumCircuit, QuantumRegister
import numpy as np


# SPECIFY The `trotter_steps` you want to evaluate on
MY_TROTTER_STEPS = 7
TARGET_TIME = np.pi  # we'll not change this, you can use it for convenience

# Parameterize variable t to be evaluated at t=pi later
t = TARGET_TIME / MY_TROTTER_STEPS

def XX():
    # Build a subcircuit for XX(t) two-qubit gate
    XX_qr = QuantumRegister(2)
    XX_qc = QuantumCircuit(XX_qr, name='XX')

    XX_qc.ry(np.pi/2,[0,1])
    XX_qc.cnot(0,1)
    XX_qc.rz(2 * t, 1)
    XX_qc.cnot(0,1)
    XX_qc.ry(-np.pi/2,[0,1])

    # Convert custom quantum circuit into a gate
    return XX_qc.to_instruction()

def YY():
    # Build a subcircuit for YY(t) two-qubit gate
    YY_qr = QuantumRegister(2)
    YY_qc = QuantumCircuit(YY_qr, name='YY')

    YY_qc.rx(np.pi/2,[0,1])
    YY_qc.cnot(0,1)
    YY_qc.rz(2 * t, 1)
    YY_qc.cnot(0,1)
    YY_qc.rx(-np.pi/2,[0,1])

    # Convert custom quantum circuit into a gate
    return YY_qc.to_instruction()

def ZZ():
    # Build a subcircuit for ZZ(t) two-qubit gate
    ZZ_qr = QuantumRegister(2)
    ZZ_qc = QuantumCircuit(ZZ_qr, name='ZZ')

    ZZ_qc.cnot(0,1)
    ZZ_qc.rz(2 * t, 1)
    ZZ_qc.cnot(0,1)

    # Convert custom quantum circuit into a gate
    return ZZ_qc.to_instruction()

# we combine XX YY ZZ in a single circuit which uses only two CX plus one CRX
def XXYYZZ():

    qc = QuantumCircuit(2, name='XXYYZZ')
    
    # XXYYZZ in a single step
    qc.cx(0, 1)
    qc.rz(2 * t, 1)
    qc.crx(4 * t, 1, 0)
    qc.cx(0, 1)
    
    return qc.to_instruction()


def my_trotter(trotter_steps):
    num_qubits = 3
    Trot_qr = QuantumRegister(num_qubits)
    Trot_qc = QuantumCircuit(Trot_qr, name="Trot")

    for i in range(0, num_qubits - 1):
        Trot_qc.append(XXYYZZ(), [Trot_qr[i], Trot_qr[i+1]])
        #Trot_qc.append(ZZ(), [Trot_qr[i], Trot_qr[i+1]])
        #Trot_qc.append(YY(), [Trot_qr[i], Trot_qr[i+1]])
        #Trot_qc.append(XX(), [Trot_qr[i], Trot_qr[i+1]])

    Trot_gate = Trot_qc.to_instruction()

    return Trot_gate, [1, 3, 5]