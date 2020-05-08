"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array of strings of lowercase letters.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 15.

[output] boolean

Return true if the strings can be reordered in such a way that each neighbouring pair of strings differ by exactly one character (false otherwise).
"""

def inserted(str1, config_array):
    new_config = []
    for element in config_array:
        for i in range(0,len(element)+1):
            tmp = []
            tmp = element*1
            tmp.insert(i, str1)
            new_config.append(tmp)
    return new_config
        
def buildConfigurationArray(inputArray):
    config_array = []
    config_array.append([inputArray.pop()])
    return factorial(inputArray, config_array)

def factorial(inputArray, config_array):
    if len(inputArray) ==0:
        return config_array
    else:
        str1=inputArray.pop()
        config_array = inserted(str1, config_array)
        return factorial(inputArray, config_array)      

def check_difference(str1, str2):
    letters_different =0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            letters_different +=1
    return letters_different

def check_arrangement(inputArray):
    for i in range(0, len(inputArray)):
        if i == len(inputArray)-1:
            break
        letters_different = check_difference(inputArray[i], inputArray[i+1])
        if letters_different != 1:
            return False
    return True

def stringsRearrangement(inputArray):
    config_array = buildConfigurationArray(inputArray)
    num_of_configurations = len(config_array)
    checked_configurations = 0
    while checked_configurations != num_of_configurations:
        inputArray = config_array[checked_configurations]
        if check_arrangement(inputArray):
            return True
        checked_configurations +=1
    return False
