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
