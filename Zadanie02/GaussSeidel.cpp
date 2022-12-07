//############################################//
//                                            //
//    Jan Kwinta                05.12.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 2. Podpunkt a                   //
//                                            //
//############################################//

#include <iostream>
#include <algorithm>
#include <Eigen/Dense>

Eigen::VectorXd gaussseidel(Eigen::MatrixXd A, Eigen::VectorXd e, int k)
{
    Eigen::VectorXd xk(128);

    if(k == 0)
        return xk;

    Eigen::VectorXd xkm1 = gaussseidel(A, e, k - 1);

    for(int i = 0; i < 128; i++)
    {
        double sum1 = 0, sum2 = 0;

        for(int j = std::max(0, i - 5); j < i; j++)
        {
            sum1 += A(i, j) * xk(j, 0);
        }

        for(int j = i + 1; j < std::min(128, i + 5); j++)
        {
            sum2 += A(i, j) * xkm1(j, 0);
        }

        xk(i, 0) = (1 / A(i, i)) * (1 - sum1 - sum2);
    }

    // std::cout << k << "-th iteration norm = " << (xk - xkm1).norm() << std::endl;

    return xk;
}

int main(int argc, char **argv)
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);

    Eigen::MatrixXd A(128, 128);
    Eigen::VectorXd x(128);
    Eigen::VectorXd e(128);

    for(int i = 0; i < 128; i++)
        A(i, i) = 4;

    for(int i = 0; i < 127; i++)
    {
        A(i, i + 1) = 1;
        A(i + 1, i) = 1;
    }

    for(int i = 0; i < 124; i++)
        A(i, i + 4) = 1;

    for(int i = 127; i > 3; i--)
        A(i, i - 4) = 1;


    for(int i = 0; i < 128; i++)
        e(i, 0) = 1;    

    x = gaussseidel(A, e, 128); 

    std::cout << x << std::endl;
}