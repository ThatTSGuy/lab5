'''
Author: Jack Temko
KUID: 3161174
Date: 10/02/2024
Lab: lab05
Last modified: 10/02/2024
Purpose: Rook Path
'''

n = int(input("Grid Size (NxN)? "))

rY = int(input("Rook Y Coord? "))
rX = int(input("Rook X Coord? "))

for y in range(n):
    row = ""
    for x in range(n):
        if rY == y and rX == x:
            row += "R"
        elif rY == y:
            row += "-"
        elif x == rX:
            row += "|"
        else:
            row += "*"
    print(row)