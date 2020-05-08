"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
10 ≤ n ≤ 106.

[output] integer
"""

def deleteDigit(n):
    long = len(list(str(n)))

    max = 0
    for i in range(long):
        lista = list(str(n))
        del lista[i]
        num = int(''.join(lista))
        if num > max:
            max = num
    
    return max
    