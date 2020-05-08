"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""

def commonCharacterCount(s1, s2):
    d1 = {}
    d2 = {}
    for each in s1:
        if each in d1:
            d1[each] += 1
        else:
            d1[each] = 1
    for each in s2:
        if each in d2:
            d2[each] += 1
        else:
            d2[each] = 1
    f = 0
    for each in d1:
        if each in d2:
            f = f + min(d1[each], d2[each])
        else:
            pass
    return f

