#include <stdio.h>

int Sosu(int num)
{
    int i = 0;
    for (int i = 2; i<=num/2 ;i++ )
    {
        if (num%i ==0)
        {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    int cnt = 2;
    int i = 0;

    while (1)
    {
        i += Sosu(cnt);

        if (i == 10001)
        {
            printf("[+] %d\n",cnt);
            return 0;
        }
        cnt += 1;
    }


    return 0;
}
