#remember to add case for elements that have more than 1 valence electron type

#excluding transition metals and the Lanthanids and actinides
class periodic_table:
	def __init__(self,initial,name,atomic_number,atomic_mass,valence_e,metal_or_not,nonmetal_or_not,noble_gas,row,column,electronegativity):
		self.initial = initial
		self.name = name
		#print(name)
		self.atomic_mass = atomic_mass
		#print(atomic_mass)
		self.atomic_number = atomic_number
		#print(atomic_number)
		self.valence_e = valence_e
		#print(valence_e)
		self.metal_or_not = metal_or_not
		self.nonmetal_or_not = nonmetal_or_not
		self.noble_gas = noble_gas
		self.row = row
		self.column = column
		self.electronegativity = electronegativity
	def ionic_bonding(atom1,atom2):
		if (atom1.metal_or_not == 'yes' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes') or (atom1.initial == 'H' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes'):
			if (atom1.valence_e+atom2.valence_e == 2 or atom1.valence_e+atom2.valence_e == 8):
				print(atom1.initial,atom2.initial)
			elif atom2.valence_e%2!=0 and (atom1.valence_e%2 != 0 or atom1.valence_e == 1):
				atom1number = (8-atom2.valence_e)/atom1.valence_e
				atom2number = 1
				print(str(atom1number),atom1.initial,str(atom2number),atom2.initial)
			else:
				atom1number = atom2.valence_e
				atom2number = atom1.valence_e
				while atom1number%2 == 0 and atom2number%2 == 0:
					atom1number=atom1number/2
					atom2number = atom2number/2
				print(str(atom1number),atom1.initial,str(atom2number),atom2.initial)
		
		elif atom1.metal_or_not == 'no' and atom1.nonmetal_or_not == 'yes' and atom2.metal_or_not == 'yes':
			if (atom1.valence_e+atom2.valence_e == 2 or atom1.valence_e+atom2.valence_e == 8):
				print(atom2.initial,atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal mental not metal nonmetal')
			elif atom1.valence_e%2!=0 and (atom2.valence_e%2 != 0 or atom2.valence_e == 1):
				atom2number = (8-atom1.valence_e)/atom2.valence_e
				atom1number = 1
				print(str(atom2number),atom2.initial,str(atom1number),atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal mental not metal nonmetal')
			else:
				atom2number = atom1.valence_e
				atom1number = atom2.valence_e
				while atom2number%2 == 0 and atom1number%2 == 0:
					atom2number=atom2number/2
					atom1number = atom1number/2
				print(str(atom2number),atom2.initial,str(atom1number),atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal mental not metal nonmetal')
		else:
			if (atom1.initial == 'H' and atom2.initial == 'H'):
				print('Hydrogen and Hydrogen is a covalent bond so the program will restart this is a covalent bond')
				periodic_table.covalent_bonding(atom1,atom2)
			elif (atom1.nonmetal_or_not == 'yes' and atom2.nonmetal_or_not == 'yes'):
				print('error due to the fact that two nonmetals are being input this is a covalent bond')
				periodic_table.covalent_bonding(atom1,atom2)
	def ionic_bonding_and_number_identifier_and_covalent_identifier(atom1,atom2):
		metal = ''
		nonmetal = ''
		'''if atom1.metal_or_not == 'yes' and atom2.nonmetal_or_not == 'yes':
			metal = atom1
			nonmetal = atom2
		elif atom2.metal_or_not == 'yes' and atom1.nonmetal_or_not == 'yes':
			metal = atom2
			nonmetal = atom1
		if (metal == atom2) or (nonmetal == atom1):
			print('ionic bond detected outright')
			if (metal.valence_e+nonmetal.valence_e == 2 or metal.valence_e+nonmetal.valence_e == 8):
				print(metal.initial,nonmetal.initial)
			elif nonmetal.valence_e%2 != 0 and (metal.valence_e%2 != 0 or atom1.valence_e == 1):
				metalnumber = (8-nonmetal.valence_e)/metal.valence_e
				nonmetalnumber = 1
				print(str(metalnumber),metal.initial,str(nonmetalnumber),nonmetal.initial)
			else:
				atom1number = nonmetal.valence_e
				atom2number = metal.valence_e
				while atom1number%2 == 0 and atom2number%2 == 0:
					atom1number=atom1number/2
					atom2number = atom2number/2
				print(str(atom1number),metal.initial,str(atom2number),nonmetal.initial)'''
		if (atom1.noble_gas == 'yes' and atom2.nonmetal_or_not == 'yes') or (atom2.noble_gas == 'yes' and atom1.nonmetal_or_not == 'yes'):
			print('that is a covalent bond')
			print('two of the nonmetals needed you cannot just have an electon by itself')
			if (atom2.noble_gas == 'yes' and atom1.nonmetal_or_not == 'yes'):
				if atom1.electon%2 == 0:
					print(str(1),atom1.initial,str(1),atom2.initial)
					print('we put an answer of one for the metal but just remember that you can have any number of that metal that does not use up more than the 8 noble gas electrons')
				else:
					print(str(2),atom1.initial,str(1),atom2.initial)
					print('we put an answer of two for the metal but just remember that you can have any even number of that metal that does not use up more than the 8 noble gas electrons')
			else:
				terminateduetomistake()
		elif abs(atom1.electronegativity-atom2.electronegativity)>=2:
			print('this is an ionic bond')
			if atom1.electronegativity<atom2.electronegativity:
				metal = atom1
				nonmetal = atom2
				periodic_table.ionic(metal,nonmetal)
			elif atom1.electronegativity>atom2.electronegativity:
				metal = atom2
				nonmetal = atom1
				periodic_table.ionic(metal,nonmetal)
			else:
				terminateduetomistake()
		elif abs(atom1.electronegativity-atom2.electronegativity)<=.4:
			print('this is a pure covalent bond')
			periodic_table.covalent_bonding(atom1,atom2)
		elif abs(atom1.electronegativity-atom2.electronegativity)<2:
			print('this is a polar covalent pond')
			periodic_table.covalent_bonding(atom1,atom2)
	def ionic(metal,nonmetal):
		if (metal.valence_e+nonmetal.valence_e == 2 or metal.valence_e+nonmetal.valence_e == 8):
			print(metal.initial,nonmetal.initial)
		elif(metal.valence_e == 1):
			metalnumber = (8-nonmetal.valence_e)/metal.valence_e
			nonmetalnumber = 1
			print(str(metalnumber),metal.initial,str(nonmetalnumber),nonmetal.initial)
		else:
			atom1number = nonmetal.valence_e
			atom2number = metal.valence_e
			num = [1,2,3,4,5,6,7,8]
			for i in num:
				while atom2number%i == 0:
					atom2number = atom2number/i
				while atom1number%i == 0:
					atom1number=atom1number/i
				print(str(atom1number),metal.initial,str(atom2number),nonmetal.initial)
	def covalent_bonding(atom1,atom2):
		print('for the time being only put one of one element and however you need of the other')
		print('')
		numberofatom1 = int(input('what number of atoms for atom1 do you want? '))
		numberofatom2 = int(input('what number of atoms for atom2 do you want? '))
		if (atom1.valence_e+atom2.valence_e)%2 != 0:
			charge = int(input('what is the charge on the compound'))
			if charge != 0:
				covalent1(atom1,atom2,charge)
				#deal with number of electrons due to charge
			else:
				print('there is no way this would work uneven electron numbers do not work')
				terminate()
		elif (atom1.valence_e+atom2.valence_e)%2 == 0:
			covalent1(atom2,atom1,0)
		else:
			terminateduetomistake()
	def covalent1(atom1,atom2,charge):
		pass

def terminate():
	print('invalid inputs')
	quit()
def terminateduetomistake():
	print('error error error')
	quit()
#row one
H = periodic_table('H','Hydrogen',1,1.008,1,'no','yes','no',1,1,2.1)
He = periodic_table('He','Helium',2,4.0026,2,'no','yes','no',1,18,'no data')
#figure out fix for helium bonding


#row two
Li = periodic_table('Li','Lithium',3,6.94,1,'yes','no','no',2,1,1.0)
Be = periodic_table('Be','Beryllium',4,9.0122,2,'yes','no','no',2,2,1.5)
B = periodic_table('B','Boron',5,10.81,3,'no','no','no',2,13,2)
C = periodic_table('C','Carbon',6,12.011,4,'no','yes','no',2,14,2.5)
N = periodic_table('N','Nitrogen',7,14.007,5,'no','yes','no',2,15,3)
O = periodic_table('O','Oxygen',8,15.999,6,'no','yes','no',2,16,3.5)
F = periodic_table('F','Fluorine',9,18.998,7,'no','yes','no',2,17,4)
Ne = periodic_table('Ne','Neon',10,20.180,8,'no','yes','yes',2,18,'no data')
#row three
Na = periodic_table('Na','Sodium',11,22.990,1,'yes','no','no',3,1,.9)
Mg = periodic_table('Mg','Magnesium',12,24.305,2,'yes','no','no',3,2,1.2)
Al = periodic_table('Al','Aluminium',13,26.982,3,'yes','no','no',3,13,1.5)
Si = periodic_table('Si','Silicon',14,28.085,4,'no','no','no',3,14,1.8)
P = periodic_table('P','Phosphorus',15,30.974,5,'no','yes','no',3,15,2.1)
S = periodic_table('S','Sulfur',16,32.06,6,'no','yes','no',3,16,2.5)
Cl = periodic_table('Cl','Chlorine',17,35.45,7,'no','yes','no',3,17,3)
Ar = periodic_table('Ar','Argon',18,39.948,8,'no','yes','yes',3,18,'no data')

#row four
K = periodic_table('K','Potassium',19,39.098,1,'yes','no','no',4,1,.8)
Ca = periodic_table('Ca','Calcium',20,40.078,2,'yes','no','no',4,2,1)
Ga = periodic_table('Ga','Gallium',31,69.723,3,'yes','no','no',4,13,1.6)
Ge = periodic_table('Ge','Germanium',32,72.630,4,'no','no','no',4,14,1.8)
As = periodic_table('As','Arsenic',33,74.922,5,'no','no','no',4,15,2)
Se = periodic_table('Se','Selenium',34,78.972,6,'no','yes','no',4,16,2.4)
Br = periodic_table('Br','Bromine',35,79.904,7,'no','yes','no',4,17,2.8)
Kr = periodic_table('Kr','Kyrpton',36,83.798,8,'no','yes','yes',4,18,'no data')

#row five
Rb = periodic_table('Rb','Rubidium',37,85.468,1,'yes','no','no',5,1,.8)
Sr = periodic_table('Sr','Strontium',38,87.62,2,'yes','no','no',5,2,1)
In = periodic_table('In','Indium',49,114.82,3,'yes','no','no',5,13,1.7)
Sn = periodic_table('Sn','Tin',50,118.71,4,'yes','no','no',5,14,1.8)
Sb = periodic_table('Sb','Antimony',51,121.76,5,'no','no','no',5,15,1.9)
Te = periodic_table('Te','Tellurium',52,127.60,6,'no','no','no',5,16,2.1)
I = periodic_table('I','Iodine',53,126.90,7,'no','yes','no',5,17,2.5)
Xe = periodic_table('Xe','Xenon',54,131.29,8,'no','yes','yes',5,18,'no data')

#row six
Cs = periodic_table('Cs','Caesium',55,132.91,1,'yes','no','no',6,1,.7)
Ba = periodic_table('Ba','Barium',56,137.33,2,'yes','no','no',6,2,.9)
Tl = periodic_table('Tl','Thallium',38,204.38,3,'yes','no','no',6,13,1.8)
Pb = periodic_table('Pb','Lead',84,207.2,4,'yes','no','no',6,14,1.9)
Bi = periodic_table('Bi','Bismuth',85,208.98,5,'yes','no','no',6,15,1.9)
Po = periodic_table('Po','Polonium',86,209,6,'yes','no','no',6,16,2.0)
At = periodic_table('At','Astatine',87,210,7,'no','no','no',6,17,2.2)
Rn = periodic_table('Rn','Radon',86,222,8,'no','yes','yes',6,18,'no data')

#row seven
Fr = periodic_table('Fr','Francium',86,223,1,'yes','no','no',7,1,.7)
Ra = periodic_table('Ra','Radium',87,226,2,'yes','no','no',7,2,.9)
Nh = periodic_table('Nh','Nihonium',113,286,3,'not_defined','not_defined','no',7,13,'no data')
Fl = periodic_table('Fl','Flerovium',114,289,4,'yes','no','no',7,14,'no data')
Mc = periodic_table('Mc','Moscovium',115,290,5,'not_defined','not_defined','no',7,15,'no data')
Lv = periodic_table('Lv','Livermorium',116,293,6,'not_defined','not_defined','no',7,16,'no data')
Ts = periodic_table('Ts','Tennessine',117,294,7,'not_defined','not_defined','no',7,17,'no data')
Og = periodic_table('Og','Oganesson',118,294,8,'not_defined','not_defined','not_defined',7,18,'no data')

#periodic_table.ionic_bonding(Na,F)
periodic_table.ionic_bonding_and_number_identifier_and_covalent_identifier(F,Cl)