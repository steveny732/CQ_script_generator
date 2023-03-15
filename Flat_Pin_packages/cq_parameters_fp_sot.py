# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating Flat Pin models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from Jedec MS-026D document.

## file of parametric definitions
print("Import cq_parameters_fp_sot.py")
from Params import *

class SeriesParams():

    lib_name = "SOT_SMD"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "metal grey pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {
	'DRT-3': Pkg_params( # from http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/sc70ks/ks_4.pdf
        the = 4.0,      # body angle in degrees
        c = 0.15,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.0,       # body length
        E1 = 0.8,       # body width
        E = 1.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.47,  # body height
        b = 0.2,  # pin width
        e = 0.35,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'DRT-3', #modelName
        rotation = 0, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'HVSOF5': Pkg_params( # from http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/hall/bu52002gul-e.pdf
        the = 4.0,      # body angle in degrees
        c = 0.13,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (0.8, 0.41), # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'HVSOF5', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'HVSOF6': Pkg_params( # from http://rohmfs.rohm.com/en/products/databook/datasheet/ic/audio_video/video_amplifier/bh76106hfv-e.pdf
        the = 4.0,      # body angle in degrees
        c = 0.145,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 2.6,       # body width
        E = 3.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.75,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (1.2, 1.5), # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'HVSOF6', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'SOT-543': Pkg_params( # from https://www.centralsemi.com/PDFS/CASE/SOT-543PD.PDF
        the = 4.0,      # body angle in degrees
        c = 0.12,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.55,  # body height
        b = 0.22,  # pin width
        e = 1.0,  # pin (center-to-center) distance
        npx = 2,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-543', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'SOT-665': Pkg_params( # from http://www.nxp.com/documents/outline_drawing/SOT665.pdf
        the = 4.0,      # body angle in degrees
        c = 0.13,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.55,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-665', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'SOT-666': Pkg_params( # from http://www.nxp.com/documents/outline_drawing/SOT666.pdf
        the = 4.0,      # body angle in degrees
        c = 0.13,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.55,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-666', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'SOT-963': Pkg_params( # from https://www.centralsemi.com/PDFS/CASE/SOT-963_PD.PDF
        the = 4.0,      # body angle in degrees
        c = 0.1,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.02,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.0,       # body length
        E1 = 0.8,       # body width
        E = 1.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.0,  # body-board separation
        A2 = 0.45,  # body height
        b = 0.15,  # pin width
        e = 0.35,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-963', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'TDSON-8-1': Pkg_params( # from http://www.infineon.com/dgdl/PG-TDSON-8-1,-2,-3-Package_Overview.pdf?fileId=db3a30431c69a49d011cdbc468254110
        the = 3.0,      # body angle in degrees
        c = 0.25,        # pin thickness, body center part height
#        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.3,     # first pin indicator radius
        fp_d = 0.3,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        L = 0.55, #length of pins, if None the pins will be the distance from the body to the overall length
        D1 = 5.15,       # body length
        E1 = 5.9,       # body width
        E = 6.15,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 1.0,  # body height
        b = 0.44,  # pin width
        e = 1.27,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = (4.2, 4.15, 0, 0, '-topin'), # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'TDSON-8-1', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
	'VSOF5': Pkg_params( # from http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/voltage_detector/bd48xxg-e.pdf
        the = 3.0,      # body angle in degrees
        c = 0.13	,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'VSOF5', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
    'SOT-553': Pkg_params( # from http://www.goodark.com/en/products/outline/s5779.html
        the = 3.0,      # body angle in degrees
        c = 0.11    ,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #pin 5 excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-553', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
    'SOT-563': Pkg_params( # from http://www.goodark.com/en/products/outline/s5779.html
        the = 3.0,      # body angle in degrees
        c = 0.11    ,        # pin thickness, body center part height
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.1,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        D1 = 1.6,       # body length
        E1 = 1.2,       # body width
        E = 1.6,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.03,  # body-board separation
        A2 = 0.6,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-563', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '/TO_SOT_Packages_SMD'
        ),
}
