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

me = os.path.basename(sys.argv[0])

all_palettes = {
    "advanced":
    {
        "maroon"                  : [128, 0, 0],
        "dark_red"                : [139, 0, 0],
        "brown"                   : [165, 42, 42],
        "firebrick"               : [178, 34, 34],
        "crimson"                 : [220, 20, 60],
        "red"                     : [255, 0, 0],
        "tomato"                  : [255, 99, 71],
        "coral"                   : [255, 127, 80],
        "indian_red"              : [205, 92, 92],
        "light_coral"             : [240, 128, 128],
        "dark_salmon"             : [233, 150, 122],
        "salmon"                  : [250, 128, 114],
        "light_salmon"            : [255, 160, 122],
        "orange_red"              : [255, 69, 0],
        "dark_orange"             : [255, 140, 0],
        "orange"                  : [255, 165, 0],
        "gold"                    : [255, 215, 0],
        "dark_golden_rod"         : [184, 134, 11],
        "golden_rod"              : [218, 165, 32],
        "pale_golden_rod"         : [238, 232, 170],
        "dark_khaki"              : [189, 183, 107],
        "khaki"                   : [240, 230, 140],
        "olive"                   : [128, 128, 0],
        "yellow"                  : [255, 255, 0],
        "yellow_green"            : [154, 205, 50],
        "dark_olive_green"        : [85, 107, 47],
        "olive_drab"              : [107, 142, 35],
        "lawn_green"              : [124, 252, 0],
        "chart_reuse"             : [127, 255, 0],
        "green_yellow"            : [173, 255, 47],
        "dark_green"              : [0, 100, 0],
        "green"                   : [0, 128, 0],
        "forest_green"            : [34, 139, 34],
        "lime"                    : [0, 255, 0],
        "lime_green"              : [50, 205, 50],
        "light_green"             : [144, 238, 144],
        "pale_green"              : [152, 251, 152],
        "dark_sea_green"          : [143, 188, 143],
        "medium_spring_green"     : [0, 250, 154],
        "spring_green"            : [0, 255, 127],
        "sea_green"               : [46, 139, 87],
        "medium_aqua_marine"      : [102, 205, 170],
        "medium_sea_green"        : [60, 179, 113],
        "light_sea_green"         : [32, 178, 170],
        "dark_slate_gray"         : [47, 79, 79],
        "teal"                    : [0, 128, 128],
        "dark_cyan"               : [0, 139, 139],
        "aqua"                    : [0, 255, 255],
        "cyan"                    : [0, 255, 255],
        "light_cyan"              : [224, 255, 255],
        "dark_turquoise"          : [0, 206, 209],
        "turquoise"               : [64, 224, 208],
        "medium_turquoise"        : [72, 209, 204],
        "pale_turquoise"          : [175, 238, 238],
        "aqua_marine"             : [127, 255, 212],
        "powder_blue"             : [176, 224, 230],
        "cadet_blue"              : [95, 158, 160],
        "steel_blue"              : [70, 130, 180],
        "corn_flower_blue"        : [100, 149, 237],
        "deep_sky_blue"           : [0, 191, 255],
        "dodger_blue"             : [30, 144, 255],
        "light_blue"              : [173, 216, 230],
        "sky_blue"                : [135, 206, 235],
        "light_sky_blue"          : [135, 206, 250],
        "midnight_blue"           : [25, 25, 112],
        "navy"                    : [0, 0, 128],
        "dark_blue"               : [0, 0, 139],
        "medium_blue"             : [0, 0, 205],
        "blue"                    : [0, 0, 255],
        "royal_blue"              : [65, 105, 225],
        "blue_violet"             : [138, 43, 226],
        "indigo"                  : [75, 0, 130],
        "dark_slate_blue"         : [72, 61, 139],
        "slate_blue"              : [106, 90, 205],
        "medium_slate_blue"       : [123, 104, 238],
        "medium_purple"           : [147, 112, 219],
        "dark_magenta"            : [139, 0, 139],
        "dark_violet"             : [148, 0, 211],
        "dark_orchid"             : [153, 50, 204],
        "medium_orchid"           : [186, 85, 211],
        "purple"                  : [128, 0, 128],
        "thistle"                 : [216, 191, 216],
        "plum"                    : [221, 160, 221],
        "violet"                  : [238, 130, 238],
        "magenta"                 : [255, 0, 255],
        "orchid"                  : [218, 112, 214],
        "medium_violet_red"       : [199, 21, 133],
        "pale_violet_red"         : [219, 112, 147],
        "deep_pink"               : [255, 20, 147],
        "hot_pink"                : [255, 105, 180],
        "light_pink"              : [255, 182, 193],
        "pink"                    : [255, 192, 203],
        "antique_white"           : [250, 235, 215],
        "beige"                   : [245, 245, 220],
        "bisque"                  : [255, 228, 196],
        "blanched_almond"         : [255, 235, 205],
        "wheat"                   : [245, 222, 179],
        "corn_silk"               : [255, 248, 220],
        "lemon_chiffon"           : [255, 250, 205],
        "light_golden_rod_yellow" : [250, 250, 210],
        "light_yellow"            : [255, 255, 224],
        "saddle_brown"            : [139, 69, 19],
        "sienna"                  : [160, 82, 45],
        "chocolate"               : [210, 105, 30],
        "peru"                    : [205, 133, 63],
        "sandy_brown"             : [244, 164, 96],
        "burly_wood"              : [222, 184, 135],
        "tan"                     : [210, 180, 140],
        "rosy_brown"              : [188, 143, 143],
        "moccasin"                : [255, 228, 181],
        "navajo_white"            : [255, 222, 173],
        "peach_puff"              : [255, 218, 185],
        "misty_rose"              : [255, 228, 225],
        "lavender_blush"          : [255, 240, 245],
        "linen"                   : [250, 240, 230],
        "old_lace"                : [253, 245, 230],
        "papaya_whip"             : [255, 239, 213],
        "sea_shell"               : [255, 245, 238],
        "mint_cream"              : [245, 255, 250],
        "slate_gray"              : [112, 128, 144],
        "light_slate_gray"        : [119, 136, 153],
        "light_steel_blue"        : [176, 196, 222],
        "lavender"                : [230, 230, 250],
        "floral_white"            : [255, 250, 240],
        "alice_blue"              : [240, 248, 255],
        "ghost_white"             : [248, 248, 255],
        "honeydew"                : [240, 255, 240],
        "ivory"                   : [255, 255, 240],
        "azure"                   : [240, 255, 255],
        "snow"                    : [255, 250, 250],
        "black"                   : [0, 0, 0],
        "dim_gray"                : [105, 105, 105],
        "gray"                    : [128, 128, 128],
        "dark_gray"               : [169, 169, 169],
        "silver"                  : [192, 192, 192],
        "light_gray"              : [211, 211, 211],
        "gainsboro"               : [220, 220, 220],
        "white_smoke"             : [245, 245, 245],
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
        "dark_gray"               : [85, 85, 85],
        "bright_blue"             : [85, 85, 255],
        "bright_green"            : [85, 255, 85],
        "bright_cyan"             : [85, 255, 255],
        "bright_red"              : [255, 85, 85],
        "bright_magenta"          : [255, 85, 255],
        "yellow"                  : [255, 255, 85],
        "white"                   : [255, 255, 255]
    }
}

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

