#!/opt/local/bin/python2.7

import numpy
import scipy.io
from sklearn import cluster
from sklearn.decomposition import FastICA


vox_data = scipy.io.loadmat('pieman_meanLis.mat')
meanVox = vox_data["meanVox"] #unpacking clutter

#Let's take a look at what we are working with
v = len(meanVox)
t = len(meanVox[1])
print "Time steps ", t          # 38326
print "Number of voxels ", v    # 259

#We got 38326 voxels a 259 measurements
#Assuming the number of time steps is the same for all entries

#Let's take a look at another data set
#Broadman indices for the voxels 
brod_data = scipy.io.loadmat('brodmann_area.mat')
indices = data["brodmannIdx"][0] #unpacking clutter
max_idx = len(indices)
print "Number of indexed voxels", max_idx
print "Up to Brodman area ", indices.max() # 47

#Not good. Number of indeces (35593) does not match with number of voxels (38326) 

#Let's see if naively clustering voxels using kmeans into 47 classes
#will show any overlap with the actualy recorded indices we got from brodmanIdx
#Doing this for all 30k voxels would take for ever. let's first look at a couple of hundred
mv = meanVox[:100]
k_means = cluster.KMeans(n_clusters=47) 
k_means.fit(mv)
print k_means.labels_[::10]
