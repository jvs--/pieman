#!/opt/local/bin/python2.7

import numpy
import scipy.io
import pylab as pl

from scipy.stats import norm, skew, skewtest
from sklearn import cluster
from numpy import corrcoef, linspace

##--- UTILITY FUNCTIONS -------------------------------------------------------
def vox_by_bidx(voxels, indices):
    idx_to_vox = {}
    for count, idx in enumerate(indices):
        #meanVox[count]
        if idx_to_vox.has_key(idx):
            idx_to_vox[idx].append(voxels[count])
            #idx_to_vox[idx].append((count, voxels[count]))
        else:
            idx_to_vox[idx] = [voxels[count]]
            #idx_to_vox[idx] = [(count, voxels[count])] 

    print "# distinct brodmann areas:", len(idx_to_vox)
    print "brodmann areas:", idx_to_vox.keys()
    for i in idx_to_vox.keys():
        print i, len(idx_to_vox[i])
    return idx_to_vox



def maxima(vb_dict, brodmann_area):
    vb_maxima = []
    for item in vb_dict[41]:
        maximum = item.max()
        vb_maxima.append(maximum)
        #print maximum
    return vb_maxima
    
def means(vb_dict, brodmann_area):
    vb_means = []
    for item in vb_dict[41]:
        mean = item.mean()
        vb_means.append(mean)
        #print "mean", mean
    #print "overall mean", numpy.mean(vb_means)
    return vb_means

def flatten(area):
    all_values = []
    for seq in area:
        #print seq
        all_values = all_values + list(seq)
    #print all_values
    return all_values 
 
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


#--- PLOTTING ------------------------------------------------------------------

param1 = norm.fit(vb1[41]) # distribution fitting
param2 = norm.fit(vb2[41]) # distribution fitting
param3 = norm.fit(vb3[41]) # distribution fitting

"""
x = linspace(1,4,100)
pdf_fitted1 = norm.pdf(x,loc=param1[0],scale=param1[1])
pdf_fitted2 = norm.pdf(x,loc=param2[0],scale=param2[1])
pdf_fitted3 = norm.pdf(x,loc=param3[0],scale=param3[1])
pl.title("Activity distribution of voxels in area 41")
pl.plot(x,pdf_fitted1,'g-',x,pdf_fitted2,'b-', x,pdf_fitted3,'r-')
"""

#pl.hist(vb1[41], 60, alpha=.5)
#pl.hist(vb2[41], 60, alpha=.5)
#pl.hist(vb3[41], 60, alpha=.5)

pl.savefig("dist41.png",dpi=100)
pl.show()

print "Skew of distribution:"
print skew(flatten(vb1[41]))
print skew(flatten(vb2[41]))
print skew(flatten(vb3[41]))


# Compare histogram of maximum activatio in brodmann areas 41 and 42
param1 = norm.fit(maxima(vb1,41)) # distribution fitting
param2 = norm.fit(maxima(vb2,41)) # distribution fitting
param3 = norm.fit(maxima(vb3,41)) # distribution fitting

print "Mean and std for max"
print param1
print param2
print param3

# plot gaussian
x = linspace(1,4,100)
pdf_fitted1 = norm.pdf(x,loc=param1[0],scale=param1[1])
pdf_fitted2 = norm.pdf(x,loc=param2[0],scale=param2[1])
pdf_fitted3 = norm.pdf(x,loc=param3[0],scale=param3[1])
pl.plot(x,pdf_fitted1,'g-',x,pdf_fitted2,'b-', x,pdf_fitted3,'r-')

#print "FIT", fit(vb1[41][3])
"""
# now, param[0] and param[1] are the mean and 
# the standard deviation of the fitted distribution
x = linspace(-5,5,100)
# fitted distribution
pdf_fitted = norm.pdf(x,loc=param[0],scale=param[1])
# original distribution
pdf = norm.pdf(x)

pl.title('Normal distribution')
pl.plot(x,pdf_fitted,'r-')
#pl.plot(x,pdf_fitted,'r-',x,pdf,'b-')
"""
print skew(maxima(vb1, 41))
print skew(maxima(vb2, 41))
print skew(maxima(vb3, 41))
print skewtest(maxima(vb1, 41))
print skewtest(maxima(vb2, 41))
print skewtest(maxima(vb3, 41))

pl.hist(maxima(vb1, 41), 60, color='#A8E29C', alpha=.5) # while listening to meaningful story
pl.hist(maxima(vb2, 41), 60, color='#9CA8E2', alpha=.5) # while listening to words 
pl.hist(maxima(vb3, 41), 60, color='#E29CA8', alpha=.5) # while listening to backward story
pl.savefig("hist-max.png",dpi=100)
pl.show()

"""
pl.hist(maxima(vb1, 42), 60)
pl.hist(maxima(vb2, 42), 60)
pl.show()
"""

print skew(means(vb1, 41))
print skew(means(vb2, 41))
print skew(means(vb3, 41))
print skewtest(means(vb1, 41))
print skewtest(means(vb2, 41))
print skewtest(maxima(vb3, 41))

param1 = norm.fit(means(vb1,41)) # distribution fitting
param2 = norm.fit(means(vb2,41)) # distribution fitting
param3 = norm.fit(means(vb3,41)) # distribution fitting

print "Mean and std for mean"
print param1
print param2
print param3

# Plot gaussian
x = linspace(-6e-8,6e-8,100)
pdf_fitted1 = norm.pdf(x,loc=param1[0],scale=param1[1])
pdf_fitted2 = norm.pdf(x,loc=param2[0],scale=param2[1])
pdf_fitted3 = norm.pdf(x,loc=param3[0],scale=param3[1])
pl.plot(x,pdf_fitted1,'g-',x,pdf_fitted2,'b-', x,pdf_fitted3,'r-')
pl.show()

pl.hist(means(vb1, 41), 60, color='#A8E29C', alpha=.5)
pl.hist(means(vb2, 41), 60, color='#9CA8E2', alpha=.5)
pl.hist(means(vb3, 41), 60, color='#E29CA8', alpha=.5)
pl.savefig("hist-mean.png",dpi=100)
pl.show()


print "MEANS"
print numpy.mean(means(vb1, 0))
print numpy.mean([1,2,3])
print numpy.mean(means(vb1, 4))
#print means(vb1, 41)

"""
# plot activtion of single all single voxels in this region
for voxel in vb[41]:
    pl.plot(voxel[1])
#pl.savefig("voxelsovertime.png",dpi=100)
pl.show()

for voxel in vb[5]:
    pl.plot(voxel[1])
#pl.savefig("voxelsovertime.png",dpi=100)
pl.show()
"""


    