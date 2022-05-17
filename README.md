# Bare Bones ctypes Package

 - Dependencies: Eigen3

 - Usage:
 ```
 cd pkg/c_code
 mkdir build
 cd build
 cmake  -DC_INTERFACE_INSTALL=/Users/memyselfandi/jrc/usr/pkg ../
 make -j4
 make install
 cd ../../../tests/
 python t00.py
 ```
