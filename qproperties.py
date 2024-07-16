import numpy as np
from scipy import constants
from qconstants import *
import os.path
import pandas as pd

############################## Choose a Cluster from list below ###############################################

cluster='A2029'

############################## List of Cluster ##################################################################

d1=pd.DataFrame.from_dict({
'A2142'  : ['A2142','RH',0.0909,418600,23,129,0.57,0.810,5.82,10.0,0.5,2000,1331.7523,550.5568,1.7174e-23,3.4930e-23,0.3706,3.8467e-23,3534.8085,0.3736,1.8465e-26,3.4682e-23],
'A2744'  : ['A2744','RH',0.3080, 28840,218, 520, 7.7, 0.680, 10.0, 10.0, 0.5,1100,1405.7293,452.7817,1.5182e-23,5.3495e-23,0.3914,5.8209e-23,2624.9476,0.3929,2.1322e-26,2.7964e-23],
'A2199'  : ['A2199','ULRH',0.0302, 127000 ,250 , 99.3, 2.0, 0.655, 10.1, 11.7, 0.9, 1000.0,270.9569,467.5118,2.9931e-22,2.2202e-23,0.2756,2.3553e-23,3399.5242,0.2801,1.078e-26,1.0107e-21],
'A119'   : ['A119','ULRH',0.0440,832000, 243 , 357.9, 5.8, 0.675, 0.15, 7.5, 0.9, 1100.0,512.1827,550.5964,1.1673e-22,2.8549e-23,0.3391,3.0990e-23,3704.7853,0.3431,1.5608e-26,3.3656e-22],
'A478'   : ['A478','MH',0.0880,132300, 16.6, 70, 7.75, 0.613, 3.55, 10.0, 0.5, 180,456.4341,530.5936,1.4927e-22,3.0531e-23,0.3421,3.3315e-23,3473.5247,0.3457,1.6124e-26,4.4271e-22],
'A2029'  : ['A2029','MH',0.0767, 342240, 18.8, 58, 4.00, 0.582, 3.90, 16.0, 0.5, 125,333.5070,563.5962,4.0380e-22,3.5754e-23,0.3793,3.9413e-23,3627.4741,0.3823,1.845e-26,1.4106e-21]},
orient='index',columns=['Label','type','redshift','DL','S_nu','r_c_dum','T_gas_dum','beta','n0','B_dum','eta','r','rs1','rs2','rhosnfw','rhosein','alphaein','rhosdk14','rt','alphadk14','rhoo','rhoshern'])


############################# Set and decide the constants start ##################################################

#Hubble constants
h		=0.7		#little h.		unit :	-

#Critical density:
sigm		=0.3		#matter density.	unit :	-
sigl		=0.7		#dark energy density.	unit :	-
sig8		=0.829

#Properties of cluster:
redshift	=d1.loc[cluster,'redshift']
DL		=d1.loc[cluster,'DL']*kpc*100.0	# luminosity distance, in unit of cm.	z=0.0302
#DA		=100000*kpc*100.0
S_nu            =d1.loc[cluster,'S_nu']            #mJy
r_c_dum	=h*(d1.loc[cluster,'r_c_dum'])*50**-1*100.0		#Core radius.		unit :	h50^-1 kpc, where H0=50 kms^-1Mpc^-1
T_gas_dum	=d1.loc[cluster,'T_gas_dum']		#T_gas in unit of keV
beta		=d1.loc[cluster,'beta']		#Beta parameter.	unit :	-
n0		=d1.loc[cluster,'n0']		#Thermal electron central density	#unit :	cm^-3. A&A 540, A38 (2012)
B_dum		=d1.loc[cluster,'B_dum']	#central magnetic field.		#unit :	Gauss.  A&A 540, A38 (2012)
eta		=d1.loc[cluster,'eta']		#proportional coefficient related to magnetic field profile

#Temperature of CMB at any redshift z. (want ot know more? See http://www.cv.nrao.edu/course/astr534/CMB.html)
T		=T0*(1.0+redshift)

#conversion if necessary
B0	=B_dum*(10**-6)
H_0	=100.0*h				#hubble constant.	unit :	km s^-1 Mpc^-1
H_0m	=H_0/(1000.0*si_pc)			#hubble constant.	unit :	s^-1
Ez	=np.sqrt(sigm*(1.0+redshift)**3+sigl)
Hz	=H_0m*Ez				#H(z). 			unit :	s^-1
rho_crit=3.0*Hz**2/(8.0*constants.pi*si_G)	#critical density.	unit :	kg m^-3

T_gas	=T_gas_dum*1000.0*si_e/si_k		#T_gas in unit of Kelvin
r_c_dum2=r_c_dum*0.5/h				#Core radius.		unit :	kpc, where h=0.673
r_c	=r_c_dum2*1000.0*si_pc*100.0		#Core radius.		unit :	cm

############################# Particle upper-limit ################################################################
Relic_density_limit =3.0e-26
Calet=3.0e-24
Boudaud=1.0e-24
Ibarra=0.9e-25

############################# Set and decide the constants end ####################################################
############################# start: parameters for nfw profile ####################################################

#characteristic density in unit of kg m^-3 	( multiplied by rho_crit ) 
rhosnfw= (d1.loc[cluster,'rhosnfw']/h**2)
#characteristic radius in unit of meter
rs1= kpc*d1.loc[cluster,'rs1']*h
r=d1.loc[cluster,'r']*kpc
############################# end: parameters for nfw profile ####################################################
############################# start: parameters for einasto profile ####################################################

#characteristic density in unit of kg m^-3	( multiplied by rho_crit )
rhosein= (d1.loc[cluster,'rhosein']/h**2)
#characteristic alpha
alphaein= d1.loc[cluster,'alphaein']
rs2= kpc*d1.loc[cluster,'rs2']*h
############################# end: parameters for einasto profile ####################################################
############################# start: parameters for DK14 ####################################################

#characteristic density in unit of kg m^-3	( multiplied by rho_crit )
rhosdk14= (d1.loc[cluster,'rhosdk14']/h**2)
#characteristic radius in unit of meter and alpha
rt= kpc*d1.loc[cluster,'rt']*h
rhoo=(d1.loc[cluster,'rhoo']/h**2)
alphadk14= d1.loc[cluster,'alphadk14']
############################# end: parameters for DK14 ####################################################
############################# start: parameters for hernequist profile ####################################################

#characteristic density in unit of kg m^-3	( multiplied by rho_crit )
rhoshern= (d1.loc[cluster,'rhoshern']/h**2)

############################# end: parameters for hernequist profile ####################################################






