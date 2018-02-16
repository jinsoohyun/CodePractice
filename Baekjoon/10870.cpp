#include <stdio.h>
#include <stdlib.h>

static int *Fibonacci_array = 0;
static int tmp_malloc_size = 0;

int Fibonacci_function(int num)
{
    int num_tmp = num;
    int result =1;
    int cnt = 1;
    int tmp = 1;
    int i = 1;

    //Calc Fibornacci
    Fibonacci_array = (int*)malloc(sizeof(int)*num_tmp);

    Fibonacci_array[0] = 0;
    Fibonacci_array[1] = 1;

    if (num == 0){
        tmp_malloc_size = 1;
        return 0;
    }

    else if (num == 1){
        tmp_malloc_size = 2;
        return 0;
    }


    while (i < num){
       // printf("%d ",result);
        Fibonacci_array[i] = result;
        i++;

        tmp = result;
        result += cnt;
        cnt = tmp;
    }

    //set malloc size
    tmp_malloc_size = i;
    return 0;
}



int main(int argc, char *argv[]){

    int T;
    scanf("%d", &T);
    Fibonacci_function(T);

    Fibonacci_array[0] = 0;
    Fibonacci_array[1] = 1;
    printf("%d\n", Fibonacci_array[tmp_malloc_size-1]);


    //    for (int j=0;j< tmp_malloc_size;j++){
    //        printf("%d,", Fibonacci_array[j]);
    //    }

    //malloc free
    free(Fibonacci_array);
    return 0;
}
