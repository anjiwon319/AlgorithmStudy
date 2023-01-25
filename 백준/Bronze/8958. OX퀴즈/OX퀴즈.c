#include <stdio.h>
#include <string.h>

int main()
{
    int testCaseNum;
    scanf("%d", &testCaseNum);

    while (testCaseNum--)
    {
        int sum = 0, point = 1;
        char answer[80];
        scanf("%s", answer);

        for(int i = 0; i < strlen(answer); i++){
            if(answer[i] == 'O'){
                sum += point;
                point++;
            }
            else
                point = 1;
            
        }

        printf("%d\n", sum);
        
    }
    return 0;
}