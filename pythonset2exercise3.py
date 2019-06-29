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






    
    
