# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating fw models in 
#   3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author s. yoder
#
# Dimensions are from Jedec MS-026D document.                               *
#                                                                           *
## requirements                                                             *
# cadquery2                                                                 *
##   https://cadquery.readthedocs.io/en/latest                              *
##   ??? https://github.com/???                                             *

#                                                                           *
## to run the script just do: python main_generator.py series=[series,ser]  *
## e.g. python main_generator.py series=fw_x,fw_y                           *

## the script will generate STEP parametric models                          *
## to be used with KiCad                                                    *
#                                                                           *
#* These are cadquery 2.0 tools                                             *
#* to export generated models in STEP format.                               *
#*                                                                          *
#* cadquery script for generating fw models in STEP AP214                   *
#*   Copyright (c) 2020                                                     *
#* Maurice https://??                                                       *
#* All trademarks within this guide belong to their legitimate owners.      *
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Lesser General Public License (LGPL)     *
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

__title__ = "make FW 3D models"
__author__ = "s. yoder"
__Comment__ = 'make fw 3D models exported to STEP script'
___ver___ = "0.00.1 12/08/2020"

global stop_on_first_error
global place_pinmark
global color_pinmark
global ink_thickness
global build_all
global no_export
global case_only
global trial_run
global debug_plot
global debug_print
global global_3dpath
global lib_name
global cmd_line
global pkg_cnt
global pkg_cnt
pkg_cnt = 1

global body_color_key
global body_top_color_key
global pins_color_key
global mark_color_key
global ink_color_key

stop_on_first_error = True
build_log_file = 'build-log.md'
place_pinmark=True
color_pinmark=True
build_all = False
no_export = False
trial_run = False
case_only = False
debug_plot = False
debug_print = False
global_3dpath = '../_3Dmodels/' # production path

import argparse

import cadquery as cq
from cadquery import *
from math import tan, sin, cos, radians, sqrt
from collections import namedtuple

global edge_none
global edge_filt
global edge_cham
global edge_type

import sys, os
import importlib
import traceback
import datetime
from datetime import datetime

def AddSysPath(new_path):
	""" AddSysPath(new_path): adds a directory to Python's sys.path

	Does not add the directory if it does not exist or if it's already on
	sys.path. Returns 1 if OK, -1 if new_path does not exist, 0 if it was
	already on sys.path.
	"""
	# Avoid adding nonexistent paths
	if not os.path.exists(new_path): return -1   
    # Standardize the path. Windows is case-insensitive, so lowercase
    # for definiteness.
	new_path = os.path.abspath(new_path)
	if sys.platform == 'win32':
		new_path = new_path.lower(  )
   # Check against all currently available paths
	for x in sys.path:
		x = os.path.abspath(x)
		if sys.platform == 'win32':
				x = x.lower(  )				
		if new_path in (x, x + os.sep):
			return 0
	sys.path.append(new_path)
	return 1

scriptdir=os.path.dirname(os.path.realpath('__file__'))
toolsdir=os.path.dirname(os.path.realpath('scriptdir'+"/../"))+"/_tools"
outdir=os.path.dirname(os.path.realpath('scriptdir'+"/../"))+"/_3Dmodels"
AddSysPath(scriptdir)
AddSysPath(outdir)
AddSysPath(toolsdir)
import re, fnmatch

import shaderColors

# Licence information of the generated models.
###############################################################################
import add_license as Lic

STR_licAuthor = "CadQuery2"
STR_licEmail = "ksu"
STR_licOrgSys = "CadQuery2"
STR_licPreProc = "OCC"
STR_licOrg = "CadQuery2"

LIST_license = ["",]
###############################################################################
###############################################################################
###############################################################################
###############################################################################

