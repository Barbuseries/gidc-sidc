#!/usr/bin/python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

import argcomplete, argparse
from datetime import datetime

from PIL import Image
from math import sqrt
import numpy
import random
import os,sys
import operator
import itertools

me = os.path.basename(sys.argv[0])

# NOTE: 64 seems to yield the most accurate result (compared to
#       testing against every color) while being a massive improvement
#       speed-wise.
#
#       32 seems to be the fastest (by 25%, compared to 64), but the
#       results are up to 15% off...
#
#       I need to do a benchmark to make sure.
SAFE_PALETTE_GRID_WIDTH = 64
FASTEST_PALETTE_GRID_WIDTH = 32

ALL_PALETTES = {
    "advanced":
    {
        "maroon"                  : [128, 0, 0],
        "dark-red"                : [139, 0, 0],
        "brown"                   : [165, 42, 42],
        "firebrick"               : [178, 34, 34],
        "crimson"                 : [220, 20, 60],
        "red"                     : [255, 0, 0],
        "tomato"                  : [255, 99, 71],
        "coral"                   : [255, 127, 80],
        "indian-red"              : [205, 92, 92],
        "light-coral"             : [240, 128, 128],
        "dark-salmon"             : [233, 150, 122],
        "salmon"                  : [250, 128, 114],
        "light-salmon"            : [255, 160, 122],
        "orange-red"              : [255, 69, 0],
        "dark-orange"             : [255, 140, 0],
        "orange"                  : [255, 165, 0],
        "gold"                    : [255, 215, 0],
        "dark-golden-rod"         : [184, 134, 11],
        "golden-rod"              : [218, 165, 32],
        "pale-golden-rod"         : [238, 232, 170],
        "dark-khaki"              : [189, 183, 107],
        "khaki"                   : [240, 230, 140],
        "olive"                   : [128, 128, 0],
        "yellow"                  : [255, 255, 0],
        "yellow-green"            : [154, 205, 50],
        "dark-olive-green"        : [85, 107, 47],
        "olive-drab"              : [107, 142, 35],
        "lawn-green"              : [124, 252, 0],
        "chart-reuse"             : [127, 255, 0],
        "green-yellow"            : [173, 255, 47],
        "dark-green"              : [0, 100, 0],
        "green"                   : [0, 128, 0],
        "forest-green"            : [34, 139, 34],
        "lime"                    : [0, 255, 0],
        "lime-green"              : [50, 205, 50],
        "light-green"             : [144, 238, 144],
        "pale-green"              : [152, 251, 152],
        "dark-sea-green"          : [143, 188, 143],
        "medium-spring-green"     : [0, 250, 154],
        "spring-green"            : [0, 255, 127],
        "sea-green"               : [46, 139, 87],
        "medium-aqua-marine"      : [102, 205, 170],
        "medium-sea-green"        : [60, 179, 113],
        "light-sea-green"         : [32, 178, 170],
        "dark-slate-gray"         : [47, 79, 79],
        "teal"                    : [0, 128, 128],
        "dark-cyan"               : [0, 139, 139],
        "aqua"                    : [0, 255, 255],
        "cyan"                    : [0, 255, 255],
        "light-cyan"              : [224, 255, 255],
        "dark-turquoise"          : [0, 206, 209],
        "turquoise"               : [64, 224, 208],
        "medium-turquoise"        : [72, 209, 204],
        "pale-turquoise"          : [175, 238, 238],
        "aqua-marine"             : [127, 255, 212],
        "powder-blue"             : [176, 224, 230],
        "cadet-blue"              : [95, 158, 160],
        "steel-blue"              : [70, 130, 180],
        "corn-flower-blue"        : [100, 149, 237],
        "deep-sky-blue"           : [0, 191, 255],
        "dodger-blue"             : [30, 144, 255],
        "light-blue"              : [173, 216, 230],
        "sky-blue"                : [135, 206, 235],
        "light-sky-blue"          : [135, 206, 250],
        "midnight-blue"           : [25, 25, 112],
        "navy"                    : [0, 0, 128],
        "dark-blue"               : [0, 0, 139],
        "medium-blue"             : [0, 0, 205],
        "blue"                    : [0, 0, 255],
        "royal-blue"              : [65, 105, 225],
        "blue-violet"             : [138, 43, 226],
        "indigo"                  : [75, 0, 130],
        "dark-slate-blue"         : [72, 61, 139],
        "slate-blue"              : [106, 90, 205],
        "medium-slate-blue"       : [123, 104, 238],
        "medium-purple"           : [147, 112, 219],
        "dark-magenta"            : [139, 0, 139],
        "dark-violet"             : [148, 0, 211],
        "dark-orchid"             : [153, 50, 204],
        "medium-orchid"           : [186, 85, 211],
        "purple"                  : [128, 0, 128],
        "thistle"                 : [216, 191, 216],
        "plum"                    : [221, 160, 221],
        "violet"                  : [238, 130, 238],
        "magenta"                 : [255, 0, 255],
        "orchid"                  : [218, 112, 214],
        "medium-violet-red"       : [199, 21, 133],
        "pale-violet-red"         : [219, 112, 147],
        "deep-pink"               : [255, 20, 147],
        "hot-pink"                : [255, 105, 180],
        "light-pink"              : [255, 182, 193],
        "pink"                    : [255, 192, 203],
        "antique-white"           : [250, 235, 215],
        "beige"                   : [245, 245, 220],
        "bisque"                  : [255, 228, 196],
        "blanched-almond"         : [255, 235, 205],
        "wheat"                   : [245, 222, 179],
        "corn-silk"               : [255, 248, 220],
        "lemon-chiffon"           : [255, 250, 205],
        "light-golden-rod-yellow" : [250, 250, 210],
        "light-yellow"            : [255, 255, 224],
        "saddle-brown"            : [139, 69, 19],
        "sienna"                  : [160, 82, 45],
        "chocolate"               : [210, 105, 30],
        "peru"                    : [205, 133, 63],
        "sandy-brown"             : [244, 164, 96],
        "burly-wood"              : [222, 184, 135],
        "tan"                     : [210, 180, 140],
        "rosy-brown"              : [188, 143, 143],
        "moccasin"                : [255, 228, 181],
        "navajo-white"            : [255, 222, 173],
        "peach-puff"              : [255, 218, 185],
        "misty-rose"              : [255, 228, 225],
        "lavender-blush"          : [255, 240, 245],
        "linen"                   : [250, 240, 230],
        "old-lace"                : [253, 245, 230],
        "papaya-whip"             : [255, 239, 213],
        "sea-shell"               : [255, 245, 238],
        "mint-cream"              : [245, 255, 250],
        "slate-gray"              : [112, 128, 144],
        "light-slate-gray"        : [119, 136, 153],
        "light-steel-blue"        : [176, 196, 222],
        "lavender"                : [230, 230, 250],
        "floral-white"            : [255, 250, 240],
        "alice-blue"              : [240, 248, 255],
        "ghost-white"             : [248, 248, 255],
        "honeydew"                : [240, 255, 240],
        "ivory"                   : [255, 255, 240],
        "azure"                   : [240, 255, 255],
        "snow"                    : [255, 250, 250],
        "black"                   : [0, 0, 0],
        "dim-gray"                : [105, 105, 105],
        "gray"                    : [128, 128, 128],
        "dark-gray"               : [169, 169, 169],
        "silver"                  : [192, 192, 192],
        "light-gray"              : [211, 211, 211],
        "gainsboro"               : [220, 220, 220],
        "white-smoke"             : [245, 245, 245],
        "white"                   : [255, 255, 255]
    },
    "basic":
    {
        "black"                   : [0, 0, 0],
        "blue"                    : [0, 0, 255],
        "cyan"                    : [0, 255, 255],
        "gray"                    : [128, 128, 128],
        "green"                   : [0, 128, 0],
        "lime"                    : [0, 255, 0],
        "magenta"                 : [255, 0, 255],
        "maroon"                  : [128, 0, 0],
        "navy"                    : [0, 0, 128],
        "olive"                   : [128, 128, 0],
        "purple"                  : [128, 0, 128,],
        "red"                     : [255, 0, 0],
        "silver"                  : [192, 192, 192],
        "teal"                    : [0, 128, 128],
  	"white"                   : [255, 255, 255],
  	"yellow"                  : [255, 255, 0]
    },
    "vga":
    {
        "black"                   : [0, 0, 0],
        "blue"                    : [0, 0, 170],
        "green"                   : [0, 170, 0],
        "cyan"                    : [0, 170, 170],
        "red"                     : [170, 0, 0],
        "magenta"                 : [170, 0, 170],
        "brown"                   : [170, 85, 0],
        "gray"                    : [170, 170, 170],
        "dark-gray"               : [85, 85, 85],
        "bright-blue"             : [85, 85, 255],
        "bright-green"            : [85, 255, 85],
        "bright-cyan"             : [85, 255, 255],
        "bright-red"              : [255, 85, 85],
        "bright-magenta"          : [255, 85, 255],
        "yellow"                  : [255, 255, 85],
        "white"                   : [255, 255, 255]
    }
}

