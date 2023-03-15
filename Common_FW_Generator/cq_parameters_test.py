# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating test models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author s. yoder
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions
import importlib
print("Import cq_parameters_test.py")
import Params
importlib.reload(Params)
from Params import *

class SeriesParams():
    lib_name = "Test"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"
    ink_thickness = .001

pkg_defs = {
        'D_PowerDI-123': Pkg_params( # from http://www.diodes.com/_files/datasheets/ds30497.pdf
        the = 4.0,      # body angle in degrees
        c = 0.2,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.6,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 3.0,       # body length
        E1 = 1.93,       # body width
        E = 2.83,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.02,  # body-board separation
        A2 = 0.98,  # body height
        b = 1.0,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 0,   # number of pins along X axis (width)
        npy = 1,   # number of pins along y axis (length)
        epad = (1.35, 1.1, 0.0, '-topin', 0.0), # e all_params_sod
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_PowerDI-123', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
    # 'LQFP-32-1EP_5x5mm_Pitch0.5mm': Pkg_params(
    # #from http://www.nxp.com/documents/outline_drawing/SOT401-1.pdf
    #     the = 12.0,           # body angle in degrees
    #     tb_s = 0.15,          # top part of body is that much smaller
    #     c = 0.15,             # pin thickness, body center part height
    #     R1 = 0.1,             # pin upper corner, inner radius
    #     R2 = 0.1,             # pin lower corner, inner radius
    #     S = 0.2,              # pin top flat part length (excluding corner arc)
    #     L = 0.6,              # pin bottom flat part length (including corner arc)
    #     fp_s = True,          # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.5,           # first pin indicator radius
    #     fp_d = 0.2,           # first pin indicator distance from edge
    #     fp_z = 0.1,           # first pin indicator depth
    #     ef = 0,               # 0.05, # fillet of edges  Note: bigger bytes model with fillet
    #     cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
    #     cc = 0.25,            # 0.45 chamfer of the other pin corners
    #     D1 = 5.0,             # body length
    #     E1 = 5.0,             # body width
    #     E = 7.0,              # body overall width  E=E1+2*(S+L+c)
    #     A1 = 0.1,             # body-board separation
    #     A2 = 1.4,             # body height
    #     b = 0.22,             # pin width
    #     e = 0.5,              # pin (center-to-center) distance
    #     npx = 8,              # number of pins along X axis (width)
    #     npy = 8,              # number of pins along y axis (length)
    #     epad = (3.45,3.45),   # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    #     excluded_pins = None, # no pin excluded
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'LQFP-32-1EP_5x5mm_P0.5mm', #modelName
    #     rotation = -90, # rotation if required
    #     dest_dir_prefix = '',
    # ),
    # 'OnSemi_Micro8': Pkg_params( # from https://www.onsemi.com/pub/Collateral/846A-02.PDF
    #     the = 12.0,           # body angle in degrees
    #     tb_s = 0.15,          # top part of body is that much smaller
    #     c = 0.18,             # pin thickness, body center part height
    #     R1 = 0.05,             # pin upper corner, inner radius
    #     R2 = 0.05,             # pin lower corner, inner radius
    #     S = 0.25,              # pin top flat part length (excluding corner arc)
    #     L = 0.64,            # pin bottom flat part length (including corner arc)
    #     fp_s = True,        # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.5,           # first pin indicator radius
    #     fp_d = 0.2,           # first pin indicator distance from edge
    #     fp_z = 0.1,           # first pin indicator depth
    #     ef = 0, # 0.05,       # fillet of edges  Note: bigger bytes model with fillet
    #     cc1 = 0.25,           # 0.45 chamfer of the 1st pin corner
    #     cc = 0.25,           # 0.45 chamfer of the other pin corners
    #     D1 = 3.0,             # body length
    #     E1 = 3.0,             # body width
    #     E = 4.9,              # body overall width  E=E1+2*(S+L+c)
    #     A1 = 0.1,            # body-board separation
    #     A2 = 0.85,             # body height
    #     b = 0.33,             # pin width
    #     e = 0.65,            # pin (center-to-center) distance
    #     npx = 4,             # number of pins along X axis (width)
    #     npy = 0,              # number of pins along y axis (length)
    #     epad = None,          # ePad is guessed from datasheet
    #     excluded_pins = None, # no pin excluded
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'OnSemi_Micro8',
    #     rotation = -90.,       # rotation if required
    #     dest_dir_prefix = '',
    #     ),
    # 'D_SOD-123': Pkg_params( # from https://www.diodes.com/assets/Package-Files/SOD123.pdf
    #     the = 7.0,      # body angle in degrees
    #     tb_s = 0.0,    # top part of body is that much smaller
    #     c = 0.11,        # pin thickness, body center part height
    #     R1 = 0.11,       # pin upper corner, inner radius
    #     R2 = 0.11,       # pin lower corner, inner radius
    #     S = 0.0,       # pin top flat part length (excluding corner arc)
    #     L = 0.3,       # pin bottom flat part length (including corner arc)
    #     fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.5,     # first pin indicator radius
    #     fp_d = 0.2,     # first pin indicator distance from edge
    #     fp_z = 0.01,     # first pin indicator depth
    #     ef = 0.1, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
    #     cc1 = 0.12, #0.45 chamfer of the 1st pin corner
    #     cc = 0.06, #0.45 chamfer of the other pin corners
    #     D1 = 1.55,       # body length
    #     E1 = 2.65,       # body width
    #     E = 3.65,        # body overall width  E=E1+2*(S+L+c)
    #     A1 = 0.05,  # body-board separation
    #     A2 = 1.,  # body height
    #     b = 0.57,  # pin width
    #     e = 1.27,  # pin (center-to-center) distance
    #     npx = 1,   # number of pins along X axis (width)
    #     npy = 0,   # number of pins along y axis (length)
    #     epad = None, # e all_params_sod
    #     excluded_pins = None, #no pin excluded
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'D_SOD-123', #modelName
    #     rotation = 0, # rotation if required
    #     dest_dir_prefix = '',
    #     ),
    # 'D_SOD-323': Pkg_params( # from https://www.diodes.com/assets/Package-Files/SOD323.pdf
    #     the = 7.0,      # body angle in degrees
    #     tb_s = 0.,    # top part of body is that much smaller
    #     c = 0.11,        # pin thickness, body center part height
    #     R1 = 0.05,       # pin upper corner, inner radius
    #     R2 = 0.05,       # pin lower corner, inner radius
    #     S = 0.0,       # pin top flat part length (excluding corner arc)
    #     L = 0.3,       # pin bottom flat part length (including corner arc)
    #     fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.4,     # first pin indicator radius
    #     fp_d = 0.15,     # first pin indicator distance from edge
    #     fp_z = 0.01,     # first pin indicator depth
    #     ef = 0.05, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
    #     cc1 = 0.12, #0.45 chamfer of the 1st pin corner
    #     cc = 0.06, #0.45 chamfer of the other pin corners
    #     D1 = 1.3,       # body length
    #     E1 = 1.7,       # body width
    #     E = 2.5,        # body overall width  E=E1+2*(S+L+c)
    #     A1 = 0.1,  # body-board separation
    #     A2 = 1.0,  # body height
    #     b = 0.35,  # pin width
    #     e = 1.27,  # pin (center-to-center) distance
    #     npx = 1,   # number of pins along X axis (width)
    #     npy = 0,   # number of pins along y axis (length)
    #     epad = None, # e all_params_sod
    #     excluded_pins = None, #no pin excluded
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'D_SOD-323', #modelName
    #     rotation = 0, # rotation if required
    #     dest_dir_prefix = '',
    #     ),
    # 'TEST_1': Pkg_params(                       # from http://www.???
    #     the = 9.0,                              # body angle in degrees
    #     tb_s = 0.15,                            # top part of body is that much smaller
    #     c = 0.2,                                # pin thickness, body center part height
    #     R1 = 0.1,                               # pin upper corner, inner radius
    #     R2 = 0.1,                               # pin lower corner, inner radius
    #     S = 0.1,                               # pin top flat part length (excluding corner arc)
    #     L = 1.5,                               # pin bottom flat part length (including corner arc)
    #     fp_s = True,                           # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.,                             # first pin indicator radius
    #     fp_d = 0.05,                            # first pin indicator distance from edge
    #     fp_z = 0.05,                            # first pin indicator depth
    #     ef = 0.0,                               # fillet of edges ... if tuple (top fillet,bottom fillet,[edge_type])
    #     cc1 = 0.25,                             # chamfer of the 1st pin corner, if tuple (chamf,edge_type)
    #     cc = 0.15,                              # chamfer of the other pin corners, if tuple (chamf,edge_type)
    #     D1 = 12.,                               # body length
    #     E1 = 6.,                                # body width
    #     E = 10.0,                               # body overall width
    #     A1 = 0.2,                               # body-board separation
    #     A2 = 2.1,                               # body height
    #     b = 0.6,                                # pin width
    #     e = (1.75,1.5),                         # pin (center-to-center) distance
    #     npx = 6,                                # number of pins along X axis (width)
    #     npy = 3,                                # number of pins along y axis (length)
    #     epad = (2.5,2.,.3,0.),           # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    #     excluded_pins = (2,8,11,),              # list of excluded pins
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'TST_1',                    # modelName
    #     rotation = 0,                           # rotation if required
    #     text_defs = {
    #         'Line_1': Txt_params(
    #             txt = "RS1MT\nE1 YYWW",
    #             fsize = 1.,
    #             loc = (1.75, .75),
    #             valign = 'top',
    #             ink_color_key = "white body",
    #             ink_thickness = .1,
    #         ),
    #         'Line_2': Txt_params(
    #             dot = (.5, 1.75, 3.5),
    #             ink_color_key = "white body",
    #             ink_thickness = .05,
    #         ),
    #         'Line_3': Txt_params(
    #             txt = "C X X",
    #             fsize = 1.,
    #             loc = (3.2,3.3),
    #             valign = 'center',
    #             ink_color_key = "white body",
    #         ),
    #     },
    #     dest_dir_prefix = '/FW'               # destination sub directory
    # ),
    # 'TEST_2': Pkg_params(                       # from http://www.???
    #     the = 9.0,                              # body angle in degrees
    #     tb_s = 0.15,                            # top part of body is that much smaller
    #     c = 0.3,                                # pin thickness, body center part height
    #     # R1 = 0.1,                              # pin upper corner, inner radius
    #     # R2 = 0.1,                              # pin lower corner, inner radius
    #     # S = 0.30,                              # pin top flat part length (excluding corner arc)
    #     L = 1.5,                                # pin bottom flat part length (including corner arc)
    #     fp_s = False,                           # True for circular pinmark, False for square pinmark (useful for diodes)
    #     fp_r = 0.,                             # first pin indicator radius
    #     fp_d = 0.05,                            # first pin indicator distance from edge
    #     fp_z = 0.05,                            # first pin indicator depth
    #     ef = 0.0,                               # fillet of edges  Note: bigger bytes model with fillet
    #     cc1 = 0.25,                             # chamfer of the 1st pin corner
    #     cc = 0.15,                              # chamfer of the other pin corners
    #     D1 = 12.,                               # body length
    #     E1 = 6.,                                # body width
    #     D = 14.,                                # body overall width
    #     E = 8.0,                               # body overall width
    #     A1 = 0.05,                              # body-board separation
    #     A2 = 2.1,                               # body height
    #     b = 0.6,                                # pin width
    #     e = (1.75,1.5),                         # pin (center-to-center) distance
    #     npx = 6,                                # number of pins along X axis (width)
    #     npy = 3,                                # number of pins along y axis (length)
    #     epad = (2.5,2.,.3),              # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    #     excluded_pins = (2,8,11,),              # list of excluded pins
    #     body_color_key = "dark grey body",      # body color
    #     pins_color_key = "gold pins",           # pins color
    #     mark_color_key = "light brown label",   # marker color
    #     modelName = 'TST_2',                    # modelName
    #     rotation = 0,                           # rotation if required
    #     text_defs = {
    #         'Line_1': Txt_params(
    #             txt = "RS1MT\nE1 YYWW",
    #             fsize = 1.,
    #             loc = (1.75, .75),
    #             valign = 'top',
    #             ink_color_key = "white body",
    #             ink_thickness = .1,
    #         ),
    #         'Line_2': Txt_params(
    #             dot = (.5, 1.75, 3.5),
    #             ink_color_key = "white body",
    #             ink_thickness = .05,
    #         ),
    #         'Line_3': Txt_params(
    #             txt = "C X X",
    #             fsize = 1.,
    #             loc = (3.2,3.3),
    #             valign = 'center',
    #             ink_color_key = "white body",
    #         ),
    #     },
    #     dest_dir_prefix = '/FW'                 # destination sub directory
    # ),
}