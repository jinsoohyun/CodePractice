#include <stdio.h>
#include <math.h>

int Answer;

/*
    360 도 atan2 로 표현하기 -> https://stackoverflow.com/questions/1311049/how-to-map-atan2-to-degrees-0-360
    radian, degree 표기 방식 때문에 상당히 삽질했다...
    score 를 배열로 만들어 두고, radian 에서 degree 로 변환한 값을 총 20개의 점수 즉, 360/20 = 18 이다. 각 점수당
    18' 씩 영역을 가지는데, 자세히 보면 0'에 시작 점수 6이 딱 맞게 배치된게 아니라 중간에 걸쳐져 있다. 10'에 다트가 맞은 경우 10/18을 하였을 때,
    몫이 0이 된다.
    때문에 degree에 +9를 하고 18로 나눠줘야 한다. 즉 9' 만큼의 영역을 0'에서 부터 가지는데 이를 처리하기 위해서 구한 degree 에 9'를 + 해야한다.

    >> resultScore 초기화 안해줘서 통과했는데 5점 받는 사태 발생 ;;; 한참 디버깅하다가 발견해서 고치니 100점 통과.
*/

//좌표 담을 구조체
struct Point2D {
    int x;
    int y;
};


int main(void)
{
    int T, test_case;
    setbuf(stdout, NULL);

    //테스트 케이스 갯수 입력
    scanf("%d", &T);
    for(test_case = 0; test_case < T; test_case++)
    {
        unsigned int Answer=0;
        int dartCount = 0;
        int defaultScore, resultScore;
        int bullRadian, tripleRadinanStart, tripleRadinanEnd, doubleRadianStart, doubleRadianEnd;

        //score list
        int score[] = {6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10};

        //반지름 입력
        scanf("%d %d %d %d %d",&bullRadian, &tripleRadinanStart, &tripleRadinanEnd, &doubleRadianStart, &doubleRadianEnd);

        //다트 갯수 입력
        scanf("%d",&dartCount);
        struct Point2D p[dartCount-1];

        //좌표 입력
        for (int i=0; i<dartCount; i++){
          scanf("%d %d",&p[i].x, &p[i].y);
        }

        //bull, triple, double, out, single 구간 확인
        for (int i=0; i<dartCount; i++){

            double dist = p[i].x*p[i].x + p[i].y*p[i].y;
            double degrees = atan2(p[i].y,p[i].x);
            degrees = degrees*(double)180/3.1415 +9;
            if(degrees<0)
                degrees = degrees+360;

            if (dist <= bullRadian*bullRadian)
                resultScore += 50;

            else{
                defaultScore = score[(int)degrees/18];
                if(dist>bullRadian*bullRadian && dist <tripleRadinanStart*tripleRadinanStart){
                    resultScore += defaultScore;
                }else if(dist>tripleRadinanStart*tripleRadinanStart && dist<tripleRadinanEnd*tripleRadinanEnd){
                    resultScore += defaultScore*3;
                }else if(dist>tripleRadinanEnd*tripleRadinanEnd && dist<doubleRadianStart*doubleRadianStart){
                    resultScore += defaultScore;
                }else if(dist>doubleRadianStart*doubleRadianStart && dist<doubleRadianEnd*doubleRadianEnd){
                    resultScore += defaultScore*2;
                }
            }
        }

        // Print the answer to standard output(screen).
        printf("Case #%d\n", test_case+1);
        printf("%d\n", resultScore);
        resultScore = 0;

    }

    // Your program should return 0 on normal termination.
    return 0;
}
