#this is code for log-log model

import qproperties
import qfunctions
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd


DMPro = np.array(['NFW','EIN','DK14','HERN'])
labels=np.array(['NFW','Einasto','DK14','Hernquist'])
channel=np.array(["bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz","tot"])
sign=np.array(["bb","cc","dd","e^+e^-","\mu^+\mu^-","ss",r"\tau^+\tau^-","tt","uu","w^+w^-","zz","Total"])



#import file

for j in range(0,12):
	kkfile  ="%s/%s%s%s.out"%(qproperties.cluster,qproperties.cluster,DMPro[3],channel[j])
	
#input data
	if j==7:
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
	sns.regplot(x=x,y=y_fit, label = r'$%s$'%sign[j],marker = "o", ci=95,logx=True)

#plot real data
#plt.scatter(x1, y1, color = "red", marker = ".", s = 30)
#plt.scatter(x2, y2, color = "black", marker = "|", s = 30)
#plt.scatter(x3, y3, color = "blue", marker = "_", s = 30)
#plt.scatter(x4, y4, color = "cyan", marker = "^", s = 30)


#graph title
#plt.title(r'Synchrotron flux/Cross-section vs Mass for %s fitting model'%qproperties.cluster)
	

#graph label
plt.xlabel(r'$M_\chi$ (GeV)')
plt.ylabel(r'$S_{v}/\langle\sigma_v\rangle$ (MJy/$cm^{3}$ $s^{-1}$)')

#graph scale
plt.xscale('log')
#plt.yscale('log')
    	
		
#plt.legend()
plt.show()







