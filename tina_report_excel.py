import pandas as pd
import os

#use this to print entire dfs if needed: 
#pd.set_option("display.max_rows", None, "display.max_columns", None)

###############################################
#create list of files to use
def getListOfExcels(dir_name):
    # create a list of file and sub directories' names in the given directory 
    listOfFiles = os.listdir(dir_name)
    excels = list()
    # Iterate over all the entries
    for entry in listOfFiles:
        # Create full path
        fullPath = os.path.join(dir_name, entry)
        if fullPath.endswith('.xls') or fullPath.endswith('.xlsx'):
	        excels.append(fullPath)
    return excels

def df_from_excel(excel_file):
	df = pd.read_excel(excel_file)
	return df

def reformat_df(df):
	#create org_name column and value
	org = df.iloc[1,0]
	df.loc[len(df)] = ['org_name', org]
	#transpose
	dfT = df.T
	#drop unneeded columns 
	dfT.drop(dfT.iloc[:, 0:6], inplace = True, axis = 1)
	#replace column headers
	dfT.columns = dfT.iloc[0]
	dfT = dfT.drop(dfT.index[0])
	dfT = dfT.reset_index(drop=True)
	#move org_name to first column
	org_col = dfT['org_name']
	dfT.drop(labels=['org_name'], axis=1,inplace = True)
	dfT.insert(0, 'org_name', org_col)
	return dfT

#then need to join dataframes together
def join_to_master_excel(df, master):
	return pd.concat([master, df], axis=0, ignore_index=True)

#print to csv
def print_to_master_excel(df):
	return df.to_excel(r'./master.xlsx', index = False)

#Begin Main Block
dir_name = os.getcwd()
file_list = getListOfExcels(dir_name)
master = pd.DataFrame()

for file in file_list:
	df = df_from_excel(file)
	df_formatted = reformat_df(df)
	master = join_to_master_excel(df_formatted, master)
print_to_master_excel(master)