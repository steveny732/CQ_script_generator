# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating QFP/GullWings models in X3D format.
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

    lib_name = "SOT"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {
    'SOT23_6': Pkg_params( # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 3.1,       # body length
        E1 = 1.8,       # body width
        E = 2.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.35,  # body height
        b = 0.40,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'sot23_6_18x29_p095', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT23_3': Pkg_params( # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.0,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 3.0,       # body length
        E1 = 1.4,       # body width
        E = 2.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.40,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2,4,6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'sot23_3_25x30_p095', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT23_5': Pkg_params( # 1.8x3.1, pitch 0.95 5pin 1.45mm height
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 3.1,       # body length
        E1 = 1.8,       # body width
        E = 2.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.35,  # body height
        b = 0.40,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'sot23_5_18x29_p095', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '',
        ),
    'SC70_3': Pkg_params( # 1.8x3.1, pitch 0.95 6pin 1.45mm height
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.2,       # body length
        E1 = 1.35,       # body width
        E = 2.2,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.35,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2,4,6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'sc70_3_22x22_p065', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '',
        ),
}
