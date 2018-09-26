"""
Parses xkcd colorlist to csv.
Colors from the xkcd color name survey over about 140,000 participants,
see: https://xkcd.com/color/rgb/
"""

import csv

with open('xkcd_colors.txt') as readf, open('xkcd_colors.csv', 'wb') as writef:
    next(readf)
    lis = [line.split('\t', 1) for line in readf]
    for name, hex_val in lis:
        hex_val = hex_val.rstrip('\t\n')
        hex_val = hex_val.replace('#', '0x') 
        fwriter = csv.writer(writef, delimiter=',')
        fwriter.writerow([hex_val, name])