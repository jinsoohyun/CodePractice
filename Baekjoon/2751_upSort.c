#include <stdio.h>
#include <stdlib.h>

int compare (const void *first, const void *second);

int main(void)
{
    int caseCount=0;
    int *tmp;

    scanf("%d",&caseCount);
    tmp = (int*) malloc(sizeof(int)*caseCount);

    for (int i=0; i<caseCount; i++){
      scanf("%d",&tmp[i]);
    }

    // qsort
    qsort(tmp, caseCount, sizeof(int), compare);

    for (int i=0; i<caseCount; i++){
      printf("%d\n",tmp[i]);
    }
    free(tmp);
    return 0;
}

// 정렬 비교
int compare (const void *first, const void *second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}
