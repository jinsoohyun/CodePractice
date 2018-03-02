#include <stdio.h>
#include <stdlib.h>

#define MAX 1000001
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
    makePrime();

    int numA, numB;
    int result = 0;

    scanf("%d %d",&numA, &numB);

    //iptr[x] == 0 is Prime
    for (;numA <= numB;numA++){
        if (iptr[numA] == 0){
            printf("%d\n",numA);
        }
    }

    return 0;
}
