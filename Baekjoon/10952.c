#include <stdio.h>
#include <stdlib.h>

//Exercise 10952

int main(int argc, char * argv[]){
    int T, test_case;
    //int *tmp;
    //tmp = (int*) malloc(sizeof(int)*T);
    int num1 = 1;
    int num2 = 1;

    while (num1 != 0 && num2 != 0){
        scanf("%d %d",&num1, &num2);
        if (num1 == 0 && num2 == 0)
            exit(0);
        printf("%d\n",num1+num2);
    }


    return 0;
}
