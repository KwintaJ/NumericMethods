//############################################//
//                                            //
//    Jan Kwinta                28.11.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 1.                              //
//                                            //
//############################################//


(a)

Rozwiązanie:

          0.2281
        0.315699
        0.509103
   x =  0.647887
        0.899347
        0.754723
         2.08176



(b)

Rozwiązanie:

       -0.260163
        0.447154
        0.471545
   x =  0.666667
        0.861789
        0.886179
          1.5935


Uzasadnienie wyboru metody:

Dla macierzy rzadkich algorytm faktoryzacji LU działa 
w czasie liniowym. Zarówno w podpunkcie (a) jak i (b)
występowały macierze rzadkie, dlatego obydwa układy
można było rozwiązać metodą rozkładu LU. 

Potrzebne do tego funkcje biblioteki Eigen są dostępne
w plikach nagłówkowych Eigen/SparseCore (stworzenie i
wypełnienie macierzy rzadkiej) oraz Eigen/SparseLU
(faktoryzacja oraz rozwiązanie układu).