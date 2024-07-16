
###### This one for plot ##########

import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.simplefilter('always',Warning)

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp   = PdfPages('massvsSigmaV.pdf')
tmp1 = plt.figure(1)
kkfile ="masslist.out"
mass =np.loadtxt(kkfile)[:,2]
sigmavtot =np.loadtxt(kkfile)[:,1]
#sigmavBB =np.loadtxt(kkfile)[:,3]
#sigmavUU =np.loadtxt(kkfile)[:,4]
plt.plot(mass,sigmavtot, label='$\sigma v_{total}$')
#plt.plot(R,sigmavBB, label='$\sigma v_{\chi\chi->bb}$')
#plt.plot(R,sigmavUU, label='$\sigma v_{\chi\chi->\mu^+\mu^-}$')
plt.title(r'Mass (100 GeV) vs Cross section annihilation at Galaxy Cluster environment')
plt.ylabel(r'Mass ($R^{-1}$) (GeV)')
plt.xlabel(r'$\sigma v$ $(s^{-1} GeV^{-1} cm^{-3})$')
plt.legend()
#plt.xscale('log')
plt.yscale('log')
pp.savefig(tmp1,bbox_inches='tight',)
plt.show()
plt.clf()
pp.close()



