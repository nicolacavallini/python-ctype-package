import numpy as np

from context import ray_t

import ray_t.c_interface as ci




def test_cosine():

    x = np.linspace(0,1)

    y = ci.cos(x)

    ck = np.cos(x)

    assert np.allclose(y,ck)


if __name__ == "__main__":

    test_cosine()