def rect(wp, rw, rh, cc1 = 0, cc = 0, ed1 = 2, eds = 2):
    """
    Creates a rectangle with fillet corners.
    wp: workplane object
    rw: rectangle width
    rh: rectangle height
    ef: corner fillet
    ed1:
        edge_none - square   : 0
        edge_filt - fillet   : 1
        edge_cham -  chamfer : 2
    eds:
        edge_none - square   : 0
        edge_filt - fillet   : 1
        edge_cham -  chamfer : 2
    """
    global edge_filt
    global edge_cham

    acen1 = sin(radians(45))
    if cc1 > 0 : acen1 = 1-acen1 # Positive fillet

    acen = sin(radians(45))
    if cc > 0 or cc > 0: acen = 1-acen # Positive fillet

    cc1 = abs(cc1)
    cc = abs(cc)

    wp = wp.moveTo(-rw/2+cc1, -rh/2)
    if cc1 > 0:
        if ed1 != edge_cham: 
            wp = wp.threePointArc((-rw/2+acen1*cc1, -rh/2+acen1*cc1), (-rw/2, -rh/2+cc1))
        else: 
            wp = wp.lineTo(-rw/2, -rh/2+cc1)
    wp = wp.lineTo(-rw/2, rh/2-cc)
    if cc > 0:
        if eds != edge_cham: 
            wp = wp.threePointArc((-rw/2+acen*cc, rh/2-acen*cc), (-rw/2+cc, rh/2))
        else: 
            wp = wp.lineTo(-rw/2+cc, rh/2)
    wp = wp.lineTo(rw/2-cc,rh/2)
    if cc > 0:
        if eds != edge_cham: 
            wp = wp.threePointArc((rw/2-acen*cc, rh/2-acen*cc), (rw/2, rh/2-cc))
        else: 
            wp = wp.lineTo(rw/2, rh/2-cc)
    wp = wp.lineTo(rw/2,-rh/2+cc)
    if cc > 0:
        if eds != edge_cham: 
            wp = wp.threePointArc((rw/2-acen*cc, -rh/2+acen*cc), (rw/2-cc, -rh/2))
        else: 
            wp = wp.lineTo(rw/2-cc, -rh/2)
    wp = wp.close()

    return(wp) #, forConstruction=True)


def wr_body_txt(assy, params):

    global series_def
    text_defs = params.text_defs
    if params.rotation: rot = params.rotation
    else: rot = 0.
    if params.D1: D1 = params.D1
    D = params.D
    if not D: D = params.D1
    E = params.E
    if params.E1: E1 = params.E1
    else: E1 = E
    A1 = params.A1
    A2 = params.A2
    A = A1 + A2

    lines = 0
    y_offset = 0
    for variant in text_defs:
        line = text_defs[variant]
        # Set defaults if value not defined
        if line.txt: txt = line.txt
        else: txt = ""
        if line.fsize: fsize = line.fsize
        else: fsize = .2
        if line.loc and type(line.loc) == tuple: pos_x, pos_y = line.loc
        elif line.loc: 
            pos_x = line.loc
            pos_y = line.loc
        else:
            pos_x = 0.
            pos_y = 0.
        if line.style: style = line.style
        else: style = "regular"
        if line.halign: halign = line.halign
        else: halign = "left"
        if line.valign: valign = line.valign
        else: valign = "top"
        if line.rotation: txt_rot = line.rotation
        else: txt_rot = 0.
        if line.ink_thickness: ink_thickness = line.ink_thickness
        elif series_def.ink_thickness: ink_thickness = series_def.ink_thickness
        else: ink_thickness = .005

        wp = cq.Workplane(cq.Plane.XY()).workplane(offset=A)

        if txt: wp=wp.text(cut=False,txt=txt,fontsize=fsize,distance=ink_thickness,clean=True,halign=halign,valign=valign)

        if line.dot:
            pos_z = 0
            if len(line.dot) == 3: r,pos_x,pos_y = line.dot
            elif len(line.dot) == 4: r,pos_x,pos_y,pos_z = line.dot
            wp=wp.circle(r).extrude(ink_thickness)
        else:
            pos_z = 0
            if len(line.loc) == 2: pos_x,pos_y = line.loc
            elif len(line.loc) == 3: pos_x,pos_y,pos_z = line.loc

        txt_offset = (-D1/2+pos_x,E1/2-pos_y-y_offset, pos_z)

        wp = wp.rotate((0,0,0), (0,0,1), txt_rot).translate(txt_offset).rotate((0,0,0), (0,0,1), rot)
        lines += 1
        y_offset += fsize
        #if debug_plot: show_object(wp)

        ink_color_key = "white body"
        if line.ink_color_key: ink_color_key = line.ink_color_key
        r,g,b,a = shaderColors.named_colors[ink_color_key].getDiffuseFloat()
        assy.add(wp, color=Color(r,g,b,a))

    return(assy)

