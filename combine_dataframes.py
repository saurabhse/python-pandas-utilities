import pandas as pd


df_data = {'col1':[1,2,3],'col2':['a','b','c']}
df = pd.DataFrame(data=df_data)
df_1_data = {'col1':[1,2,3],'col3':['x','y','z']}
df_1 = pd.DataFrame(data=df_1_data)

#merge
merge_combined_df = pd.merge(left=df,right=df_1,how='left',left_on='col1', right_on='col1')

#concat
concat_combined_df = pd.concat([df,df1],axis=0,ignore_index=true)