class Box(object):
    def __init__(self, min_x, max_x, min_y, max_y, is_invert, is_excluding):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        
        self.is_invert = is_invert
        self.is_excluding = is_excluding

def eprint(*args, **kwargs):
    """
    Error print.

    Send output to stderr. If prog_name is set to True, prefix output
    by the program's name.
    """
    if (kwargs.pop("prog_name", True)):
        print("%s: %s" % (me, *args), file=sys.stderr, **kwargs)
    else:
        print(*args, file=sys.stderr, **kwargs)


def rgb_to_color_key(red, green, blue, color_mask):
    return ((((red & color_mask) * 256) +
             (green & color_mask)) * 256 + 
            (blue & color_mask))
        
def rgb_from_color_key(color_key):
    r = color_key // (256 * 256)
    color_key -= (r * 256 * 256)
    
    g = color_key // 256
    color_key -= (g * 256)
    
    b = color_key

    return r, g, b

def raw_channel_to_s_channel(channel):
    c = channel / 255
    
    if (c <= 0.04045):
        return c / 12.92
    else:
        a = 0.055
        return (c + a) / (1 + a)

def make_palette_grid(palette, max_grid_dim_width):
    grid_dim_size = int(255/max_grid_dim_width) + 1

    palette_grid = []

    palette_grid = [[[[]
                      for r in range(grid_dim_size)]
                     for g in range(grid_dim_size)]
                    for b in range(grid_dim_size)]

    for color in palette.items():
        red, green, blue = color[1]

        r_index = int(red/max_grid_dim_width)
        g_index = int(green/max_grid_dim_width)
        b_index = int(blue/max_grid_dim_width)
        
        # IMPORTANT: If max_grid_dim_width is
        #            FASTEST_PALETTE_GRID_WIDTH, uncomment comments,
        #            comment non-comments.
        
        # min_r_index = r_index
        # max_r_index = r_index
        
        # min_g_index = g_index
        # max_g_index = g_index
        
        # min_b_index = b_index
        # max_b_index = b_index
        
        # offset_r = ((red >= max_grid_dim_width) and
        #             ((red % max_grid_dim_width) == 0))
        # offset_g = ((green >= max_grid_dim_width) and
        #             ((green % max_grid_dim_width) == 0))
        # offset_b = ((blue >= max_grid_dim_width) and
        #             ((blue % max_grid_dim_width) == 0))

        # min_r_index = max(r_index - offset_r, 0)
        # max_r_index = r_index
        
        # min_g_index = max(g_index - offset_g, 0)
        # max_g_index = g_index
        
        # min_b_index = max(b_index - offset_b, 0)
        # max_b_index = b_index
        
        # for r, g, b in itertools.product(range(min_r_index, max_r_index + 1), 
        #                                  range(min_g_index, max_g_index + 1), 
        #                                  range(min_b_index, max_b_index + 1)):
        #     palette_grid[r][g][b].append(color)
        palette_grid[r_index][g_index][b_index].append(color)

    return palette_grid

