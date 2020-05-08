"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string
"""

def longestDigitsPrefix(inputString):
    f = ""
    for each in inputString:
        if each.isdigit():
            f = f + each
        else:
            break
    return f