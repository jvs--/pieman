#!/opt/local/bin/python2.7

import numpy
import scipy.io
import pylab as pl

from numpy import corrcoef, linspace
#from sklearn import cluster

##--- UTILITY FUNCTIONS -------------------------------------------------------
def vox_by_bidx(voxels, indices):
    """Returns dict of voxels by region given a sequence of voxels and 
    corresponding indices.
    
    Keyword arguments:
    voxel -- an array of voxel activations 
    indices -- an array of indices of each voxels
    """
    idx_to_vox = {}
    for count, idx in enumerate(indices):
        #meanVox[count]
        if idx_to_vox.has_key(idx):
            idx_to_vox[idx].append(voxels[count])
            #idx_to_vox[idx].append((count, voxels[count]))
        else:
            idx_to_vox[idx] = [voxels[count]]
            #idx_to_vox[idx] = [(count, voxels[count])] 

    #print "# distinct brodmann areas:", len(idx_to_vox)
    #print "brodmann areas:", idx_to_vox.keys()
    for i in idx_to_vox.keys():
        print i, len(idx_to_vox[i])
    return idx_to_vox

##--- DATA INPUT --------------------------------------------------------------
# Reading voxel files
vox_data1 = scipy.io.loadmat('fullStory_meanLis.mat')
vox_data2 = scipy.io.loadmat('Words_meanLis.mat')
vox_data3 = scipy.io.loadmat('Reverse_meanLis.mat')

# Unpacking clutter
meanVox1 = vox_data1["meanVox"]
meanVox2 = vox_data2["meanVox"]
meanVox3 = vox_data3["meanVox"]
#meanVox = meanVox[0:10000] # only use part of the data

# Brodmann indices of each voxel
brod_data = scipy.io.loadmat('brodmann_area.mat') 
indices = brod_data["brodmannIdx"][0]


##--- IMPLEMENTATION ----------------------------------------------------------
# Sort voxels by brodmann indices 
vb1 = vox_by_bidx(meanVox1, indices)
vb2 = vox_by_bidx(meanVox2, indices)
vb3 = vox_by_bidx(meanVox3, indices)


# Calculating and plotting correlations between different brodmann areas
# Area 41 and 41 (Auditory cortex)
print "VB1", vb1[41]

corr = corrcoef(vb1[41]+vb1[42])
pl.title('area 41 vs area 42')
pl.pcolor(corr)
pl.colorbar()
pl.savefig("corr41-42.png",dpi=100)
pl.show()

# Area 41 and 22 (Auditory Cortex and superior temoral gyrus)
corr = corrcoef(vb1[41]+vb1[22])
pl.title('area 41 vs area 22')
pl.pcolor(corr)
pl.axis([0, 700, 0, 700])
pl.colorbar()
pl.savefig("corr41-22.png",dpi=100)
pl.show()

# Area 41 and 4 (Auditory Cortex and primary motor cortex)
corr = corrcoef(vb2[41]+vb1[4])
pl.title('area 41 vs area 4')
pl.pcolor(corr)
pl.axis([0, 700, 0, 700])
pl.colorbar()
pl.savefig("corr41-4.png",dpi=100)
pl.show()


# Area 22 of the word scamble condition
corr = corrcoef(vb2[22])
pl.title('area 22')
pl.pcolor(corr)
pl.colorbar()
pl.savefig("corr22.png",dpi=100)
pl.show()


# Area 22 of the word scamble condition
corr = corrcoef(vb1[41]+vb1[40])
pl.title('area 41 vs area 40')
pl.pcolor(corr)
pl.axis([0, 1200, 0, 1200])
pl.colorbar()
pl.savefig("corr41-40.png",dpi=100)
pl.show()

# Let's try if kmeans can pick up on the difference in the recoding of case 1 and 2
data = vb1[41]+vb3[41]
k_means = cluster.KMeans(n_clusters=2) 
k_means.fit(data)
print k_means.labels_ # looks good

#for k in range(2):
#    my_members = k_means.labels_ == k
#    pl.plot(data[my_members, 0], data[my_members, 1], marker='o')            
#pl.savefig("cluster1.png",dpi=100)
#pl.show()

# Let's try the same for somewhat mixed data
data = vb1[41][:10]+vb3[41][:10]+vb1[41][10:20]+vb3[41][10:20]
k_means = cluster.KMeans(n_clusters=2) 
k_means.fit(data)
print k_means.labels_ # looks good

#for k in range(2):
#    my_members = k_means.labels_ == k
#    pl.plot(data[my_members, 0], data[my_members, 1], marker='o')
#pl.savefig("cluster2.png",dpi=100)
#pl.show()

data = vb1[42]+vb1[22]+vb1[4]
k_means = cluster.KMeans(n_clusters=3) 
k_means.fit(data)
print k_means.labels_ 

# Nr of voxels in each area
"""
0 19367
1 2
2 137
3 229
4 503
5 216
6 1869
7 1422
8 557
9 856
10 474
13 856
17 237
18 956
19 958
20 31
21 140
22 528
23 157
24 555
25 43
27 34
28 21
29 152
30 449
31 981
32 739
33 38
34 19
35 49
36 83
37 447
38 53
39 494
40 1027
41 201
42 149
43 96
44 122
45 61
46 136
47 149"""




