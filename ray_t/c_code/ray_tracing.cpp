#include "ray_tracing.h"

#include <iostream>

#include <chrono>

extern "C" void c_cos(int n_, double * x_p, double * y_p)
{
    auto start = std::chrono::steady_clock::now();

    Vector x(Eigen::Map<Vector>(x_p,n_));
    Vector y(Eigen::Map<Vector>(x_p,n_));

    std::cout << x << std::endl;


    std::chrono::duration<double> elapsed_seconds = std::chrono::steady_clock::now()-start;
    std::cout << "run time: " << elapsed_seconds.count() << "s\n";
}
