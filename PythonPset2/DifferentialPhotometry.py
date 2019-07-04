##Write a Python function to compute the magnitude of the asteroid in an image using a
##star of known magnitude. This function should take as parameters the filename of a
##FITS image, the x- and y-coordinates of a relatively isolated star, the width of the
##star in pixels, the magnitude of that star, the x- and y-coordinates of the asteroid,
##the width of the asteroid in pixels, and the x- and y-coordinates of a nearby blank
##portion of the image (ten parameters in all). This function should:
##a. Extract a box (2D array) of the width of the star centered on the star’s x-ycoordinates
##from the image. Sum the pixel counts of all pixels inside the box. This
##count is ‘star+sky.’
##b. Extract a 3-by-3 box of blank sky centered at the given x-y-coordinates for blank
##sky. Determine the average pixel count of all pixels inside that box. This is ‘avgSky.’
##c. We’ll refer to the pixel counts for just the star as the ‘Signal,’ which is given by
##Signal = ‘star+sky’ – (avgSky*Nap)
##where Nap is the number of pixels in the ‘star+sky’ aperture.
##The general formula for determining a magnitude is:
##mag = -2.5*log10(Signal) + const
##(It’s really the flux of the star that is inserted into the magnitude formula, but here
##we assume that pixel count is directly proportional to flux and the constant of
##proportionality is absorbed into the constant term.) Since we know the magnitude
##of the star, we can determine the constant value.
##d. Repeat the process for your asteroid in the image. Now that you know the constant,
##you can calculate its magnitude.


import numpy as np
import math
from astropy.io import fits

def photo(img, starX, starY,starW,starM,asterX, asterY,asterW, skyX, skyY):
    asterR = int(asterW/2)
    starR = int(starW/2)
    #a
    star = fits.getdata(img)
    starskyarr = star[starY-starR:starY+starR+1,starX-starR:starX+starR+1 ]
    starskysum = np.sum(starskyarr)
    #b
    avgSky = np.sum(star[skyX-1: skyX + 2, skyY-1: skyY+2])/9
    #c
    signal1 = starskysum - (avgSky*len(starskyarr)**2)
    const = starM + 2.5 * math.log10(signal1)
    #d
    asterskyarr = star[asterY-asterR:asterY+asterR+1, asterX-asterR:asterX+asterR+1]
    asterskysum = np.sum(asterskyarr)
    signal2 = asterskysum - (avgSky*len(asterskyarr)**2)
    mag = -2.5*math.log10(signal2) + const
    return mag
print(photo("sampleimage.fits",173,342,5,15.26,351,154,3,200,200))
print(photo("sampleimage.fits",355,285,5,16.11,351,154,3,200,200))






    
    
