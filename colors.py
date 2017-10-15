"""
This script tries to find the name of color using a given hex value
List of colors has been obtained from
https://en.wikipedia.org/wiki/List_of_colors:_A-F
https://en.wikipedia.org/wiki/List_of_colors:_G-M
https://en.wikipedia.org/wiki/List_of_colors:_N-Z

"""

colors = dict()
with open('color_list.csv') as f:
    lis = [line.split(',') for line in f]
    for hex_val, name in lis:
        colors[hex_val] = (name.rstrip(), int(hex_val, base=16))


class Color:
    def __init__(self, value: "value of color. default hexadecimal", base: "Optional. d,b,or hex"='hex'):
        self.value = value
        self.base=base
        if '#' in value:
            self.value = value.replace('#', '0x')

    def nearest_match(self):
        # Find the nearest matching color from the list
        if self.base=='d':
            hex_val = hex(int(self.value))
        if self.base=='b':
            hex_val = hex(int(self.value, base=2))
        else:
            hex_val = hex(int(self.value, base=16))
        print(hex_val)
        if hex_val in list(colors.keys()):
            return "Exact Match Found: " + colors[hex_val][0]
        else:
            # This is not the correct way of comparing colors
            # See https://en.wikipedia.org/wiki/Color_difference
            color = None
            min = 16777215  # FFFFFF
            color_int = int(hex_val,base=16)
            for item in colors.values():
                if abs(item[1] - color_int) < min:
                    min = abs(item[1] - color_int)
                    color = item[0]
            return "Nearest Match: " + color
