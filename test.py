import numpy as np
from scipy.linalg import expm, sinm, cosm

target_time = np.pi

trotter_steps = 2

t = target_time / trotter_steps

X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0, -1j],[1j, 0]],dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)

I = np.eye(2)

CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)

SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=complex)

def RY(theta):
    return expm(-1j * (theta / 2) * Y)

def RZ(lambd):
    return expm(-1j * (lambd / 2) * Z)

def RX(theta):
    return expm(-1j * (theta / 2) * X)

def CRX10(lambd):
    return np.kron(np.array([[1,0],[0,0]], dtype=complex), I) + np.kron(np.array([[0,0],[0,1]], dtype=complex), RX(lambd))

def CRX01(lambd):
    return np.kron(I, np.array([[1,0],[0,0]], dtype=complex)) + np.kron(RX(lambd), np.array([[0,0],[0,1]], dtype=complex))

def matrixClose(m1, m2, epsilon=10**-7):
    return np.allclose(m1, m2, atol=epsilon)

standardXX = expm(-1j * t * np.kron(X, X))

standardYY = expm(-1j * t * np.kron(Y, Y))

standardZZ = expm(-1j * t * np.kron(Z, Z))

standardAll = standardZZ @ standardYY @ standardXX

XX = np.kron(RY(np.pi/2), RY(np.pi/2)) @ CNOT @ np.kron(I, RZ(2 * t)) @ CNOT @ np.kron(RY(-np.pi/2), RY(-np.pi/2))

YY = np.kron(RX(np.pi/2), RX(np.pi/2)) @ CNOT @ np.kron(I, RZ(2 * t)) @ CNOT @ np.kron(RX(-np.pi/2), RX(-np.pi/2))

ZZ = CNOT @ np.kron(I, RZ(2 * t)) @ CNOT

ALL = ZZ @ YY @ XX

newALL = CNOT @ np.kron(np.eye(2), RZ(2 * t)) @ CRX01(4 * t) @ CNOT

print(matrixClose(standardXX, XX))
print(matrixClose(standardYY, YY))
print(matrixClose(standardZZ, ZZ))
print(matrixClose(standardAll, newALL))
# print(standardAll)
# print(newALL)