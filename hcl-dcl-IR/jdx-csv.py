import numpy as np
from jcamp import jcamp_readfile

jcamp_dict = jcamp_readfile("./HCl_DCl_0.125res.jdx")

XY = np.asarray([jcamp_dict['x'], jcamp_dict['y']])
np.savetxt('hcl-dcl-0.25res.csv', XY.T, header='wavenumber, absorbance', delimiter=',')
