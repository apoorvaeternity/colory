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
    def __init__(self, value: "hexadecimal value of color"):
        self.value = value
        if '#' in value:
            self.value = value.replace('#', '0x')

    def nearest_match(self):
        # Find the nearest matching color from the list
        hex_val = hex(int(self.value, base=16))

        if hex_val in colors:
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
