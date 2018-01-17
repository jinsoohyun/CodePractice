#include <stdio.h>

//Exercise 1547

int main(int argc, char * argv[]){
    int ball[3] = {1,2,3};
    int T, test_case;
    scanf("%d", &T);

    int tmp, swap1, swap2;
    for(test_case = 0; test_case < T; test_case++){
        scanf("%d %d",&swap1, &swap2);
        swap1--;
        swap2--;
        tmp = ball[swap1];
        ball[swap1] = ball[swap2];
        ball[swap2] = tmp;

    }

    for (int i=0;i<3;i++){
        if (ball[i] == 1)
            printf("%d\n",i+1);
        continue;
    }

    return 0;
}