# all_params = dict(all_params1.items() | all_params2.items())

def make_pkg(params):

    c  = params.c
    the  = params.the
    tb_s  = params.tb_s
    ef  = params.ef
    cc1 = params.cc1
    cc = params.cc
    fp_s = params.fp_s
    fp_r  = params.fp_r
    fp_d  = params.fp_d
    fp_z  = params.fp_z
    R1  = params.R1
    R2  = params.R2
    S  = params.S
    L  = params.L
    D1  = params.D1
    E1  = params.E1
    D   = params.D
    E   = params.E
    A1  = params.A1
    A2  = params.A2
    b   = params.b
    e   = params.e
    npx = params.npx
    npy = params.npy
    epad  = params.epad
    mN  = params.modelName
    rot = params.rotation
    text_defs = params.text_defs # list of top of pakcage text lines

    global dest_dir_pref
    global body_color_key
    global body_top_color_key
    global pins_color_key
    global mark_color_key
    global ink_color_key
    global place_pinmark
    global edge_type
    global edge_none
    global edge_filt
    global edge_cham

    body_color_key = None
    body_top_color_key = None
    pins_color_key = None
    mark_color_key = None
    ink_color_key = None

    if not tb_s: tb_s = 0
    if not D: D = params.D1

    # Process ef fillet parameters,
    h_edges = edge_filt
    if type(ef) != tuple: 
        ef_t = ef
        ef_b = 0.
    else:
        if len(ef) >1: 
            ef_t = ef[0]
            ef_b = ef[1]
        if len(ef)>2: 
            h_edges = ef[2]
    ef = ef_t
    if ef_t == 0 and ef_b == 0: h_edges = edge_none
    elif not h_edges: h_edges = edge_none

    # Process cc1 corner parameters, 
    v_edge1=edge_cham
    v_edges=edge_cham
    if type(cc1) == tuple: cc1,v_edge1 = cc1
    if type(cc) == tuple: cc,v_edges = cc
    
    if params.excluded_pins: excluded_pins = params.excluded_pins
    else: excluded_pins=() ##no pin excluded

    if params.body_color_key: body_color_key  = params.body_color_key # number of pins along y axis (length)
    if params.body_top_color_key: body_top_color_key  = params.body_top_color_key # number of pins along y axis (length)
    if params.pins_color_key: pins_color_key  = params.pins_color_key  # number of pins along y axis (length)
    if params.mark_color_key: mark_color_key  = params.mark_color_key  # number of pins along y axis (length)

    if body_color_key: body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    if body_top_color_key: body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
    if pins_color_key: pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
    if mark_color_key: mark_color = shaderColors.named_colors[mark_color_key].getDiffuseFloat()
        
# Parameter definitions
    A = A1 + A2

    # flat pin parts have c
    ### Non-flat pin calcs
    if R1 and R2:
        A2_t = (A2-c)/2 # body top part height
        A2_b = A2_t     # body bottom part height
        D1_b = D1-2*tan(radians(the))*A2_b # bottom width
        E1_b = E1-2*tan(radians(the))*A2_b # bottom length
        # Pin offsets
        x_pin_offset = (E1)/2
        y_pin_offset = (D1)/2
    # Calculate flat pin parameters
    else: 
        A2_t = A2-c+A1
        A2_b = 0.
        D1_b = D1
        E1_b = E1
        # Pin offsets
        x_pin_offset = (E-L)/2
        y_pin_offset = (D-L)/2

    D1_t1 = D1-tb_s # top part bottom width
    E1_t1 = E1-tb_s # top part bottom length
    D1_t2 = D1_t1-2*tan(radians(the))*A2_t # top part upper width
    E1_t2 = E1_t1-2*tan(radians(the))*A2_t # top part upper length

