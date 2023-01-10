#include <stdio.h>

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    int count = 0;

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            count++;
            if (count == k)
            {
                printf("%d", i);
                break;
            }
        }
    }
    if (count < k)
        printf("0");
}