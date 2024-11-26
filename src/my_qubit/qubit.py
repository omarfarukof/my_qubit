import numpy as np
class qubit:
    # qubit = alpha*|0> + beta*|1>
    __zero_qubit_s = '|0)'
    __one_qubit_s = '|1)'
    dirac_notation = True
    __qubit_vector = np.array([[0], [0]])
    @property
    def qubit_vector(self):
        return self.__qubit_vector
    @qubit_vector.setter
    def qubit_vector(self, value):
        raise AttributeError("property 'qubit_vector' of 'qubit' objects is not writable ")

    def __init__(self, qubit_in, beta=None):
        if isinstance(qubit_in , np.ndarray):
            if qubit_in.shape != (2,1):
                raise ValueError("qubit_in must be a 2x1 array")
        elif isinstance(qubit_in , tuple):
            if len(qubit_in) != 2:
                raise ValueError("qubit_in must be a tuple of length 2")
            qubit_in = np.array(qubit_in).reshape(2,1)
        elif isinstance(qubit_in , list):
            if len(qubit_in) != 2:
                raise ValueError("qubit_in must be a list of length 2")
            qubit_in = np.array(qubit_in).reshape(2,1)
        elif isinstance(qubit_in , (int,float,complex)):
            qubit_in = np.array([[qubit_in], [0]])
            if beta is not None:
                qubit_in[1][0] = beta
            elif np.allclose(qubit_in[0][0] , 0):
                qubit_in[1][0] = 1
            elif np.allclose(qubit_in[0][0] , 1):
                qubit_in[1][0] = 0
            else:
                raise ValueError("beta must be provided")
            
        self.__qubit_vector = qubit_in
        if not self.qubit_valid():
            raise ValueError("qubit_in must be a valid qubit")


    @property
    def alpha(self):
        return self.qubit_vector[0][0]
    @alpha.setter
    def alpha(self, value):
        raise AttributeError("property 'alpha' of 'qubit' objects is not writable ")
    @property
    def beta(self):
        return self.qubit_vector[1][0]
    @beta.setter
    def beta(self, value):
        raise AttributeError("property 'beta' of 'qubit' objects is not writable ")
        
    @property
    def theta(self):
        return np.arccos(self.alpha)*2

    @property
    def phi(self):
        return np.arcsin(np.abs(self.beta))*2


    def __state(self):
        return ( self.qubit_vector.conj().T @ self.qubit_vector ).item()
    # print method
    def __str__(self):

        if self.dirac_notation:
            return f"{self.alpha:.2g} {self.__zero_qubit_s} + {self.beta:.2g} {self.__one_qubit_s}"
        else:
            return str(self.qubit_vector)

    def qubit_valid(self) -> bool:
        return np.allclose(self.__state() , 1)

    def x_gate(self , _qubit = None):
        _X_gate = np.array([[0, 1], [1, 0]])
        if _qubit is None:
            _qubit = self
        _qubit_vector = _X_gate @ _qubit.qubit_vector
        return qubit(_qubit_vector)

    def y_gate(self , _qubit = None):
        _Y_gate = np.array([[0, -1j], [1j, 0]])
        if _qubit is None:
            _qubit = self
        _qubit_vector = _Y_gate @ _qubit.qubit_vector
        return qubit(_qubit_vector)

    def z_gate(self , _qubit = None):
        _Z_gate = np.array([[1, 0], [0, -1]])
        if _qubit is None:
            _qubit = self
        _qubit_vector = _Z_gate @ _qubit.qubit_vector
        return qubit(_qubit_vector)

    

class zero_qubit(qubit):
    def __init__(self):
        super().__init__(1, 0)

class one_qubit(qubit):
    def __init__(self):
        super().__init__(0, 1)

