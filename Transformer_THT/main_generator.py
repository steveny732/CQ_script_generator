# -*- coding: utf8 -*-
#!/usr/bin/python
#
# This is derived from a cadquery script for generating THT Xformer models in 3D format.
#
# from https://bitbucket.org/hyOzd/freecad-macros
# author hyOzd
#
# ???? Dimensions are from Jedec MS-026D document ????

## requirements
# cadquery2                                                                 *
##   https://cadquery.readthedocs.io/en/latest                              *
##   ??? https://github.com/jmwright/cadquery-freecad-module                *

## to run the script just do: freecad make_gwexport_fc.py modelName
## e.g. c:\freecad\bin\freecad make_gw_export_fc.py SOIC_8

## the script will generate STEP models
## to be used with kicad

#* These are Cadquery 2.0 tools                                             *
#* to export generated models in STEP format.                               *
#*                                                                          *
#* cadquery script for generating THT Transformer models in STEP AP214      *
#*   Copyright (c) 2015                                                     *
#* Maurice https://launchpad.net/~easyw                                     *
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
print("Start")
__title__ = "make THT Transformer 3D models"
__author__ = "maurice and hyOzd"
__Comment__ = 'make THT Transformer 3D models exported to STEP script'
___ver___ = "1.4.0 12/09/2020"

global stop_on_first_error
global place_pinmark
global color_pinmark
global ink_thickness
global build_all
global no_export
global case_only
global trial_run
global test_plot
global test_print
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
ink_thickness = .005
build_all = False
no_export = False
trial_run = False
case_only = False
test_plot = False
test_print = False
global_3dpath = '../_3Dmodels/' # production path

import argparse

import cadquery as cq
from cadquery import *
from math import tan, radians, sqrt
from collections import namedtuple

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
#################################################################################################
import add_license as Lic

STR_licAuthor = "CadQuery2"
STR_licEmail = "ksu"
STR_licOrgSys = "CadQuery2"
STR_licPreProc = "OCC"
STR_licOrg = "CadQuery2"

LIST_license = ["",]
#################################################################################################

# all_params = dict(all_params1.items() | all_params2.items())


def make_pkg(params):

    modelName = params.modelName
    serie = params.serie
    A1 = params.A1
    body = params.body
    top = params.top
    pin = params.pin
    npth = params.npth
    body_top_color_key = params.body_top_color_key
    body_color_key = params.body_color_key
    pin_color_key = params.pin_color_key
    rotation = params.rotation
    dest_dir_prefix = params.dest_dir_prefix
    
    
    body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
    body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    pins_color = shaderColors.named_colors[pin_color_key].getDiffuseFloat()
    
    # Dummy
    tx = body[0]
    if body[0] < 0:
        tx = tx + 1
    else:
        tx = body[0] - 1
    ty = body[1]
    if body[0] < 0:
        ty = ty + 1
    else:
        ty = body[0] - 1
    case_top = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(tx, 0-ty).rect(0.1, 0.1, False).extrude(0.1)

    if top != None:
        case_top = cq.Workplane("XY").workplane(offset=A1 + body[4] - 0.1).moveTo(top[0], 0-top[1]).rect(top[2], 0-top[3], False).extrude(top[4] + 0.1)
        case_top = case_top.faces(">Y").edges("<X").fillet(1.0)
        case_top = case_top.faces(">Y").edges(">X").fillet(1.0)
        case_top = case_top.faces("<Y").edges("<X").fillet(1.0)
        case_top = case_top.faces("<Y").edges(">X").fillet(1.0)
        case_top = case_top.faces(">Z").edges(">X").fillet(1.0)
        #
        if (rotation != 0):
            case_top = case_top.rotate((0,0,0), (0,0,1), rotation)    
    
    case = cq.Workplane("XY").workplane(offset=A1).moveTo(body[0], 0-body[1]).rect(body[2], 0-body[3], False).extrude(body[4])
    case = case.faces(">Y").edges("<X").fillet(1.0)
    case = case.faces(">Y").edges(">X").fillet(1.0)
    case = case.faces("<Y").edges("<X").fillet(1.0)
    case = case.faces("<Y").edges(">X").fillet(1.0)
    case = case.faces(">Z").edges(">X").fillet(1.0)
    #
    if (rotation != 0):
        case = case.rotate((0,0,0), (0,0,1), rotation)    
        
    p = pin[0]
    pins = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(p[2] / 2.6, False).extrude(0 - (p[3] + A1 + 1.0))
    pins = pins.faces("<Z").fillet(p[2] / 5.0)
    for i in range(1, len(pin)):
        p = pin[i]
        pint = cq.Workplane("XY").workplane(offset=A1 + 1.0).moveTo(p[0], -p[1]).circle(p[2] / 2.6, False).extrude(0 - (p[3] + A1 + 1.0))
        pint = pint.faces("<Z").fillet(p[2] / 5.0)
        pins = pins.union(pint)

    if (rotation != 0):
        pins = pins.rotate((0,0,0), (0,0,1), rotation)
        
    # Create pkg assembly
    r,g,b,a = body_color
    pkg = (
        Assembly(case, color=Color(r,g,b,a))
    )
    if test_plot: show_object(pkg)
    if top != None:
        r,g,b,a = body_top_color
        pkg.add(case_top, color=Color(r,g,b,a))
        
    r,g,b,a = pins_color
    pkg.add(pins, color=Color(r,g,b,a))
        
    return (pkg)


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
import cq_parameters_THT_transformer