# Pin calculations
    # accomodate differnt X and Y pin pitches
    if not e: e = 0.
    if isinstance(e, tuple): e_x, e_y = e
    else:
        e_x = e
        e_y = e

    first_pos_x = (npx-1)*e_x/2
    first_pos_y = (npy-1)*e_y/2

# Epad calculations
    epad_rotation = 0.0
    epad_offset_x = 0.0
    epad_offset_y = 0.0

    # Process epad definition
    if epad:
        if not isinstance(epad, tuple):
            rec_epad = False
            epad_r = epad
        else:
            rec_epad = True
            D2 = epad[0]
            E2 = epad[1]
            if len(epad) > 2:
                epad_thickness = epad[2]
            else:
                epad_thickness = A1
            if epad_thickness <= 0: epad_thickness = c
            if len(epad) > 3:
                if len(epad) == 5 and isinstance(epad[3],str):
                    print("New epad",epad)
                    epad = list(epad)
                    epad.insert(3,0.)
                    epad = tuple(epad)
                epad_rotation = epad[3]
            if len(epad) > 4:
                if isinstance (epad[4], str):
                    if epad[4] == '-topin':
                        epad_offset_x = -D/2+L+D2/2
                    elif epad[4] == '+topin':
                        epad_offset_x = D/2-L-D2/2
                else:
                    epad_offset_x = epad[4]
            if len(epad) > 5:
                if isinstance (epad[5], str):
                    if epad[5] == '-topin':
                        epad_offset_y = -E/2+L+E2/2
                    elif epad[5] == '+topin':
                        epad_offset_y = E/2-L-E2/2
                else:
                    epad_offset_y = epad[5]

# calculate chamfers
    totpinwidthx = (npx-1)*e_x+b # total width of all pins on the X side
    totpinwidthy = (npy-1)*e_y+b # total width of all pins on the Y side
    if not cc: cc = 0.
    if not cc1: cc1 = 0.
    max_cc1 = 1
    max_cc = 1

    # process cc1
    if cc1!=0:
        sign = 1
        if cc1 < 0: sign = -1
        cc1 = abs(min((D1-totpinwidthx)/2., (E1-totpinwidthy)/2.,cc1) - 0.5*tb_s)
        cc1 = min(cc1, max_cc1)
        cc1_t = abs(cc1-(D1-D1_t2)/4.) * sign # this one is defined because we use it later
        if abs(cc1_t) < abs(ef_t): cc1_t = abs(ef_t) * sign
        if abs(cc1) < abs(ef_b): cc1 = abs(ef_b) * sign
    else: 
        cc1_t = 0
        cc1_b = 0

    # process cc
    if cc!=0:
        sign = 1
        if cc < 0: sign = -1
        cc = abs(min((D1-totpinwidthx)/2., (E1-totpinwidthy)/2.,cc) - 0.5*tb_s)
        cc = min(cc, max_cc)
        cc_t = abs(cc-(D1-D1_t2)/4.) * sign # this one is defined because we use it later
        if abs(cc_t) < abs(ef_t): cc_t = abs(ef_t) * sign
        if abs(cc) < abs(ef_b): cc = abs(ef_b) * sign
    else:
        cc_t = 0
        cc_b = 0

###############################################################################
# *****************************************************************************
# cadquery model creation
# *****************************************************************************

