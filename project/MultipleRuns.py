def WriteScenarioName(iNumber, inputFile):
	filetoOpen = inputFile
	f = open(filetoOpen,'r')
	filedata = f.read()
	f.close()

	oldname = "test_run"
	if iNumber > 1:
		oldname = oldname + str(iNumber-1)
	newname = "test_run" + str(iNumber)
	newdata = filedata.replace(oldname,newname)

	f = open(filetoOpen,'w')
	f.write(newdata)
	f.close()

def WriteNewDemand(iNumber, firstLine, lastLine, inputFile, newD, oldD):
	import linecache
	
	#Geting the last data from the input file
	filetoOpen = inputFile
	f = open(filetoOpen,'r')
	filedata = f.read()
	f.close()

	f = open(filetoOpen,'r')	
	lines = [firstLine, lastLine] #Point out the lines we will make changes

	oldname = ['']

	#Geting the old data and changing it into memory by the new one 
	k=0
	if iNumber == 1:
		for i in range (lines[0], lines[1]):
			oldname = str(linecache.getline(filetoOpen,i).strip('\n\r'))
			newname = newD[k]
			print(oldname, newname)
			filedata = filedata.replace(oldname,newname)
			oldD[k] = newD[k]
			k=k+1
	else:
		for i in range (lines[0], lines[1]):
			newname = newD[k]
			oldname = oldD[k]
			print(oldname, newname)
			filedata = filedata.replace(oldname,newname)
			oldD[k] = newD[k]
			k=k+1

	f.close()
	
	#Writing the new demand to the input file
	f = open(filetoOpen,'w')
	f.write(filedata)
	f.close()

def GetDemand(iNumber, nm, ncps, demFile, newD):
	import linecache

	filetoOpen = demFile
	f = open(filetoOpen,'r')	

	firstLine = (iNumber-1)*nm*ncps
	lastLine  = firstLine + nm*ncps

	lines = [firstLine, lastLine] #Point out the lines we will make changes

	#Geting the old data and changing it into memory by the new one 
	k = 1
	for i in range (lines[0], lines[1]):
		newD[k-1] = str(linecache.getline(filetoOpen,i+1).strip('\n\r'))
		k=k+1
	f.close()

def TemoaRun():
	from time import time
	import sys
	import os
	from subprocess import call
	import sqlite3
	import csv
	#from IPython import embed

	sys.stderr.write('\nSolving temoa for Energy Systems\n')

	configInputFile = 'temoa_model/config_sample'

	#This information is associated with the places where we modify the model file
	mInputFile = 'data_files/24UC_Fixed4_Ramping_Numbers.dat'
	firstLine = 13485  #First line to change in the model file
	lastLine  = 13536

	#This information is associated with the demand file for multiple runs
	demInputFile = 'analyses/UC_ESM/demand_60_60_60.dat'
	nmonths = 3
	ncp = 17
	newDemand = ['']*((nmonths*ncp))
	oldDemand = ['']*((nmonths*ncp))

	#This is associated to the multiple Temoa runs
	for count in range(1, 100):
		WriteScenarioName(count, configInputFile)
		GetDemand(count, nmonths, ncp, demInputFile, newDemand)
		WriteNewDemand(count, firstLine, lastLine, mInputFile, newDemand, oldDemand)
		os.system("python temoa_model/ --config=temoa_model/config_sample")

	#Attaching and getting Data from the Database
	dbInputFile = 'db_io/temoa_schema.sqlite'
	con = sqlite3.connect(dbInputFile)
	cur = con.cursor()     # A database cursor enables traversal over DB records
	con.text_factory = str # This ensures data is explored with UTF-8 encoding
	generators =  ('i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'i10', 'i11', 'i12', 'i13', 'i14', 'i15', 'i16', 'i17', 'i18', 'i19', 'i20', 'i21', 'i22', 'i23', 'i24', 'i25', 'i26', 'i27', 'i28', 'i29', 'i30', 'i31', 'i32')

	#data = cur.execute("SELECT t_periods, tech, scenario, sum(vflow_out) from Output_VFlow_Out WHERE tech like 'i_%' GROUP BY scenario, t_periods, tech")
	data = cur.execute("SELECT t_periods, tech, scenario, sum(vflow_out) from Output_VFlow_Out WHERE tech IN ('i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9', 'i10', 'i11', 'i12', 'i13', 'i14', 'i15', 'i16', 'i17', 'i18', 'i19', 'i20', 'i21', 'i22', 'i23', 'i24', 'i25', 'i26', 'i27', 'i28', 'i29', 'i30', 'i31', 'i32') GROUP BY scenario, t_periods, tech")
	#WHERE tech is '"+generators+"'
	
	with open('output_60_60_60.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['Month', 'Technology', 'Scenario', 'GWh'])
		writer.writerows(data)
	#cur.execute("DELETE FROM "+tables[table]+" WHERE scenario is '"+options.scenario+"'") 

	#Create a dictionary in which to store "solved" variable values
	#svars = defaultdict( lambda: defaultdict( float ))  


if __name__ == '__main__':
    TemoaRun()
