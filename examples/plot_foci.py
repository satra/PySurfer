"""
====================
Plot Activation Foci
====================

Plot spheroids at positions on the surface manifold
according to coordinates or vertex ids.

"""
print __doc__

import os
import os.path as op
from numpy import arange
from numpy.random import permutation
from surfer import Brain
from surfer import io

subject_id = "fsaverage"
subjects_dir = os.environ["SUBJECTS_DIR"]

"""
Bring up the visualization.
"""
brain = Brain(subject_id, "lh", "inflated")

"""
First we'll get a set of stereotaxic foci in the MNI
coordinate system. These might be peak activations from
a volume based analysis.
"""
coords = [[-36, 18, -3],
          [--39, 17, 2],
          [-43, 25, 24],
          [-48, 26, -2]]

"""
We can control the color of the sphereoids with 
an rgb triplet where values range from 0 to 1.
(They are white by default.)
"""
rgb = (1, .63, .49)

"""
Now we plot the foci on the inflated surface. We will map
the foci onto the surface by finding the vertex on the "white"
mesh that is closest to the coordinate of each point we want 
to display.

While this is not a perfect transformation, it can give you
some idea of where peaks from a volume-based analysis would
be located on the surface.
"""
brain.add_foci(coords, map_surface="white", color=rgb)

"""
You can also plot foci with a set of surface vertex ids.
For instance, you might want to plot the peak activation
within an ROI for each of your indivdiual subjects over
the group activation map.

Here, we will just demonstrate with a set of randomly
choosen vertices from within the superior temporal sulcus.

First, we load in the Destrieux parcellation annotation file.
"""
annot_path = op.join(subjects_dir, subject_id, "label/lh.aparc.a2009s.annot")
ids, ctab = io.read_annot(annot_path)

"""
Then, find 10 random vertices within the STS.
"""
verts = arange(0, len(ids))
coords = permutation(verts[ids == 74])[:10]

"""
You can also control the size of the spheroids.
We'll make these a little bit bigger than our
other foci.
"""
scale_factor = 1.3

"""
Finally, plot the foci using the coords_as_verts option to
center each sphereoid at its vertex id.
"""
brain.add_foci(coords, coords_as_verts=True, 
               scale_factor=scale_factor, color=(.46, .7, .87))
