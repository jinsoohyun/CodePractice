#include <stdio.h>
#include <stdlib.h>

//Exercise 10950

int main(int argc, char * argv[]){
    int T, test_case;
    int *tmp;
    scanf("%d", &T);
    tmp = (int*) malloc(sizeof(int)*T);

    for(test_case = 0; test_case < T; test_case++){
        int Answer=0;
        int num1 = 0;
        int num2 = 0;

        scanf("%d %d",&num1, &num2);
        tmp[test_case] = num1+num2;
    }

    for(test_case = 0; test_case < T; test_case++){
        printf("%d\n",tmp[test_case]);
    }

    return 0;
}
