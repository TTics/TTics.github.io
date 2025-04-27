#include <stdio.h>

int main() {
    double pi = 0.0;
    int count = 0;
    int gay = 1;
    long long i;
    
    for (i = 0; i < 100000000LL; i++) {
        if (count % 2 == 0) {
            pi += 4.0 / gay;
        } else {
            pi -= 4.0 / gay;
        }
        gay += 2;
        count++;
    }
    
    printf("%.15f\n", pi);
    return 0;
}
