#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금, 세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에, 그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서, 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최소값을 구하는 프로그램을 작성하라.


>> 주어지는 y-x 가 이동해야할 총 거리 dist 이다.
>> 총 거리를 하나씩 증가시키며, 이동할 최소 횟수를 구해보면 아래와 같은 규칙이 나온다.
    >> 최소 이동 횟수 : N
    >> 이동 거리 : dist
        >> N**2을 기준으로
            좌측은 : [N**2-N+1, N**2]
            우측은 : [N**2+1, N**2+N]
            의 범위를 가지는 것을 알 수 있다.

        >> cnt 값을 초기 이동 횟수인 1로 두고 해당 이동횟수를 증가시키면서 주어진 거리가 해당 좌.우측 범위 내에 속하는지를 구분함으로써, 최소 이동횟수를 구할 수 있다.
            >> N 이 속하는 범위를 구할 수 있다면, 좌측에 위치하는 이동횟수는 N*2-1, 우측은 N*2 의 최소 이동횟수를 가진다.


*/


int Answer;
int main(void){
    int T, test_case;
    scanf("%d", &T);

    int *answer;
    answer = (int*) malloc(sizeof(int)*T);

    int move[3] = {-1,0,1};

    for(test_case = 0; test_case < T; test_case++)
    {
        int x,y,dist;
        scanf("%d %d",&x, &y);

        dist = y-x;
        int cnt = 1;
        int moveCount = 1;

        while (1){
            // left
            if (pow(cnt,2)-cnt+1 <= dist  && dist <= pow(cnt,2)){
                Answer = cnt*2-1;
                break;
            }

            //right
            else if ( pow(cnt,2)+1 <= dist && dist <= pow(cnt,2)+cnt){
                Answer = cnt*2;
                break;
            }

            else
                cnt ++;
        }
        answer[test_case] = Answer;
    }

    for(int i = 0; i < T; i++)
        printf("%d\n",answer[i]);

    return 0;
}
