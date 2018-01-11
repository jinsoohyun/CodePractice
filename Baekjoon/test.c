//2108 C test
#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
    int N, center, bool_center = 0, bool_common = 0, common = 0,
    max = -4000, min = 4000, count[8001]; //0~8000 -4000~4000
    float avr = 0;

    memset(count, 0, sizeof(count));
    scanf("%d", &N);

    for (int i = 0, j; i < N; ++i){
        scanf("%d", &j);
        avr += (float)j;
        ++count[j + 4000];
        max = (j > max) ? j : max;
        min = (j < min) ? j : min;
    }

    avr /= (float)N;
    if (avr < 0)
        avr = ceil(avr - 0.5); // 올림함수
    else
        avr = floor(avr + 0.5); // 내림함수

    center = count[0];
    for (int i = 1; i < 8001; ++i){
        if (!bool_center){
            if (center > N / 2){
                bool_center = 1;
                center = i - 4001;
            }

            else
                center += count[i];
        }

        if (count[i] > count[common]){
            bool_common = 0;
            common = i;
        }

        else if (count[i] == count[common])

        if (!bool_common){
            bool_common = 1;
            common = i;
        }
    }

    common -= 4000;
    printf("%d\n%d\n%d\n%d", (int)avr, center, common, (max - min));
}
