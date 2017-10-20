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
            min_diff = 16777215  # FFFFFF
            for item in colors[self.colset].values():
                color_to_compare_hex = "0x{:06x}".format(item[1])
                if self.euclean_calculate(self.value, color_to_compare_hex) < min_diff:
                    min_diff = self.euclean_calculate(self.value, color_to_compare_hex)
                    color = item[0]
            return "Nearest Match: " + color
            
    def euclean_calculate(self, c1, c2):
        # self un-needed here but python will riase argument exception since it passes it automatically
        # check the last formula in https://en.wikipedia.org/wiki/Color_difference#Euclidean
        #c1 rgb
        c1 = c1.replace('0x', '')
        c2 = c2.replace('0x', '')
        c1_r_int = int(c1[0:2], base=16)
        c1_g_int = int(c1[2:4], base=16)
        c1_b_int = int(c1[4:6], base=16)
        #c2 rgb
        c2_r_int = int(c2[0:2], base=16)
        c2_g_int = int(c2[2:4], base=16)
        c2_b_int = int(c2[4:6], base=16)
        #delta square
        delta_r = (c1_r_int - c2_r_int)**2 
        delta_g = (c1_g_int - c2_g_int)**2 
        delta_b = (c1_b_int - c2_b_int)**2
        r = (c1_r_int + c2_r_int)/2
        delta_c = ((2 + r/256)*delta_r + 4*delta_g + (2 + (255 - r)/2)*delta_b)
        return delta_c**0.5