#include <stdio.h>

int main()
{
    int idx = 1;
    while (1)
    {
        int n, nasty = 0;
        scanf("%d", &n);

        if (n == 0)
            break;

        char names[n][61]; // 이름 60글자 이하
        int msg[n][n - 1];
        for (int i = 0; i < n; i++)
        {
            scanf("%s", names[i]);
            for (int j = 0; j < (n - 1); j++)
            {
                msg[i][j] = -1;
                char m;
                scanf(" %c", &m);
                if (m == 'N')
                {
                    msg[i][j] = (i - (j + 1)) < 0 ? (n + (i - (j + 1))) : (i - (j + 1));
                }
            }
        }

        printf("Group %d\n", idx);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < (n - 1); j++)
            {
                if (msg[i][j] > -1)
                {
                    nasty++;
                    printf("%s was nasty about %s\n", names[msg[i][j]], names[i]);
                }
            }
        }
        if (!nasty)
        {
            printf("Nobody was nasty\n");
        }
        printf("\n");
        idx++;
    }
    return 0;
}