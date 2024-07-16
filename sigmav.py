import numpy as np 
import matplotlib.pyplot as plt 
import qproperties
import qfunctions
import math
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
 
 
#pp   = PdfPages("AConstraintlines.pdf")
tmp5 = plt.figure(5)
channel=np.array(["tot","bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz"])
 
for k in range(0,12): 
#input data	
	kkfile  ="%s/%sNFW%s.out"%(qproperties.cluster,qproperties.cluster,channel[k])
	kkfile1 ="%s/%sEIN%s.out"%(qproperties.cluster,qproperties.cluster,channel[k])
	kkfile2 ="%s/%sDK14%s.out"%(qproperties.cluster,qproperties.cluster,channel[k])
	kkfile3 ="%s/%sHERN%s.out"%(qproperties.cluster,qproperties.cluster,channel[k])

	if k == 8:
		x = np.loadtxt(kkfile)[1:,1]
		y = np.divide(np.loadtxt(kkfile)[1:,6],np.loadtxt(kkfile)[1:,0])
		x1 = np.loadtxt(kkfile1)[1:,1]
		y1 = np.divide(np.loadtxt(kkfile1)[1:,6],np.loadtxt(kkfile1)[1:,0])
		x2 = np.loadtxt(kkfile2)[1:,1]
		y2 = np.divide(np.loadtxt(kkfile2)[1:,6],np.loadtxt(kkfile2)[1:,0])
		x3 = np.loadtxt(kkfile3)[1:,1]
		y3 = np.divide(np.loadtxt(kkfile3)[1:,6],np.loadtxt(kkfile3)[1:,0])

	else:
		x = np.loadtxt(kkfile)[:,1]
		y = np.divide(np.loadtxt(kkfile)[:,6],np.loadtxt(kkfile)[:,0])
		x1 = np.loadtxt(kkfile1)[:,1]
		y1 = np.divide(np.loadtxt(kkfile1)[:,6],np.loadtxt(kkfile1)[:,0])
		x2 = np.loadtxt(kkfile2)[:,1]
		y2 = np.divide(np.loadtxt(kkfile2)[:,6],np.loadtxt(kkfile2)[:,0])
		x3 = np.loadtxt(kkfile3)[:,1]
		y3 = np.divide(np.loadtxt(kkfile3)[:,6],np.loadtxt(kkfile3)[:,0])


	y_ob = qproperties.S_nu
 
#define coefficient
	
	if k == 8:
		b_2=np.random.normal(scale=1.0, size=9)
		
		
	else:
		b_2=np.random.normal(scale=1.0, size=10)

	p  = np.polyfit(np.log10(x+b_2), np.log10(y), 1)
	p1 = np.polyfit(np.log10(x1+b_2), np.log10(y1), 1)
	p2 = np.polyfit(np.log10(x2+b_2), np.log10(y2), 1)
	p3 = np.polyfit(np.log10(x3+b_2), np.log10(y3), 1)


	print (p[0],p[1],p1[0],p1[1],p2[0],p2[1],p3[0],p3[1])

#list of eq.
	A=np.log10(y_ob)	
	B=np.log10(x+b_2)
	C=A-p[0]*B-p[1]
	A1=np.log10(y_ob)
	B1=np.log10(x1+b_2)
	C1=A1-p1[0]*B1-p1[1]
	A2=np.log10(y_ob)
	B2=np.log10(x2+b_2)
	C2=A2-p2[0]*B2-p2[1]
	A3=np.log10(y_ob)
	B3=np.log10(x3+b_2)
	C3=A3-p3[0]*B3-p3[1]
    	
#sigmav-m_kk constraint sigmav=10*(log(observed radio emission)-slope of line*log(x+np.random)-(Y-intercept)
	y_upper =(10**(C))
	y_upper1=(10**(C1))
	y_upper2=(10**(C2))
	y_upper3=(10**(C3))


#plotting the actual points as scatter plot
	plt.plot(x,y_upper, label= 'NFW', linestyle='solid')
	plt.plot(x1,y_upper1, label= 'Einasto',linestyle='dotted')
	plt.plot(x2,y_upper2, label= 'DK14',linestyle=(0, (5, 10)))
	plt.plot(x3,y_upper3,label= 'Hernquist',linestyle=(0, (3, 10, 1, 10)))


# putting labels 
	plt.xlabel(r'$M_\chi$ (GeV)') 
	plt.ylabel(r'$\langle\sigma_v\rangle_{total}$ (cm$^{3}$ s$^{-1}$)')
	
# turn to log
	plt.yscale('log')
#plt.xscale('log')

#save
	line1= 'mass   upper(sigmavNFW    sigmavEIN   sigmavDK14      sigmavHERN)'
	np.savetxt('SigTot_%s%s.out'%(qproperties.cluster,channel[k]),np.c_[x,y_upper,y_upper1,y_upper2,y_upper3],'%25.15e',header=line1)

# Putting title
#plt.title(r'$\sigma_v-M_{LKP}$ constraint for %s'%qproperties.cluster)
	
# function to show plot 
#plt.legend() 
#plt.show()

#save into pdf
#pp.savefig(tmp5,bbox_inches='tight',)
#plt.savefig('totalconstraint.png',format='png')
#pp.close()
	
	
