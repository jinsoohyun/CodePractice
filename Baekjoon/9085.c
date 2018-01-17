#include <stdio.h>
#include <stdlib.h>

//Exercise 9085

int main(int argc, char * argv[]){
    int T, test_case;
    int *tmp;
    scanf("%d", &T);
    tmp = (int*) malloc(sizeof(int)*T);

    for(test_case = 0; test_case < T; test_case++){
        int caseCount=0;
        int Answer=0;
        scanf("%d",&caseCount);

        int num = 0;
        for (int i=0; i<caseCount; i++){
            scanf("%d",&num);
            Answer += num;
        }
        //printf("%d\n",Answer);
        tmp[test_case] = Answer;
    }

    for(test_case = 0; test_case < T; test_case++){
        printf("%d\n",tmp[test_case]);
    }

    return 0;
}
