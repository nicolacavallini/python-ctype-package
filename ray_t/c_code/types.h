#ifndef TYPES_H
#define TYPES_H

#include <Eigen/Dense>

typedef Eigen::Matrix<double,2,3> Edge;

typedef Eigen::Matrix<double,3,1> Point;

typedef Eigen::Matrix<double,3,1> Direction;

typedef Eigen::Matrix<double,3,3> Face;

typedef Eigen::Matrix<double,4,1> FaceCoeffs;

typedef Eigen::Matrix<double,4,4> Simplex;

#endif //TYPES_H
