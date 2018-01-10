"""
Read multiple large files, process them in chunks and prepare
combined file.

Merge happens in append mode.
This is very effective to combine large files without 
creating large memory footprint
"""

import os, glob
import pandas as pd

"""
Writes to file in batch mode.
Only first batch will write the column names
Next batches will just append data
"""
def write_file(chunk,file_name,head,output_file_name,separator):
	if head:
		chunk.to_csv(os.path.join("output_folder_directory",output_file_name), sep=separator,index=False, mode='a', encoding='utf-8')
	else:
		chunk.to_csv(os.path.join("output_folder_directory",output_file_name), sep=separator,index=False, mode='a', encoding='utf-8',header=head)

"""
Combines multiple files into single file
Customizable batch_size, separator and rows to be skipped
"""
def combine(skip_rows=None,separator="|",batch_size=10):
	
	files = glob.glob(os.path.join("input_folder_directory", "*.csv")) 
	rows_to_skip = skip_rows
	if rows_to_skip:
		rows_to_skip = [int(s) for s in rows_to_skip.split(',')]
		
	df = pd.DataFrame()
	head = ' '
	for file_name in files:
		if rows_to_skip:
			for chunk in pd.read_csv(file_name,sep=separator, chunksize = batch_size, low_memory=False,skiprows=rows_to_skip,encoding = 'utf8'):
				write_file(chunk,file_name,head,"output_file_name.csv",separator)
				head = None
		else:
			for chunk in pd.read_csv(file_name,sep=separator, chunksize = batch_size, low_memory=False,encoding = 'utf8'):
				write_file(chunk,file_name,head,"output_file_name.csv",separator)
				head = None
	
"""
pass skip_rows,separator,batch_size for providing non-default values
"""
combine()
