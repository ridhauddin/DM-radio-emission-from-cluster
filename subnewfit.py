#this is code for log-log model

import qproperties
import qfunctions
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

fig, ax = plt.subplots(2, 2, sharey='row',sharex='col')

#pp   = PdfPages('Afitting.pdf')
#tmp5 = plt.figure(5)
DMPro = np.array(['NFW','EIN','DK14','HERN'])
labels=np.array(['NFW','Einasto','DK14','Hernquist'])
channel=np.array(["bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz","tot"])
k=0
l=0

for i in range(0,2):
	for j in range(0,2):
#import file
		for chn in channel:
			for k in range(4):
				kkfile  ="%s/%s%s%s.out"%(qproperties.cluster,qproperties.cluster,DMPro[k],chn)
		
	#input data
				if  chn == "tt":
					x = np.loadtxt(kkfile)[1:,1]
					y = np.divide(np.loadtxt(kkfile)[1:,6],np.loadtxt(kkfile)[1:,0])
					b_2=np.random.normal(scale=1.0, size=9)

				else:
					x = np.loadtxt(kkfile)[:,1]
					y = np.divide(np.loadtxt(kkfile)[:,6],np.loadtxt(kkfile)[:,0])
					b_2=np.random.normal(scale=1.0, size=10)


				p = np.polyfit(np.log10(x+b_2), np.log10(y), 1)


		#fitting eq. (log-log model)
				y_fit=10**(p[0]*np.log10(x+b_2)+p[1])



		#plot fitting line
		#plt.plot(x, y_fit, color = "orange", label = 'NFW', linestyle = 'solid')
		#plt.plot(x1, y_fit1, color = "red", label = 'NFWasto', linestyle = 'dashed')
		#plt.plot(x2, y_fit2, color = "black", label = 'NFW', linestyle ='dashdot' )
		#plt.plot(x3, y_fit3, color = "blue", label = 'NFWquist', linestyle = (0, (5, 10)))


		#plot 95%
				ax[i,j].plot(x, y_fit)


		#plot real data
				ax[i,j].scatter(x, y)

	#plt.scatter(x1, y1, color = "red", marker = ".", s = 30)
	#plt.scatter(x2, y2, color = "black", marker = "|", s = 30)
	#plt.scatter(x3, y3, color = "blue", marker = "_", s = 30)
	#plt.scatter(x4, y4, color = "cyan", marker = "^", s = 30)


		#graph title
		#plt.title(r'Synchrotron flux/Cross-section vs Mass for %s fitting model'%qproperties.cluster)
				ax[i,j].set_title(r'$%s$'%labels[k],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor='b',alpha =0.5))
				fig.legend(labels=channel, loc="lower center", ncol=6)
		k+=1
			#	l+=1

#graph label
fig.text(0.04, 0.5, r'$\langle\sigma v\rangle}$ ($cm^{3}$ $s^{-1}$)', va='center', rotation='vertical')
fig.text(0.5, 0.04, r'$m_\chi$ (GeV)', ha='center')
plt.subplots_adjust(wspace=0, hspace=0)  

#graph scale
for ax in ax.flat:
    ax.set(yscale='log')
    ax.set(xlim=(90, 1010))
		
#plt.legend()
plt.savefig('try.png')
plt.show()







