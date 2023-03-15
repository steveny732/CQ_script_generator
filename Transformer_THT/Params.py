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
    'modelName',            # Model name
    'serie',                # Serie 'cube' or 'cubefeet'
    'A1',                   # body-board separation 
    'body',                 # Body (x, y, w, l, h) 
    'top',                  # Top (x, y, w, l, h) 
    'pin',                  # pin (x, y, drill, length)
    'npth',                 # npth None or (x, y, drill)
    'body_top_color_key',   # Top color
    'body_color_key',       # Body color
    'pin_color_key',        # Pin color
    'rotation',             # Rotation if required
    'dest_dir_prefix'       # prefix for destination directroy
])