# NOTE: This is a bottleneck when the palette is 'advanced' and --bits
#       is 8 (too many distances to calculate)...
# TODO: Add distance function parameter.
def group_color_by_nearest(color_map, palette):
    name_color_map = {}

    # NOTE: When palette is not too big, both path take around the
    #       same time.
    #       Otherwhise, the second path is _way_ faster (x5).
    if (len(palette) <= 16):
        for color in color_map:
            red, green, blue = rgb_from_color_key(color)

            color_name = min(palette.items(), key=lambda c: abs(c[1][0] - red) + abs(c[1][1] - green) + abs(c[1][2] - blue))[0]
        
            try:
                name_color_map[color_name] += color_map[color]
            except:
                name_color_map[color_name] = color_map[color]

    else:
        max_grid_dim_width = SAFE_PALETTE_GRID_WIDTH
        palette_grid = make_palette_grid(palette, max_grid_dim_width)
        
        for color in color_map:
            red, green, blue = rgb_from_color_key(color)
            color_name, color_value = nearest_palette_color(red, green, blue, palette_grid, max_grid_dim_width)
        
            try:
                name_color_map[color_name] += color_map[color]
            except:
                name_color_map[color_name] = color_map[color]

    return name_color_map

def print_color_map(color_map, palette, pixel_count, display_color_format, group_by_name):
    max_grid_dim_width = SAFE_PALETTE_GRID_WIDTH
    palette_grid = make_palette_grid(palette, max_grid_dim_width)
    
    for color in color_map:
        if (group_by_name):
            red, green, blue = palette[color[0]]
        else:
            red, green, blue = rgb_from_color_key(color[0])

        sRed = raw_channel_to_s_channel(red)
        sGreen = raw_channel_to_s_channel(green)
        sBlue = raw_channel_to_s_channel(blue)
        
        print(display_color_format.replace("%c", "(%d,%d,%d)" % (red, green, blue)) \
              .replace("%r", str(red)) \
              .replace("%g", str(green)) \
              .replace("%b", str(blue)) \
              .replace("%h", "#{:02x}{:02x}{:02x}".format(red, green, blue)) \
              .replace("%H", "#{:02X}{:02X}{:02X}".format(red, green, blue)) \
              .replace("%n", nearest_palette_color(red, green, blue, palette_grid, max_grid_dim_width)[0]) \
              .replace("%p", "%.02f" % ((color[1] * 100) / pixel_count)) \
              .replace("%l", "%.02f" % (0.2126 * sRed + 0.7152 * sGreen + 0.0722 * sBlue)))
            

