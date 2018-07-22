import re,datetime
import pandas as pd
import sqlalchemy
import sqlalchemy import create_engine

def dfToDb(df,table_name,user,password,db_url):
  engine= create_engine('oracle+cx_oracle://%s:%s@%s' % (user,password,db_url))
  df.to_sql(table_name,engine,if_exists='append',index=False,chunksize=5000,dtype=type_mapping(df))

def type_mapping(df):
  type_dict = {}
  for cols,types in zip(df.columns,df.dtypes):
    if "object" in str(types):
      type_dict.update({col:sqlalchemy.types.VARCHAR(length=255)})
      df[col] = df[col].apply(lambda x:format_date(x))
    if "float" in str(types):
      type_dict.update({col:sqlalchemy.types.Float})
    if "int" in str(types):
      type_dict.update({col:sqlalchemy.types.INT()})
  return type_dict
  
  
  def format_date(date):
    try:
      match_found,date_format = match_date_format(date)
      if match_found:
        date_str = datetime.datetime.strptime(date.strip(),date_format)
    except (AttributeError,valueError) as  exception:
      pass
    return date_str
    
  def match_date_format(date):
    format_1 = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})',str(date))
    format_2 = re.match(r'(\d{4}-\d{2}-\d{2})',str(date))
    format_3 = re.match(r'(\d{2}/\d{2}/\d{4})',str(date))
    match_found = False
    date_format = None
    if format_1:
      match_found = True
      date_format = '%Y-%m-%d %H:%M:%S'
    elif format_2:
      match_found = True
      date_format = '%Y-%m-%d'
    elif format_3:
      match_found = True
      date_format = '%m/%d/%Y'
    return match_found,date_format
    
 if __name__ == "main":
    dfToDb(df,"table_name","user","password","db_url")
