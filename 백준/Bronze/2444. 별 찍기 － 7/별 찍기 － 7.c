// 별찍기 7 - 2444

#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int start = (2 * n - 1) / 2, end = (2 * n - 1) / 2;
    while (start > 0)
    {
        for (int i = 0; i < 2 * n - 1; i++)
        {
            if (i >= start && i <= end)
                printf("*");
            else if (i > end)
                break;
            else
                printf(" ");
        }
        start--;
        end++;
        printf("\n");
    }
    while (start <= (2 * n - 1) / 2)
    {
        for (int i = 0; i < 2 * n - 1; i++)
        {
            if (i >= start && i <= end)
                printf("*");
            else if (i > end)
                break;
            else
                printf(" ");
        }
        start++;
        end--;
        printf("\n");
    }
    return 0;
}