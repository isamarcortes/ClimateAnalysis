import h5py as h5
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
from pyproj import proj

data_file = sorted(glob.glob('/Users/isamarcortes/Dropbox/Isamar/Satellite_Imagery_Analysis/2015_2020Precip_EvapData/*.HDF5')) ## imports h5 files
list = [] #empty list to put h5 files in

for i in data_file:
    list.append(i)
    read = h5.File(i,'r')
    new = read['Grid']
    surfacePrecipitation = new['surfacePrecipitation'][...,]
    #rainwater = new['rainWater'][...,]
    #npixtotal = new['npixTotal']
    
    surfacePrecipitation1 = np.where(surfacePrecipitation>0, surfacePrecipitation, np.nan)
    test = np.transpose(surfacePrecipitation1)
    #print(read.keys())
    ###Indexing based on converted coordinates per region
    Venezuela = test[406,445]
    PR1 = test[430, 446]
    PR3 = test[430, 448]
    PR6 = test[430, 446]
    MX = test[445, 526]
    BarnesK = test[458, 502]
    ButtonwoodK=test[460, 502]
    CrabK = test[458, 502]
    CraneK= test[460, 501]
    FL1= test[460, 502]
    FL3 = test[460, 501]
    FL5 = test[460, 502]
    ShellK = test[458, 502]
    SidK = test[460, 502]
    UpperArsK = test[458, 502]
    Cuba2 = test[448, 506]
    Cuba3 = test[449,509]
    Belize1 = test[429, 529]
    Bahamas1= test[466, 493]
    index = np.linspace(-90,90,720)
    columns = np.linspace(-180,180,1440)

    test1 = pd.DataFrame(data = test,index=index, columns=columns)
    #test1.to_csv('/Users/isamarcortes/Desktop/HDF_Files/test.csv')
    
    #print(test1.head())
    #print(test1)
    #print(Bahamas1)



'''

#z_array=np.empty((1440,720))
#z_array[index, columns] = test
print(type(test))

plt.contourf(test)
plt.colorbar()
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Original')
plt.show()

plt.contourf(columns,index,test)
plt.colorbar()
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Lat Lon')
plt.show()

'''
