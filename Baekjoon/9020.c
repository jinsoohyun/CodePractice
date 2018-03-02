#include <stdio.h>
#include <stdlib.h>

#define MAX 5001
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
    int T, numA, flag, min, tmp;
    int resultm, resultn;
    scanf("%d",&T);


    for (int i=0;i<T;i++){
        min = 0;
        tmp = 0;
        scanf("%d",&numA);
        for (int n=2;n<=numA/2+1;n++){
            for (int m=2;m<=numA;m++){
                if (n>2 && n%2 ==0)
                    break;
                if (m>2 && m%2 ==0)
                    continue;

                if(n+m == numA && iptr[n] == 0 && iptr[m] == 0){
                    min = m-n;
                    //printf("min : %d\n",min);
                    if (min <= tmp){
                        resultm = m;
                        resultn = n;
                    }
                    tmp = min;
                }
            }
        }
        printf("%d %d\n",resultn,resultm);
    }

    return 0;
}
