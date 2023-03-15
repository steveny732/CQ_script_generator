# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating fw_x models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author s. yoder
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions
# import importlib
# print("Import cq_parameters_fw_x.py")
# import Params
# importlib.reload(Params)
from Params import *

class SeriesParams():

    lib_name = "FW"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"
    ink_thickness = .001

pkg_defs = {
    'DEV_1_8pins': Pkg_params(                  # from http://www.???
    the = 9.0,                              # body angle in degrees
    tb_s = 0.15,                            # top part of body is that much smaller
    c = 0.1,                                # pin thickness, body center part height
    R1 = 0.1,                               # pin upper corner, inner radius
    R2 = 0.1,                               # pin lower corner, inner radius
    S = 0.30,                               # pin top flat part length (excluding corner arc)
    L = 0.65,                               # pin bottom flat part length (including corner arc)
    fp_s = True,                            # True for circular pinmark, False for square pinmark (useful for diodes)
    fp_r = 0.6,                             # first pin indicator radius
    fp_d = 0.05,                            # first pin indicator distance from edge
    fp_z = 0.05,                            # first pin indicator depth
    ef = 0.0,                               # fillet of edges  Note: bigger bytes model with fillet
    cc1 = 0.25,                             # chamfer of the 1st pin corner
    cc = 0.15,                              # chamfer of the other pin corners
    D1 = 12.,                               # body length
    E1 = 6.,                                # body width
    E = 10.0,                               # body overall width
    A1 = 0.1,                               # body-board separation
    A2 = 2.1,                               # body height
    b = 0.38,                               # pin width
    e = 1.27,                               # pin (center-to-center) distance
    npx = 4,                                # number of pins along X axis (width)
    npy = 0,                                # number of pins along y axis (length)
    epad = None,                            # e Pad
    excluded_pins = None,                   # no pin excluded
    body_color_key = "black body",          # body color
    pins_color_key = "metal grey pins",     # pins color
    mark_color_key = "light brown label",   # marker color
    modelName = 'DEV_1_8pins',              # modelName
    rotation = 0,                           # rotation if required
    dest_dir_prefix = '/FW_x'               # destination sub directory
    ),
    'DEV_2_10_pins': Pkg_params(                 # from http://www.???
    the = 9.0,                              # body angle in degrees
    tb_s = 0.15,                            # top part of body is that much smaller
    c = 0.1,                                # pin thickness, body center part height
    R1 = 0.1,                               # pin upper corner, inner radius
    R2 = 0.1,                               # pin lower corner, inner radius
    S = 0.30,                               # pin top flat part length (excluding corner arc)
    L = 0.65,                               # pin bottom flat part length (including corner arc)
    fp_s = True,                            # True for circular pinmark, False for square pinmark (useful for diodes)
    fp_r = 0.6,                             # first pin indicator radius
    fp_d = 0.05,                            # first pin indicator distance from edge
    fp_z = 0.05,                            # first pin indicator depth
    ef = 0.0,                               # fillet of edges  Note: bigger bytes model with fillet
    cc1 = 0.25,                             # chamfer of the 1st pin corner
    cc = 0.25,                              # chamfer of the other pin corners
    D1 = 12.,                               # body length
    E1 = 6.,                                # body width
    E = 10.0,                               # body overall width
    A1 = 0.1,                               # body-board separation
    A2 = 2.1,                               # body height
    b = 0.38,                               # pin width
    e = 1.27,                               # pin (center-to-center) distance
    npx = 5,                                # number of pins along X axis (width)
    npy = 0,                                # number of pins along y axis (length)
    epad = None,                            # e Pad
    excluded_pins = None,                   # no pin excluded
    body_color_key = "black body",          # body color
    pins_color_key = "metal grey pins",     # pins color
    mark_color_key = "light brown label",   # marker color
    modelName = 'DEV_2_10_pins',             # modelName
    rotation = 0,                           # rotation if required
    dest_dir_prefix = '/FW_x'               # destination sub directory
    ),
    'DEV_3_params': Pkg_params(                 # from http://www.???
    the = 9.0,                              # body angle in degrees
    tb_s = 0.15,                            # top part of body is that much smaller
    c = 0.1,                                # pin thickness, body center part height
    R1 = 0.1,                               # pin upper corner, inner radius
    R2 = 0.1,                               # pin lower corner, inner radius
    S = 0.30,                               # pin top flat part length (excluding corner arc)
    L = 0.65,                               # pin bottom flat part length (including corner arc)
    fp_s = True,                            # True for circular pinmark, False for square pinmark (useful for diodes)
    fp_r = 0.6,                             # first pin indicator radius
    fp_d = 0.05,                            # first pin indicator distance from edge
    fp_z = 0.05,                            # first pin indicator depth
    ef = 0.0,                               # fillet of edges  Note: bigger bytes model with fillet
    cc1 = 0.25,                             # chamfer of the 1st pin corner
    cc = 0.25,                              # chamfer of the other pin corners
    D1 = 12.,                               # body length
    E1 = 6.,                                # body width
    E = 10.0,                               # body overall width
    A1 = 0.1,                               # body-board separation
    A2 = 2.1,                               # body height
    b = 0.38,                               # pin width
    e = 1.27,                               # pin (center-to-center) distance
    npx = 6,                                # number of pins along X axis (width)
    npy = 0,                                # number of pins along y axis (length)
    epad = None,                            # e Pad
    excluded_pins = None,                   # no pin excluded
    body_color_key = "black body",          # body color
    pins_color_key = "metal grey pins",     # pins color
    mark_color_key = "light brown label",   # marker color
    modelName = 'DEV_3_pkg',                # modelName
    rotation = 0,                           # rotation if required
    dest_dir_prefix = '/FW_x'               # destination sub directory
    ),
}