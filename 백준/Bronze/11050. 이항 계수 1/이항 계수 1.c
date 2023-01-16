// 11050 이항계수 nCm
#include <stdio.h>

int binCoefficient(int n, int k)
{
    if (n == 1 || k == 0 || n == k)
        return 1;

    return binCoefficient(n - 1, k - 1) + binCoefficient(n - 1, k);
}

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);

    printf("%d", binCoefficient(n, k));

    return 0;
}