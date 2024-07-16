import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy as sp
from scipy import integrate
import pandas as pd
import astropy
from astropy.io import ascii
import os.path
import warnings
import glob
import math

warnings.simplefilter('always',Warning)

import qproperties
import qfunctions
from qconstants import *

#reload(qproperties)
#reload(qfunctions)
channel=np.array(["tot","bb","cc","dd","ee","mumu","ss","tautau","tt","uu","ww","zz"])
for y in range (1,11):
	mass =y*100
	filearray	='out%s.source'%(mass)
	for k in range (1,13):
		givesigmav	=np.loadtxt('masslist.out')[y-1,k]
		outfilename	='%sDK14%s.out'%(qproperties.cluster,channel[k-1])
############################### start: info table ###########################################################
		cluster	=qproperties.cluster
		print ('cluster = '),cluster

		d1=pd.DataFrame.from_dict({
		'A2142'  : ['A2142' ,'RH',1.37  ,  23.0, 2000.0],
		'A2744'  : ['A2744' ,'RH',0.325  , 218.0,1100.0],
		'A2199'  : ['A2199' ,'ULRH',0.50  , 250.0,1000.0],
		'A119'   : ['A119'  ,'ULRH',1.4 ,243.0 ,1100.0],
		'A478'   : ['A478'  ,'MH', 1.4, 16.6, 180],
		'A2029'  : ['A2029' ,'MH', 1.4, 18.8, 125]},
		orient='index',columns=['Label','type','Freq/GHz','S_nu/mJy','r/kpc'])

############################### end: info table ###########################################################
############################### start: nfw parameters ###################################
#characteristic central density in unit of kg m^-3 (has been multiplied by rho_crit)
		rhos	=qproperties.rhosdk14
#characteristic scale radius in unit of meter
		rs	=qproperties.rs2
#alpha
		n=qproperties.alphadk14
#radius where the profile steepens beyond the Einasto profile
		rt	=qproperties.rt
#outer density
		rhoo	=qproperties.rhoo
############################### end: nfw parameters #####################################
############################### Properties of A2199 start ##############################################
#Properties of A2199:
		redshift=qproperties.redshift
		DL	=qproperties.DL

		rto=d1.loc[cluster,'r/kpc']*kpc
##rto=float(input('The radius that you want to look at, in the cluster (In kpc) ['+str(d1.loc[cluster,'r/kpc'])+']: ') or d1.loc[cluster,'r/kpc']) 

#( 500.0*kpc*100.0 )\n: ')
############################### Properties of A2199 end ################################################
############################### You have to decide these start ########################################
##nuobs=float(input('What is the frequency of photon that you receive? (in GHz)	['+str(d1.loc[cluster,'Freq/GHz'])+']: ') or d1.loc[cluster,'Freq/GHz'])
		nuobs=d1.loc[cluster,'Freq/GHz']
############################### You have to decide these end   ########################################








		for fileis in [filearray]:
#This flow depends on the file, qout_msugra - the total electron source spectrum. The e- energy column & Q_e,E(E) total column are needed.
#What is qout_msugra? It is from darksusy-5.1.1 >> test >> qmyown2msugra.f de output file in /home/wallnut/Desktop/fortran_n_ds/seeresult/qmyown2_msugra.
			testtable1=np.loadtxt(fileis)
			m_neutralino	=testtable1[0,0]		#neutralino mass, in unit of GeV
			dssigmav=testtable1[0,1]		#dssigmav, in unit of cm^3 s^-1
			if np.isnan(testtable1[0,1])==True:
				print ('sigmav is NaN')
				continue
			for w in np.arange(1,len(testtable1)):
				if w==1:
					latesttable	=np.array([testtable1[1,0],testtable1[1,2]*givesigmav,np.trapz(2.0*testtable1[1:,2]*givesigmav,x=testtable1[1:,0],axis=0)])
				elif w>1:
					newline	=np.array([testtable1[w,0],testtable1[w,2]*givesigmav,np.trapz(2.0*testtable1[w:,2]*givesigmav,x=testtable1[w:,0],axis=0)])
					latesttable	=np.vstack((latesttable,newline))

			del w
