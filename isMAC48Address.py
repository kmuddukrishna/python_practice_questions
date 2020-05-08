"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
15 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString corresponds to MAC-48 address naming rules, false otherwise.
"""

def isMAC48Address(inputString):
    a = ['A','B','C','D','E','F']
    n = ['1','2','3','4','5','6','7','8','9','0']
    l = inputString.split("-")
    if len(l) != 6:
        return False
    else:
        for each in l:
            if len(each) != 2:
                return False
            else:
                for t in each:
                    if t not in a and t not in n:
                        return False
    return True