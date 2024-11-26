import pytest
from my_qubit.qubit import qubit
import numpy as np

test_Qubits = [
    ((0.8, 0.8)),
    ([1,1]),
    (0,0),
    (1j),
    ([0]),
    ((1 , 1/np.sqrt(2)))
]

@pytest.mark.parametrize("test_qubit" , test_Qubits)
def test_value_error(test_qubit):
    with pytest.raises(ValueError):
        qubit(test_qubit)