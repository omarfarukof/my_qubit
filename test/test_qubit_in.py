import pytest
from my_qubit.qubit import qubit
import numpy as np

test_Qubits = [
    ((0.8, 0.6)),
    ([0,1j]),
    (0,1),
    ((1j/np.sqrt(2) , 1/np.sqrt(2))),
    (0),
    (1),
    (np.array([[1], [0]])),
]


@pytest.mark.parametrize("test_qubit" , test_Qubits)
def test_qubit_in(test_qubit):
    # with not pytest.raises(ValueError):
    qubit(test_qubit)

