import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import glob

##### this part of code is specific to EC_Earth3 data###############################################
test = sorted(glob.glob('/Users/isamarcortes/Dropbox/Isamar/Satellite_Imagery_Analysis/EvapFuture1/*.nc'))##change to where your files are
test1 = []

for i in test:
    test1.append(i)
    same = nc.Dataset(i)
    #print(same)
    #plt.imshow(same['evs'][1,::-1,:]) ####this part is meant to plot the map grid
    #plt.show()
    for j in range(12):
    ##### printing values for each region below (change evs to appropriate variable you are looking at in files)
        tes2 = same['evs'][(j),193.3751,  105.5265] #Venezuela
        #tes2 = same['pr'][(j),199.4042 , 105.3801] #PuertoRico
        #tes2 = same['pr'][(j),203.0375,  93.2228] #Mexico
        #tes2 = same['pr'][(j),206.3144,  96.9133] #Florida
        #tes2 = same['pr'][(j),203.8592,  96.2606] #Cuba 2
        #tes2 = same['pr'][(j),204.077, 95.858] #Cuba 3
        #tes2 = same['pr'][(j),199.0874 , 92.747] #Belize
        #tes2 = same['pr'][(j),208.2746, 98.2004] #Bahamas
        #print(tes2)
