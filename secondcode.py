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

warnings.simplefilter('always',Warning)


############################### start: define here ###################################
b		=int(input('what is your file no. (1-10)?: '))
kkfile		="run_01_0%s/positrons_spectrum_PPPC4DMID_ew.dat"%b
if b==10: kkfile="run_01_10/positrons_spectrum_PPPC4DMID_ew.dat"
mass		= b*100		#GeV
outfile	="out%s.source"%mass

############################### end: define here ###################################

print "Read dN/dE from file '%s'."%kkfile

x  =np.loadtxt(kkfile)[:,0]
y =np.loadtxt(kkfile)[:,1]		#unit: # annihilation^-1 Gev^-1
dNdE=y/((10**x)*m_kk)*np.log(10)
GeV=(10**x)*mass

#Q_source = sigmav * dN/dE * BR * (Nx**2) / 2.0'
#Please give your sigmav and Nx:'
sigmav=1.0	#unit: cm^3 s^-1
BR    =1.0	                #shouldn't be changed anymore, since I've considered BR in dN/dE calculation from Pythia."
Nx    =1.0	        #Neutralino number density (cm^-3)

Qsource=sigmav*dNdE*BR*(Nx**2/2.0)	#unit: # s^-1 GeV^-1 cm^-3

dummytable =np.array([[mass,sigmav,sigmav]])
line1='  E                           Q_source\n  GeV                         # s^-1 GeV^-1 cm^-3\n #.....mchi..... ...sigmav...'

latesttable=np.array([GeV,dNdE,Qsource]).transpose()
latesttable=np.concatenate((dummytable,latesttable),axis=0)
np.savetxt(outfile,latesttable,'%25.15e', header=line1)

print "\nSource spectrum written to file '%s'."%outfile

