#include <stdio.h>
#include <string.h>
#define MAX_NUM 10000

/*
메모리가 8mb 로 제한되기 때문에, before code 처럼 malloc 을 이용해 input array, count array, result array 등을
할당하여 계산할 수 없다. 이를 해결하려면 할당하는 배열을 줄여야 하는데 문제에서 최대 N 의 수는 10,000을 넘지 않는 자연수로 정해져 있기 때문에
count array 하나만 선언하여, counting sort 를 진행할 수 있다.
*/
int main(void)
{
    //케이스 카운트
    int caseCount=0;
    scanf("%d",&caseCount);

    //카운팅 배열
    int countArr[MAX_NUM+1];
    memset(countArr,0,sizeof(countArr));

    int tmp = 0;

    //input & counting
    for (int i=0; i<caseCount; i++){
      scanf("%d",&tmp);
      countArr[tmp]++;
    }

    //result print
    for(int i=0; i<=MAX_NUM;i++){
        for (int j=0; j<countArr[i];j++){
            if (countArr[i] != 0){
                printf("%d\n", i);
            }
        }
    }

    return 0;
}
