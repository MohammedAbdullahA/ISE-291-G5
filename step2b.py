import matplotlib.pyplot as plt
import seaborn as sns
# There are inconsistent values and it will be fixed in the coming code
print(f'The number of null rows for each column are:\n{df.isna().sum()}') #Number of rows that contain null values (incomplete)
# Identify numeric columns
num_columns = df.select_dtypes(exclude='object').columns #Identifying numerical columns

for c in num_columns: #Drawing box plots to identify and list outliers
    plt.figure()
    sns.boxplot(y=c,x='BMI Category',data=df);
    plt.show()
##There is no data needs reformatting to another format, all data is in the appropriate dtTypes (Munging and Wrangling concept)

##To fix the inconsistencies and noisiness, we will apply the following temp-functions
df["Age"] = df["Age"].apply(lambda x : x if x > 0 else abs(x))
df["Sleep Duration"]=df["Sleep Duration"].apply(lambda x: x if x>1 else 10*x)
df["Physical Activity Level"] = df["Physical Activity Level"].apply(lambda x : x if x >= 10 else x*10)
df['BMI Category'] = df['BMI Category'].replace('Normal Weight', 'Normal') #We have changed "Normal Weight" to "Weight" to get the best output
df["Systolic Blood Pressure"] = df["Systolic Blood Pressure"].apply(lambda x : x if x >= 100 else x * 100)
df["Diastolic Blood Pressure"] = df["Diastolic Blood Pressure"].apply(lambda x : x if x >= 10 else x * 100)
df["Heart Rate"] = df["Heart Rate"].apply(lambda x : x if x > 10 else x *10)
#Mean imputation based on data type, mode for categorical values and mean for numerical values
null_columns=df.columns[df.isna().any()]
for c in null_columns:
    if df[c].dtype!='object':
        value = df[c].mean()
    else:
        value = df[c].mode()
        #print (value)
        value = value[0]  #0 will be the row(s) name
        #print (value)
    df[c].fillna(value,inplace=True)
display(df.head(50))
