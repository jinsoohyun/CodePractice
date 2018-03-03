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

void gbPartition(int n){
    int i,j,mid = n/2;
    for(i=j=mid; i<=n; i--, j++)
        if (iptr[i] == 0 && iptr[j] == 0){
            printf("%d %d\n",i,j);
            return;
        }

}

int main(int argc, char *argv[]){
    //generate prime
    makePrime();
    int T, numA;
    scanf("%d",&T);

    for (int i=0;i<T;i++){
        scanf("%d",&numA);
        gbPartition(numA);
    }

    return 0;
}
