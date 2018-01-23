#include <stdio.h>

/*
    평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

    이 아파트에 거주를 하려면 조건이 있는데, “a 층의 b 호에 살려면 자신의 아래(a-1)층에 1호부터 b 호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

    아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정 했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있나를 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층에 i호에는 i명이 산다.
*/

int main(void){
    int T;
    scanf("%d", &T);



    for(int k=0; k<T; k++){
        int n,k;
        scanf("%d %d",&n, &k);

        // init people
        int room[15][15] = {0};
        for (int i=1;i<15;i++) {
            room[0][i] = i+1;
            room[i][0] = 1;

        }


        for (int i=1; i<15; i++){
            for (int j=1; j<15; j++){
                room[i][j] = room[i-1][j] + room[i][j-1];
              //  printf("%6d",room[i][j]);
            }
            //printf("\n");
        }

        printf("%d\n",room[n][k-1]);

        //
        //printf("%d%02d\n", (N-1)%H+1, (N-1)/H+1);
    }

    return 0;
}