########################### Delete the zero rows start #######################
			ab=0
			cc=[]
			for a in np.arange(0,len(latesttable[:,2])):
				if latesttable[a,0]>m_neutralino:
					latesttable[a,1]=0.0
					latesttable[a,2]=0.0
				if latesttable[a,2]==0.0:
						ab=ab+1
						cc=np.append(cc,a)
				else:
					pass

			cc=cc.astype(int)

			if ab>=20:
				latesttable=np.delete(latesttable,cc[2:],axis=0)

			del ab,cc,a
########################### Delete the zero rows end #########################
			line1='  E                         Source,Q_e,E(E) TOTAL            Equilibrium,trapz(Q_e,E(E),(E->Big E))\n  GeV                       # s^-1 cm^3 GeV^-1       # GeV^-1  cm^3'	
			np.savetxt('try.out',latesttable,'%25.15e',header=line1)

			del testtable1

#This part do the integration to get the radio power.

############################### np.loadtxt start ####################################
		E_and_intQ=latesttable		#column 2 is the \int_E^\infty Q_{e,E'}(E') \, dE', in unit of # s^-1 cm^3.
		rayE=E_and_intQ[:,0]		#The array of e- kinetic energy, in unit of GeV.
		rayEerg=rayE*GeV*1.0e+7		#The array of e- kinetic energy, in unit of erg.

############################### np.loadtxt end ######################################
#
#
#def PAtR2(r,nuu):			# (intermediate)
#		'''Radio power per unit frequency, per unit volume. It is the integration of PAtR(r,ie) over e- energy.
#		r		= spherical radius	, in unit of cm;
#		nuu		= photon frequency	, in unit of GHz;
#		PAtR2(r) 	: erg s^-1 Hz^-1 cm^-3'''
#		PAtR2Y= qfunctions.AA()*E_and_intQ[:,2]*qfunctions.funcR(nuu,rayE,qfunctions.rayB(r,'radial'))*qfunctions.rayB(r,'radial')
#		return np.trapz(PAtR2Y,x=rayEerg) 
#
#def Psphere2(radii,nuu):       #Total radio power from sphere.
#		'''Radio power per unit frequency over the cluster up to radius radii.
#		radii		= spherical radius that you want to look at, in unit of cm;
#		Psphere2	: erg s^-1 Hz^-1'''
#		def PAtR2_rr(r,nuu):
#			return r**2*PAtR2(r,nuu)
#		return 4.0*np.pi*integrate.nquad(PAtR2_rr,[[0.0,radii]],args=(nuu,))[0]


############################### Integration start #####################################################
#=================================================================================================
#Section below is without integrating over e- K.E., and calculated nfw profile.
#=================================================================================================
#	def PAtR(r,ie,nuu):
#		'''Radio power per unit frequency, per unit e- energy, per unit volume.
#		r	= spherical radius	, in unit of cm;
#		ie	= the position in e- energy array, unitless;
#		PAtR(r,ie) : erg s^-1 Hz^-1 erg^-1 cm^-3'''
#		return qfunctions.AA() * bur_numdens_neu(r,m_neutralino,rhos,rs)**2 * E_and_intQ[ie,2] / qfunctions.btot_sph(rayE[ie],qfunctions.rayB(r,'const'),r) * #qfunctions.funcR(nuu,rayE[ie],qfunctions.rayB(r,'const')) * qfunctions.rayB(r,'const')
#
#	def Psphere(ie,nuu):	#Total radio power from sphere.
#		'''Radio power per unit frequency over the cluster up to radius radii.
#		Psphere	: erg s^-1 Hz^-1'''
#		def PAtR_rr(r,ie,nuu):
#			return r**2*PAtR(r,ie,nuu)
#		return 4.0*np.pi*integrate.nquad(PAtR_rr,[[0.0,r_s]],args=(ie,nuu))[0]