def rgb_from_color_key(color_key):
    r = color_key // (256 * 256)
    color_key -= (r * 256 * 256)
    
    g = color_key // 256
    color_key -= (g * 256)
    
    b = color_key

    return r, g, b

# TODO: Use a more sophisticated distance function.
def nearest_palette_color(palette, red, green, blue):
    current_nearest = None
    current_dist = -1
    
    for color_name, color_values in palette.items():
        dist = ((color_values[0] - red) * .299)**2 + ((color_values[1] - green) * .587)**2 + ((color_values[2] - blue) * .114)**2

        if ((current_nearest == None) or
            (dist < current_dist)):
            current_nearest = color_name
            current_dist = dist

    return current_nearest

def group_color_by_nearest(color_map, palette):
    name_color_map = {}

    for color in color_map:
        red, green, blue = rgb_from_color_key(color)
                
        color_name = nearest_palette_color(palette, red, green, blue)
                
        try:
            name_color_map[color_name] += color_map[color]
        except:
            name_color_map[color_name] = color_map[color]

    return name_color_map

def print_color_map(color_map, palette, pixel_count, display_color_format, group_by_name):
    if (group_by_name):
        for color in color_map:
            print(display_color_format.replace("%n", color[0]) \
                  .replace("%p", "%0.2f" % ((color[1] * 100) / pixel_count)))
    else:
        for color in color_map:
            red, green, blue = rgb_from_color_key(color[0])
                
            print(display_color_format.replace("%c", "(%d,%d,%d)" % (red, green, blue)) \
                  .replace("%r", str(red)) \
                  .replace("%g", str(green)) \
                  .replace("%b", str(blue)) \
                  .replace("%h", "#{:02x}{:02x}{:02x}".format(red, green, blue)) \
                  .replace("%H", "#{:02X}{:02X}{:02X}".format(red, green, blue)) \
                  .replace("%n", nearest_palette_color(palette, red, green, blue)) \
                  .replace("%p", "%.02f" % ((color[1] * 100) / pixel_count)))

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
    
