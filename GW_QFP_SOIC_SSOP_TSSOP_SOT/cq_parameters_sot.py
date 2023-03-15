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

    lib_name = "Package_TO_SOT_SMD"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {
	'Analog_KS-4': Pkg_params( # from http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/sc70ks/ks_4.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.1,  # pin width
        e = 0.1,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (4,5,6,7,8,9,10,20,21,22,23,24,25,26,27,28,29), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'Analog_KS-4', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SC-59': Pkg_params( # from http://www.infineon.com/dgdl/SC59-Package_Overview.pdf?fileId=5546d462580663ef0158069ca21703c1
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
        D1 = 3.0,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.2,  # body height
        b = 0.4,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SC-59', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SC-70-8': Pkg_params( # from http://cds.linear.com/docs/en/packaging/SOT_8_05-08-1639.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.22,  # pin width
        e = 0.5,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SC-70-8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),

    'SOT-23': Pkg_params( # http://www.ti.com/lit/ml/mpds026k/mpds026k.pdf
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
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-23', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
	'SOT-23W': Pkg_params( 	# A1120ELHLX-T http://www.allegromicro.com/~/media/Files/Datasheets/A112x-Datasheet.ashx?la=en&hash=7BC461E058CC246E0BAB62433B2F1ECA104CA9D3
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.18,       # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.05,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,    # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,    # first pin indicator depth
        ef = 0.0, 		#0      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, 	#0.45 chamfer of the 1st pin corner
        cc = 0.12, 	#0.45 chamfer of the other pin corners
        D1 = 2.98,      # body length
        E1 = 1.91,      # body width
        E = 2.9,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.05,  	# body-board separation
        A2 = 0.95,  	# body height
        b = 0.4,  		# pin width
        e = 0.95,  		# pin (center-to-center) distance
        npx = 3,   		# number of pins along X axis (width)
        npy = 0,   		# number of pins along y axis (length)
        epad = None, 	# e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-23W', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
	'SOT-23-5': Pkg_params( # http://www.ti.com/lit/ml/mpds026k/mpds026k.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.45,  # body height
        b = 0.5,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-23-5', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),

    'SOT-23-6': Pkg_params( # http://www.ti.com/lit/ml/mpds026k/mpds026k.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.45,  # body height
        b = 0.5,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-23-6', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-23-8': Pkg_params( # http://www.ti.com/lit/ml/mpds099c/mpds099c.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.38,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-23-8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-143': Pkg_params( # http://www.nxp.com/documents/outline_drawing/SOT143B.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.38,  # pin width
        e = 0.38,  # pin (center-to-center) distance
        npx = 6,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (3,4,5,8,9,10,11), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-143', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-143R': Pkg_params( # http://www.nxp.com/documents/outline_drawing/SOT143R.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.1,  # body height
        b = 0.38,  # pin width
        e = 0.38,  # pin (center-to-center) distance
        npx = 6,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2,3,4,8,9,10,11), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-143R', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-223': Pkg_params( # http://www.nxp.com/documents/outline_drawing/SOT223.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.03,    # top part of body is that much smaller
        c = 0.27,        # pin thickness, body center part height
        R1 = 0.2,       # pin upper corner, inner radius
        R2 = 0.2,       # pin lower corner, inner radius
        S = 0.5,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.0,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.0, #0.45 chamfer of the 1st pin corner
        cc = 0.0, #0.45 chamfer of the other pin corners
        D1 = 6.5,       # body length
        E1 = 3.5,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.6,  # body height
        b = 0.7667,  # pin width
        e = 0.7667,  # pin (center-to-center) distance
        npx = 7,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2,3,5,6,8,9,13,14), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-223', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-323_SC-70': Pkg_params( # from http://www.ti.com/lit/ml/mpds114c/mpds114c.pdf
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
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-323_SC-70', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-343_SC-70-4': Pkg_params( # from http://www.ti.com/lit/ml/mpds114c/mpds114c.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 5), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-343_SC-70-4', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-353_SC-70-5': Pkg_params( # from http://www.ti.com/lit/ml/mpds114c/mpds114c.pdf
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
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-353_SC-70-5', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-363_SC-70-6': Pkg_params( # from http://www.ti.com/lit/ml/mpds114c/mpds114c.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.95,  # body height
        b = 0.3,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-363_SC-70-6', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TSOT-23': Pkg_params( # http://cds.linear.com/docs/en/packaging/SOT_6_05-08-1636.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.85,  # body height
        b = 0.35,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'TSOT-23', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TSOT-23-5': Pkg_params( # http://cds.linear.com/docs/en/packaging/SOT_6_05-08-1636.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.85,  # body height
        b = 0.35,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (5,), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'TSOT-23-5', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TSOT-23-6': Pkg_params( # http://cds.linear.com/docs/en/packaging/SOT_6_05-08-1636.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.85,  # body height
        b = 0.35,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'TSOT-23-6', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'TSOT-23-8': Pkg_params( # http://cds.linear.com/docs/en/packaging/SOT_8_05-08-1637.pdf
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
        D1 = 2.9,       # body length
        E1 = 1.6,       # body width
        E = 2.8,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.85,  # body height
        b = 0.29,  # pin width
        e = 0.65,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'TSOT-23-8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SC-82AA': Pkg_params( # from http://media.digikey.com/pdf/Data%20Sheets/Rohm%20PDFs/da227.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.1,  # pin width
        e = 0.1,  # pin (center-to-center) distance
        npx = 17,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (1,4,5,6,7,8,9,10,11,12,13,14,18,21,22,23,24,25,26,27,28,29,30,31,34), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SC-82AA', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SC-82AB': Pkg_params( # from http://www.infineon.com/dgdl/SOT343-Package_Overview.pdf?fileId=5546d462580663ef015806a5338d04ef
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.1,       # pin upper corner, inner radius
        R2 = 0.1,       # pin lower corner, inner radius
        S = 0.00,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.15,     # first pin indicator radius
        fp_d = 0.08,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 2.0,       # body length
        E1 = 1.25,       # body width
        E = 2.1,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.9,  # body height
        b = 0.1,  # pin width
        e = 0.1,  # pin (center-to-center) distance
        npx = 16,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (4,5,6,7,8,9,10,11,12,20,21,22,23,24,25,26,27,28,29), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SC-82AB', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SuperSOT-3': Pkg_params( # from https://www.fairchildsemi.com/package-drawings/MA/MA03B.pdf
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
        D1 = 2.92,       # body length
        E1 = 1.4,       # body width
        E = 2.51,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 0.94,  # body height
        b = 0.45,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = (2, 4, 6), #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SuperSOT-3', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SuperSOT-6': Pkg_params( # from http://www.mouser.com/ds/2/149/FMB5551-889214.pdf
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
        cc1 = 0.24, #0.45 chamfer of the 1st pin corner
        cc = 0.24, #0.45 chamfer of the other pin corners
        D1 = 2.92,       # body length
        E1 = 1.58,       # body width
        E = 2.85,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.02,  # body height
        b = 0.45,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 3,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SuperSOT-6', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SuperSOT-8': Pkg_params( # from http://www.icbank.com/icbank_data/semi_package/ssot8_dim.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.15,        # pin thickness, body center part height
        R1 = 0.15,       # pin upper corner, inner radius
        R2 = 0.15,       # pin lower corner, inner radius
        S = 0.1,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.24, #0.45 chamfer of the 1st pin corner
        cc = 0.24, #0.45 chamfer of the other pin corners
        D1 = 4.06,       # body length
        E1 = 3.3,       # body width
        E = 4.7,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.02,  # body height
        b = 0.45,  # pin width
        e = 0.95,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SuperSOT-8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
    'SOT-223-8': Pkg_params( # from https://www.diodes.com/assets/Datasheets/ZXSBMR16PT8.pdf
        the = 8.0,      # body angle in degrees
        tb_s = 0.05,    # top part of body is that much smaller
        c = 0.30,        # pin thickness, body center part height
        R1 = 0.15,       # pin upper corner, inner radius
        R2 = 0.15,       # pin lower corner, inner radius
        S = 0.2,       # pin top flat part length (excluding corner arc)
        L = 0.4,       # pin bottom flat part length (including corner arc)
        fp_s = True,     # True for circular pinmark, False for square pinmark (useful for diodes)
        fp_r = 0.5,     # first pin indicator radius
        fp_d = 0.1,     # first pin indicator distance from edge
        fp_z = 0.03,     # first pin indicator depth
        ef = 0.0, #0.02,      # fillet of edges  Note: bigger bytes model with fillet
        cc1 = 0.12, #0.45 chamfer of the 1st pin corner
        cc = 0.12, #0.45 chamfer of the other pin corners
        D1 = 6.5,       # body length
        E1 = 3.5,       # body width
        E = 7.0,        # body overall width  E=E1+2*(S+L+c)
        A1 = 0.1,  # body-board separation
        A2 = 1.7,  # body height
        b = 0.7,  # pin width
        e = 1.53,  # pin (center-to-center) distance
        npx = 4,   # number of pins along X axis (width)
        npy = 0,   # number of pins along y axis (length)
        epad = None, # e Pad
        excluded_pins = None, #no pin excluded
        body_color_key = "dark grey body",      # body color
        pins_color_key = "gold pins",           # pins color
        mark_color_key = "light brown label",   # marker color
        modelName = 'SOT-223-8', #modelName
        rotation = -90, # rotation if required
        dest_dir_prefix = '',
        ),
}
