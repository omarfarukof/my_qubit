import pytest
from my_qubit.qubit import qubit , zero_qubit , one_qubit
import numpy as np

test_Qubits = [
    (qubit(0.8, 0.6)),
    (zero_qubit()),
    (one_qubit()),
    (qubit(1/np.sqrt(2) , 1/np.sqrt(2)))
]

@pytest.mark.parametrize("test_qubit" , test_Qubits)
def test_qubit_vector_immute(test_qubit):
    with pytest.raises(AttributeError):
        test_qubit.qubit_vector = np.array([[1], [0]])

@pytest.mark.parametrize("test_qubit" , test_Qubits)
def test_alpha_immute(test_qubit):
    with pytest.raises(AttributeError):
        test_qubit.alpha = 0

@pytest.mark.parametrize("test_qubit" , test_Qubits)
def test_beta_immute(test_qubit):
    with pytest.raises(AttributeError):
        test_qubit.beta = 1