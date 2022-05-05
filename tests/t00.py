import numpy as np
import matplotlib.pyplot as plt

from context import ray_t

import ray_t.c_interface as ci




def test_cosine():

    x = np.linspace(0,1,7)

    y = ci.cos(x)

    #plt.plot(x,y)
    #plt.show()

    ck = np.cos(x)

    assert np.allclose(y,ck)


if __name__ == "__main__":

    test_cosine()
