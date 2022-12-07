//############################################//
//                                            //
//    Jan Kwinta                05.12.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 2. Podpunkt b                   //
//                                            //
//############################################//

#include <iostream>
#include <vector>
#include <Eigen/Dense>

std::vector<int> nonZeroPositionsOfRow(int k)
{
    std::vector<int> pos;

    if((k - 4) >= 0)
        pos.push_back(k - 4);

    if((k - 1) >= 0)
        pos.push_back(k - 1);

    pos.push_back(k);

    if((k + 1) < 128)
        pos.push_back(k + 1);
    
    if((k + 4) < 128)
        pos.push_back(k + 4);

    return pos;
}

Eigen::VectorXd specificMultiplication(Eigen::MatrixXd A, Eigen::VectorXd v)
{
    Eigen::VectorXd w(128);

    for(int i = 0; i < 128; i++)
    {
        double sum = 0;

        std::vector<int> positions = nonZeroPositionsOfRow(i);
        for(int j : positions)
            sum += A(i, j) * v(j, 0);

        w(i, 0) = sum;
    }

    return w;
}

Eigen::VectorXd gradient(Eigen::MatrixXd A, Eigen::VectorXd e, int k)
{
    Eigen::VectorXd x(128);
    for(int i = 0; i < 128; i++)
        x(i, 0) = 1;  

    Eigen::VectorXd r = e - specificMultiplication(A, x);
    Eigen::VectorXd p = r;

    for(int k = 0; k < 128; k++)
    {
        double aM = p.dot(specificMultiplication(A, p));
        double alpha;
        if(aM == 0)
            alpha = 0;
        else
            alpha = (r.dot(r)) / (aM);

        Eigen::VectorXd xkp1 = x + alpha * p;

        // std::cout << k << "-th iteration norm = "  << (xkp1 - x).norm() << std::endl;

        x = xkp1;

        Eigen::VectorXd rkp1 = r - alpha * specificMultiplication(A, p);
        if(rkp1.norm() < 1e-18)
            return x;

        double bM = r.dot(r);
        double beta; 
        if(bM == 0)
            beta = 0;
        else
            beta = (rkp1.dot(rkp1)) / (bM);

        Eigen::VectorXd pkp1 = rkp1 + beta * p;    

        p = pkp1;
        r = rkp1;
    }

    return x;
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

    x = gradient(A, e, 128); 

    std::cout << x << std::endl;
}    