#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 2000000
#define MOD 1000000007
unsigned long factorial[MAX_SIZE];

int main(int argc, char *argv[]){
    int T, test_case;
    setbuf(stdout, NULL);

    //테스트 케이스 갯수 입력
    scanf("%d", &T);


    int i=0;
    factorial[0] = 1;
    for (i = 1; i < MAX_SIZE; i++){
        factorial[i] = (factorial[i-1]*i)%MOD;
    }


    for(test_case = 0; test_case < T; test_case++)
    {
        int n,m;
        int tmp = 0;
        scanf("%d %d",&n,&m);

        printf("Case #%d\n", test_case+1);
        printf("%lu %lu %lu\n",factorial[n+m+2], factorial[n+1], factorial[m+1]);
        printf("%lu\n",factorial[n+m+2]/(factorial[n+1]*factorial[m+1])-1);
    }

    return 0;
}
