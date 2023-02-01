import os

path = "..\..\Level1"
file_name = "Input.dat"

with open(file_name,"w") as file:
	for filename in os.listdir(path):
		file.write("<BeginHDF5File>\n")
		file.write("NAME       : " + path + "\\" + filename + "\\Hydrodynamic_2.hdf5")
		file.write("\n")
		file.write("<EndHDF5File>\n")