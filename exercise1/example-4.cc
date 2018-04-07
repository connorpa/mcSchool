#include "courselib.h"
#include <cmath>
#include <iostream>

using namespace std;

/*
   Testing Monte Carlo integration.
   We have a test function:  g0=1
   we calculate the integral \int_0^x\int_0^1dxdy

   We calculate the result and its error.

   The random number generator is RANLUX by M. Luescher.
   M. L�scher, A portable high-quality random number generator 
   for lattice field theory simulations, 
   Computer Physics Communications 79 (1994) 100  
*/

int main (int argc,char **argv)
{
    const int npoints = 10000000;
    // initialise random number generator: rlxd_init( luxory level, seed )
    rlxd_init(2,32767);

    int nhit = 0;

    for (int n1 = 0; n1 < npoints; ++n1) {

        // insert here the values for x,y and the rejection condition   

        double x = Rand();
        double y = Rand();

        if (y < x)    
            ++nhit;
        //                                  
    }

    double Int = double(nhit)/npoints;
    // the uncertainty is calcualted from a Binominal distribution
    double sigma2 = (1. - Int)/nhit ;
    double error = sqrt(sigma2)*Int ;

    cout<<" integral for  is: "<<Int<<"+/-"<< error<<endl;
    cout<<" true integral  is : 0.5 "<< endl;

    return EXIT_SUCCESS;
}

