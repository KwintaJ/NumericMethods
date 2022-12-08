//############################################//
//                                            //
//    Jan Kwinta                12.12.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 7. Macierz Vandermonde'a        //
//                                            //
//############################################//

#include <iostream>
#include <Eigen/Dense>

int main(int argc, char **argv)
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);

    Eigen::MatrixXd X(8, 8); // macierz Vandermonde'a
    Eigen::VectorXd a(8); // wektor wspolczynnikow

    /* wartosci w wezlach */
    Eigen::VectorXd f{{
    	1.13092041015625,
    	2.3203125,
    	1.92840576171875,
    	1,
    	0.05548095703125,
    	-0.6015625,
    	-0.75250244140625,
    	0
    }};

    /* wezly */
    Eigen::VectorXd points{{
    	-0.75,
    	-0.5,
    	-0.25,
    	0,
    	0.25,
    	0.5,
    	0.75,
    	1
    }};

    /* uzupelnienie macierzy Vandermonde'a */
    for(int i = 0; i < 8; i++)
    {
    	for(int j = 0; j < 8; j++)
    	{
    		if(j == 0)
    			X(i, j) = 1;
    		else
    			X(i, j) = X(i, j - 1) * points[i];
    	}
    }    

    /* rozwiazanie ukladu */
    a = X.partialPivLu().solve(f);

    std::cout << a << std::endl;
}    