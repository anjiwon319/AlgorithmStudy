// 2445 - 별찍기 8

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int start = 1, end = 2 * n - 2;
    while (start < n)
    {
        for (int i = 0; i < 2 * n; i++)
        {
            if (i >= start && i <= end)
                printf(" ");
            else
                printf("*");
        }
        printf("\n");
        start++;
        end--;
    }
    while (start > 0)
    {
        for (int i = 0; i < 2 * n; i++)
        {
            if (i >= start && i <= end)
                printf(" ");
            else
                printf("*");
        }
        printf("\n");
        start--;
        end++;

    }
    return 0;
}