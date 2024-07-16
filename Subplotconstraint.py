###### This code for constrain line subplot ##########

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, sharey='row',sharex='col')


labels=np.array(['A119','A478','A2029','A2142','A2199','A2744'])

channel=np.array(["bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz","tot"])

sign=np.array(["bb","cc","dd","e^+e^-","\mu^+\mu^-","ss",r"\tau^+\tau^-","tt","uu","w^+w^-","zz","Total"])

k=0

xticks=np.arange(0, 1050, 500)

		
for i in range(0, 2):
	for j in range(0,2):
	

		####A119#####
		output ="SigTot_A119%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[0], linestyle='solid')

		######A478######
		output ="SigTot_A478%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[1],linestyle='dotted')

		######A2029#######
		output ="SigTot_A2029%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[2], linestyle=(0, (5, 10)))

		########A2142#########
		output ="SigTot_A2142%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[3], linestyle=(0, (3, 10, 1, 10)))

		########A2199#########
		output ="SigTot_A2199%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[4], linestyle=(0, (3, 1, 1, 1, 1, 1)))

		########A2744#########
		output ="SigTot_A2744%s.out"%channel[k]
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label= labels[5], linestyle=(0, (5, 1)))

		ax[i,j].set_title(r'$%s$'%sign[k],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor = 'blue',alpha =0))
		
		ax[i,j].set_xticks(xticks)
		
		fig.legend(labels=labels, loc="lower center", ncol=6)
		
		
		k=k+1
	
for ax in ax.flat:
    ax.set(yscale='log')
    ax.set(xlim=(100, 1000))

fig.text(0.04, 0.5, r'$\langle\sigma v\rangle}$ ($cm^{3}$ $s^{-1}$)', va='center', rotation='vertical')
fig.text(0.5, 0.04, r'$m_\chi$ (GeV)', ha='center')
plt.subplots_adjust(wspace=0, hspace=0)   
    
plt.show()


                      
