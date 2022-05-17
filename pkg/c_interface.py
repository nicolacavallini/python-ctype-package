import ctypes
import numpy as np
import numpy.ctypeslib as npct

from pkg.c_code.install_path import c_interface_path
from pkg.c_code.install_path import lib_name

import scipy.sparse as sp
import os


lib_file = os.path.join(c_interface_path, lib_name)

aux = os.path.abspath(lib_file)

_lib_ = ctypes.CDLL(aux)

array_1d_double = npct.ndpointer(dtype=np.double, ndim=1,
        flags='CONTIGUOUS')
array_1d_int = npct.ndpointer(dtype=np.int32, ndim=1,
        flags='CONTIGUOUS')

array_1d_int64 = npct.ndpointer(dtype=np.int64, ndim=1,
        flags='CONTIGUOUS')

pointer_int = ctypes.POINTER(ctypes.c_int)
pointer_double = ctypes.POINTER(ctypes.c_double)

_lib_.c_cos.restype = None
_lib_.c_cos.argtypes = [ctypes.c_int,array_1d_double,array_1d_double]


def cos(x):

    x_ = np.float64(x.flatten())
    n_ = np.int32(len(x))
    y_ = np.float64(np.zeros_like(x_))

    _lib_.c_cos(n_,x_,y_)

    y = np.reshape(y_,x.shape)

    return y
