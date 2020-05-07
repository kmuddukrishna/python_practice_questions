"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer product

Guaranteed constraints:
0 ≤ product ≤ 600.

[output] integer
"""

def digitsProduct(product):
    if product == 0:
        return 10
    if product < 10:
        return product
  
    l = []
    i = 9
    while i > 1:
        if product%i == 0:
            product = int(product/i)
            l.insert(0,i)
            if product < 10:
                l.insert(0,product)
                return int("".join(str(x) for x in l))
        else:
            i-=1
    if i == 1:
        return -1