def sort_and_print_colors(color_map, palette, group_by_name, display_color_count, display_color_format, prepend_filename, filename = 'None'):
    if (group_by_name):
        color_map = group_color_by_nearest(color_map, palette)
        
    sorted_color_map = sorted(color_map.items(), key=operator.itemgetter(1), reverse=True)
    pixel_count = sum([color[1] for color in sorted_color_map])
        
    if (display_color_count != 0):
        sorted_color_map = sorted_color_map[:display_color_count]
            
    if (prepend_filename):
        print("%s:" % filename)
                
    print_color_map(sorted_color_map, palette, pixel_count, display_color_format, group_by_name)
    color_map = {}

def parse_box_dim(dim, default_min, default_max):
    if (len(dim) == 1):
        if (len(dim[0]) == 0): # '', take default values
            dim = [str(default_min), str(default_max)]
        else: # 'X', take default max value
            dim = [dim[0], str(default_max)]
    elif (len(dim) == 2): # ',X', ',', 'X,'
        if (len(dim[0]) == 0): # ',X' or ',', take default min value
            dim = [str(default_min), dim[1]]
        if (len(dim[1]) == 0): # 'X,' or ',', take default min value
            dim = [dim[0], str(default_max)]

    return dim

# TODO: Use a more sophisticated distance function, add way to specify
#       one.
#       Use HSL and HSV.
def nearest_palette_color(red, green, blue, palette_grid, max_grid_dim_width):
    red_index = int(red/max_grid_dim_width)
    green_index = int(green/max_grid_dim_width)
    blue_index = int(blue/max_grid_dim_width)

    grid_dim_size = len(palette_grid)

    offset = 1
    min_distance = -1
    color = None

    while (color is None):
        min_red_index = max(red_index - offset, 0)
        max_red_index = min(red_index + offset, grid_dim_size - 1)

        min_green_index = max(green_index - offset, 0)
        max_green_index = min(green_index + offset, grid_dim_size - 1)

        min_blue_index = max(blue_index - offset, 0)
        max_blue_index = min(blue_index + offset, grid_dim_size - 1)
        
        for r, g, b in itertools.product(range(min_red_index, max_red_index + 1), 
                                         range(min_green_index, max_green_index + 1), 
                                         range(min_blue_index, max_blue_index + 1)):
            color_list = palette_grid[r][g][b]
            
            for c in color_list:
                c_r, c_g, c_b = c[1]
                
                distance = abs(c_r - red) + abs(c_g - green) + abs(c_b - blue)

                if ((color is None) or
                    (distance < min_distance)):
                    color = c
                    min_distance = distance
                    
        offset += 1

    return color

