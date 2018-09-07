import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS

def getAxisObject(filename):
	"""
	return Axis Object
	Author: Jürgen Hinterreiter
	Date: 20180907
	"""
	hdulist = fits.open(filename)
	wcs = WCS(hdulist[0].header)
	
	ax = plt.subplot(projection=wcs)
	ax.imshow(hdulist[0].data)
	ax.set_xlabel("Right Ascension [degrees]")
	ax.set_ylabel("Declination [degrees]")
	ax.coords.grid(grid_type='contours', alpha = 0.3, linestyle='dashed')

	return ax