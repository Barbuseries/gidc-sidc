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
    # TODO: Add colors and/or different palettes.
    palette = {
        "blue": [0, 0, 255],
        "black": [0, 0, 0],
        "cyan": [0, 255, 255],
        "gray": [128,128,128],
        "green": [0, 255, 0],
        "lime": [0,255,0],
        "magenta": [255, 0, 255],
        "maroon": [128,0,0],
        "navy": [0,0,128],
        "olive": [128,128,0],
        "purple": [128,0,128],
        "red": [255, 0, 0],
        "silver": [192,192,192],
        "teal": [0,128,128],
        "white": [255, 255, 255],
        "yellow": [255, 255, 0],
    }


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

    color_map = {}
    pixel_count = 0
    filename_index = 0
    
    for filename in args.all_images:
        color_byte_shift = 8 - color_bits

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
