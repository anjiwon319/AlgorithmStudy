#include <stdio.h>
#include <string.h>
#define MAX_SIZE 51

char stack[MAX_SIZE];
int topIdx = -1;

int isEmpty()
{
    if (topIdx == -1)
        return 1;
    else
        return 0;
}

void push(char x)
{
    stack[++topIdx] = x;
}

char pop()
{
    if (!isEmpty())
    {
        return stack[topIdx--];
    }
}

int main()
{
    int numTestCases;
    scanf("%d", &numTestCases);
    while (numTestCases--)
    {
        topIdx = -1;
        char ps[MAX_SIZE];
        scanf("%s", ps);

        int psLen = strlen(ps);
        for (int i = 0; i < psLen; i++)
        {
            if (ps[i] == '(')
                push(ps[i]);
            else
            {
                if (isEmpty())
                    push(ps[i]);
                else
                {
                    if (stack[topIdx] != ps[i])
                        pop();
                }
            }
        }
        if (isEmpty())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}