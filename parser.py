'''
OUTLINE
1. Duplicate Sensor Data
2. Clean Original Sensor Data
'''
import csv
import os
import shutil
from config import *

def find_wdfs(directory):
	wdfList = []
	for f_name in os.listdir(directory):
		if f_name.endswith(IN_EXT):
			wdfList.append(f_name)
	return wdfList


# copyfile("C:/Users/CALIBR8/Desktop/FRANCISCARILLO_instrument19_667064122.wdf","C:/Users/CALIBR8/Google Drive/EDC - Projects and Scripts/tempLogger/Duplicates/a.wdf")

# with open("C:/Users/CALIBR8/Desktop/FRANCISCARILLO_instrument19_667064122.wdf") as f:
# 	with open("fileName.csv", "w", newline="") as csvfile:
# 		dataWriter = csv.writer(csvfile, delimiter=",", quotechar="'")
# 		for line in f:
# 			if (line[0] == "<"):
# 				if (line[:13] == "<Sensor Name>"):
# 					sensorName = line.lstrip("<Sensor Name>").rstrip("\n")
# 					print(type(sensorName))
# 			else:
# 				break
# 		for line in f:
# 				rowData = line.split(",")
# 				rowData.insert(0, sensorName)
# 				#print(rowData[:3])\
# 				dataWriter.writerow(rowData[:3])

def parser(f_name):
	no_ext = os.path.splitext(f_name)[0]
	print(no_ext)
	with open(SENSOR_DATA_DIR+f_name) as f:
		with open(FOR_UFL+no_ext+OUT_EXT, "w", newline="") as csvfile:
			dataWriter = csv.writer(csvfile, delimiter=",", quotechar="'")
			for line in f:
				if (line[0] == "<"):
					if (line[:13] == "<Sensor Name>"):
						sensorName = line.lstrip("<Sensor Name>").rstrip("\n")
				else:
					break
			for line in f:
					rowData = line.split(",")
					rowData.insert(0, sensorName)
					dataWriter.writerow(rowData[:3])
	os.rename(SENSOR_DATA_DIR+f_name, SENSOR_DATA_DIR+no_ext+"_OK")

def main():
	dataList = find_wdfs(SENSOR_DATA_DIR)
	for i in dataList:
		#1. Duplicate Sensor Data
		shutil.copy2(SENSOR_DATA_DIR+i, DUPLICATES_FOLDER+i)
		
		#2. Clean Original Sensor Data
		parser(i)


if __name__ == '__main__':
	main()

