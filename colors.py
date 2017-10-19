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
    def __init__(self, value: "value of color. default hexadecimal", base: "Optional. d,b,or hex"='hex'):
        self.value = value
        self.base = base
        if '#' in value:
            self.value = value.replace('#', '0x')

    def nearest_match(self):
        if self.base=='d':
            hex_val = hex(int(self.value))
        elif self.base=='b':
            hex_val = hex(int(self.value, base=2))
        elif self.base=='hex':
            hex_val = hex(int(self.value, base=16))
        # Find the nearest matching color from the list
        if hex_val in list(colors.keys()):
            return "Exact Match Found: " + colors[hex_val][0]
        else:
            # This is not the correct way of comparing colors
            # See https://en.wikipedia.org/wiki/Color_difference
            color = None
            min = 16777215  # FFFFFF
            color_int = int(self.value, base=16)
            for item in colors.values():
                if abs(item[1] - color_int) < min:
                    min = abs(item[1] - color_int)
                    color = item[0]
            return "Nearest Match: " + color
