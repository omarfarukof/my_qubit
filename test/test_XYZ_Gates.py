import pytest
from my_qubit.qubit import qubit , zero_qubit , one_qubit
import numpy as np

test_cases_X_gate = [
    (zero_qubit() , np.array([[1], [0]])),
    (one_qubit() , np.array([[0], [1]])),
    (qubit(0.8, 0.6) , np.array([[0.6], [0.8]])),
    (qubit(1/np.sqrt(2) , 1/np.sqrt(2)) , np.array([[1/np.sqrt(2)], [1/np.sqrt(2)]]))
]
@pytest.mark.parametrize("test_qubit , test_return" , test_cases_X_gate)
def test_x_gate(test_qubit , test_return):
    assert ( test_qubit.x_gate().qubit_vector == test_return ).all
    assert test_qubit.qubit_valid()
    assert test_qubit.x_gate().qubit_valid()

test_cases_Y_gate = [
    (zero_qubit() , np.array([[1], [0]])),
    (one_qubit() , np.array([[0], [1]])),
    (qubit(0.8, 0.6) , np.array([[0.8], [-0.6]])),
    (qubit(1/np.sqrt(2) , 1/np.sqrt(2)) , np.array([[1/np.sqrt(2)], [-1/np.sqrt(2)]]))
]
@pytest.mark.parametrize("test_qubit , test_return" , test_cases_Y_gate)
def test_y_gate(test_qubit , test_return):
    assert (test_qubit.qubit_vector == test_return).all
    assert test_qubit.qubit_valid()
    assert test_qubit.y_gate().qubit_valid()

test_cases_Z_gate = [
    (zero_qubit() , np.array([[1], [0]])),
    (one_qubit() , np.array([[1], [0]])),
    (qubit(0.8, 0.6) , np.array([[1], [0]])),
    (qubit(1/np.sqrt(2) , 1/np.sqrt(2)) , np.array([[1], [0]]))
]
@pytest.mark.parametrize("test_qubit , test_return" , test_cases_Z_gate)
def test_z_gate(test_qubit , test_return):
    assert (test_qubit.z_gate().qubit_vector == test_return).all
    assert test_qubit.qubit_valid()
    assert test_qubit.z_gate().qubit_valid()
