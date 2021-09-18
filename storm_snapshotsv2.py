# -*- coding: utf-8 -*-
"""
ATMO555 Assignment 02. Snapshots of tropical storm, 09/01/2021

@author: eduardo
"""

from os import listdir
from os.path import isfile, join
from osgeo import gdal
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import imageio

THRESHOLD = 0 # Remove data below this value
EXTENSIONS = ['HDF5']

def snapshot(fn):
    """ Create an snapshot"""
    
    # Open the file
    ds = gdal.Open(fn, gdal.GA_ReadOnly)
    
    datasets = ds.GetSubDatasets()
    band = gdal.Open(datasets[7][0])
    
    # Extract the temperature matrix data
    data = band.ReadAsArray(0, 0, band.RasterXSize, band.RasterYSize)
    # data = band.ReadAsArray()
    data[data < THRESHOLD] = THRESHOLD  # Remove data below threshold
    
    # Rotate the data
    data1 = data.transpose()
    
    # Create a figure and plot a coastline 
    plt.figure(figsize=(12,12))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    
    # Plot the temperature matrix data and save the figure
    plt.imshow(data1, extent=[-180,180,-90,90], cmap='RdYlBu_r', origin='lower')
    plt.title(fn)
    plt.colorbar(orientation='horizontal', pad=0.03)
    # plt.savefig('snapshot_' + fn[:-4] + '.png', dpi=300, bbox_inches='tight')
    
    # Zoom to the hurricane
    plt.xlim(-100, -70)
    plt.ylim(20, 35)
    ax.set_xticks([-100,-80,-90,-70])
    ax.set_yticks([20,30,35])
    plt.savefig(fn[:-4] + 'png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':

    # Directory where the images are located
    directory = 'D:/Downloads/DATA/'
    
    # Extract the list of files and filter by extension
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    files = [f for f in onlyfiles if f[-4:].upper() in EXTENSIONS]

    # Create the snapshots of each image
    i = 0
    for fn in files:
        i += 1
        print('Processing file {0} of {1} [{2}]'.format(i, len(files), fn))
        snapshot(fn)
    
    # Create an animated GIF
    imgfiles = [f[:-4] + 'png' for f in files]
    # print(imgfiles)
    with imageio.get_writer('precipitation.gif', mode='I') as writer:
        for filename in imgfiles:
            image = imageio.imread(filename)
            writer.append_data(image)