#!/usr/bin/python3
# For local execution (does not require installing the library):
#%load_ext autoreload
#%autoreload 2
import sys; sys.path.append('./')

# Prettymaps
from prettymaps import *
# Vsketch
import vsketch
# OSMNX
import osmnx as ox
# Matplotlib-related
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from descartes import PolygonPatch
# Shapely
from shapely.geometry import *
from shapely.affinity import *
from shapely.ops import unary_union

fig, ax = plt.subplots(figsize = (24, 24), constrained_layout = True)


# York
#name = 'York'
#location = '53.96171,-1.07576'
#r = 1550
# Marske-by-the-sea
name = "Teesside"
location = '54.59317,-1.02894'
r = 1300
# Nuneaton
#name = 'Nuneaton'
#location = '52.5267,-1.4583'
#r = 1550

layers = plot(
    location, radius = r,
    ax = ax,
        
    layers = {
            'perimeter': {'circle': False, 'dilate': 10},
            'streets': {
                'custom_filter': '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|service|unclassified|pedestrian|footway"]',
                'width': {
                    'motorway': 5,
                    'trunk': 5,
                    'primary': 4.5,
                    'secondary': 4,
                    'tertiary': 3.5,
                    'residential': 3,
                    'service': 2,
                    'unclassified': 2,
                    'pedestrian': 2,
                    'footway': 1,
                },
                'circle': False
            },
            'building': {'tags': {'building': True, 'landuse': 'construction'}, 'union': False, 'circle': False},
            'water': {'tags': {'natural': ['water', 'bay', 'beach', 'sea'], 'place': ['sea']}, 'circle': False},
            'green': {'tags': {'landuse': ['grass', 'recreation_ground', 'farmland'], 'natural': ['island'], 'leisure': 'park'}, 'circle': False},
            'farm': {'tags': {'landuse': ['farmland']}, 'circle': False},
            'forest': {'tags': {'landuse': 'forest', 'natural': ['wood']}, 'circle': False},
            'parking': {'tags': {'amenity': 'parking', 'highway': 'pedestrian', 'man_made': 'pier'}, 'circle': False},
            'railway':{'custom_filter': '["railway"~"rail|light_rail|rail|station"]', 'dilate':2000}
        },
        drawing_kwargs = {
            'background': {'fc': '#c7c5c5', 'ec': '#e1dede', 'hatch': 'ooo...', 'zorder': -1},
            'perimeter': {'fill': False, 'lw': 0, 'zorder': 0},
            'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'hatch': '\\\\\\', 'lw': 1, 'zorder': 1},
            'farm': {'fc': '#9BAFB7', 'ec': '#486D7B', 'hatch': '\\\\\\', 'lw': 1, 'zorder': 1},
            'forest': {'fc': '#64B96A', 'ec': '#1E7B24', 'hatch': 'o.', 'lw': 1, 'zorder': 1},
            'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'hatch': 'ooo...', 'hatch_c': '#85c9e6', 'lw': 1, 'zorder': 2},
            'parking': {'fc': '#a7b9bf', 'ec': '#2F3737', 'hatch': '\\\\\\', 'lw': 1, 'zorder': 3},
            'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'lw': 0, 'zorder': 3},
            'building': {'palette': ['#6c95a3', '#406977', '#1c4351'], 'ec': '#2F3737', 'lw': .5, 'zorder': 4},
            'railway': {'fc': '#2F3737', 'ec': '#6c95a3', 'alpha': 1, 'lw': 3, 'zorder': 3},
        },
        osm_credit = False
)

# Set bounds
xmin, ymin, xmax, ymax = layers['perimeter'].bounds
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

plt.savefig("./prints/{}.png".format(name))
plt.savefig("./prints/{}.svg".format(name))
