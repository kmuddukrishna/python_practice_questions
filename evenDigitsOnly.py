"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 109.

[output] boolean

true if all digits of n are even, false otherwise.
"""

def evenDigitsOnly(n):
    f=0
    while n!=0:
        if n%2!=0:
            f=f+1
            break
        n=n//10
    return False if f!=0 else True