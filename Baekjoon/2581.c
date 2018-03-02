#include <stdio.h>
#include <stdlib.h>

#define MAX 10001
int* iptr;

//generate prime abot MAX range
void makePrime(){

    int i, j;

    iptr = (int*)calloc(MAX, sizeof(int));
    iptr[0] = 1;
    iptr[1] = 1;

    for (i = 2; i < MAX; i++){
        if (iptr[i] == 1)
            continue;
        j = i;
        while ((j += i) <= MAX){
            iptr[j] = 1;
        }
    }
}

int main(int argc, char *argv[]){
    //make 10000 prime
    makePrime();

    int numA, numB;
    int result = 0;
    int minPrime = 0;

    scanf("%d %d",&numA, &numB);

    //iptr[x] == 0 is Prime
    for (;numA <= numB;numA++){
        //min prime
        if (minPrime == 0 && iptr[numA] == 0){
            minPrime = numA;
            result += numA;
        }

        else if (iptr[numA] == 0){
            result += numA;
        }

    }
    if (result == 0)
        printf("-1\n");
    else
        printf("%d %d\n",result, minPrime);
    return 0;
}
