# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating THT Transformer models in X3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Dimensions are from ???.
 
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

    lib_name = "Test"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {

    'Transformer_Breve_TEZ-47x57': Pkg_params(
        #
        # 
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-47x57.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-47x57',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-13.5, -38.5, 57.0, 47.0, 36.0),  # Body (x, y, w, l, h) 
        top = (-6.00, -33.50, 42.00, 37.5, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(20, 0, 0.9, 5.0),(25, 0, 0.9, 5.0),(30, 0, 0.9, 5.0),(30, -30, 0.9, 5.0),(25, -30, 0.9, 5.0),(20, -30, 0.9, 5.0),(15, -30, 0.9, 5.0),(10, -30, 0.9, 5.0),(10, 0, 0.9, 5.0),(0, -30, 0.9, 5.0),(5, -30, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    # 'Transformer_37x44': Pkg_params(
    #     #
    #     # transformer 37x44mm
    #     # This model have been auto generated based on the foot print file
    #     # A number of paramters have been fixed or guessed, such as A1
    #     # 
    #     # The foot print that uses this 3D model is Transformer_37x44.kicad_mod
    #     # 
    #     modelName = 'Transformer_37x44',                  # Model name
    #     serie = 'cube',                                   # Serie 'cube' or 'cubefeet'
    #     A1 = 0.1,                                         # body-board separation 
    #     body = (-13.97, -6.35, 43.18, 38.1, 19.05),       # Body (x, y, w, l, h) 
    #     top = (-6.99, 1.27, 29.22, 22.86, 5.0),           # Top (x, y, w, l, h) 
    #     pin = [(20.32, 0, 1.5, 5.0),(-5.08, 25.4, 1.5, 5.0),(5.08, 25.4, 1.5, 5.0),(0, 0, 1.5, 5.0),(-5.08, 0, 1.5, 5.0),(5.08, 0, 1.5, 5.0),(10.16, 0, 1.5, 5.0),(15.24, 0, 1.5, 5.0),(0, 25.4, 1.5, 5.0),(10.16, 25.4, 1.5, 5.0),(15.24, 25.4, 1.5, 5.0),(20.32, 25.4, 1.5, 5.0),],  # pin (x, y, drill, length)
    #     npth = None,                                      # npth None or (x, y, drill)
    #     body_top_color_key = 'black body',                # Top color
    #     body_color_key = 'black body',                    # Body color
    #     pin_color_key = 'metal grey pins',                # Pin color
    #     rotation = 0,                                     # rotation if required
    #     dest_dir_prefix = '',  # destination directory
    #     ),

}
