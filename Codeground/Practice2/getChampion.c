#include <stdio.h>
#include <stdlib.h>

int Answer;
int compare (const void *first, const void *second);

int main(void)
{
    int T, test_case;
    setbuf(stdout, NULL);

    scanf("%d", &T);
    for(test_case = 0; test_case < T; test_case++)
    {
        int caseCount=0;
        int *tmp;
        unsigned int Answer=0;

        scanf("%d",&caseCount);
        tmp = (int*) malloc(sizeof(int)*caseCount);

        for (int i=0; i<caseCount; i++){
          scanf("%d",&tmp[i]);
        }

        // 내림차순 qsort
        qsort(tmp, caseCount, sizeof(int), compare);

        // 최댓값 구하기
        int temp = 0;
        int max = tmp[0];
        for (int i=0; i<caseCount; i++){
          temp = tmp[i] + (i+1);
          if (temp > max)
            max = temp;
        }

        // n 번째 인원 최고점 받는 경우 카운트
        for (int i=0; i<caseCount; i++){
          temp = tmp[i] + caseCount;
          if (temp >= max)
            Answer += 1;
        }

        // Print the answer to standard output(screen).
        printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
        free(tmp);

    }

    return 0;//Your program should return 0 on normal termination.
}

//내림차순 정렬 비교
int compare (const void *first, const void *second)
{
    if (*(int*)first < *(int*)second)
        return 1;
    else if (*(int*)first > *(int*)second)
        return -1;
    else
        return 0;
}