######
## Build case in a stack of three enclosed shapes to prevent
## pins and pinmark cut operations from removing necessary walls,
## maintainingthe integrity of the shape.
## Otherwise case will not pass geometry checks.
######
# if no chamfer then make corners same as fillet would have been
    case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1)
    case = rect(case, D1_b, E1_b, cc1, cc, v_edge1, v_edges)  # bottom edges
    #show_object(case)
    if R1 and R2:
        case = case.pushPoints([(0,0)]).workplane(offset=A2_b)
        case = rect(case, D1, E1, cc1, cc, v_edge1, v_edges)     # center (lower) outer edges
        #show_object(case)            
        case = case.loft(ruled=True)
        #show_object(case)            
        if ef_b != 0.:
            try:
                case = case.faces("<Z").fillet(ef_b)
            except Exception as exeption:
                print("Case bottom face failed failed.\n")
                print('{:s}\n'.format(exeption))
        #show_object(case)            
        case = case.pushPoints([(0,0)]).workplane(offset=0)
        case = rect(case, D1,E1,cc1, cc, v_edge1, v_edges)       # center (lower) outer edges
   # show_object(case)            
        case = case.pushPoints([(0,0)]).workplane(offset=c)
    else:
        case = case.pushPoints([(0,0)]).workplane(offset=c-A1)
    case = rect(case, D1,E1,cc1, cc, v_edge1, v_edges)       # center (upper) outer edges
    #show_object(case)            
    case = case.loft(ruled=True)
    #show_object(case)            
    if ef_b != 0.:
        try:
            if h_edges == edge_filt: case = case.faces("<Z").fillet(ef_b)
            else: case = case = case.faces("<Z").chamfer(ef_b)            
        except Exception as exeption:
            print("Case bottom face failed failed.\n")
            print('{:s}\n'.format(exeption))
    case=case.pushPoints([(0,0)]).workplane(offset=0)
    case = rect(case, D1_t1, E1_t1, cc1, cc, v_edge1, v_edges) # center (upper) inner edges
    #show_object(case)            
    case = case.pushPoints([(0,0)]).workplane(offset=A2_t)
    case = rect(case, D1_t2, E1_t2, cc1_t, cc_t, v_edge1, v_edges) # top edges
    #show_object(case)            
    case = case.loft(ruled=True)
    if ef_t!=0:
        try:
            if h_edges == edge_filt: case = case.faces(">Z").fillet(ef_t)
            else: case = case.faces(">Z").chamfer(ef_t)
        except Exception as exeption:
            print("Case top face failed failed.\n")
            print('{:s}\n'.format(exeption))
    #show_object(case)
    case = case.rotate((0,0,0), (0,0,1), rot)
    #show_object(case)

    #fp_s = True
    pinmark = None
    if fp_r == 0: place_pinmark=False
    else: place_pinmark=True
    
    if place_pinmark:
        if not fp_s:
            pinmark = cq.Workplane(cq.Plane.XY()).workplane(offset=A).box(D1_t2-((fp_d+ef)*2), fp_r, fp_z*2)
            #show_object(pinmark)
            #translate the object
            print("rot ...",rot)
            pinmark=pinmark.translate((first_pos_x, E1/2-fp_r, 0)).rotate((0,0,0), (0,0,1), rot)
            # pinmark=pinmark.translate((first_pos_x, E1/2-fp_r, 0)).rotate((0,0,0), (0,0,1), 180+rot)
            #show_object(pinmark)
        else:
            # first pin indicator is created with a spherical pocket
            sphere_r = (fp_r*fp_r/2 + fp_z*fp_z) / (2*fp_z)
            sphere_z = A + sphere_r * 2 - fp_z - sphere_r
            # Revolve a cylinder from a rectangle
            pinmark=cq.Workplane("XY").sphere(sphere_r).translate((-D1_t2/2+fp_d+fp_r, -E1_t2/2+fp_d+fp_r, sphere_z))
        # Rotate pinmark
        pinmark = pinmark.rotate((0,0,0), (0,0,1), rot)
        # extract pinmark from case
        temp = pinmark.intersect(case)
        if (place_pinmark==True):
            case = case.cut(pinmark)
        pinmark = temp

    # calculated dimensions for pin
    if R1 and R2:
        R1_o = R1+c # pin upper corner, outer radius
        R2_o = R2+c # pin lower corner, outer radius
    else:
        R1_o = 0.
        R2_o = 0.
        R1 = 0.
        R2 = 0.

    L_h = L - R2_o
    S1 = tan(radians(the))*A2_b
    S_h = ((E-E1)/2 - L - R1)
    P_v = (A1 + A2_b) - R1 - R2_o

    # Create a pin object at the center of top side.
    #   This one reference pin is duplicated into all locations around the case
    if not case_only and R1 and R2:
        bpin = cq.Workplane("YZ", (0,0,0,)).moveTo(-S1, A1+A2_b).\
        line(S1+S_h, 0).\
        threePointArc((S_h+R1/sqrt(2), (A1+A2_b)-R1*(1-1/sqrt(2))),(S_h+R1, A1+A2_b-R1)).\
        line(0, -P_v).\
        threePointArc((S_h+R1+R2_o*(1-1/sqrt(2)), A1+A2_b-R1-P_v-R2_o*1/sqrt(2)),(S_h+R1+R2_o, 0)).\
        line(L_h, 0).\
        line(0, c).\
        line(-(L_h), 0).\
        threePointArc((S_h+R1_o+R2-R2/sqrt(2), c+R2*(1-1/sqrt(2))),(S_h+R1_o, c+R2)).\
        line(0, P_v).\
        threePointArc((S_h+R1_o-R1_o*(1-1/sqrt(2)), A1+A2_b+c-R1_o*(1-1/sqrt(2))),(S_h,A1+A2_b+c)).\
        line(-S_h-S1, 0).\
        close().extrude(b).translate((-b/2,0,0))
        #
    else:
        bpin = cq.Workplane("XY").box(b,L,c).translate((0,0,c/2.))
    #if debug_plot: show_object(bpin)

    if not case_only:
        print("Start Pins")
        mpins = None
        pincounter = 1
        first_pos_x = (npx-1)*e_x/2
        r,g,b,a = pins_color

        for i in range(npx):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e_x, x_pin_offset, 0)).\
                    rotate((0,0,0), (0,0,1), 180+rot)
                case = case.cut(pin)
                if mpins == None : mpins = Assembly(pin, color=Color(r,g,b,a))
                else : mpins = mpins.add(pin, color=Color(r,g,b,a))                    
            pincounter += 1
        #show_object(mpins)
        print("Done Side 1")
        
        for i in range(npy):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_y-i*e_y, y_pin_offset, 0)).\
                    rotate((0,0,0), (0,0,1), 270+rot)
                case = case.cut(pin)
                if mpins == None : mpins = Assembly(pin, color=Color(r,g,b,a))
                else : mpins = mpins.add(pin, color=Color(r,g,b,a))
            pincounter += 1
        #show_object(mpins)
        print("Done Side 2")
        
        for i in range(npx):
            if pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e_x, x_pin_offset, 0)).\
                    rotate((0,0,0), (0,0,1), rot)
                case = case.cut(pin)
                if mpins == None : mpins = Assembly(pin, color=Color(r,g,b,a))
                else : mpins = mpins.add(pin, color=Color(r,g,b,a))
            pincounter += 1
        print("Done Side 3")
        
        for i in range(npy):
            if D and pincounter not in excluded_pins:
                pin = bpin.translate((first_pos_y-i*e_y, y_pin_offset, 0)).\
                    rotate((0,0,0), (0,0,1), 90+rot)
                case = case.cut(pin)
                if mpins == None: mpins = Assembly(pin, color=Color(r,g,b,a))
                else:  mpins = mpins.add(pin, color=Color(r,g,b,a))
            pincounter += 1
        print("Done Side 4")
        #if debug_plot: show_object(mpins)
                
        # create exposed thermal pad if requested
        if epad:
            print("epad,epad_thickness,epad_rotation",epad,epad_thickness,epad_rotation)
            if rec_epad:
                pin = cq.Workplane("XY").box(D2, E2, epad_thickness).\
                    translate((epad_offset_x,epad_offset_y,epad_thickness/2)).\
                    rotate((0,0,0), (0,0,1), epad_rotation+rot)
                case = case.cut(pin)
                mpins = mpins.add(pin, color=Color(r,g,b,a))
            else:
                pin = cq.Workplane("XY").circle(epad_r).extrude(A1)#.translate((0,0,A1/2))
                case = case.cut(pin)
                mpins = mpins.add(pin, color=Color(r,g,b,a))                    
        
    r,g,b,a = body_color
    pkg = Assembly(case, color=Color(r,g,b,a))

    if (color_pinmark==True) and (place_pinmark==True):
       r,g,b,a = mark_color
       pkg = pkg.add(pinmark, color=Color(r,g,b,a))

    if case_only == False:
       r,g,b,a = pins_color
       pkg = pkg.add(mpins)

    ##############
    # Process text lines here            
    if text_defs: pkg = wr_body_txt(pkg, params)

    if debug_plot: show_object(pkg)

    return (pkg)

