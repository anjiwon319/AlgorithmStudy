// 2675 - 문자열 반복
#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        int num;
        scanf("%d", &num);

        char word[20];
        scanf("%s", word);
        for (int j = 0; j < strlen(word); j++)
        {
            for (int k = 0; k < num; k++)
                printf("%c", word[j]);
        }
        printf("\n");
    }

    return 0;
}