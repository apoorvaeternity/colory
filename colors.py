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
