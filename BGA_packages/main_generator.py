
__title__ = "make BGA ICs 3D models"
__author__ = "s. yoder"
__Comment__ = 'make BGA ICs 3D models exported to STEP'

___ver___ = "1.4 12/23/2020"

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
from math import tan, sin, cos, radians, sqrt
from collections import namedtuple

global typ_fil
global typ_cham
typ_fil = 1
typ_cham = 2

import sys, os
import importlib
import traceback
import datetime
from datetime import datetime

def AddSysPath(new_path):
	if not os.path.exists(new_path): return -1   
	new_path = os.path.abspath(new_path)
	if sys.platform == 'win32':
		new_path = new_path.lower(  )
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

def rect(wp, rw, rh, ef_cc1 = 0, ef_cc = 0, c_type = 2):
    """
    Creates a rectangle with fillet corners.
    wp: workplane object
    rw: rectangle width
    rh: rectangle height
    ef: corner fillet
    type:
        typ_fil - fillet   : 1
        typ_cham -  chamfer : 2
    """
    global typ_fil
    global typ_cham

    acen1 = sin(radians(45))
    if ef_cc1 > 0 : acen1 = 1-acen1 # Positive fillet

    acen = sin(radians(45))
    if ef_cc > 0 or ef_cc > 0: acen = 1-acen # Positive fillet

    ef_cc1 = abs(ef_cc1)
    ef_cc = abs(ef_cc)

    wp = wp.moveTo(-rw/2+ef_cc1, -rh/2)
    if ef_cc1 > 0:
        if c_type != typ_cham: 
            wp = wp.threePointArc((-rw/2+acen1*ef_cc1, -rh/2+acen1*ef_cc1), (-rw/2, -rh/2+ef_cc1))
        else: 
            wp = wp.lineTo(-rw/2, -rh/2+ef_cc1)
    wp = wp.lineTo(-rw/2, rh/2-ef_cc)
    if ef_cc > 0:
        if c_type != typ_cham: 
            wp = wp.threePointArc((-rw/2+acen*ef_cc, rh/2-acen*ef_cc), (-rw/2+ef_cc, rh/2))
        else: 
            wp = wp.lineTo(-rw/2+ef_cc, rh/2)
    wp = wp.lineTo(rw/2-ef_cc,rh/2)
    if ef_cc > 0:
        if c_type != typ_cham: 
            wp = wp.threePointArc((rw/2-acen*ef_cc, rh/2-acen*ef_cc), (rw/2, rh/2-ef_cc))
        else: 
            wp = wp.lineTo(rw/2, rh/2-ef_cc)
    wp = wp.lineTo(rw/2,-rh/2+ef_cc)
    if ef_cc > 0:
        if c_type != typ_cham: 
            wp = wp.threePointArc((rw/2-acen*ef_cc, -rh/2+acen*ef_cc), (rw/2-ef_cc, -rh/2))
        else: 
            wp = wp.lineTo(rw/2-ef_cc, -rh/2)
    wp = wp.close()

    return(wp) #, forConstruction=True)

#def tst_print()

def wr_body_txt(assy, params):

    text_defs = params.text_defs
    if params.rotation: rot = params.rotation
    else: rot = 0.
    D = params.D
    E = params.E
    if params.D1: D1 = params.D1
    else: D1 = D
    if params.E1: E1 = params.E1
    else: E1 = E

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

        wp = cq.Workplane(cq.Plane.XY()).workplane(offset=params.A)

        if txt: wp=wp.text(cut=False,txt=txt,fontsize=fsize,distance=.005,clean=True,halign=halign,valign=valign)
        if line.dot:
            r,pos_x,pos_y = line.dot
            wp=wp.circle(r).extrude(ink_thickness)
            print(r,pos_x,pos_y)

        txt_offset = (-D1/2+pos_x,E1/2-pos_y-y_offset)

        wp = wp.rotate((0,0,0), (0,0,1), txt_rot).translate(txt_offset).rotate((0,0,0), (0,0,1), rot)
        lines += 1
        y_offset += fsize
        if test_plot: show_object(wp)

        ink_color_key = "white body"
        if line.ink_color_key: ink_color_key = line.ink_color_key
        r,g,b,a = shaderColors.named_colors[ink_color_key].getDiffuseFloat()
        assy.add(wp, color=Color(r,g,b,a))

    return(assy)