################################################################################
################################################################################
################################################################################
################################################################################

def export_one_part(params, log):
    global lib_name
    ModelName = params.modelName
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')

    print('\n######################### {:s} ###########################\n'.format(ModelName))
    global pkg_cnt
    dest_dir_pref = params.dest_dir_prefix
    subf = ''
    if dest_dir_pref != '': subf = '->'
    log.write('\nPkg # {:d}: {:s}: {:s} {:s} {:s}'.format(pkg_cnt,series.__name__,ModelName,subf,dest_dir_pref))
    pkg_cnt += 1

    if not trial_run: pkg = make_pkg(params)
    #show_object(pkg)
    dest_dir_pref = params.dest_dir_prefix        
    mod_out_dir='{:s}{:s}{:s}'.format(global_3dpath, lib_name, dest_dir_pref)
    if not os.path.exists(mod_out_dir):
        os.makedirs(mod_out_dir)
        
    if no_export == False and trial_run == False:
        StepFileName=mod_out_dir+os.sep+ModelName+'.step'
        pkg.save(StepFileName, exportType = 'STEP')
        
        global LIST_license
        if LIST_license[0]=="":
            LIST_license=Lic.LIST_int_license
            LIST_license.append("")
        Lic.addLicenseToStep(mod_out_dir, ModelName+".step", LIST_license,\
            STR_licAuthor, STR_licEmail, STR_licOrgSys, STR_licOrg, STR_licPreProc)
    else:
        print("Not exporting models")

