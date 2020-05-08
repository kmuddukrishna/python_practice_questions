"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def isLucky(n):
    s = str(n)
    ln = len(s) / 2
    m = 10**ln
    s1 = str(int(n // m))
    s2 = str(int(n % m))
    s1l = 0
    s2l = 0
    for each in s1:
        s1l = s1l + int(each)
    for each in s2:
        s2l = s2l + int(each)
    return True if s1l == s2l else False