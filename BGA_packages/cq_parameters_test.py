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

import importlib
print("Import cq_parameters_test.py")
import Params
importlib.reload(Params)
from Params import *

global typ_fil
global typ_cham
typ_fil = 1
typ_cham = 2

class SeriesParams():
    # footprint_dir="Housings_BGA.pretty"
    # lib_name = "Housings_BGA"

    lib_name = "Test"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {
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
    # 'Texas_DSBGA-12_1.86x1.36mm_Layout4x3_P0.5mm': Pkg_params( # from http://www.ti.com/lit/ds/symlink/txs0104e.pdf page 29
    #     fp_r = 0.3,     # first pin indicator radius ***************BAD!!!!!
    #     fp_d = 0.01,    # first pin indicator distance from edge
    #     fp_z = 0.01,    # first pin indicator depth
    #     ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
    #     D = 1.36,       # body overall width
    #     E = 1.86,       # body overall length
    #     A1 = 0.17,      # body-board separation
    #     A = 0.625,      # body  overall height
    #     b = 0.23,       # ball pin width diameter with a small extra to obtain a union of balls and case
    #     e = 0.5,        # pin (center-to-center) distance
    #     npx = 3,        # number of pins along X axis (width)
    #     npy = 4,        # number of pins along y axis (length)
    #     excluded_pins = ("None",), #pins to exclude -> None or "internals"
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'Texas_DSBGA-12_1.86x1.36mm_Layout4x3_P0.5mm', #old_modelName
    #     rotation = -90, # rotation if required
    #     dest_dir_prefix = '/Non_Square',
    #     ),
    # 'Texas_MicroStar_Junior_BGA-12_4x3_2.0x2.5mm_Pitch0.5mm': Pkg_params( # from http://www.ti.com/lit/ds/symlink/txb0104.pdf
    #     fp_r = 0.3,     # first pin indicator radius CHECKED GOOD
    #     fp_d = 0.01,    # first pin indicator distance from edge
    #     fp_z = 0.01,    # first pin indicator depth
    #     ef = 0.0,       # 0.05,      # fillet of edges  Note: bigger bytes model with fillet
    #     D = 2.00,       # body overall length
    #     E = 2.50,       # body overall width
    #     A1 = 0.20,      # body-board separation
    #     A = 0.36,       # body  overall height
    #     b = 0.30,       # ball pin width diameter with a small extra to obtain a union of balls and case
    #     e = 0.5,        # pin (center-to-center) distance
    #     npx = 3,        # number of pins along X axis (width)
    #     npy = 4,        # number of pins along y axis (length)
    #     excluded_pins = ("None",), #pins to exclude -> None or "internals"
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm', #old_modelName
    #     rotation = -90, # rotation if required
    #     dest_dir_prefix = '/Non_Square',
    #     ),
    # 'BGA-625_25x25_27.0x27.0mm_Pitch1.0mm': Pkg_params( # from http://www.analog.com/media/en/technical-documentation/data-sheets/ADSP-TS101S.pdf
    #     the2 = 15.,      # angle of top
    #     cb1 = 0.,        # 0.5 chamfer of the 1st pin corner
    #     cb = -0.75,      # 0.5 chamfer of the others corner
    #     tp_tct = typ_fil,  # top corner type
    #     ct1 = 2.,        # 0.5 chamfer of the 1st pin corner
    #     ct = 2.,         # 0.5 chamfer of the others corner
    #     D = 27.0,        # body overall length
    #     E = 27.0,        # body overall width
    #     D1 = 24.0,       # top body overall length
    #     E1 = 24.0,       # top body overall width
    #     A1 = 0.40,       # body-board separation
    #     A2 = .55,        # body bottom height optional, needed for molded
    #     A  = 2.5,        # body overall height
    #     b = 0.6,         # ball pin width diameter with a small extra to obtain a union of balls and case
    #     e = 1.0,         # pin (center-to-center) distance
    #     npx = 25,        # number of pins along X axis (width)
    #     npy = 25,        # number of pins along y axis (length)
    #     excluded_pins = ("internals",),   #"internals", #pins to exclude -> None or "internals"
    #     body_color_key = "green body",    # body color
    #     body_top_color_key = "black body",# body top color
    #     modelName = 'BGA-625_21.0x21.0mm_Layout25x25_P1.0mm',
    #     rotation = -90,   # rotation if required
    #     dest_dir_prefix = '',
    #     ),
}