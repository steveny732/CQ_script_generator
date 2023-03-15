#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating BGA models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions

#import importlib
from Params import *

global typ_fil
global typ_cham
typ_fil = 1
typ_cham = 2

class SeriesParams():

    lib_name = "Package_BGA"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"


pkg_defs = {      ## Dictionary of Package Paramters ##
    'BGA-48_8x6mm_Layout8x6_P0.75mm': Pkg_params( # from https://www.mouser.com/datasheet/2/954/anv22a88a-1774275.pdf
        fp_r = 0.4,     # first pin indicator radius CHECKED GOOD
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 8.0,       # body overall length
        E = 6.0,       # body overall width
        A1 = 0.25,  # body-board separation
        A = 1.27,  # body height
        b = 0.35,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.75,  # pin (center-to-center) distance
        npx = 8,  # number of pins along X axis (width)
        npy = 6,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        modelName = 'BGA-48_8x6mm_Layout8x6_P0.75mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '/Non_Square',
        ),
    'BGA-9_3x3_1.6x1.6mm_Pitch0.5mm': Pkg_params( # from http://www.ti.com/lit/ds/symlink/bq27421-g1.pdf
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.04,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.6,       # body overall length
        E = 1.6,       # body overall width
        A1 = 0.25,  # body-board separation
        A = 0.625,  # body  overall height
        b = 0.3,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,  # number of pins along X axis (width)
        npy = 3,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'BGA-9_1.6x1.6mm_Layout3x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'Maxim_WLP-12': Pkg_params( # W121B2+1 from http://pdfserv.maximintegrated.com/package_dwgs/21-0009.PDF
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.04,    # first pin indicator distance from edge
        fp_z = 0.01,    # first pin indicator depth
        ef = 0.0    , 	# 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.6,       	# body overall length
        E = 2.0,       	# body overall width
        A1 = 0.24,  	# body-board separation
        A = 0.64,  		# body  overall height
        b = 0.31,  		# ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,  		# pin (center-to-center) distance
        npx = 3,  		# number of pins along X axis (width)
        npy = 4,  		# number of pins along y axis (length)
        excluded_pins = ("None",), #pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'Maxim_WLP-12', #old_modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/WLP',
        ),
    'BGA-400_20x20_21.0x21.0mm_Pitch1.0mm': Pkg_params( # from https://www.xilinx.com/support/documentation/package_specs/fg400.pdf
        the2 = 30.,      # angle of top
        cb1 = 0.,        # 0.5 chamfer of the 1st pin corner
        cb = -0.75,      # 0.5 chamfer of the others corner
        tp_tct = typ_cham,  # top corner type
        ct1 = 2.,        # 0.5 chamfer of the 1st pin corner
        ct = 2.,         # 0.5 chamfer of the others corner
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.2,     # first pin indicator distance from edge
        fp_z = 0.1,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 21.0,       # body overall length
        E = 21.0,       # body overall width
        D1 = 19.2,       # top body overall length
        E1 = 19.2,       # top body overall width
        A1 = 0.50,  # body-board separation
        A2 = 0.60,  # body bottom height optional, needed for molded
        A  = 2.23,  # body  overall height
        b = 0.6,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.0,  # pin (center-to-center) distance
        npx = 20,  # number of pins along X axis (width)
        npy = 20,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #"internals", #pins to exclude -> None or "internals"
        body_color_key = "green body",      # body color
        body_top_color_key = "black body",# body top color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "gold pins",   # marker color
        modelName = 'BGA-400_21.0x21.0mm_Layout20x20_P1.0mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '/plastic_top',
        ),
    'BGA-352_26x26_35.0x35.0mm_Pitch1.27mm': Pkg_params( # from https://www.fujitsu.com/downloads/MICRO/fma/pdfmcu/b352p05.pdf
        cb1 = -0.75,     # chamfer of the bottom 1st pin corner
        cb = 0.,         # chamfer of the other bottom corners
        tp_bct = typ_cham,  # bottom corner type
        D = 35.0,        # body overall length
        E = 35.0,        # body overall width
        ct1 = 2.,        # chamfer of the bottom 1st pin corner
        ct = 2.,         # chamfer of the other bottom corners
        D1 = 25.0,       # top body overall length
        E1 = 25.0,       # top body overall width
        A1 = 0.6,        # body-board separation
        A2 = 2.0,        # body bottom height optional, needed for molded
        A  = 3.1,        # body  overall height
        b = 0.6,         # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 1.27,        # pin (center-to-center) distance
        npx = 26,        # number of pins along X axis (width)
        npy = 26,        # number of pins along y axis (length)
        excluded_pins = ("internals",),         #"internals", #pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        body_top_color_key = "metal copper",    # body top color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'BGA-352_35.0x35.0mm_Layout26x26_P1.27mm',
        rotation = -90,  # rotation if required
        dest_dir_prefix = '/metal_top',
        ),
    'BGA-324_15.0x15.0mm_Layout18x18_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD': Pkg_params( # from https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00474-02.pdf
        fp_r = 0.8,     # first pin indicator radius
        fp_d = 0.12,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0    , # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 15.0,       # body overall length
        E = 15.0,       # body overall width
        A1 = 0.4,  # body-board separation
        A = 1.40,  # body overall height
        b = 0.5,  # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.80,  # pin (center-to-center) distance
        npx = 18,  # number of pins along X axis (width)
        npy = 18,  # number of pins along y axis (length)
        excluded_pins = ("internals",), #pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'BGA-324_15.0x15.0mm_Layout18x18_P0.8mm_Ball0.5mm_Pad0.4mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD': Pkg_params(
        #
        # Altera MBGA-153, https://www.altera.com/content/dam/altera-www/global/en_US/pdfs/literature/packaging/04r00471-00.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 8.0,      # body overall length
        E = 8.0,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.3,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        npx = 15,      # number of pins along X axis (width)
        npy = 15,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'BGA-153_8.0x8.0mm_Layout15x15_P0.5mm_Ball0.3mm_Pad0.25mm_NSMD',
        rotation = -90, # rotation if required
        dest_dir_prefix = '/uBGA',
        ),
    'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm': Pkg_params(
        #
        # Texas Instruments, DSBGA, 0.9x1.4mm, 6 bump 2x3 (perimeter) array, NSMD pad definition (http://www.ti.com/lit/ds/symlink/ts5a3159a.pdf)
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm.kicad_mod
        # 
        fp_z = 0.2,     # first pin indicator depth CHECED GOOD
        fp_r = 0.2,          # First pin indicator radius
        fp_d = 0.1,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 1.4,      # body overall length
        E = 0.94,      # body overall width
        A1 = 0.025,      # body-board separation
        A = 0.75,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.5,       # pin (center-to-center) distance
        npx = 3,      # number of pins along X axis (width)
        npy = 2,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'Texas_DSBGA-6_0.9x1.4mm_Layout2x3_P0.5mm',
        rotation = -90, # rotation if required
        dest_dir_prefix = '/Non_Square/uBGA',
        ),
    'WLCSP-143,_5.849x4.539mm_Layout13x11_P0.4mm': Pkg_params(
        #
        # WLCSP-143, 11x13 raster, 4.539x5.849mm package, pitch 0.4mm;
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A and A1
        # 
        # The foot print that uses this 3D model is WLCSP-143 4.5x5mm_Layout11x13
        # 
        fp_z = 0.2,     # first pin indicator depth
        fp_r = 0.4,          # First pin indicator radius
        fp_d = 0.3,          # First pin indicator distance from edge
        ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
        D = 5.849,      # body overall width
        E = 4.539,      # body overall length
        A1 = 0.175,      # body-board separation
        A = .555,       # body overall height
        b = 0.25,      # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.4,       # pin (center-to-center) distance
        npx = 13,      # number of pins along X axis (width)
        npy = 11,      # number of pins along y axis (length)
        excluded_pins = ("internals",), # pins to exclude -> None or "internals"
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'WLCSP-143_5.8x4.5mm_Layout13x11_P0.4mm',
        rotation = -90, # rotation if required
        text_defs = {
            'Line_1': Txt_params(
                txt = "RS1MT\nE1 YYWW",
                fsize = .5,
                loc = (.3, .4),
            ),
            'Line_2': Txt_params(
                dot = (.2, .5, 1.3),
            ),
            'Line_3': Txt_params(
                txt = "C X X",
                fsize = .5,
                loc = (1.2,.9),
            ),
        },
        dest_dir_prefix = '/Non_Square/WLP',
        ),
    'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.5mm': Pkg_params( # from https://www.fujitsu.com/uk/Images/MB85RS1MT-DS501-00022-7v0-E.pdf
        fp_r = -0.2,       # first pin indicator radius (Negative for square)
        # fp_d = (fp_x,fp_y) where fp_y is E/2 - fp_x
        fp_d = (0.11, 1.039), # first pin indicator distance from edge (Negative for bottom of chip)
        fp_z = -0.025,       # first pin indicator depth (tupple for x,y coordinates)
        D = 3.09,          # body overall length
        E = 2.28,          # body overall width
        A1 = 0.08,         # body-board separation
        A = 0.33,          # body  overall height
        b = 0.23,          # ball pin width diameter with a small extra to obtain a union of balls and case
        e = 0.3,           # pin (center-to-center) distance
        ex = 0.4,          # pin (center-to-center) distance
        npx = 5,           # number of pins along X axis (width)
        npy = 3,           # number of pins along y axis (length)
        excluded_pins = (2, 4, 6, 8, 10, 12, 14), # pins to exclude -> None or "internals"
        mark_color_key = "no color",   # marker color
        modelName = 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.5mm',
        rotation = -90,   # rotation if required
        text_defs = {
            'Line_1': Txt_params(
                txt = "RS1MT\nE1 YYWW",
                fsize = .5,
                loc = (.3, .4),
            ),
            'Line_2': Txt_params(
                dot = (.2, .5, 1.3),
                ink_color_key = "white body",
            ),
            'Line_3': Txt_params(
                txt = "C X X",
                fsize = .5,
                loc = (1.2,.9),
            ),
        },
        dest_dir_prefix = '/Non_Square/WLP',
        ),
}
