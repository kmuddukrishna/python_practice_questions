"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""

def almostIncreasingSequence(sequence):
    c0,c1=1,1
    n=len(sequence)
    l1=[]
    l2=[]
    for i in sequence:
        l1.append(i)
        l2.append(i)
    for i in range(1,n):
        if sequence[i-1]>=sequence[i]:
            del l1[i]
            del l2[i-1]
            break
    for i in range(1,n-1):
        if l1[i-1]>=l1[i]:
            c0=0
            break
    for i in range(1,n-1):
        if l2[i-1]>=l2[i]:
            c1=0
            break
    return bool(c0 or c1)
