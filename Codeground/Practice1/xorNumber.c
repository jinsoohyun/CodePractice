#include <stdio.h>

int main(void)
{
    int T, test_case;

    setbuf(stdout, NULL);
    scanf("%d", &T);
    for(test_case = 0; test_case < T; test_case++)
    {
        int caseCount=0;
        unsigned int tmp=0;
        unsigned int Answer=0;

        scanf("%d",&caseCount);
        for (int i=0; i<caseCount; i++){
          scanf("%d",&tmp);
          Answer ^= tmp;
        }

        printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
    }

    return 0;//Your program should return 0 on normal termination.
}
