#Reading and displaying the data
import numpy as np 
import pandas as pd
df = pd.read_excel('G5-ISE291.xlsx') #Reading the excel file 



print("\n")
display(df.info())
print("\n"*2)

#in order to arrange the data, we will display the numerical data followed by the catagorecal data respectively
Numerical_Columns = df.select_dtypes(exclude='object').columns.tolist()
Categorical_Columns = df.select_dtypes(include='object').columns.tolist()
print('Numerical columns:', Numerical_Columns)
print("\n")
print('Categorical columns:', Categorical_Columns)
print("\n"*2)

#Describe the two lists but two use .describe(), change the lists to DataFrames again
print(f' the Numerical columns are \n:{df[Numerical_Columns].describe()}\n' )
print(f' the CATEGORICAl columns are \n:{df[Categorical_Columns].describe()}\n' )

print(f'The number of rows: {len(df.index)}, the number of columns : {len(df.columns)}.') #The number of rows and columns
print(f'The number of non-null rows for each column are:\n{df.count()}')
display(df.head(10))
display(df.count())
