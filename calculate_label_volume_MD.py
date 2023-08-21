import MDAnalysis as mda
from MDAnalysis.lib.distances import distance_array
import numpy as np
import matplotlib.pyplot as plt

u = mda.Universe('structure.pdb', 'trajectory.xtc') # set the PDB and trajectory files
resname = 'M28' # label resname
L = 30 # offset for the box in Angstrom from the label_ca atom
random_size = 10000 # number of random dots
cutoff = 3 # minimal distance to count a random dot as matching the label position
stride = 10 # do calculation every stride-th step

label_ca = u.select_atoms("resname "+ resname +" and name CA").positions[0]

label_xyz = []
for ts in u.trajectory:
    label = u.select_atoms("resname " + resname)
    label_xyz.append(label.positions)

# generate random dots within the box defined by (label_ca - L, label_ca + L)
random_x = np.random.uniform(label_ca[0] - L, label_ca[0] + L, random_size)
random_y = np.random.uniform(label_ca[1] - L, label_ca[1] + L, random_size)
random_z = np.random.uniform(label_ca[2] - L, label_ca[2] + L, random_size)
box_vol = (2*L)**3
radom_xyz = np.vstack([random_x, random_y, random_z]).T

# calculate volume
vols = []
for i in range(1, len(label_xyz), stride):
    dist_arr = np.zeros((np.vstack(label_xyz[:i]).shape[0], radom_xyz.shape[0]))
    distance_array(np.vstack(label_xyz[:i]), radom_xyz, result = dist_arr)
    count = ((dist_arr < cutoff).sum(axis = 0) > 0).sum()
    p = count/random_size
    vols.append(p * box_vol)
    print(p * box_vol)
    
plt.plot(vols)