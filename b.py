# import math as m
# n = int(input())
# fact = list(str(m.factorial(n)))
# print(sum(list(map(int, fact))))



'''
void main()
{
    int sum = 0, i, len;
    char string1[100];
 
    printf("Enter the string : ");
    scanf("%[^\n]s", string1);
        len = strlen(string1);
    for (i = 0; i < len; i++)
    {
        sum = sum + string1[i];
    }
    printf("\nSum of all characters : %d ",sum);
}
'''

str = "HELLO AND (WELCOME(TO THE) WORLD (CONTEST)TODAY) IS (SATARDAY())"
o = "("
l = ")"

str.count(o)
str.count(l)

if str.count(o) == str.count(l):
    print(0)
else:
    print(1)