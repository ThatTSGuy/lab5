'''
Author: Jack Temko
KUID: 3161174
Date: 10/02/2024
Lab: lab05
Last modified: 10/02/2024
Purpose: Numeric File Analysis
'''

fd = open(input("File name? "), "r")

rows = []
for row_str in fd:
    row_float = []
    for f in row_str.split(" "):
        row_float.append(float(f))
    rows.append(row_float)

# AVERAGE

avg_rows = []
total = 0
for (i, row) in enumerate(rows):
    s = sum(row)
    total += s
    avg_rows.append(f"Row {i+1} average: {s / len(row)}")
avg_rows.insert(0, f"Total average: {total / (len(rows)*len(rows[0]))}")

open("averages.txt", "w").write("\n".join(avg_rows))

# REVERSE
# for these next ones we cant use list.reverse() because it mutates the array

rev_out = ""
for row in rows:
    for f in row[::-1]:
        rev_out += str(f) + " "
    rev_out += "\n"

open("reverse.txt", "w").write(rev_out)

# FLIP

flip_out = ""
for row in rows[::-1]:
    for f in row:
        flip_out += str(f) + " "
    flip_out += "\n"

open("flipped.txt", "w").write(flip_out)

# TRANSPOSE

# DIAGONAL

if len(rows) != len(rows[0]):
    exit(0)

diag_out = ""
for col in range(len(rows[0])):
    for row in rows:
        diag_out += str(row[col]) + " "
    diag_out += "\n"

open("diagonal.txt", "w").write(diag_out)