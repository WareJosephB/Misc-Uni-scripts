''' This code wrote an HTML page for each observation I was studying, which then were linked to from a master/home page.'''


from os import listdir
from astropy.io import fits

A = "<html><head>"
B = "</head><body>"
H = '</body></html>'

for K in listdir('/export/data/josephw/Data/'):
    with fits.open('/export/data/josephw/Data/'+K+'LC.fits') as HDA:
        P = 'Observation performed on: '+HDA[0].header['DATE']
        R = 'Source Object = '+HDA[0].header['OBJECT']
    C = "<title>"+K+"</title>"
    D = '<a href="/export/data/josephw/dir/Home.html">Back</a></br>'
    E = '<img src="/export/data/josephw/Picture/'+K+'.png" height=199 width=64></br>'
    J = '<img src="/export/data/josephw/dir/pic.png" height=3 width=64></br>'
    F = '<img src="/export/data/josephw/Picture/'+K+'_SZ_LC.png" height=600 width=800></br>'
    G = '<img src="/export/data/josephw/Picture/'+K+'_LS.png" height=600 width=800>'
    i = [A, B, C, D, R, P, E, J, F, G, H]
    L = open("/export/data/josephw/dir/"+K+".html", 'w+')
    for Q in i:
        L.write(Q+'\n')
    L.close()

    
    # For observation K of object R on date P make a page showing:
    # E = 'trace' of image in timing mode
    # J = 'source area' of image (a ~40 pixel wide strip shown by a coloured bar under the image, each used the same region)'
    # F = Light curve of observation
    # G = Lomb-Scargle periodogram of the data
    
    # This is an early enough version that the Fast-Fourier Transform was not included, but I also had that on the final version
