
###### This one for plot ##########

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
import numpy as np
import qproperties
import qfunctions
import math

#pp   = PdfPages('A-95%sigmaline.pdf')
tmp5 = plt.figure(5)
channel = "bb"
sign=r"\chi\chi->bb"

####NFW#####
output ="SigTot_%s%s.out"%(qproperties.cluster,channel)
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,1]
plt.plot(valx,valy, label='NFW', linestyle='solid')
######EIN######
output ="SigTot_%s%s.out"%(qproperties.cluster,channel)
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,2]
plt.plot(valx,valy, label='Einasto', linestyle='dashed')
######ISO#######
output ="SigTot_%s%s.out"%(qproperties.cluster,channel)
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,3]
plt.plot(valx,valy, label='DK14', linestyle='dotted')
########BUR#########
output ="SigTot_%s%s.out"%(qproperties.cluster,channel)
valx  =np.loadtxt(output)[:,0]
valy =np.loadtxt(output)[:,4]
plt.plot(valx,valy, label='Hernquist', linestyle='dashdot')


########MSSM########################
output ="masslist100.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist200.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist300.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist400.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist500.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist600.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist700.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist800.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist900.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')

output ="masslist1000.out"
valx  =np.loadtxt(output)[:,11]
valy =np.loadtxt(output)[:,8]
plt.scatter(valx,valy,c='b',marker='o')


#plt.title(r'Constraint on cross-section with LKP annihilation')
plt.xlabel(r'$M_\chi$ (GeV)')
plt.ylabel(r'$\langle\sigma v\rangle_{%s}$ (cm$^{3}$ s$^{-1}$)'%sign)
plt.yscale('log')
#plt.xscale('log')
plt.xlim(90,1010)
plt.legend()
#pp.savefig(tmp5,bbox_inches='tight',)
plt.show()
#plt.savefig('total95%.png',format='png')
plt.clf()
#pp.close()



