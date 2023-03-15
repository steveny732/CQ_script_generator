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
from Params import *

global typ_fil
global typ_cham
typ_fil = 1
typ_cham = 2

class SeriesParams():

    lib_name = "Test"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {       ## Dictionary of Package Paramters ##
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
        text_defs = {
            'DOT': Txt_params(
                dot = (.5, .2, 19.,-1.03),
                ink_color_key = "white body",
                rotation = 90.,
            ),
            'TEXT': Txt_params(
                txt = "XILINX",
                fsize = 2.5,
                loc = (5.,8.),
                ink_color_key = "white body",
            ),
        },
        dest_dir_prefix = '/plastic_top',
        ),

    # 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.5mm': Pkg_params( # from https://www.fujitsu.com/uk/Images/MB85RS1MT-DS501-00022-7v0-E.pdf
    #     fp_r = -0.2,       # first pin indicator radius (Negative for square)
    #     # fp_d = (fp_x,fp_y) where fp_y is E/2 - fp_x
    #     fp_d = (0.11, 1.039), # first pin indicator distance from edge (Negative for bottom of chip)
    #     fp_z = -0.025,       # first pin indicator depth (tupple for x,y coordinates)
    #     D = 3.09,          # body overall length
    #     E = 2.28,          # body overall width
    #     A1 = 0.08,         # body-board separation
    #     A = 0.33,          # body  overall height
    #     b = 0.23,          # ball pin width diameter with a small extra to obtain a union of balls and case
    #     e = 0.3,           # pin (center-to-center) distance
    #     ex = 0.4,          # pin (center-to-center) distance
    #     npx = 5,           # number of pins along X axis (width)
    #     npy = 3,           # number of pins along y axis (length)
    #     excluded_pins = (2, 4, 6, 8, 10, 12, 14), # pins to exclude -> None or "internals"
    #     mark_color_key = "no color",   # marker color
    #     modelName = 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.5mm',
    #     rotation = -90,   # rotation if required
    #     text_defs = {
    #         'Line_1': Txt_params(
    #             txt = "RS1MT\nE1 YYWW",
    #             fsize = .5,
    #             loc = (.3, .4),
    #             ink_color_key = "white body",
    #         ),
    #         'Line_2': Txt_params(
    #             dot = (.2, .5, 1.3),
    #             ink_color_key = "white body",
    #         ),
    #         'Line_3': Txt_params(
    #             txt = "C X X",
    #             fsize = .5,
    #             loc = (1.2,.9),
    #             ink_color_key = "white body",
    #         ),
    #     },
    #     dest_dir_prefix = '/Non_Square/WLP',
    #     ),
}