def make_pkg(params):    
    the  = params.the        # body angle of body in degrees  
    the2 = params.the2       # body angle of body top in degrees  
    ef   = params.ef         # 0.05,fillet of edges  
    tp_tct = params.tp_tct   # top corner type
    ct1  = params.ct1        # 0.5 chamfer of the top 1st pin corner
    ct   = params.ct         # 0.5 chamfer of the others top corners
    tp_bct = params.tp_bct   # bottom corner type
    cb1  = params.cb1        # 0.5 chamfer of the bottom 1st pin corner
    cb   = params.cb         # 0.5 chamfer of the others bottom corners
    fp_r = params.fp_r       # first pin indicator radius
    fp_d = params.fp_d       # first pin indicator distance from edge
    fp_z = params.fp_z       # first pin indicator depth
    D    = params.D          # body overall length
    E    = params.E          # body overall width
    D1   = params.D1         # top body overall length
    E1   = params.E1         # top body overall width
    A1   = params.A1         # body-board separation
    A2   = params.A2         # body bottom height optional, needed for molded
    A    = params.A          # body  overall height
    b    = params.b          # ball pin width diameter with a small extra to obtain a union of balls and case
    e    = params.e          # pin (center-to-center) distance
    ex   = params.ex         # 
    npx  = params.npx        # number of pins along X axis (width)
    npy  = params.npy        # number of pins along y axis (length)
    mN   = params.modelName  #
    rot  = params.rotation   #
    text_defs = params.text_defs # list of top of pakcage text lines
    #case_text = params[params]case_text
    #if test_print: print("text_list: ",text_list)

    global dest_dir_pref
    global body_color_key
    global body_top_color_key
    global pins_color_key
    global mark_color_key
    global ink_color_key
    global place_pinmark
    
    if params.body_color_key: body_color_key = params.body_color_key
    if params.body_top_color_key: body_top_color_key = params.body_top_color_key
    if params.pins_color_key: pins_color_key = params.pins_color_key
    if params.mark_color_key: mark_color_key = params.mark_color_key

    if not ex or ex == 0: ex = e
    if not cb1: cb1 = 0
    if not cb: cb = 0
    if not ct1: ct1 = 0
    if not ct: ct = 0

    if params.excluded_pins:
        epl = list(params.excluded_pins)
        i=0
        for i in range (0, len(epl)):
            if isinstance(epl[i], int): #long is not supported in python 3
                epl[i]=str(int(epl[i]))
                i=i+1
        excluded_pins=tuple(epl)
    else:
        excluded_pins=() ##no pin excluded

    if body_color_key: 
        body_color = shaderColors.named_colors[body_color_key].getDiffuseFloat()
    if body_top_color_key: 
        body_top_color = shaderColors.named_colors[body_top_color_key].getDiffuseFloat()
    if pins_color_key: 
        pins_color = shaderColors.named_colors[pins_color_key].getDiffuseFloat()
    if mark_color_key: 
        mark_color = shaderColors.named_colors[mark_color_key].getDiffuseFloat()

    # Build Case
    case = None
    case_t = None
    D1_t = None
    E1_t = None
    dif_b = 0
    dif_t = 0

    if not the: the = 0.
    if not the2: the2 = 0.
    if not A2: A2 = round(A - A1, 4)
    
    dif_b = tan(radians(the))*A2 # bottom width 

    if A > round(A1 + A2, 2): 
        dif_t = tan(radians(the2))*(A - A2) # top width 

    case = cq.Workplane(cq.Plane.XY()).workplane(offset=A1)
    case = rect(case, D, E, cb1, cb, tp_bct)  # bottom edges
    #if test_plot: show_object(case)
    case = case.pushPoints([(0,0)]).workplane(offset=A2)
    case = rect(case, D-2*dif_b, E-2*dif_b, cb1-dif_b, cb-dif_b, tp_bct)  # center (lower) outer edges
    #if test_plot: show_object(case)
    case = case.loft(ruled=True)
    #if test_plot: show_object(case)
    if A > round(A1 + A2, 4):
        case_t = cq.Workplane(cq.Plane.XY()).workplane(offset=A1+A2)
        case_t = rect(case_t, D1, E1, ct1, ct, tp_tct)  # bottom edges
        #if test_plot: show_object(case_t)
        case_t = case_t.pushPoints([(0,0)]).workplane(offset=A-A1-A2)
        case_t = rect(case_t, D1-2*dif_t, E1-2*dif_t, ct1-dif_t, ct-dif_t, tp_tct)  # center (lower) outer edges
        #if test_plot: show_object(case_t)
        case_t = case_t.loft(ruled=True)
        #if test_plot: show_object(case_t)
    case = case.rotate((0,0,0), (0,0,1), rot)
    if case_t: case_t = case_t.rotate((0,0,0), (0,0,1), rot)
    #if test_plot: show_object(case_t)
    #if test_plot: show_object(case)

    # Gemerate pinmark
    # first pin indicator is created with a spherical pocket
    if fp_z and fp_z <0.:
        mark_bottom = True
        fp_z = -fp_z
    else:
        mark_bottom = False

    if fp_r:
        place_pinmark = True
        if fp_r < 0.:  # Square pinmark
            fp_r = -fp_r
            pinmark=cq.Workplane("XY").box(fp_r, fp_r, fp_z)
        else:
            sphere_r = ((fp_r*fp_r/2) + (fp_z*fp_z)) / (2*fp_z)
            fp_z = (A + sphere_r*2) - fp_z - sphere_r
            pinmark=cq.Workplane("XY").sphere(sphere_r)

        if test_print: print("fp_d type: ",type(fp_d))
        if type(fp_d) == tuple: 
            #if test_print: print("XY type")
            fp_x,fp_y = fp_d
            fp_d = fp_x
            #if test_print: print("xy: ",fp_x, fp_y, fp_d)
        else: 
            #if test_print: print("single value?")
            fp_x = fp_d
            fp_y = fp_d

        #pinmark = pinmark.intersect(pm_inner)
        # extract pinmark from case
        if case_t and not mark_bottom: 
            tmp_case = case_t
            x_offset = (-D1/2+fp_d+fp_r+2*dif_t, -E1/2+fp_d+fp_r+2*dif_t, fp_z)
            if test_print: print("Mark Top two peice case")
        elif not mark_bottom: 
            tmp_case = case
            x_offset = (-D/2+fp_d+fp_r+2*dif_t, -E/2+fp_d+fp_r+2*dif_t, fp_z)
            if test_print: print("Mark Top simple case")
        else:
            tmp_case = case
            x_offset = (-D/2+fp_r/2+fp_x,-E/2+fp_r/2+fp_y,A1+fp_z/2)
            if test_print: print("Mark Bottom")
            if test_print: print(fp_x,fp_y,fp_z)

        if test_print: print("x_offset: ",x_offset)
        #if test_plot: show_object(pinmark)
        pinmark = pinmark.translate(x_offset).rotate((0,0,0), (0,0,1), rot).intersect(tmp_case)
        if place_pinmark: tmp_case = tmp_case.cut(pinmark)
        #if test_plot: show_object(pinmark)
        #if test_plot: show_object(tmp_case)

        if case_t: case_t = tmp_case
        else: case = tmp_case
    else:
        place_pinmark = False
    #show_object(pinmark)
    #show_object(case)
    # Generate BGA balls or pins
    sphere_r = b/2 *(1.05) #added extra 0.5% diameter for fusion
    s_center =(0,0,0)
    sphere = cq.Workplane("XY", s_center).sphere(sphere_r)
    bpin=sphere.translate((0,0,b/2))

    mpins = None
    r,g,b,a = pins_color
    # create top, bottom side pins
    pincounter = 1
    first_pos_x = (npx-1)*e/2
    for j in range(npy):
        for i in range(npx):
            if "internals" in excluded_pins:
                if str(int(pincounter)) not in excluded_pins:
                    if j==0 or j==npy-1 or i==0 or i==npx-1:
                        pin = bpin.translate((first_pos_x-i*e, (npy*ex/2-ex/2)-j*ex, 0)).\
                                rotate((0,0,0), (0,0,1), 180+rot)
                        if not mpins: mpins = Assembly(pin, color=Color(r,g,b,a))
                        else: mpins = mpins.add(pin, color=Color(r,g,b,a))
            elif str(int(pincounter)) not in excluded_pins:
                pin = bpin.translate((first_pos_x-i*e, (npy*ex/2-ex/2)-j*ex, 0)).\
                        rotate((0,0,0), (0,0,1), 180+rot)
                if not mpins: mpins = Assembly(pin, color=Color(r,g,b,a))
                else: mpins = mpins.add(pin, color=Color(r,g,b,a))
            pincounter += 1

    if test_print: print("body_color: ", body_color)
    r,g,b,a = body_color
    pkg = Assembly(case, color=Color(r,g,b,a))
    r,g,b,a = pins_color
    pkg.add(mpins, color=Color(r,g,b,a))

    if (place_pinmark and mark_color_key != "no color"):
        if test_print: print("add pinmark")
        r,g,b,a = mark_color
        pkg.add(pinmark, color=Color(r,g,b,a))

    if case_t:
        r,g,b,a = body_top_color
        pkg.add(case_t, color=Color(r,g,b,a))

    ##############
    # Process text lines here            
    if text_defs: pkg = wr_body_txt(pkg, params)

    if test_plot: show_object(pkg)

    return (pkg)

