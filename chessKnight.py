"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnight(cell) = 2.



For cell = "c2", the output should be
chessKnight(cell) = 6.



Input/Output

[execution time limit] 4 seconds (py3)

[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

[output] integer
"""

def chessKnight(cell):
    c = [ord(cell[0]), int(cell[1])]
    t = 0
    if 97 <= c[0] + 2 <= 104:
        if 1 <= c[1] + 1 <= 8:
            t += 1
        if 1 <= c[1] - 1 <= 8:
            t += 1
    if 97 <= c[0] + 1 <= 104:
        if 1 <= c[1] + 2 <= 8:
            t += 1
        if 1 <= c[1] - 2 <= 8:
            t += 1
    if 97 <= c[0] - 2 <= 104:
        if 1 <= c[1] + 1 <= 8:
            t += 1
        if 1 <= c[1] - 1 <= 8:
            t += 1
    if 97 <= c[0] - 1 <= 104:
        if 1 <= c[1] + 2 <= 8:
            t += 1
        if 1 <= c[1] - 2 <= 8:
            t += 1

    return t
        
    
        


