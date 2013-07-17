#!/opt/local/bin/python2.7

import numpy
import scipy.io

import pylab as pl

from sklearn import cluster
from sklearn.decomposition import FastICA


vox_data = scipy.io.loadmat('reverse_meanLis.mat')
meanVox = vox_data["meanVox"] #unpacking clutter

# Let's take a look at what we are working with
v = len(meanVox)
t = len(meanVox[1])
print "Time steps ", t          # 35593
print "Number of voxels ", v    # 260

# We got 35593 voxels a 260 measurements
# Assuming the number of time steps is the same for all entries

# Let's take a look at another data set
# Broadman indices for the voxels 
brod_data = scipy.io.loadmat('brodmann_area.mat')
indices = brod_data["brodmannIdx"][0] #unpacking clutter

max_idx = len(indices)
print "Number of indexed voxels", max_idx
print "Up to Brodman area ", indices.max() # 47

# Let's see if naively clustering voxels using kmeans into 47 classes
# will show any overlap with the actualy recorded indices we got from brodmanIdx
# Doing this for all 30k voxels would take for ever. 
# Let's first look at a couple of hundred
#mv = meanVox[:100]
#k_means = cluster.KMeans(n_clusters=47) 
#k_means.fit(mv)
# Suppose if we use reverse_meansList we will also have to reverse our indices
rev = indices[::-1] 
#print k_means.labels_
#print rev[:100]
# Set number of 47 clusters doesn't work anymore when only using a fraction of 
# the data because not all classes might show up.
# The first hundred entries of rev only feature 5 different brodman areas
# Let's fix this
k_means = cluster.KMeans(n_clusters=5) 
k_means.fit(mv)
print k_means.labels_
print rev[:100]
# No obvious correlation between the two
# TODO: Check if the indices and the reverse_meanList really express what you 
# think they do. You might be looking at wrong sections




