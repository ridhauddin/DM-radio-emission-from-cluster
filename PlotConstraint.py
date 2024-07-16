
###### This one for plot ##########

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
#import seaborn as sns
import numpy as np
import qproperties
import qfunctions
import math

pp   = PdfPages('Asigmaline.pdf')
tmp5 = plt.figure('total')
channel="zz"
sign=r"\chi\chi->zz"

####A119#####
output ="SigTot_A119%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= 'A119', linestyle='solid')

######A478######
output ="SigTot_A478%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= r'A478',linestyle='dotted')

######A2029#######
output ="SigTot_A2029%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= 'A2029', linestyle=(0, (5, 10)))

########A2142#########
output ="SigTot_A2142%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= 'A2142', linestyle=(0, (3, 10, 1, 10)))

########A2199#########
output ="SigTot_A2199%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= 'A2199', linestyle=(0, (3, 1, 1, 1, 1, 1)))

########A2744#########
output ="SigTot_A2744%s.out"%channel
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label= 'A2744', linestyle=(0, (5, 1)))



#plt.title(r'Constraint on cross-section with LKP annihilation')
plt.xlabel(r'$m_\chi$ (GeV)')
plt.ylabel(r'$\langle\sigma v\rangle_{%s}$ ($cm^{3}$ $s^{-1}$)'%sign)
plt.yscale('log')
#plt.xscale('log')
plt.xlim(100, 1000)
#plt.legend()
pp.savefig(tmp5,bbox_inches='tight',)
plt.show()
plt.clf()
pp.close()



