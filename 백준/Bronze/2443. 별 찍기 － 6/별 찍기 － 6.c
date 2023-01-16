#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int start = 0;
    int mid = (2 * n - 1) / 2;
    int end = 2 * n - 2;

    while (start <= mid)
    {
        for (int i = 0; i < 2 * n - 1; i++)
        {
            if (i >= start && i <= end)
                printf("*");
            else if (i < start)
                printf(" ");
            else
                continue;
        }
        printf("\n");
        start++;
        end--;
    }

    return 0;
}