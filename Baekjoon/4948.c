#include <stdio.h>
#include <stdlib.h>

#define MAX 123456*2+1
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
    int numA = 1;
    int cnt;


    while(1){
        cnt = 0;
        scanf("%d",&numA);
        if (numA == 0)
            exit(0);

        for (int i = numA+1; i <= numA*2;i++){
            if (iptr[i] == 0){
                cnt ++;
            }
        }
        printf("%d\n",cnt);
    }

    return 0;
}
