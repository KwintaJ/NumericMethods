//############################################//
//                                            //
//    Jan Kwinta                12.12.2022    //
//                                            //
//    Metody Numeryczne                       //
//                                            //
//    Zadanie 7.                              //
//                                            //
//############################################//

Rozwiązanie:

Wektor współczynników a jest równy:

     1
    -4
     0
 a = 4
    -2
     1
    -1
     1

Czyli wielomian interpolacyjny jest postaci:

x^7 - x^6 + x^5 - 2x^4 + 4x^3 - 4x + 1

______________________________________________________________

Do odzyskiwania współczynników z wzoru interpolacyjnego
Lagrange'a trzeba założyć, że żaden z węzłów interpolacji
nie jest zerem (slajd 25 wykład 7), dlatego nie możemy 
zastosować tej metody. Do obliczenia współczynników
rozwiązuję układ równań z macierzą Vandermonde'a
przy użyciu funkcji wbudowanych biblioteki Eigen.

Wzór Lagrange'a może posłużyć do rysowania wykresu 
wielomianu. W skrypcie w pythonie napisałem dwie 
funkcje: polynomial(x) zwracającą wartość wielomianu
wprost (korzystającą z obliczonych współczynników) oraz
lagrange(x), która korzysta ze wzoru interpolacyjnego
Lagrange'a. Wyrysowanie obydwu funkcji daje ten sam 
rezultat.

Wykres zapisany jest w grafice wykres.png
