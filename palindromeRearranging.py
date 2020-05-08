"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

def palindromeRearranging(inputString):
    dic = {}
    f=0
    for each in inputString:
        if each in dic:
            dic[each]+=1
        else:
            dic[each]=1
    for each in dic:
        if dic[each]%2!=0:
            f=f+1
    if f>1:
        return False
    else:
        return True



