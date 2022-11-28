//############################################//
//                                            //
//    Jan Kwinta                28.11.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 1. Podpunkt a                   //
//                                            //
//############################################//

#include <iostream>
#include <Eigen/Dense>
#include <Eigen/SparseCore>
#include <Eigen/SparseLU>

int main(int argc, char **argv)
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);

    Eigen::SparseMatrix<double> A(7, 7);
    Eigen::VectorXd x(7);
    Eigen::VectorXd b{{1, 2, 3, 4, 5, 6, 7}};

    A.insert(0, 0) = 3;

    for(int i = 1; i <= 5; i++)
        A.insert(i, i) = 4;

    A.insert(6, 6) = 3;

    for(int i = 0; i <= 5; i++)
    {
        A.insert(i, i + 1) = 1;
        A.insert(i + 1, i) = 1;
    }

    Eigen::SparseLU<Eigen::SparseMatrix<double>, Eigen::COLAMDOrdering<int>> solver;
    solver.analyzePattern(A); 
    solver.factorize(A); 
    x = solver.solve(b); 

    std::cout << x << std::endl;
}    