all_series = {
    'test':cq_parameters_test,
    'tht_xformer':cq_parameters_THT_transformer,
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
        if name == 'model_filter':
            self.model_filter = value
        elif name == 'log':
            global build_log_file
            build_log_file = value
        elif name == 'series':
            series_str = value.split(',')
            self.series = []
            for s in series_str:
                if s.lower() in all_series:
                    self.series.append(all_series[s.lower()])
                elif s.lower() == 'all':
                    self.series = []
                    for s in all_series:
                        self.series.append(all_series[s.lower()])
                elif s.lower() == '?':
                    self.series = [] # don't build if series list requested
                    print("\n**************\nSeries List:")
                    for s in all_series:
                        print("\t"+s)
                    print("**************\n")

    def argSwitchArg(self, name):
        if name == '?' or name == 'help':
            self.print_usage()
            exit()
        elif name == 'error_tolerant':
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
        elif name == 'test_plot':
            global test_plot
            test_plot = True
        elif name == 'test_print':
            global test_print
            test_print = True
        elif name == 'disable_marker_color':
            global color_pinmark
            color_pinmark = False
            no_export = True

    def print_usage(self):
        print("\nGenerater script for gull wing type packages 3d models.")
        print('usage: main_generator.py [optional arguments and switches]')
        print('optional arguments:')
        print('\tmodel_filter=[filter pincount using linux file filter syntax]')
        print('\tlog=[log file path]')
        print('\tseries=[series name],[series name],...')
        print('\t*** use series=all to build all packages ***')
        print('\t*** use series=? to print a list of series ***')
        print('switches:')
        print('\t? or help - this message')
        print('\terror_tolerant')
        print('\tno_export')
        print('\tcase_only')
        print('\rtrial_run - produce trial-run without building packages, log file is generated')
        print('\ttest_plot - use only with cq-editor, will crash from cmd line')
        print('\ttest_print')
        print('\tdisable_marker_color\n')
        print('series:')
        for s in all_series:
            print("\t"+s)


    def __str__(self):
        return 'config:{:s}, filter:{:s}, series:{:s}'.format(
            self.config, self.model_filter, str(self.series))

if __name__ == "temp":
    print("Re-import")
    importlib.reload(cq_parameters_test) # For debug reload
    importlib.reload(cq_parameters_THT_transformer) # For debug reload

    print("Fake out command line below\n")
    __name__ = "__main__"
    sys.argv=['main_generator.py', 'series=test', 'test_plot']

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
        log.write('# Build report for THT Transformer packages 3d model genration\n')
        log.write('# Command line: {:s}'.format(cmd_line))
        for series in args.series:
            try:
                if exportSeries(series, log, model_filter_regobj) != 0:
                    break
            except Exception as exeption:
                traceback.print_exc()
                break
        log.write('\n\nEND LOG FILE\n')
    
    print('\n\nDone\n')
