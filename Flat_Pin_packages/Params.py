## file of parametric definitions
## Params.py
print("Import Params.py")
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

global edg_type
global edge_none
global edge_filt
global edge_cham
edge_none = 0
edge_filt = 1
edge_cham = 2

Txt_params = namedtuple_with_defaults ("line_def", [
    'txt',
    'fsize',
    'loc',             # x y position
    'font',
    'style',
    'halign',
    'valign',
    'rotation',
    'ink_color_key',
    'ink_thickness',
    'dot'              # (radius, x_offset, y_offset)
])

Pkg_params = namedtuple_with_defaults ("pkg_def", [
    'the',                # body angle in degrees
    'tb_s',               # top part of body is that much smaller
    'c',                  # pin thickness, body center part height
    'R1',                 # pin upper corner, inner radius
    'R2',                 # pin lower corner, inner radius
    'S',                  # pin top flat part length (excluding corner arc)
    'L',                  # pin bottom flat part length (including corner arc, R2_o)
    'fp_s',               # True for circular pinmark, False for square pinmark (useful for diodes)
    'fp_r',               # first pin indicator radius
    'fp_d',               # first pin indicator distance from edge
    'fp_z',               # first pin indicator depth
    'ef',                 # fillet of edges ... if tuple (top fillet,bottom fillet,[edge_type])
    'cc1',                # chamfer of the 1st pin corner, if tuple (chamf,edge_type)
    'cc',                 # chamfer of the other pin corners, if tuple (chamf,edge_type)
    'D1',                 # body length
    'E1',                 # body width
    'D',                  # body overall length
    'E',                  # body overall width
    'A1',                 # body-board separation
    'A2',                 # body height
    'b',                  # pin width
    'e',                  # pin (center-to-center) distance, if tupple then e_x,e_y
    'npx',                # number of pins along X axis (width)
    'npy',                # number of pins along y axis (length)
    'epad',               # exposed pad, None, radius as float for circular or the dimensions as tuple: (width, length) for square
    'excluded_pins',      # pins to exclude
    'body_color_key',     # body color
    'body_top_color_key', # body color
    'pins_color_key',     # pins color
    'mark_color_key',     # marker color
    'ink_color_key',      # marker color
    'modelName',          # modelName
    'rotation',           # rotation if required
    'dest_dir_prefix',    # destination dir prefixD2 = params.epad[0]
    'text_defs'           # destination dir prefixD2 = params.epad[0]
])
