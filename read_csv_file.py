"""
Read csv files and convert it into 
pandas dataframe

"""


"""
read csv file with a specific delimiter.
This will return dataframe

sample.csv
Column1|Column2
a|b
a1|b1
a2|b2

"""
df = pd.read_csv("sample.csv",sep="|")


"""
read csv file with a specific delimiter.
discard rows in csv file
This will return dataframe

discard second row
"""
df = pd.read_csv("sample.csv",sep="|",skiprows=[1]):

"""
Column1   Column2
a 			b
a2			b2

"""
