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
print("Import cq_parameters_THT_transformer.py")
import Params
importlib.reload(Params)
from Params import *

global typ_fil
global typ_cham
typ_fil = 1
typ_cham = 2


class SeriesParams():

    lib_name = "Package_THT_Transformer"

    body_color_key = "black body"
    body_top_color_key = "metal copper"
    pins_color_key = "gold pins"
    mark_color_key = "light brown label"
    ink_color_key = "white body"

pkg_defs = {

    'Transformer_37x44': Pkg_params(
        #
        # transformer 37x44mm
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_37x44.kicad_mod
        # 
        modelName = 'Transformer_37x44',                  # Model name
        serie = 'cube',                                   # Serie 'cube' or 'cubefeet'
        A1 = 0.1,                                         # body-board separation 
        body = (-13.97, -6.35, 43.18, 38.1, 19.05),       # Body (x, y, w, l, h) 
        top = (-6.99, 1.27, 29.22, 22.86, 5.0),           # Top (x, y, w, l, h) 
        pin = [(20.32, 0, 1.5, 5.0),(-5.08, 25.4, 1.5, 5.0),(5.08, 25.4, 1.5, 5.0),(0, 0, 1.5, 5.0),(-5.08, 0, 1.5, 5.0),(5.08, 0, 1.5, 5.0),(10.16, 0, 1.5, 5.0),(15.24, 0, 1.5, 5.0),(0, 25.4, 1.5, 5.0),(10.16, 25.4, 1.5, 5.0),(15.24, 25.4, 1.5, 5.0),(20.32, 25.4, 1.5, 5.0),],  # pin (x, y, drill, length)
        npth = None,                                      # npth None or (x, y, drill)
        body_top_color_key = 'black body',                # Top color
        body_color_key = 'black body',                    # Body color
        pin_color_key = 'metal grey pins',                # Pin color
        rotation = 0,                                     # rotation if required
        dest_dir_prefix = '',  # destination directory
        ),

    'Transformer_Breve_TEZ-22x24': Pkg_params(
        #
        # http://www.breve.pl/pdf/ANG/TEZ_ang.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-22x24.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-22x24',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-4.5, -18.5, 24.0, 22.0, 16.0),  # Body (x, y, w, l, h) 
        top = (-1.50, -15.5, 18.00, 16.00, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(15, 0, 0.9, 5.0),(15, -15, 0.9, 5.0),(10, -15, 0.9, 5.0),(5, -15, 0.9, 5.0),(0, -15, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Breve_TEZ-28x33': Pkg_params(
        #
        # http://www.breve.pl/pdf/ANG/TEZ_ang.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-28x33.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-28x33',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-5.5, -24.0, 31.0, 28.0, 19.0),  # Body (x, y, w, l, h) 
        top = (-1.50, -21.00, 23.00, 22.00, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(15, 0, 0.9, 5.0),(20, 0, 0.9, 5.0),(20, -20, 0.9, 5.0),(15, -20, 0.9, 5.0),(10, -20, 0.9, 5.0),(5, -20, 0.9, 5.0),(0, -20, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Breve_TEZ-35x42': Pkg_params(
        #
        # http://www.breve.pl/pdf/ANG/TEZ_ang.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-35x42.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-35x42',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-11.0, -30.0, 42.0, 35.0, 26),  # Body (x, y, w, l, h) 
        top  = ( -8.0, -27.0, 36.0, 29.0, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(15, 0, 0.9, 5.0),(20, 0, 0.9, 5.0),(20, -25, 0.9, 5.0),(15, -25, 0.9, 5.0),(10, -25, 0.9, 5.0),(5, -25, 0.9, 5.0),(0, -25, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Breve_TEZ-38x45': Pkg_params(
        #
        # 
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-38x45.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-38x45',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-10.0, -31.5, 45.0, 38.0, 29),  # Body (x, y, w, l, h) 
        top = (-4.50, -28.00, 34.00, 31.00, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(20, 0, 0.9, 5.0),(25, 0, 0.9, 5.0),(25, -25, 0.9, 5.0),(20, -25, 0.9, 5.0),(12.5, -25, 0.9, 5.0),(5, -25, 0.9, 5.0),(0, -25, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Breve_TEZ-44x52': Pkg_params(
        #
        # 
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Breve_TEZ-44x52.kicad_mod
        # 
        modelName = 'Transformer_Breve_TEZ-44x52',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-14.5, -35.75, 54.0, 44.0, 32.0),  # Body (x, y, w, l, h) 
        top  = (-11.5, -32.75, 48.0, 38.0, 3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 0.9, 5.0),(5, 0, 0.9, 5.0),(20, 0, 0.9, 5.0),(25, 0, 0.9, 5.0),(25, -27.5, 0.9, 5.0),(20, -27.5, 0.9, 5.0),(15, -27.5, 0.9, 5.0),(10, -27.5, 0.9, 5.0),(5, -27.5, 0.9, 5.0),(0, -27.5, 0.9, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'green body',   # Top color
        body_color_key = 'green body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

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

    'Transformer_CHK_EI30-2VA_1xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI30, 2VA, 1x Sec, http://www.eratransformers.com/downloads/030-7585.0.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI30-2VA_1xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI30-2VA_1xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-3.5, -26.0, 27.0, 32.0, 32.0),  # Body (x, y, w, l, h) 
        top  = (-0.5, -23.0, 21.0, 26.0,  2.6),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(20, -20, 1.5, 3.5),(20, -15, 1.5, 3.5),(20, -10, 1.5, 3.5),(20, -5, 1.5, 3.5),(20, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI30-2VA_2xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI30, 2VA, 2x Sec, http://www.eratransformers.com/product-detail/28#
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI30-2VA_2xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI30-2VA_2xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-3.5, -26.0, 27.0, 32.0, 31.00),  # Body (x, y, w, l, h) 
        top  = (-0.5, -23.0, 21.0, 26.0,  3.00),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(20, -20, 1.5, 3.5),(20, -15, 1.5, 3.5),(20, -10, 1.5, 3.5),(20, -5, 1.5, 3.5),(20, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI30-2VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI30, 2VA, neutral,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI30-2VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI30-2VA_Neutral',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-3.5, -26.0, 27.0, 32.0, 31.00),  # Body (x, y, w, l, h) 
        top  = (-0.5, -23.0, 21.0, 26.0,  3.00),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(20, -20, 1.5, 3.5),(20, -15, 1.5, 3.5),(20, -10, 1.5, 3.5),(20, -5, 1.5, 3.5),(20, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI38-3VA_1xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI38, 3VA, 1x Sec,http://www.eratransformers.com/product-detail/20
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI38-3VA_1xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI38-3VA_1xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-5.0, -30.25, 35.0, 40.5, 25.00),  # Body (x, y, w, l, h) 
        top  = (-2.0, -27.25, 29.0, 34.5,  3.00),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(25, -20, 1.5, 3.5),(25, -15, 1.5, 3.5),(25, -10, 1.5, 3.5),(25, -5, 1.5, 3.5),(25, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Body color
        pin_color_key = 'metal grey pins',   # Pin color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI38-3VA_2xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI38, 3VA, 2x Sec,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI38-3VA_2xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI38-3VA_2xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-5.0, -30.25, 35.0, 40.5, 25.00),  # Body (x, y, w, l, h) 
        top  = (-2.0, -27.25, 29.0, 34.5,  3.00),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 5.0),(0, -5, 1.5, 5.0),(0, -10, 1.5, 5.0),(0, -15, 1.5, 5.0),(0, -20, 1.5, 5.0),(25, -20, 1.5, 5.0),(25, -15, 1.5, 5.0),(25, -10, 1.5, 5.0),(25, -5, 1.5, 5.0),(25, 0, 1.5, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI38-3VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI38, 3VA, neutral,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI38-3VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI38-3VA_Neutral',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-5.0, -30.25, 35.0, 40.5, 25.00),  # Body (x, y, w, l, h) 
        top  = (-2.0, -27.25, 29.0, 34.5,  3.00),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 5.0),(0, -5, 1.5, 5.0),(0, -10, 1.5, 5.0),(0, -15, 1.5, 5.0),(0, -20, 1.5, 5.0),(25, -20, 1.5, 5.0),(25, -15, 1.5, 5.0),(25, -10, 1.5, 5.0),(25, -5, 1.5, 5.0),(25, 0, 1.5, 5.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI42-5VA_1xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI42, 5VA, 1x Sec,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI42-5VA_1xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI42-5VA_1xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-6.0, -32.0, 37.0, 44.0, 32.0),  # Body (x, y, w, l, h) 
        top  = (-3.0, -29.0, 31.0, 38.0,  3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(25, -20, 1.5, 3.5),(25, -15, 1.5, 3.5),(25, -10, 1.5, 3.5),(25, -5, 1.5, 3.5),(25, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI42-5VA_2xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI42, 5VA, 2x Sec,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI42-5VA_2xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI42-5VA_2xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-6.0, -32.0, 37.0, 44.0, 32.0),  # Body (x, y, w, l, h) 
        top  = (-3.0, -29.0, 31.0, 38.0,  3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(25, -20, 1.5, 3.5),(25, -15, 1.5, 3.5),(25, -10, 1.5, 3.5),(25, -5, 1.5, 3.5),(25, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI42-5VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI42, 5VA, neutral, http://www.eratransformers.com/product-detail/17
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI42-5VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI42-5VA_Neutral',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-6.0, -32.0, 37.0, 44.0, 32.0),  # Body (x, y, w, l, h) 
        top  = (-3.0, -29.0, 31.0, 38.0,  3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.5, 3.5),(0, -5, 1.5, 3.5),(0, -10, 1.5, 3.5),(0, -15, 1.5, 3.5),(0, -20, 1.5, 3.5),(25, -20, 1.5, 3.5),(25, -15, 1.5, 3.5),(25, -10, 1.5, 3.5),(25, -5, 1.5, 3.5),(25, 0, 1.5, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI48-10VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI48, 10VA, neutral, http://www.eratransformers.com/product-detail/18
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI48-10VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI48-10VA_Neutral',            # Model name
        serie = 'cubefeet',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-7.25, -46.5, 42.0, 68.0, 31,5),  # Body (x, y, w, l, h) 
        top = (-4.25, -43.5, 36.0, 62.0,   3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -25.05, 1.2, 3.5),(27.5, -25, 1.2, 3.5),(27.5, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(27.5, -5, 1.2, 3.5),(27.5, -10, 1.2, 3.5),(27.5, -15, 1.2, 3.5),(27.5, -20, 1.2, 3.5),(13.75, 17.25, 4.5, 3.5),(13.75, -42.25, 4.5, 3.5),],  # pin (x, y, drill, length)
        npth = [(13.75, 17.25, 4.5),(13.75, -42.25, 4.5),],  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI48-8VA_1xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI48, 8VA, 1x Sec, http://www.eratransformers.com/product-detail/18
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI48-8VA_1xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI48-8VA_1xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-7.3, -37.45, 42.1, 49.9, 31,5),  # Body (x, y, w, l, h) 
        top = (-4.3, -34.45, 36.1, 43.9,   3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -25.05, 1.2, 3.5),(27.5, -25, 1.2, 3.5),(27.5, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(27.5, -5, 1.2, 3.5),(27.5, -10, 1.2, 3.5),(27.5, -15, 1.2, 3.5),(27.5, -20, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI48-8VA_2xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI48, 8VA, 2x Sec, http://www.eratransformers.com/product-detail/18
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI48-8VA_2xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI48-8VA_2xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-7.3, -37.45, 42.1, 49.9, 31,5),  # Body (x, y, w, l, h) 
        top = (-4.3, -34.45, 36.1, 43.9,   3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -25.05, 1.2, 3.5),(27.5, -25, 1.2, 3.5),(27.5, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(27.5, -5, 1.2, 3.5),(27.5, -10, 1.2, 3.5),(27.5, -15, 1.2, 3.5),(27.5, -20, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI48-8VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI48, 8VA, neutral, http://www.eratransformers.com/product-detail/18
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI48-8VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI48-8VA_Neutral',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-7.3, -37.45, 42.1, 49.9, 31,5),  # Body (x, y, w, l, h) 
        top = (-4.3, -34.45, 36.1, 43.9,   3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -25.05, 1.2, 3.5),(27.5, -25, 1.2, 3.5),(27.5, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(27.5, -5, 1.2, 3.5),(27.5, -10, 1.2, 3.5),(27.5, -15, 1.2, 3.5),(27.5, -20, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI54-12VA_1xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI54, 12VA, 1x Sec,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI54-12VA_1xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI54-12VA_1xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-8.5, -43.0, 47.0, 56.0, 36.0),  # Body (x, y, w, l, h) 
        top = (-5.5, -40.0, 41.0, 50.0,   3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(0, -25, 1.2, 3.5),(0, -30, 1.2, 3.5),(30, -30, 1.2, 3.5),(30, -25, 1.2, 3.5),(30, -20, 1.2, 3.5),(30, -15, 1.2, 3.5),(30, -10, 1.2, 3.5),(30, -5, 1.2, 3.5),(30, 0, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI54-12VA_2xSec': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI54, 12VA, 2x Sec,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI54-12VA_2xSec.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI54-12VA_2xSec',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-8.5, -43.0, 47.0, 56.0, 36.0),  # Body (x, y, w, l, h) 
        top  = (-5.5, -40.0, 41.0, 50.0,  3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(0, -25, 1.2, 3.5),(0, -30, 1.2, 3.5),(30, -30, 1.2, 3.5),(30, -25, 1.2, 3.5),(30, -20, 1.2, 3.5),(30, -15, 1.2, 3.5),(30, -10, 1.2, 3.5),(30, -5, 1.2, 3.5),(30, 0, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_CHK_EI54-12VA_Neutral': Pkg_params(
        #
        # Trafo, Printtrafo, CHK, EI54, 12VA, neutral,
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_CHK_EI54-12VA_Neutral.kicad_mod
        # 
        modelName = 'Transformer_CHK_EI54-12VA_Neutral',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-8.5, -43.0, 47.0, 56.0, 36.0),  # Body (x, y, w, l, h) 
        top  = (-5.5, -40.0, 41.0, 50.0,  3.0),  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.2, 3.5),(0, -5, 1.2, 3.5),(0, -10, 1.2, 3.5),(0, -15, 1.2, 3.5),(0, -20, 1.2, 3.5),(0, -25, 1.2, 3.5),(0, -30, 1.2, 3.5),(30, -30, 1.2, 3.5),(30, -25, 1.2, 3.5),(30, -20, 1.2, 3.5),(30, -15, 1.2, 3.5),(30, -10, 1.2, 3.5),(30, -5, 1.2, 3.5),(30, 0, 1.2, 3.5),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'blue body',   # Top color
        body_color_key = 'blue body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Microphone_Lundahl_LL1538': Pkg_params(
        #
        # AUDIO TRAFO LUNDAHL, https://www.lundahltransformers.com/wp-content/uploads/datasheets/1538_8xl.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Microphone_Lundahl_LL1538.kicad_mod
        # 
        modelName = 'Transformer_Microphone_Lundahl_LL1538',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-5.08, -19.68, 38.1, 24.12, 17.00),  # Body (x, y, w, l, h) 
        top = None,  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.52, 3.0),(0, -5.08, 1.52, 3.0),(0, -10.16, 1.52, 3.0),(0, -15.24, 1.52, 3.0),(27.94, 0, 1.52, 3.0),(27.94, -5.08, 1.52, 3.0),(27.94, -15.24, 1.52, 3.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'metal grey pins',   # Top color
        body_color_key = 'metal grey pins',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_Microphone_Lundahl_LL1587': Pkg_params(
        #
        # AUDIO TRAFO LUNDAHL
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_Microphone_Lundahl_LL1587.kicad_mod
        # 
        modelName = 'Transformer_Microphone_Lundahl_LL1587',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-3.81, -14.61, 27.94, 17.79, 12.00),  # Body (x, y, w, l, h) 
        top = None,  # Top (x, y, w, l, h) 
        pin = [(0, 0, 1.52, 3.0),(0, -3.81, 1.52, 3.0),(0, -7.62, 1.52, 3.0),(0, -11.43, 1.52, 3.0),(20.32, 0, 1.52, 3.0),(20.32, -3.81, 1.52, 3.0),(20.32, -11.43, 1.52, 3.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'metal grey pins',   # Top color
        body_color_key = 'metal grey pins',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_NF_ETAL_1-1_P1200': Pkg_params(
        #
        # NF-Transformer, 1:1, ETAL P1200,http://www.etalgroup.com/sites/default/files/products/P1200_April_2005.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_NF_ETAL_1-1_P1200.kicad_mod
        # 
        modelName = 'Transformer_NF_ETAL_1-1_P1200',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-15.35, -5.19, 18.0, 18.0, 12.60),  # Body (x, y, w, l, h) 
        top = None,  # Top (x, y, w, l, h) 
        pin = [(-12.7, 0, 0.81, 3.0),(-12.7, 7.62, 0.81, 3.0),(0, 0, 0.81, 3.0),(0, 7.62, 0.81, 3.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'black body',   # Top color
        body_color_key = 'black body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),

    'Transformer_NF_ETAL_P1165': Pkg_params(
        #
        # NF-Transformer,  ETAL, P1165,http://www.etalgroup.com/sites/default/files/products/P1165_February_2006.pdf
        # This model have been auto generated based on the foot print file
        # A number of paramters have been fixed or guessed, such as A1
        # 
        # The foot print that uses this 3D model is Transformer_NF_ETAL_P1165.kicad_mod
        # 
        modelName = 'Transformer_NF_ETAL_P1165',            # Model name
        serie = 'cube',            # Serie 'cube' or 'cubefeet'
        A1 = 0.1,  # body-board separation 
        body = (-14.75, -4.75, 19.5, 19.5, 11.00),  # Body (x, y, w, l, h) 
        top = None,  # Top (x, y, w, l, h) 
        pin = [(-10, 0, 0.81, 3.0),(-10, 10, 0.81, 3.0),(0, 0, 0.81, 3.0),(0, 10, 0.81, 3.0),],  # pin (x, y, drill, length)
        npth = None,  # npth None or (x, y, drill)
        body_top_color_key = 'black body',   # Top color
        body_color_key = 'black body',   # Top color
        pin_color_key = 'metal grey pins',   # Top color
        rotation = 0,      # rotation if required
        dest_dir_prefix = '',      # destination directory
        ),
}