def main():
    palette_name = "vga"
    filename = None
    display_color_count = 1
    display_color_format = "%p\t%n\t%c"
    color_bits = 6
    group_by_name = False
    pixels_percentage=1
    prepend_filename = False
    cumulative = False
    random = False

    version_major="0"
    version_minor="5"

    version=".".join([version_major, version_minor])

    license="Copyright © %d Barbu\n"\
        "This work is free. You can redistribute it and/or modify it under the\n"\
        "terms of the Do What The Fuck You Want To Public License, Version 2,\n"\
        "as published by Sam Hocevar. See http://www.wtfpl.net/ for more details." % datetime.now().year

    verbose_version="%s %s\n\n%s" % (me, version, license)
    
    description="Get Image's Dominant Colors."

    format_help = "Format:\n"\
                  "The following variables can be used in FORMAT:\n"\
                  "\tWhen --group-by-name is NOT set:\n"\
                  "\t\t%r - red channel\n" \
                  "\t\t%g - green channel\n" \
                  "\t\t%b - blue channel\n" \
                  "\t\t%c - RGB representation (e.g., (255, 255, 255))\n" \
                  "\t\t%h - RGB hexadecimal representation (lower case) (e.g., #ffffff)\n" \
                  "\t\t%H - RGB hexadecimal representation (upper case) (e.g., #FFFFFF)\n" \
                  "\t%n - name (e.g: white)\n" \
                  "\t%p - percentage\n"\
                  "\n"\
                  "(If you want to use escaped characters (e.g., '\\t')\n"\
                  "from the shell, precede format by '$' (e.g., $'%n\\t%p')."
              

    epilog = "\n".join([format_help])

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description=description,
                                     epilog=epilog)
    parser.add_argument("--version", action="version",
                        version="%(prog)s {version}\n\n{license}".format(version=version, license=license))

    parser.add_argument("all_images", metavar="IMG", type=str, nargs='+')
    parser.add_argument("-c", "--count", metavar="N", dest="display_color_count", type=int, nargs=1,
                        help="only display the first N dominant colors.\n"\
                        "(0 means each one)\n"\
                        "(Default %d)" % display_color_count)
    parser.add_argument("-f", "--format", metavar="FORMAT", dest="display_color_format", type=str, nargs=1,
                        help="format to display each color.\n(See format's help below)\n"\
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
    parser.add_argument("-P", "--palette", dest="palette", type=str, nargs=1, choices=all_palettes.keys(),
                        help="which color palette to use.\n"\
                        "(Default %s)" % palette_name)

    argcomplete.autocomplete(parser, always_complete_options="long")
    args = parser.parse_args()

    all_images_count = len(args.all_images)
    
    if (all_images_count > 1):
        prepend_filename = True
    
    if (not args.display_color_count is None):
        display_color_count = args.display_color_count[0]

        if (display_color_count < 0):
            eprint("-c/--count: COUNT must be >= 0.")
            quit()

    if (not args.group_by_name is None):
        group_by_name = True
        display_color_format = "%p\t%n"
    
    if (not args.display_color_format is None):
        display_color_format = args.display_color_format[0]

    if (not args.color_bits is None):
        color_bits = args.color_bits[0]

        if ((color_bits < 1) or
            (color_bits > 8)):
            eprint("-b/--bits: COUNT must be > 1 and <= 8.")
            quit()

    if (not args.pixels_percentage is None):
        pixels_percentage = args.pixels_percentage[0] * 1.0 / 100
        
        if ((pixels_percentage <= 0) or (pixels_percentage > 1)):
            eprint("-p/--percentage: N must be > 0 and <= 100.")
            quit()

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

    palette = all_palettes[palette_name]
    color_map = {}
    pixel_count = 0
    filename_index = 0
    
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

        if (not random):
            for y in numpy.linspace(0, height, num=int(height * sqrt(pixels_percentage)), endpoint=False):
                for x in numpy.linspace(0, width, num=int(width * sqrt(pixels_percentage)), endpoint=False):
                    red, green, blue = pixels[int(x), int(y)]

                    color_key = ((((red & color_mask) * 256) +
                                  (green & color_mask)) * 256 + 
                                 (blue & color_mask))

                    try:
                        color_map[color_key] += 1
                    except:
                        color_map[color_key] = 1
        else:
            all_y = numpy.linspace(0, height, num=height, endpoint=False)
            all_x = numpy.linspace(0, width, num=width, endpoint=False)

            numpy.random.shuffle(all_y)
            numpy.random.shuffle(all_x)

            all_y = sorted(all_y[:int(height * sqrt(pixels_percentage))])
            all_x = sorted(all_x[:int(width * sqrt(pixels_percentage))])

            for y in all_y:
                for x in all_x:
                    red, green, blue = pixels[int(x), int(y)]

                    color_key = ((((red & color_mask) * 256) +
                                  (green & color_mask)) * 256 + 
                                 (blue & color_mask))

                    try:
                        color_map[color_key] += 1
                    except:
                        color_map[color_key] = 1

        if (not cumulative):
            sort_and_print_colors(color_map, palette, group_by_name,
                                  display_color_count, display_color_format,
                                  prepend_filename, filename)
            
            filename_index += 1

            if (filename_index < (all_images_count - 1)):
                print("")

            color_map = {}
            
            
    if (cumulative):
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
