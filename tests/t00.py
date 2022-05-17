import numpy as np
import matplotlib.pyplot as plt

from context import pkg

import pkg.c_interface as ci

def test_cosine():

    x = np.linspace(0,1,7)

    y = ci.cos(x)
    
    ck = np.cos(x)

    assert np.allclose(y,ck)


if __name__ == "__main__":

    test_cosine()