#=================================================================================================
#Section below is with integrating over e- K.E., and calculated nfw profile.
#=================================================================================================
		def PAtR2(r,nuu):			# (intermediate)
			'''Radio power per unit frequency, per unit volume. It is the integration of PAtR(r,ie) over e- energy.
			r		= spherical radius	, in unit of cm;
			nuu		= photon frequency	, in unit of GHz;
			PAtR2(r) 	: erg s^-1 Hz^-1 cm^-3'''
			PAtR2Y=qfunctions.AA() * qfunctions.dk14_numdens_neu(r,m_neutralino,rhos,rs,rt,rhoo,n) * E_and_intQ[:,2]/ qfunctions.btot_sph(rayE,qfunctions.rayB(r,'radial'),r) * 		qfunctions.funcR(nuu,rayE,qfunctions.rayB(r,'radial')) * qfunctions.rayB(r,'radial')
			return np.trapz(PAtR2Y,x=rayEerg)

		def Psphere2(radii,nuu):		#Total radio power from sphere.
			'''Radio power per unit frequency over the cluster up to radius radii.
			radii		= spherical radius that you want to look at, in unit of cm;
			Psphere2	: erg s^-1 Hz^-1'''
			def PAtR2_rr(r,nuu):
				return r**2*PAtR2(r,nuu)
			return 4.0*np.pi*integrate.nquad(PAtR2_rr,[[0.0,radii]],args=(nuu,))[0]

############################### Integration end #######################################################



		spherearea=4.0*np.pi*DL**2	# cm^2
		nuori=nuobs*(1.0+redshift)	# Observer's photon is redshifted, so the original 1 supposingly is at slightly higher frequency.
		luminosity=Psphere2(rto,nuori)	# erg s^-1 Hz^-1
		flucy=luminosity/spherearea	# erg s^-1 Hz^-1 cm^-2

############################### Print overall table start ##########################################
		format1={'#sigmav0':'%+14.8e','mchi':'%.8e','redshift':'%7.5f','obsfreq':'%.8e','luminosity':'%+14.8e','rto':'%+14.8e','mJy':'%+14.8e'}

		name1=['sigmav0','mchi','redshift','obsfreq','luminosity','rto','mJy']
		name2=['#sigmav0','mchi','redshift','obsfreq','luminosity','rto','mJy']

		dataline=np.array([givesigmav,m_neutralino,redshift,nuobs,luminosity,rto/kpc,flucy/(1.0e-23*1.0e-3)])
			#print (dataline)
		if os.path.isfile(outfilename)==True:		#if file is there
			if os.path.getsize(outfilename)==0:			#but empty inside
				np.savetxt(outfilename,dataline.reshape(1,len(name1)),fmt='%.8e',header=' '.join(name1))
			else:								#the file is not empty
				tt1=np.loadtxt(outfilename)
				if len(tt1.shape)==1 and len(tt1)==len(name1):				#and has one record in it
					tt1=np.append(tt1.reshape(1,len(name1)),dataline.reshape(1,len(name1)),axis=0)
					ascii.write(tt1,output=outfilename,delimiter=' ',names=name2,formats=format1)
				elif (len(tt1.shape)==2 and tt1.shape[1]==len(name1)):			#Or, has more than one record in it
					tt1=np.append(tt1,dataline.reshape(1,len(name1)),axis=0)
					ascii.write(tt1,output=outfilename,delimiter=' ',names=name2,formats=format1)
				else:								#Or, content is totally incorrect, delete content, and write.
					open(outfilename, 'w').close()
					np.savetxt(outfilename,dataline.reshape(1,len(name1)),fmt='%.8e',header=' '.join(name1))
		elif os.path.isfile(outfilename)==False:		#Elseif the file is not there at all
			np.savetxt(outfilename,dataline.reshape(1,len(name1)),fmt='%.12e',header=' '.join(name1))				
	#if os.path.isfile(outfilename)==True:		#if file is there
	#	with open(outfilename,'a') as f:
	#		np.savetxt(f,dataline.reshape(1,len(name1)),fmt='%.12e',header=' '.join(name1))

		

		del format1,name1,name2,dataline
		print ("Successfully read '"),fileis,"' ."
		print ("\nOutput written to '%s'.")%outfilename
############################### Print overall table end ############################################
############################### Plot Log (mjy/sigmav) vs Log (mchi) #################################

#y = flucy/(1.0e-23*1.0e-3)/dssigmav*givesigmav
#x = mchi

#plt.plot(x, y)
#plt.yscale('log')
#plt.xscale('log')

#plt.show
#plt.savefig('kkrunthis.png')


#print ('\nqproperties.d0 : see NFW1997 parameters and critical density')
#print ('d1 : see the (observation) diffuse radio emission flux density from all the clusters\n')

