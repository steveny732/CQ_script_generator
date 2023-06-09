#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This was originaly derived from a cadquery script for generating PDIP models in X3D format
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# Adapted by easyw for step and vrlm export
# See https://github.com/easyw/kicad-3d-models-in-freecad

## requirements
## cadquery FreeCAD plugin
##   https://github.com/jmwright/cadquery-freecad-module

## to run the script just do: freecad scriptName
## e.g. FreeCAD export_conn_jst_xh.py

## the script will generate STEP and VRML parametric models
## to be used with kicad StepUp script

#* These are FreeCAD & cadquery tools                                       *
#* to export generated models in STEP & VRML format.                        *
#*                                                                          *
#* cadquery script for generating JST-XH models in STEP AP214               *
#*   Copyright (c) 2016                                                     *
#* Rene Poeschl https://github.com/poeschlr                                 *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU General Public License (GPL)             *
#*   as published by the Free Software Foundation; either version 2 of      *
#*   the License, or (at your option) any later version.                    *
#*   for detail see the LICENCE text file.                                  *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc.,                                                      *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
#*                                                                          *
#****************************************************************************

__title__ = "make 3D models of 4UCON 17809 series connectors"
__author__ = "scripts: maurice and hyOzd; models: hackscribble"
__Comment__ = '''make 3D models of 4UCON 17809 series connectors'''

___ver___ = "0.2 18/06/2020"


import sys
import os

full_path=os.path.realpath(__file__)
script_dir_name =full_path.split(os.sep)[-2]
parent_path = full_path.split(script_dir_name)[0]
out_dir = parent_path + "_3Dmodels" + "/" + script_dir_name

sys.path.append("./")
sys.path.append("../_tools")
sys.path.append("cq_models")

import shaderColors


# Model details
#################################################################################################

import conn_4ucon_17809 as UCON_17809

series = [UCON_17809]

body_color_key = "dark grey body"
body_color = shaderColors.named_colors[body_color_key].getDiffuseInt()
pins_color_key = "metal grey pins"
pins_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()
contacts_color_key = "metal grey pins"
contacts_color = shaderColors.named_colors[pins_color_key].getDiffuseInt()

#################################################################################################


import add_license as L

# Licence information of the generated models
#################################################################################################

L.STR_int_licAuthor = "Ray Benitez"
L.STR_int_licEmail = "hackscribble@outlook.com"

#################################################################################################


from datetime import datetime
import re
import fnmatch

import cadquery as cq
from collections import namedtuple


def export_one_part(modul, variant):
    if not variant in modul.all_params:
        FreeCAD.Console.PrintMessage("Parameters for %s not found - skipping." % variant)
        return
    ModelName = variant
    ModelName = ModelName.replace(".","_")
    FileName = modul.all_params[variant].file_name

    FreeCAD.Console.PrintMessage(FileName)

    Newdoc = FreeCAD.newDocument(ModelName)
    App.setActiveDocument(ModelName)
    App.ActiveDocument=App.getDocument(ModelName)
    Gui.ActiveDocument=Gui.getDocument(ModelName)

    # Model details
    #################################################################################################

    (pins, body, contacts) = modul.generate_part(variant)

    color_attr = body_color + (0,)
    show(body, color_attr)

    color_attr = pins_color + (0,)
    show(pins, color_attr)

    color_attr = contacts_color + (0,)
    show(contacts, color_attr)


    i=0
    objs[i].Label = ModelName + "__body"
    i+=1
    objs[i].Label = ModelName + "__pins"
    i+=1
    objs[i].Label = ModelName + "__contacts"
    i+=1


    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


if __name__ == "__main__":

    FreeCAD.Console.PrintMessage('\r\nRunning...\r\n')

    modelfilter = "*"

    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))
    for typ in series:
        for variant in typ.all_params.keys():
            if model_filter_regobj.match(variant):
                FreeCAD.Console.PrintMessage('\r\n'+variant+'\r\n')
                export_one_part(typ, variant)

    FreeCAD.Console.PrintMessage('\r\nDone\r\n')

