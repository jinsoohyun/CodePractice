#include <stdio.h>
#include <stdlib.h>

/*
    각각의 케이스마다 한 줄에 연세대가 이겼을 경우 "Yonsei", 고려대가 이겼을 경우 "Korea", 비겼을 경우 "Draw"를 출력한다.
*/

int main(void){
    int T;
    scanf("%d", &T);

    for(int k=0; k<T; k++){
        int yonsei=0;
        int korea=0;

        for(int i=0; i<9; i++){
            int tmp1,tmp2;
            scanf("%d %d",&tmp1, &tmp2);
            yonsei += tmp1;
            korea += tmp2;
        }

        if(yonsei>korea)
            printf("Yonsei\n");
        else if(korea>yonsei)
            printf("Korea\n");
        else
            printf("Draw\n");
    }

    return 0;
}
