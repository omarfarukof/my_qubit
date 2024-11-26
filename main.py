import numpy as np

from src.my_qubit.qubit import qubit , zero_qubit , one_qubit


# print (qubit(0.8, 0.6))
# print (zero_qubit())
# print (one_qubit())


# a = qubit(1/np.sqrt(2) , 1/np.sqrt(2))
# print(a.qubit_matrics.shape)
# print(a.qubit_matrics.conj().T.shape)
# print(( a.qubit_matrics.conj().T @ a.qubit_matrics ).item() )

# qubit(0.8, 0.6).qubit_vector = np.array([[0.8], [0.6]])
# qubit(0.8, 0.6).qubit_vector = 1
qubit(0.8, 0.6).qubit_vector = np.array([[1], [0]])