def exportSeries(series, log, model_filter_regobj):
    global series_def
    series_def = series.SeriesParams

    global body_color_key
    global body_top_color_key
    global pins_color_key
    global mark_color_key
    global lib_name

    if series_def.body_color_key: body_color_key = series_def.body_color_key
    if series_def.body_top_color_key: body_top_color_key = series_def.body_top_color_key
    if series_def.pins_color_key: pins_color_key = series_def.pins_color_key
    if series_def.mark_color_key: mark_color_key = series_def.mark_color_key
    if series_def.lib_name: lib_name = series_def.lib_name

    log.write('\n\n# Series output path: {:s}{:s}'.format(global_3dpath,lib_name))

    for variant in series.pkg_defs:
        thisPkg = series.pkg_defs[variant]
        try:
            if model_filter_regobj.match(thisPkg.modelName):
                export_one_part(thisPkg, log)
        except GeometryError as e:
            e.print_errors(stop_on_first_error)
            if stop_on_first_error:
                return -1
    return 0

#########################  ADD MODEL GENERATORS #########################
import cq_parameters_test
import cq_parameters_fp_diode
import cq_parameters_fp_sot
from cq_parameters_test import *
from cq_parameters_fp_diode import *
from cq_parameters_fp_sot import *

all_series = {
    'test':cq_parameters_test,
    'fp_diode':cq_parameters_fp_diode,
    'fp_sot':cq_parameters_fp_sot,
}

#########################################################################	
#
# Main Program Loop
#
#########################################################################


