#include <stdio.h>
#include <stdlib.h>

int Answer;
int compare (const void *first, const void *second);

/*
    N개의 과목에 대해서 최대 K개의 과목만 공부할 수 있고, 해당 과목에 대해서는 항상 동일한 점수를 획득한다.
    공부할 수 있는 K개의 과목에 대해서 얻을 수 있는 최대 합계 점수를 구하기 위해서는 N 개 과목의 점수에 대해
    정렬을 하고, 가장 높은 K개의 과목 점수를 합산하는 방식으로 해결할 수 있다.
*/
int main(void)
{
    int T, test_case;
    setbuf(stdout, NULL);
    scanf("%d", &T);
    for(test_case = 0; test_case < T; test_case++)
    {
        int testCourse=0;
        int studyCourse=0;
        int *tmp;
        unsigned int Answer=0;

        scanf("%d %d",&testCourse, &studyCourse);
        tmp = (int*) malloc(sizeof(int)*testCourse);

        for (int i=0; i<testCourse; i++){
          scanf("%d",&tmp[i]);
        }

        // 내림차순 qsort
        qsort(tmp, testCourse, sizeof(int), compare);

        // result
        for (int i=0; i<studyCourse; i++){
            Answer += tmp[i];
        }


        // Print the answer to standard output(screen).
        printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
        free(tmp);

    }

    // Your program should return 0 on normal termination.
    return 0;
}

// 정렬 비교
int compare (const void *first, const void *second)
{
    if (*(int*)first < *(int*)second)
        return 1;
    else if (*(int*)first > *(int*)second)
        return -1;
    else
        return 0;
}
