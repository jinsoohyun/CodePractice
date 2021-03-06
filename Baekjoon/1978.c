#include <stdio.h>
#include <stdlib.h>

#define MAX 1001
int* iptr;

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

int main(void){

    makePrime();
    int T, i;
    int count = 0;
    int *tmp;
    scanf("%d", &T);
    tmp = (int*) malloc(sizeof(int)*T);

    for(i = 0; i < T; i++){
        int num = 0;
        scanf("%d",&num);
        if(iptr[num]==0)
            count += 1;

    }
    printf("%d\n",count);

    return 0;
}
