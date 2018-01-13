#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_NUM 10000


int main(void)
{
    int caseCount=0;
    int *tmp;

    //원래 배열
    scanf("%d",&caseCount);
    tmp = (int*) malloc(sizeof(int)*caseCount);


    //카운팅 배열
    int countArr[MAX_NUM+1];
    memset(countArr,0,sizeof(countArr));


    //결과 배열
    int *resultArr;
    resultArr = (int*) malloc(sizeof(int)*caseCount);
    memset(resultArr,0,sizeof(resultArr));

    for (int i=0; i<caseCount; i++){
      scanf("%d",&tmp[i]);

      //counting
      countArr[tmp[i]]++;
    }

    //카운팅 배열 누적합 수정.
    for(int i=1; i<= MAX_NUM; i++){
        //if (countArr[i] != 0)
        countArr[i] += countArr[i-1];
    }


    //누적합 참조. 뒤에서 부터 배치
    for(int i=caseCount-1; i>=1; i--){
        resultArr[countArr[tmp[i]]] = tmp[i];
        countArr[tmp[i]]--;
    }


    for (int i=0; i<=caseCount; i++){
        if (resultArr[i] != 0 && resultArr[i] <= 10000)
            printf("%d\n", resultArr[i]);
    }


    free(tmp);
    free(resultArr);
    return 0;
}


