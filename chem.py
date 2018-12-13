#excluding transition metals and the Lanthanids and actinides
class periodic_table:
	def __init__(self,initial,name,atomic_number,atomic_mass,valence_e,metal_or_not,nonmetal_or_not,noble_gas,row,column):
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
	def ionic_bonding(atom1,atom2):
		if (atom1.metal_or_not == 'yes' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes') or (atom1.initial == 'H' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes'):
			if (atom1.valence_e+atom2.valence_e == 2 or atom1.valence_e+atom2.valence_e == 8):
				print(atom1.initial,atom2.initial)
			elif atom2.valence_e%2==0 and (atom1.valence_e%2 == 0 or atom1.valence_e == 1):
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
	def covalent_bonding(atom1,atom2):
		print('yet to be built')
#row one
H = periodic_table('H','Hydrogen',1,1.008,1,'yes','yes','no',1,1)
He = periodic_table('He','Helium',2,4.0026,2,'no','yes','no',1,18)

#row two
Li = periodic_table('Li','Lithium',3,6.94,1,'yes','no','no',2,1)
Be = periodic_table('Be','Beryllium',4,9.0122,2,'yes','no','no',2,2)
B = periodic_table('B','Boron',5,10.81,3,'no','no','no',2,13)
C = periodic_table('C','Carbon',6,12.011,4,'no','yes','no',2,14)
N = periodic_table('N','Nitrogen',7,14.007,5,'no','yes','no',2,15)
O = periodic_table('O','Oxygen',8,15.999,6,'no','yes','no',2,16)
F = periodic_table('F','Fluorine',9,18.998,7,'no','yes','no',2,17)
Ne = periodic_table('Ne','Neon',10,20.180,8,'no','yes','yes',2,18)
#row three
Na = periodic_table('Na','Sodium',11,22.990,1,'yes','no','no',3,1)
Mg = periodic_table('Mg','Magnesium',12,24.305,2,'yes','no','no',3,2)
Al = periodic_table('Al','Aluminium',13,26.982,3,'yes','no','no',3,13)
Si = periodic_table('Si','Silicon',14,28.085,4,'no','no','no',3,14)
P = periodic_table('P','Phosphorus',15,30.974,5,'no','yes','no',3,15)
S = periodic_table('S','Sulfur',16,32.06,6,'no','yes','no',3,16)
Cl = periodic_table('Cl','Chlorine',17,35.45,7,'no','yes','no',3,17)
Ar = periodic_table('Ar','Argon',18,39.948,8,'no','yes','yes',3,18)

#row four
K = periodic_table('K','Potassium',19,39.098,1,'yes','no','no',4,1)
Ca = periodic_table('Ca','Calcium',20,40.078,2,'yes','no','no',4,2)
Ga = periodic_table('Ga','Gallium',31,69.723,3,'yes','no','no',4,13)
Ge = periodic_table('Ge','Germanium',32,72.630,4,'no','no','no',4,14)
As = periodic_table('As','Arsenic',33,74.922,5,'no','no','no',4,15)
Se = periodic_table('Se','Selenium',34,78.972,6,'no','yes','no',4,16)
Br = periodic_table('Br','Bromine',35,79.904,7,'no','yes','no',4,17)
Kr = periodic_table('Kr','Kyrpton',36,83.798,8,'no','yes','yes',4,18)

#row five
Rb = periodic_table('Rb','Rubidium',37,85.468,1,'yes','no','no',5,1)
Sr = periodic_table('Sr','Strontium',38,87.62,2,'yes','no','no',5,2)
In = periodic_table('In','Indium',49,114.82,3,'yes','no','no',5,13)
Sn = periodic_table('Sn','Tin',50,118.71,4,'yes','no','no',5,14)
Sb = periodic_table('Sb','Antimony',51,121.76,5,'no','no','no',5,15)
Te = periodic_table('Te','Tellurium',52,127.60,6,'no','no','no',5,16)
I = periodic_table('I','Iodine',53,126.90,7,'no','yes','no',5,17)
Xe = periodic_table('Xe','Xenon',54,131.29,8,'no','yes','yes',5,18)

#row six
Cs = periodic_table('Cs','Caesium',55,132.91,1,'yes','no','no',6,1)
Ba = periodic_table('Ba','Barium',56,137.33,2,'yes','no','no',6,2)
Tl = periodic_table('Tl','Thallium',38,204.38,3,'yes','no','no',6,13)
Pb = periodic_table('Pb','Lead',84,207.2,4,'yes','no','no',6,14)
Bi = periodic_table('Bi','Bismuth',85,208.98,5,'yes','no','no',6,15)
Po = periodic_table('Po','Polonium',86,209,6,'yes','no','no',6,16)
At = periodic_table('At','Astatine',87,210,7,'no','no','no',6,17)
Rn = periodic_table('Rn','Radon',86,222,8,'no','yes','yes',6,18)

#row seven
Fr = periodic_table('Fr','Francium',86,223,1,'yes','no','no',7,1)
Ra = periodic_table('Ra','Radium',87,226,2,'yes','no','no',7,2)
Nh = periodic_table('Nh','Nihonium',113,286,3,'not_defined','not_defined','no',7,13)
Fl = periodic_table('Fl','Flerovium',114,289,4,'yes','no','no',7,14)
Mc = periodic_table('Mc','Moscovium',115,290,5,'not_defined','not_defined','no',7,15)
Lv = periodic_table('Lv','Livermorium',116,293,6,'not_defined','not_defined','no',7,16)
Ts = periodic_table('Ts','Tennessine',117,294,7,'not_defined','not_defined','no',7,17)
Og = periodic_table('Og','Oganesson',118,294,8,'not_defined','not_defined','not_defined',7,18)

periodic_table.ionic_bonding(Li,F)