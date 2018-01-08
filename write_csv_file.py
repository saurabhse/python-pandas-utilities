"""
Generate a csv file from pandas dataframe

"""

import pandas as pa

"""
Generate a csv file from pandas dataframe
"""
df.to_csv("output_file_name.csv", sep="delimiter")

"""
Generate a csv file from pandas dataframe
without index column
"""
df.to_csv("output_file_name.csv", sep="delimiter",index=False)

"""
Generate a csv file from pandas dataframe
without index column and append the data to csv file
"""

df.to_csv("output_file_name.csv", sep="delimiter",index=False, mode='a')

