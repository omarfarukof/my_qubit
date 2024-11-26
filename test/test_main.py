import pytest
from my_qubit.qubit import qubit , zero_qubit , one_qubit
import numpy as np

test_Qubits = [
    (qubit(0.8, 0.6) , np.array([[0.8], [0.6]])),
    (zero_qubit() , np.array([[1], [0]])),
    (one_qubit() , np.array([[0], [1]])),
]

@pytest.mark.parametrize("test_qubit , return_qubit" , test_Qubits ) 
def test_qubit(test_qubit , return_qubit):
    assert (test_qubit.qubit_vector == return_qubit).all
    assert test_qubit.qubit_valid()

