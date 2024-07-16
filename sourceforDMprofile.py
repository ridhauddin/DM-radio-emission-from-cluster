
###### This one for plot ##########

import matplotlib.pyplot as plt
import numpy as np
import warnings
import qproperties
import qfunctions
import qconstants

warnings.simplefilter('always',Warning)

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp   = PdfPages('yieldenergy.pdf')
tmp1 = plt.figure(1)

kkfile ="out1000_%s.source"%qproperties.cluster
mass =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,1]
plt.plot(mass,y, '-',label='NFW')

kkfile ="out1000_%s.source"%qproperties.cluster
mass =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,2]
plt.plot(mass,y, ':', label='Einasto')

kkfile ="out1000_%s.source"%qproperties.cluster
mass =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,3]
plt.plot(mass,y,'--', label='DK14')

kkfile ="out1000_%s.source"%qproperties.cluster
mass =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,4]
plt.plot(mass,y, '-.', label='Herquist')


plt.title(r'$M_\chi=1000$ GeV')
plt.xlabel(r'E (GeV)')
plt.ylabel(r'$Q_e(r,E)$ $(GeV^{-1} annihilation^{-1})$')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlim(5E-6,9E2)
pp.savefig(tmp1,bbox_inches='tight',)
plt.show()
plt.clf()
pp.close()



