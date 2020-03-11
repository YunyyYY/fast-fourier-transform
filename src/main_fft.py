"""
Simple implementation of FFT.
Use the method that generate X(w) in bit reverse order.
Adjust the order in each iteration to natural order.
"""
import numpy as np

def fft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if  np.log2(N)%1 != 0:  # check if N is power of 2
        raise ValueError("size of x is not a power of 2")

    size = min(N, 32)   # crop the original array to subarrays of size <= 32
    h = np.arange(size) # horizontal vector
    v = h[:, None]      # vertical vector
    W = np.exp(-2j * np.pi * h * v / size)  # W of shape size * size phase factors
    X = np.dot(W, x.reshape((size, -1)))    # crop x to subarrays of length=size
                                            # if N<32, already completed
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1]//2]
        X_odd = X[:, X.shape[1]//2:]
        # include the factor for multiplies of <size> in X
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])/ X.shape[0])[:, None]
        # reorder the output
        X = np.vstack([X_even + factor * X_odd, X_even - factor * X_odd])
    
    return X.ravel()