def main():
    palette_name = "basic"
    filename = None
    display_color_count = 1
    display_color_format = "%p\t%n\t%c"
    color_bits = 6
    group_by_name = False
    pixels_percentage=1
    prepend_filename = False
    cumulative = False
    random = False
    display_average = False
    image_box=[[0, 100], [0, 100]]

    version_major="0"
    version_minor="9"

    version=".".join([version_major, version_minor])

    license="Copyright © %d Barbu\n"\
        "This work is free. You can redistribute it and/or modify it under the\n"\
        "terms of the Do What The Fuck You Want To Public License, Version 2,\n"\
        "as published by Sam Hocevar. See http://www.wtfpl.net/ for more details." % datetime.now().year

    verbose_version="%s %s\n\n%s" % (me, version, license)
    
    description="Get Image's Dominant Colors."

    format_help = "-f, --format FORMAT\n\n"\
                  "The following variables can be used in FORMAT:\n"\
                  "  %r - red channel\n" \
                  "  %g - green channel\n" \
                  "  %b - blue channel\n" \
                  "  %c - RGB representation (e.g., (255, 255, 255))\n" \
                  "  %h - RGB hexadecimal representation (lower case) (e.g., #ffffff)\n" \
                  "  %H - RGB hexadecimal representation (upper case) (e.g., #FFFFFF)\n" \
                  "  %n - name (e.g: white)\n" \
                  "  %p - percentage\n"\
                  "  %l - relative luminance\n"\
                  "\n"\
                  "If you want to use escaped characters (e.g., '\\t')\n"\
                  "from the shell, precede FORMAT by '$' (e.g., $'%n\\t%p')."

    box_invert_char = '~'
    box_exclude_char = '^'
    box_syntax = "[%c%c]min_x,max_x:min_y,max_y" % (box_exclude_char, box_invert_char)

    box_help = "-b, --box BOX [BOX ...]\n\n"\
               "BOX syntax is:\n"\
               "  %s\n\n"\
               "Where values are in percentages, '%c' inverts the box,\n"\
               "and '%c' excludes it's content.\n\n"\
               "If only min_x and/or max_x are given, they are\n"\
               "copied to min_y and max_y.\n"\
               "(e.g., '25,75' is the same as '25,75:25,75')\n\n"\
               "If a value is missing, it's default value is used\n"\
               "instead (%d for min, and %d for max).\n"\
               "(e.g., '25,:0,100' is the same as '25,100:0,100',\n"\
               "'25,:,', '25,:' or just '25')\n\n"\
               "Inverting a box add every pixel not inside the specified\n"\
               "box.\n"\
               "(e.g., '~25,75:25,75' will add every pixel except\n"\
               "those inside the centered-50%%-side-length rectangle)\n\n"\
               "Excluding a box removes every pixel inside the specified\n"\
               "box.\n"\
               "(e.g., '^25,75:25,75' will remove every pixel inside\n"\
               "the centered-50%%-side-length rectangle)\n\n"\
               "Excluding boxes are processed last (whatever the order\n"\
               "they were passed in).\n\n"\
               "Pixels are only counted once, even if they appear in\n"\
               "multiple boxes." % (box_syntax,
                                    box_invert_char, box_exclude_char,
                                    image_box[0][0], image_box[0][1])

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description=description)
    parser.add_argument("--version", action="version",
                        version="%(prog)s {version}\n\n{license}".format(version=version, license=license))

    parser.add_argument("all_images", metavar="IMG", type=str, nargs='*')
    parser.add_argument("-c", "--count", metavar="N", dest="display_color_count", type=int, nargs=1,
                        help="only display the first N dominant colors.\n"\
                        "(0 means each one)\n"\
                        "(Default %d)" % display_color_count)
    parser.add_argument("-f", "--format", metavar="FORMAT", dest="display_color_format", type=str, nargs=1,
                        help="format to display each color.\n"\
                        "Type --format help for more information\n"\
                        "(Default %s)" % display_color_format.replace("%", "%%"))
    parser.add_argument("-b", "--bits", metavar="N", dest="color_bits", type=int, nargs=1,
                        help="only take into account the first N bits of each\ncolor channel.\n"\
                        "(Default %d)" % color_bits)
    parser.add_argument("-g", "--group-by-name", dest="group_by_name", action="store_const",
                        const=True,
                        help="group colors by their name.")
    parser.add_argument("-p", "--percentage", metavar="N", dest="pixels_percentage", type=float, nargs=1,
                        help="percentage of the image to take into account.\n"\
                        "(Default %.02f)" % (pixels_percentage * 100.0))
    parser.add_argument("-q", "--brief", dest="display_brief", action="store_const",
                        const=True,
                        help="do not prepend colors display by the image's filename.\n"\
                        "(Default if only one image is given)")
    parser.add_argument("-C", "--cumulative", dest="cumulative", action="store_const",
                        const=True,
                        help="merge all images into one.")
    parser.add_argument("-r", "--random", dest="random", action="store_const",
                        const=True,
                        help="select pixels at random.")
    parser.add_argument("-P", "--palette", dest="palette", type=str, nargs=1, choices=ALL_PALETTES.keys(),
                        help="which color palette to use.\n"\
                        "(Default %s)" % palette_name)
    parser.add_argument("-a", "--average", dest="display_average", action="store_const",
                        const=True,
                        help="display the image's average color.\n")
    parser.add_argument("-B", "--box", metavar="BOX,", dest="all_boxes_description", type=str, nargs='+',
                        help="which part of the image to use.\n"\
                        "Type --box help for more information.\n"
                        "(Default %d,%d:%d,%d)" % (image_box[0][0], image_box[0][1],
                                                   image_box[1][0], image_box[1][1]))
    
    argcomplete.autocomplete(parser, always_complete_options="long")
    args = parser.parse_args()

    all_image_boxes = []
    all_images_count = len(args.all_images)
    
    if (all_images_count > 1):
        prepend_filename = True
    
    if (not args.display_color_count is None):
        display_color_count = args.display_color_count[0]

        if (display_color_count < 0):
            eprint("-c/--count: COUNT must be >= 0.")
            sys.exit(1)

    if (not args.group_by_name is None):
        group_by_name = True
    
    if (not args.display_color_format is None):
        display_color_format = args.display_color_format[0]

        if (display_color_format == "help"):
            print(format_help)
            quit()

    if (not args.color_bits is None):
        color_bits = args.color_bits[0]

        if ((color_bits < 1) or
            (color_bits > 8)):
            eprint("-b/--bits: COUNT must be > 1 and <= 8.")
            sys.exit(2)

    if (not args.pixels_percentage is None):
        pixels_percentage = args.pixels_percentage[0] * 1.0 / 100
        
        if ((pixels_percentage <= 0) or (pixels_percentage > 1)):
            eprint("-p/--percentage: N must be > 0 and <= 100.")
            sys.exit(3)

    if (not args.cumulative is None):
        cumulative = True
            
    if ((not args.display_brief is None) and
        (not cumulative)):
        prepend_filename = False

    if (not args.random is None):
        if (pixels_percentage < 1):
            random = True

    if (not args.palette is None):
        palette_name = args.palette[0]

    if (not args.display_average is None):
        display_average = True

    if (not args.all_boxes_description is None):
        if ("help" in args.all_boxes_description):
            print(box_help)
            quit()
            
        for box in args.all_boxes_description:
            box_dimensions = box.split(':')
        
            if (len(box_dimensions) > 2):
                eprint("-B/--box: BOX syntax is %s." % box_syntax)
                sys.exit(4)

            is_invert = False
            is_excluding = False
            
            if ((len(box_dimensions[0]) > 0) and
                (box_dimensions[0][0] == box_exclude_char)):
                is_excluding = True
                
                box_dimensions[0] = box_dimensions[0][1:]

            if ((len(box_dimensions[0]) > 0) and
                (box_dimensions[0][0] == box_invert_char)):
                is_invert = True
                
                box_dimensions[0] = box_dimensions[0][1:]

            if (len(box_dimensions) == 1):
                box_dimensions = [box_dimensions[0], box_dimensions[0]]

            x_spec = box_dimensions[0].split(',')
            
            if (len(x_spec) > 2):
                eprint("-B/--box: BOX syntax is %s." % box_syntax)
                sys.exit(5)

            box_min_x, box_max_x = parse_box_dim(x_spec, image_box[0][0], image_box[0][1])
                
            y_spec = box_dimensions[1].split(',')

            if (len(y_spec) > 2):
                eprint("-B/--box: BOX syntax is %s." % box_syntax)
                sys.exit(6)
                
            box_min_y, box_max_y = parse_box_dim(y_spec, image_box[1][0], image_box[1][1])

            # TODO?: Handle per variable absolute pixel alternative.
            try:
                box_min_x = float(box_min_x)
                box_max_x = float(box_max_x)
                box_min_y = float(box_min_y)
                box_max_y = float(box_max_y)
            except Exception as e:
                eprint(e)
                sys.exit(7)

            if (((box_min_x < 0) or (box_min_x > 100)) or
                ((box_max_x < 0) or (box_max_x > 100)) or
                ((box_min_y < 0) or (box_min_y > 100)) or
                ((box_max_y < 0) or (box_max_y > 100))):
                eprint("-b/--box: dimensions are in percentage and must be >= 0 and <= 100.")
                sys.exit(8)

            if (box_min_x >= box_max_x):
                eprint("-b/--box: min_x must be > max_x")
                sys.exit(9)

            if (box_min_y >= box_max_y):
                eprint("-b/--box: min_y must be > max_y")
                sys.exit(10)

            all_image_boxes.append(Box(box_min_x, box_max_x,
                                       box_min_y, box_max_y,
                                       is_invert, is_excluding))

    if (len(args.all_images) == 0):
        eprint("no image given.")
        sys.exit(11)

    # Put excluding boxes at the end, so they _do_ exclude something
    # (even if they where given first).
    all_image_boxes = sorted(all_image_boxes, key=lambda x: x.is_excluding)

    # If no box is given or only excluding boxes are, add a box
    # matching the whole image.
    if ((len(all_image_boxes) == 0) or
        (len(all_image_boxes) > 0 and
         (all_image_boxes[0].is_excluding))):
        all_image_boxes.insert(0, Box(image_box[0][0], image_box[0][1],
                                      image_box[1][0], image_box[1][1],
                                      False, False))

    palette = ALL_PALETTES[palette_name]
    color_map = {}
    pixel_count = 0
    filename_index = 0
    pixel_factor = sqrt(pixels_percentage)
    old_width = None
    old_height = None
    
    for filename in args.all_images:
        try:
            image = Image.open(filename).convert("RGB")
        except Exception as e:
            eprint(e)
            continue
    
        pixels = image.load()

        try:
            red, green, blue = pixels[0, 0]
        except:
            eprint("can not decode %s." % filename)
            continue

        color_byte_shift = 8 - color_bits
        width, height = image.size            
        color_mask = 255 << color_byte_shift

        # Update final box if the image's dimensions have changed or
        # if --random is set.
        if ((old_width != width) or
            (old_height != height) or
            random):
            recalculate_x = ((old_width != width) or random)
            recalculate_y = ((old_height != height) or random)
            
            if (old_width != width):
                image_box_x = None
                
            if (old_height != height):
                image_box_y = None

            if (recalculate_x):
                all_x = numpy.array([]).astype(int)
                
            if (recalculate_y):
                all_y = numpy.array([]).astype(int)

            for box in all_image_boxes:
                if (not random):
                    if (old_width != width):
                        box_x_count = int(width * (box.max_x - box.min_x) / 100 * pixel_factor)

                    if (old_height != height):
                        box_y_count = int(height * (box.max_y - box.min_y) / 100 * pixel_factor)
                else: # take every pixel, shuffle later
                    box_x_count = int(width * (box.max_x - box.min_x) / 100)
                    box_y_count = int(height * (box.max_y - box.min_y) / 100)

                if (recalculate_x):
                    box_x = numpy.linspace(width * box.min_x / 100, width * box.max_x / 100, num=box_x_count, endpoint=False).astype(int)
                    
                if (recalculate_y):
                    box_y = numpy.linspace(height * box.min_y / 100, height * box.max_y / 100, num=box_y_count, endpoint=False).astype(int)
                    
                if (box.is_invert):
                    if (image_box_x is None):
                        if (not random):
                            image_box_x = numpy.linspace(0, width, num=int(width * pixel_factor), endpoint=False).astype(int)
                        else:
                            image_box_x = numpy.linspace(0, width, num=int(width), endpoint=False).astype(int)

                    if (image_box_y is None):
                        if (not random):
                            image_box_y = numpy.linspace(0, height, num=int(height * pixel_factor), endpoint=False).astype(int)
                        else:
                            image_box_y = numpy.linspace(0, height, num=int(height), endpoint=False).astype(int)

                    if (recalculate_x):
                        box_x = numpy.setdiff1d(image_box_x, box_x, assume_unique=True)

                    if (recalculate_y):
                        box_y = numpy.setdiff1d(image_box_y, box_y, assume_unique=True)

                if (box.is_excluding):
                    if (recalculate_x):
                        all_x = numpy.setdiff1d(all_x, box_x, assume_unique=True)
                        
                    if (recalculate_y):
                        all_y = numpy.setdiff1d(all_y, box_y, assume_unique=True)
                else:
                    if (recalculate_x):
                        all_x = numpy.union1d(all_x, box_x)

                    if (recalculate_y):
                        all_y = numpy.union1d(all_y, box_y)

            if (random):
                numpy.random.shuffle(all_x)
                numpy.random.shuffle(all_y)
                
                all_x = sorted(all_x[:int(width * pixel_factor)])
                all_y = sorted(all_y[:int(height * pixel_factor)])

        for y in all_y:
            for x in all_x:
                red, green, blue = pixels[int(x), int(y)]
                
                color_key = rgb_to_color_key(red, green, blue, color_mask)
                    
                try:
                    color_map[color_key] += 1
                except:
                    color_map[color_key] = 1

        if (not cumulative):
            if (display_average):
                average_color = [0, 0, 0]
                
                for color_key in color_map.keys():
                    red, green, blue = rgb_from_color_key(color_key)
                    count = color_map[color_key]
                    
                    average_color[0] += red * count
                    average_color[1] += green * count
                    average_color[2] += blue * count

                pixel_count = sum([p for p in color_map.values()])
                average_color = [int(channel / pixel_count) for channel in average_color]

                color_map = {rgb_to_color_key(average_color[0],
                                              average_color[1],
                                              average_color[2],
                                              color_mask): 1}
            sort_and_print_colors(color_map, palette, group_by_name,
                                  display_color_count, display_color_format,
                                  prepend_filename, filename)
            
            filename_index += 1

            if (filename_index < all_images_count):
                print("")

            color_map = {}
            
        old_width = width
        old_height = height
            
            
    if (cumulative):
        if (display_average):
            average_color = [0, 0, 0]
                
            for color_key in color_map.keys():
                    red, green, blue = rgb_from_color_key(color_key)
                    count = color_map[color_key]
                    
                    average_color[0] += red * count
                    average_color[1] += green * count
                    average_color[2] += blue * count
                    
            pixel_count = sum([p for p in color_map.values()])
            
            average_color = [int(channel / pixel_count) for channel in average_color]
            color_map = {rgb_to_color_key(average_color[0],
                                          average_color[1],
                                          average_color[2],
                                          color_mask): 1}
                
        sort_and_print_colors(color_map, palette, group_by_name,
                              display_color_count, display_color_format,
                              False)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("")
    except Exception as e:
        print("\nAn exception has occurred: %s" % e)
