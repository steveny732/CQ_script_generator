## file of parametric definitions

import collections
from collections import namedtuple

##enabling optional/default values to None
def namedtuple_with_defaults(typename, field_names, default_values=()):
    
    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T
    
Txt_params = namedtuple_with_defaults ("line_def", [
    'txt',
    'fsize',
    'loc',          # x y position
    'font',
    'style',
    'halign',
    'valign',
    'rotation',
    'ink_color_key',
    'dot'                # (radius, x_offset, y_offset)
])

Pkg_params = namedtuple_with_defaults ("pkg_def", [
    'the',                # body angle of body in degrees
    'the2',               # body angle of body top in degrees
    'fp_r',               # first pin indicator size, 0: None, +: radius, -:square side
    'fp_d',               # first pin indicator distance from edge, float: from corner or tupple: x,y
    'fp_z',               # first pin indicator depth, +: on top, -: on bottom
    'ef',                 # fillet of edges
    'tp_tct',             # top corner type : None = chamfer, else fillet
    'ct1',                # chamfer of the top 1st pin corner
    'ct',                 # chamfer of the other top corners
    'tp_bct',             # bottom corner type : None = chamfer, else fillet
    'cb1',                # chamfer of the bottom 1st pin corner
    'cb',                 # chamfer of the other bottom corners
    'D',                  # body overall lenght
    'E',                  # body overall width
    'D1',                 # top body overall length
    'E1',                 # top body overall width
    'A1',                 # body-board separation
    'A2',                 # body height or body bottom height optional, needed for molded
    'A',                  # body  overall height
    'b',                  # ball pin width diameter with a small extra to obtain a union of balls and case
    'e',                  # pin (center-to-center) distance along x and y axis unless e1 is present
    'ex',                 # pin (center-to-center) distance along x-axis, if this parameter is not present, then e is used
    'npx',                # number of pins along X axis (width)
    'npy',                # number of pins along y axis (length)
    'excluded_pins',      # pins to exclude -> None or "internal
    'body_color_key',     # body color
    'body_top_color_key', # body color
    'pins_color_key',     # pins color
    'mark_color_key',     # marker color
    'modelName',          # modelName
    'rotation',           # rotation if required
    'dest_dir_prefix',    # destination dir prefixD2 = params.epad[0]
    'text_defs'           # destination dir prefixD2 = params.epad[0]
])
