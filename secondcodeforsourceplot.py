'''
=====================================================================================
 Generate e- source spectrum (Q_source) from PYTHIA dN/dE, which is equivalent to 
 dshayield spectrum from Darksusy.

 KK or SUSY DM, up to you (it should be KK DM here..?). As long as it is from PYTHIA.

 Combination of different KK anni channels (see hooper and profumo 2007 - UED KK.pdf)

 The source spectrum is for the special case:
 sigmav=1.0	#sigmav (cm^3 s^-1)
 BR    =1.0	#BR which shouldn't be modified anymore for KK case, since I have considered BR in Pythia dN/dE
 Nx    =1.0	#DM number density (cm^-3).
=====================================================================================
'''
print(__doc__)
import numpy as np
import warnings
import qproperties
import qfunctions
import qconstants 

warnings.simplefilter('always',Warning)


############################### start: define here ###################################
y		=int(input('what is your file no. (1-10)?: '))
a		=y-1
kkfile		="run_01_0%s/positrons_spectrum_PPPC4DMID_ew.dat"%y
if y==10: kkfile="run_01_10/positrons_spectrum_PPPC4DMID_ew.dat"
m_neutralino	= y*100
outfile	="out%s_%s.source"%(m_neutralino,qproperties.cluster)
#X-section of neutralino
sigmavtot=np.loadtxt('masslist.out')[a,1]  #unit: cm^3 s^-1
############################### end: define here ###################################

print "Read dN/dE from file '%s'."%kkfile

x =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,1]		#unit: # annihilation^-1 Gev^-1
dNdE=y/((10**x)*m_neutralino)*np.log(10)
Gev=(10**x)*m_neutralino

#rhos,rs,r values of targeted clusters
rhosnfw	=qproperties.rhosnfw
rhosein	=qproperties.rhosein
n		=qproperties.alphaein
rhosdk14	=qproperties.rhosdk14
rt		=qproperties.rt
rhoo		=qproperties.rhoo
rhoshern	=qproperties.rhoshern
rs1		=qproperties.rs1
rs2		=qproperties.rs2
r       	=qproperties.r

#brancing ratio
BR    =1.0	                #since its 100% so its equal to 1.0.

#DM profile model but here we already got the neutralino number per density
Nxnfw	=qfunctions.nfw_numdens_neu(r,m_neutralino,rhosnfw,rs1)		#NFW
Nxein	=qfunctions.ein_numdens_neu(r,m_neutralino,rhosein,rs2,n)		#Einasto
Nxdk14	=qfunctions.dk14_numdens_neu(r,m_neutralino,rhosdk14,rs2,rt,rhoo,n)	#Dk14
Nxhern	=qfunctions.hern_numdens_neu(r,m_neutralino,rhoshern,rs1)		#hernquist

#yield source eq. using diff DM profile model
sourceNFW=np.array(sigmavtot*dNdE*BR*(Nxnfw**2/2.0))	#unit: # s^-1 GeV^-1 cm^-3
sourceEIN=np.array(sigmavtot*dNdE*BR*(Nxein**2/2.0))	#unit: # s^-1 GeV^-1 cm^-3
sourceDK14=np.array(sigmavtot*dNdE*BR*(Nxdk14**2/2.0))	#unit: # s^-1 GeV^-1 cm^-3
sourceHERN=np.array(sigmavtot*dNdE*BR*(Nxhern**2/2.0))	#unit: # s^-1 GeV^-1 cm^-3


#dummytable =np.array([[m_neutralino,sigmavtot,m_neutralino,sigmavtot,m_neutralino,sigmavtot]])
line1='  E                         sourceNFW        sourceEIN     sourceISO    sourceBUR    sourceMOO\n  GeV                         # s^-1 GeV^-1 cm^-3\n #.....mchi..... ...sigmavtot...'

latesttable=np.array([Gev,sourceNFW,sourceEIN,sourceDK14,sourceHERN]).transpose()
#latesttable=np.concatenate((dummytable,latesttable),axis=0)
np.savetxt(outfile,latesttable,'%25.15e', header=line1)

print "\nSource spectrum written to file '%s'."%outfile
#print(rhosnfw,rs,r)

