# StormSnapshots
Creating snapshots from hurricane using GPM IMERG data

## Summary

This code is used to create snapshots of a hurricane using the data from the GPM_3IMERGHH
product for precipitation.

There is a PowerShell script used to download the information from the
GES DISC web site, by using a text file with a list of links. The files are in HDF5
format.

The Python script opens each HDF5 file in the directory, reads the dataset and creates
a PNG image. Then an animated GIF is created. The libraries used are GDAL, matplotlib,
cartopy, and imageio.

The selected storm was hurricane Ida, the downloaded data correspond to August 28 and 29,
2021 which presented rapid intensification.

![Snapshot of hurricane Ida (Aug, 2021)](precipitation.gif "Rapid intensification in hurricane Ida")

NOTE: There are still some obvious issues, such as different scales in each picture.
