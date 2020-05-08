"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of lowercase English letters and the characters ( and ). It is guaranteed that all parentheses in inputString form a regular bracket sequence.

Guaranteed constraints:
0 ≤ inputString.length ≤ 50.

[output] string

Return inputString, with all the characters that were in parentheses reversed.
"""

def reverseInParentheses(s):
    def reverse(list1):
        list1 = list1[::-1]
        for i in range(len(list1)):
            if list1[i] == '(':
                list1[i] = ')'
            elif list1[i] == ')':
                list1[i] = '('
        return list1
    s_list = list(s)
    cnt = 0
    start = 0
    end = 0
    i = 0
    while i < len(s_list):
        if s_list[i] == '(':
            pass
            if cnt == 0:
                cnt += 1
                start = i
            else:
                cnt += 1
        elif s_list[i] == ')':
            cnt -= 1
            if cnt == 0:
                end = i
                s_list = s_list[:start]+reverse(s_list[start+1:end])+s_list[end+1:]
        i += 1
    s = ''.join(s_list)
    if '(' in s_list:
        return reverseInParentheses(s)
    else:
        return s



