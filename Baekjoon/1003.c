#include <stdio.h>
#include <stdlib.h>
#define MAX 41

/*
    주어진 피보나치 함수를 가지고 진행할 경우, 시간 복잡도가 지수단위로 상승하게 되어 상당히 오래 걸리며, 시간 초과에 걸리게 된다. 이를 해결하기 위해서 동적 계획법을 사용해야하는데, 미리 각 피보나치 수 별로 값을 구해 메모리에 올려놓는 것이다.

    자세히 보면, 아래와 같은 결과 값을 가지는데 0이 나오는 카운트, 1이 나오는 카운트 자체가 피보나치 수열로 구성되어 있음을 알 수 있다.
    n = 0    n = 1    n = 2    n = 3   n = 4   ...

     1 0      0 1      1 1      1 2     2  3    ...

    따라서, 0 카운트, 1카운트의 피보나치 초기 값을 잡아주고 배열을 구해놓은 뒤, 진행하면 해결할 수 있다.
*/

int *iptr_zero;
int *iptr_one;

int Fibonacci_function(int num){
    int i = 2;

    iptr_zero[0] = 1;
    iptr_one[0] = 0;

    iptr_zero[1] = 0;
    iptr_one[1] = 1;

    while (i < num){

        iptr_zero[i] = iptr_zero[i-1]+iptr_zero[i-2];
        iptr_one[i] = iptr_one[i-1]+iptr_one[i-2];
        i++;
    }

    return 0;
}


int main(int argc, char* argv[]){

    iptr_zero = (int*)calloc(MAX, sizeof(int));
    iptr_one = (int*)calloc(MAX, sizeof(int));
    Fibonacci_function(MAX);

    int T, N;
    scanf("%d", &T);
    for(int k=0; k<T; k++){
        scanf("%d", &N);
    	printf("%d %d\n",iptr_zero[N], iptr_one[N]);
    }

    return 0;
}
