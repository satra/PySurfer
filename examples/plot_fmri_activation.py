"""
Display fMRI Activation
=======================

Load a statistical overlay on the inflated surface.

"""

print __doc__

import os.path as op
from surfer import Brain

"""
Bring up the visualization
"""
brain = Brain("fsaverage", "lh", "inflated")

"""
Get a path to the overlay file.
"""
overlay_file = op.join("auto_examples", "data", "lh.sig.nii.gz")

"""
Display the overlay on the surface using the defaults
to control thresholding and colorbar saturation. 
These can be set through your config file.
"""
brain.add_overlay(overlay_file)

"""
To turn the overlay off, access it through the overlays
dictionary attribute and call toggle_visibility method.
"""
brain.overlays["sig"].toggle_visibility()

"""
You can also get rid of it altogether.
"""
brain.overlays["sig"].remove()

"""
Now add the overlay again, but this time with set threshold
and showing only the positive activations
"""
brain.add_overlay(overlay_file, min=5, max=20, sign="pos")