class argparse():
    def __init__(self):
        self.model_filter = '*'
        self.series = list(all_series.values())

    def parse_args(self, args):
        global cmd_line
        for arg in args:
            cmd_line +='{:s} '.format(arg)
            if '=' in arg:
                self.parseValueArg(*arg.split('='))
            else:
                self.argSwitchArg(arg)

    def parseValueArg(self, name, value):
        if name == 'model_filter' or name == 'mf':
            self.model_filter = value
        elif name == 'log':
            global build_log_file
            build_log_file = value
        elif name == 'series' or name == 's':
            series_str = value.split(',')
            self.series = []
            for s in series_str:
                if s.lower() in all_series:
                    self.series.append(all_series[s.lower()])
                elif s.lower() == 'all':
                    self.series = []
                    for s in all_series:
                        self.series.append(all_series[s.lower()])
                    break
                elif s.lower() == '?':
                    self.series = [] # don't build if series list requested
                    print("\n**************\nSeries List:")
                    for s in all_series:
                        print("\t"+s)
                    print("**************\n")
                    break
                else:
                    print("Bad series name: ", s.lower())
        else:
            print("******** Unrecognised Parameter:",name,value)
            return -1


    def argSwitchArg(self, name):
        if name == '?' or name == 'help':
            self.print_usage()
            exit()
        elif name == 'error_tolerant' or name == 'et':
            global stop_on_first_error
            stop_on_first_error = False
        elif name == 'no_export':
            global no_export
            no_export = True
        elif name == 'case_only':
            global case_only
            case_only = True
        elif name == 'trial_run':
            global trial_run
            trial_run = True
        elif name == 'debug_plot':
            global debug_plot
            debug_plot = True
        elif name == 'debug_print':
            global debug_print
            debug_print = True
        elif name == 'disable_marker_color':
            global color_pinmark
            color_pinmark = False
            no_export = True
        elif name == 'main_generator.py':
            None
        else:
            print("******** Unrecognised Switch:",name)
            return -1

    def print_usage(self):
        print("\nGenerater script for BGA type packages 3d models.")
        print('usage: main_generator.py [optional arguments and switches]\n\tNote: no argument builds all modelsn ... same as s=all')
        print('optional arguments:')
        print('\tmodel_filter=[filter pincount using linux file filter syntax]\n\t\tabbreviation: mf=[...]')
        print('\tlog=[log file path]')
        print('\tseries=[series name],[series name],..\n\t\tabreviation: s=[series name],[series name], ...')
        print('\t\t*** use series=all to build all packages ***')
        print('\t\t*** use series=? to print a list of series ***')
        print('switches:')
        print('\t? or help - this message')
        print('\terror_tolerant')
        print('\tno_export')
        print('\tcase_only')
        print('\ttrial_run - produce trial-run without building packages, log file is generated')
        print('\tdebug_plot - use only with cq-editor, will crash from cmd line')
        print('\tdebug_print')
        print('\tdisable_marker_color')
        print('series:')
        for s in all_series:
            print("\t"+s)


    def __str__(self):
        return 'filter:{:s}, series:{:s}'.format(self.model_filter, str(self.series))

if __name__ == "temp":
    print("Re-import")
    importlib.reload(cq_parameters_test) # For debug reload
    importlib.reload(cq_parameters_fp_diode) # For debug reload
    importlib.reload(cq_parameters_fp_sot) # For debug reload

    print("Fake out command line below\n")
    __name__ = "__main__"
    sys.argv=['main_generator.py', 'series=test', 'debug_plot']
    #sys.argv=['main_generator.py', 'series=test', 'debug_plot', 'debug_print']

#
# when run from command line
if __name__ == "__main__" or __name__ == "main_generator": 
    
    cmd_line = ''    
    args = argparse()
    args.parse_args(sys.argv)
    modelfilter = args.model_filter
    
    model_filter_regobj=re.compile(fnmatch.translate(modelfilter))
    
    print('\r\nRunning...\r\n')
    with open(build_log_file, 'w') as log:
        log.write('# Build report for Flat pin packages 3d model genration\n')
        log.write('# Command line: {:s}'.format(cmd_line))
        for series in args.series:
            try:
                if exportSeries(series, log, model_filter_regobj) != 0:
                    break
            except Exception as exeption:
                traceback.print_exc()
                break
        log.write('\n\nEND BUILD LOG FILE\n')
    
    print('\n\nDone\n')
