#include "ray_tracing.h"

#include <iostream>

#include <cmath>

#include <chrono>

extern "C" void c_cos(int n_, double * x_p, double * y_p)
{
    Vector x(Eigen::Map<Vector>(x_p,n_));
    Vector y(Eigen::Map<Vector>(y_p,n_));
    
    y = Eigen::cos(x.array());

    Eigen::Map<Vector>( y_p, n_) =   y;
}
