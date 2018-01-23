#include <stdio.h>
#include <stdlib.h>

/*
    첫 번째 줄에 학기의 수 T가 주어진다. 두 번째 줄부터 T개 학기에 대한 정보가 주어진다.
    각 학기에 대한 정보는 다음과 같이 구성되어 있다. 첫 번째 줄에 들었던 과목의 수 N이 주어지고, 다음 N개 줄에 걸쳐서 N개 과목들의 학점 C와 성적 G가 주어진다. (1 ≤ N ≤ 10, 1 ≤ C ≤ 6의 정수. G는 0과 x-0.3, x, x+0.3 (x=1, 2, 3, 4) 중 하나로 주어진다.)

    1. 자료형 **포인터이름 = malloc(sizeof(자료형 *) * 세로크기);와 같이 세로 공간 메모리 할당
    2. 반복문으로 반복하면서 포인터[i] = malloc(sizeof(자료형) * 가로크기);와 같이 가로 공간 메모리 할당
    3. 반복문으로 반복하면서 free(포인터[i]);와 같이 가로 공간 메모리 해제
    4. free(포인터);와 같이 세로 공간 메모리 해제
*/

int main(void){
    int T;
    scanf("%d", &T);

    //학기수, 과목수 담자.
    int *total;
    float *avg;
    total = (int*) calloc(T, sizeof(int));
    avg = (float*) calloc(T, sizeof(float));

    for(int test_case = 0; test_case < T; test_case++){
        int N = 0;
        scanf("%d", &N);

        int grade_t = 0;
        double score_t = 0;

        for(int i=0; i<N;i++){
            scanf("%d %lf", &grade_t, &score_t);
            total[test_case] += grade_t;
            avg[test_case] += (score_t*grade_t);
        }

        avg[test_case] /= total[test_case];

    }

    for(int i=0; i<T; i++){
        printf("%d %.1lf\n", total[i], avg[i]);
    }

    free(total);
    free(avg);

    return 0;
}
