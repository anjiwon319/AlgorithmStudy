#include <stdio.h>
#include <math.h>

int main()
{
    // default로 모든 숫자 +1 해야함 (오른쪽 경계 +1)

    while (1)
    {
        int n;
        scanf("%d", &n);

        if (n == 0)
            break;

        // 몇자리 수인지에 따라 반복 (각 숫자 차지하는 범위 + 경계(1))
        int sum = 1;
        int k = 1000;
        while (k)
        {
            int m;
            m = n / k;
            if (m == 0)
            {
                if (sum != 1)
                    sum += 5;
            }
            else if (m == 1)
                sum += 3;
            else
                sum += 4;

            n %= k;
            k /= 10;
        }
        printf("%d\n", sum);
    }

    return 0;
}