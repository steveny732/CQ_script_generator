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
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {
        'D_SC-80': Pkg_params( # from http://www.infineon.com/dgdl/SCD80-Package_Overview.pdf?fileId=5546d462580663ef0158069ef94f041e
        the = 4.0,      # body angle in degrees
        c = 0.13,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 0.8,       # body length
        E1 = 1.3,       # body width
        E = 1.7,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.7,  # body height
        b = 0.3,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_SC-80', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
        'D_SOD-123F': Pkg_params( # from http://www.nxp.com/documents/outline_drawing/SOD123F.pdf
        the = 4.0,      # body angle in degrees
        c = 0.2,        # pin thickness, body center part height
        L = 0.9,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 2.6,       # body width
        E = 3.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.65,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_SOD-123F', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
        'D_SOD-523': Pkg_params( # from http://www.nxp.com/documents/outline_drawing/SOD523.pdf
        the = 4.0,      # body angle in degrees
        c = 0.17,        # pin thickness, body center part height
        L = .55,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = .85,       # body length
        E1 = 1.25,       # body width
        E = 1.65,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.65,  # body height
        b = 0.3,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_SOD-523', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
        'D_SOD-923': Pkg_params( # from https://www.nxp.com/docs/en/package-information/SOD923.pdf
        the = 4.0,      # body angle in degrees
        c = 0.12,        # pin thickness, body center part height
        L = 0.15,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.25,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 0.6,       # body length
        E1 = 0.8,       # body width
        E = 1.,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.37,  # body height
        b = 0.2,  # pin width
        e = 0.9,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e all_params_sod
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_SOD-923', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
        'D_TUMD2': Pkg_params( # from http://rohmfs.rohm.com/en/products/databook/package/spec/discrete/diodepkg.pdf
        the = 4.0,      # body angle in degrees
        c = 0.17,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = False,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.4,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.01,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.3,       # body length
        E1 = 1.9,       # body width
        E = 2.5,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.02,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.8,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 1,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (0.8, 0.4, 0.0, 0.0, 0.0, '+topin'), #
        #epad = (0.8, 0.4, 0.0, '-topin', 0.0), #
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'D_TUMD2', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/Diodes_SMD'
        ),
}