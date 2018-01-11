//memory overflow 다시
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


    /*
    산술평균 : N개의 수들의 합을 N으로 나눈 값
    중 앙 값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    최 빈 값 : N개의 수들 중 가장 많이 나타나는 값:
    범    위 : N개의 수들 중 최대값과 최소값의 차이
    */

    //산술평균 : N개의 수들의 합을 N으로 나눈 값
    //첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    int sum = 0;
    for (int i=0; i<caseCount; i++){
      sum += tmp[i];
    }
    int avg = (float)sum/caseCount+0.5;



    //중 앙 값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
    // qsort
    qsort(tmp, caseCount, sizeof(int), compare);
    int middleVlaue = tmp[(caseCount-1)/2];


    //최 빈 값 : N개의 수들 중 가장 많이 나타나는 값:
    //셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    int *frequence;
    frequence = (int*) calloc(caseCount,sizeof(int)*(caseCount));
    for (int i=0; i<caseCount; i++){
        frequence[i] = -1;
    }

    int count;
    for(int i=0; i<caseCount; i++){
        count = 1;
        for(int j=i+1; j<caseCount; j++){
            /* If duplicate element is found */
            if (tmp[i]==tmp[j]){
                count++;

                /* Make sure not to count frequency of same element again */
                frequence[j] = 0;
            }
        }

        /* If frequency of current element is not counted */
        if(frequence[i] != 0){
            frequence[i] = count;
        }
    }

    // 최대 빈도 값 구하기
    int temp = 0;
    int max = frequence[0];
    for (int i=0; i<caseCount; i++){
      temp = frequence[i];
      if (temp > max)
        max = temp;
    }

    //최대 빈도에 해당하는 수 원본 배열에서 찾기
    //두번째로 작은 수 구하기


    int cnt = 0;
    int maxFrequence = 0;

    for(int i=0; i<caseCount; i++){
        if(frequence[i] != 0 && frequence[i] == max){
            cnt ++;
            //findNum[i] = tmp[i];
            //printf("%d occurs %d times\n", tmp[i], frequence[i]);
        }
    }

    int *findNum;
    findNum = (int*) calloc(cnt,sizeof(int)*(cnt));

    cnt = 0;
    for(int i=0; i<caseCount; i++){
        if(frequence[i] != 0 && frequence[i] == max){
            findNum[cnt] = tmp[i];
            cnt ++;
        }
    }
    free(frequence);

    qsort(findNum, cnt, sizeof(int), compare);
    if(cnt == 1) maxFrequence = findNum[0];
    else maxFrequence = findNum[1];
    free(findNum);

    //범    위 : N개의 수들 중 최대값과 최소값의 차이
    int minValue = tmp[caseCount-1] - tmp[0];


    //result
    printf("%d\n",avg);
    printf("%d\n",middleVlaue);
    printf("%d\n",maxFrequence);
    printf("%d\n",minValue);


    free(tmp);


    return 0;
}

// 정렬 비교
int compare (const void *first, const void *second){
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}
