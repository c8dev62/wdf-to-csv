# wdf-to-csv
Converts wdf files to csv

# Prerequisites
1. Python v3.7.4 or higher
2. Pip v20.1. or higher

# Files
1. config.py contains several variable configurations  
  A. "SENSOR_DATA_DIR" represents the path where sensor data are stored  
  B. "DUPLICATES_FOLDER" represents the path where the duplicate files are stored  
  C. "FOR_UFL" represents the path where .csv data for UFL ingestion are stored  
  D. "IN_EXT" - file extension of the input file(sensor data)  
  E. "OUT_EXT" - file extension of the output file(for UFL ingestion)  
2. parser.py  
   for each file.IN_EXT found in SENSOR_DATA_DIR, parser.py creates a duplicate of it and stores in DUPLICATES_FOLDER.  
   Then, parser.py formats each file.IN_EXT and outputs file.OUT_EXT in the FOR_UFL folder  
 
 # Usage
 1. After creating the necessary folders(SENSOR_DATA_DIR, DUPLICATES_FOLDER, FOR_UFL) and configuring the config.py, user may run the program by executing 
 <strong>python parser.py</strong>
