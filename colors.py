"""
This script tries to find the name of color using a given hex value
List of colors 'wiki_colors.csv' has been obtained from
https://en.wikipedia.org/wiki/List_of_colors:_A-F
https://en.wikipedia.org/wiki/List_of_colors:_G-M
https://en.wikipedia.org/wiki/List_of_colors:_N-Z

List of colors 'xkcd_colors.csv' has been obtained from
https://xkcd.com/color/rgb/
"""

col_files = {'wiki': 'wiki_colors.csv', 'xkcd': 'xkcd_colors/xkcd_colors.csv'}
# read in both color lists
colors = {key: {} for key in col_files}
for key, fname in col_files.items():
    with open(fname) as f:
        lis = [line.split(',') for line in f]
        for hex_val, name in lis:
            colors[key][hex_val] = (name.rstrip(), int(hex_val, base=16))


class Color:
    """
    Fetches the name of the nearest matching color to a hexadecimal color string.
    
    value: str
            hex color name
    cols: str, optional (default='xkcd')
            color list ('xkcd', 'wiki')
    """
    def __init__(self, value, colset='xkcd'):
        self.value = value.replace('#', '0x') 
        self.colset = colset

    def nearest_match(self):
        # Find the nearest matching color from the list
        hex_val = hex(int(self.value, base=16))

        if hex_val in colors[self.colset]:
            return "Exact Match Found: " + colors[self.colset][hex_val][0]
        else:
            # This is not the correct way of comparing colors
            # See https://en.wikipedia.org/wiki/Color_difference
            color = None
            min = 16777215  # FFFFFF
            color_int = int(self.value, base=16)
            for item in colors[self.colset].values():
                if abs(item[1] - color_int) < min:
                    min = abs(item[1] - color_int)
                    color = item[0]
            return "Nearest Match: " + color
    def RGB_cartesian_match(self):
        #eucledian
        color = None
        min = 16777215  # FFFFFF
        for item in colors[self.colset].values():
            colorCompareHex = "0x{:06x}".format(item[1])
            if self.eucleanCalculate(self.value, colorCompareHex) < min:
                min = self.eucleanCalculate(self.value, colorCompareHex)
                color = item[0]
        return "Nearest Match: " + color
	
    def eucleanCalculate(self, C1, C2):
        # self un-needed here but python will riase argument exception since it passes it automatically
        # check the last formula in https://en.wikipedia.org/wiki/Color_difference#Euclidean
        #c1 rgb
        C1 = C1.replace('0x', '')
        C2 = C2.replace('0x', '')
        C1_R_int = int(C1[0:2], base=16)
        C1_G_int = int(C1[2:4], base=16)
        C1_B_int = int(C1[4:6], base=16)
        #c2 rgb
        C2_R_int = int(C2[0:2], base=16)
        C2_G_int = int(C2[2:4], base=16)
        C2_B_int = int(C2[4:6], base=16)
        #delta square
        deltaR = (C1_R_int - C2_R_int)**2 
        deltaG = (C1_G_int - C2_G_int)**2 
        deltaB = (C1_B_int - C2_B_int)**2
        r = (C1_R_int + C2_R_int)/2
        deltaC = ((2 + r/256)*deltaR + 4*deltaG + (2 + (255 - r)/2)*deltaB)
        return deltaC**0.5

        
        
