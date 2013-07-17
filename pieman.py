#!/opt/local/bin/python2.7

import numpy
import scipy.io
from sklearn import cluster
from sklearn.decomposition import FastICA


vox_data = scipy.io.loadmat('reverse_meanLis.mat')
meanVox = vox_data["meanVox"] #unpacking clutter

#Let's take a look at what we are working with
v = len(meanVox)
t = len(meanVox[1])
print "Time steps ", t          # 35593
print "Number of voxels ", v    # 260

#We got 35593 voxels a 260 measurements
#Assuming the number of time steps is the same for all entries

#Let's take a look at another data set
#Broadman indices for the voxels 
brod_data = scipy.io.loadmat('brodmann_area.mat')
indices = brod_data["brodmannIdx"][0] #unpacking clutter

max_idx = len(indices)
print "Number of indexed voxels", max_idx
print "Up to Brodman area ", indices.max() # 47

#Let's see if naively clustering voxels using kmeans into 47 classes
#will show any overlap with the actualy recorded indices we got from brodmanIdx
#Working with all 30k voxels will take seceral min.
#TODO: Considere what a good fraction of the data is to develop on
mv = meanVox
k_means = cluster.KMeans(n_clusters=47) 
k_means.fit(mv)
#Suppose if we use reverse_meansList we will also have to reverse our indices
rev_indices = indices[::-1] 
labels = k_means.labels_

#There is no obvious overlap of clusteres for just the first 100 voxels
#TODO: Let's try checking whether rev_indices and the classes kmeans found have 
#any correlation 