def export_one_part(params, log):
    ModelName = params.modelName
    CheckedModelName = ModelName.replace('.', '').replace('-', '_').replace('(', '').replace(')', '')

    print('\n######################### {:s} ###########################\n'.format(ModelName))
    global pkg_cnt
    global series
    dest_dir_pref = params.dest_dir_prefix
    subf = ''
    if dest_dir_pref != '': subf = '->'
    log.write('\nPkg # {:d}: {:s}: {:s} {:s} {:s}'.format(pkg_cnt,series.__name__,ModelName,subf,dest_dir_pref))
    pkg_cnt += 1

    if not trial_run: pkg = make_pkg(params)
    if test_plot: show_object(pkg)
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
import cq_parameters_bga

all_series = {
    'test':cq_parameters_test,
    'bga':cq_parameters_bga,
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
            print("******** Unrecognised Parameter ********")
            print(name, value)
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
        print('\rtrial_run - produce trial-run without building packages, log file is generated')
        print('\ttest_plot - use only with cq-editor, will crash from cmd line')
        print('\ttest_print')
        print('\tdisable_marker_color')
        print('series:')
        for s in all_series:
            print("\t"+s)

    def __str__(self):
        return 'filter:{:s}, series:{:s}'.format(self.model_filter, str(self.series))
        
if __name__ == "temp":
    print("Re-import")
    importlib.reload(cq_parameters_test)
    importlib.reload(cq_parameters_bga)

    print("Fake out command line below\n")
    __name__ = "__main__"
    sys.argv=['main_generator.py', 'series=bga', 'test_plot', 'test_print']

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
        log.write('# Report for BGA packages 3d model genration\n')
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
