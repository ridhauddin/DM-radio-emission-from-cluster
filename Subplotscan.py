###### This code for constrain line subplot ##########

import numpy as np
import matplotlib.pyplot as plt
import qproperties

fig, ax = plt.subplots(2, 2, sharey='row',sharex='col')


labels=np.array(['NFW','Einasto','DK14','Hernquist'])

channel=np.array(["bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz","tot"])

sign=np.array(["bb","cc","dd","e^+e^-","\mu^+\mu^-","ss",r"\tau^+\tau^-","tt","uu","w^+w^-","zz","Total"])

k=0

xticks=np.arange(0, 1050, 500)

		
for i in range(0, 2):
	for j in range(0,2):
	

		####NFW#####
		output ="SigTot_%s%s.out"%(qproperties.cluster,channel[0])
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,1]
		ax[i,j].plot(valx,valy, label=labels[0], linestyle='solid')
		######EIN######
		output ="SigTot_%s%s.out"%(qproperties.cluster,channel[4])
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,2]
		ax[i,j].plot(valx,valy, label=labels[1], linestyle='dashed')
		######ISO#######
		output ="SigTot_%s%s.out"%(qproperties.cluster,channel[6])
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,3]
		ax[i,j].plot(valx,valy, label=labels[2], linestyle='dotted')
		########BUR#########
		output ="SigTot_%s%s.out"%(qproperties.cluster,channel[9])
		valx  =np.loadtxt(output)[:,0]
		valy =np.loadtxt(output)[:,4]
		ax[i,j].plot(valx,valy, label=labels[3], linestyle='dashdot')


		########MSSM########################
		output ="masslist100.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist200.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist300.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist400.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist500.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist600.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist700.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist800.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist900.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		output ="masslist1000.out"
		valx  =np.loadtxt(output)[:,11]
		valy =np.loadtxt(output)[:,8]
		ax[i,j].scatter(valx,valy,c='b',marker='o')

		ax[0,0].set_title(r'$%s$'%sign[0],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor='b',alpha =0.5))
		ax[0,1].set_title(r'$%s$'%sign[4],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor='b',alpha =0.5))
		ax[1,0].set_title(r'$%s$'%sign[6],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor='b',alpha =0.5))
		ax[1,1].set_title(r'$%s$'%sign[9],fontdict={'fontsize':10},y=1.0, pad=-20,loc='right',bbox = dict(facecolor='b',alpha =0.5))
		
		ax[i,j].set_xticks(xticks)
		
		fig.legend(labels=labels, loc='upper center', ncol=6)
		
		
		k=k+1
	
for ax in ax.flat:
    ax.set(yscale='log')
    ax.set(xlim=(90, 1010))

fig.text(0.04, 0.5, r'$\langle\sigma v\rangle}$ ($cm^{3}$ $s^{-1}$)', va='center', rotation='vertical')
fig.text(0.5, 0.04, r'$m_\chi$ (GeV)', ha='center')
plt.subplots_adjust(wspace=0, hspace=0)   
    
plt.show()


                      
