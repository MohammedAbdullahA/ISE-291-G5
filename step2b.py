import matplotlib.pyplot as plt
import seaborn as sns
# There are inconsistent values and it will be fixed in the coming code
print(f'The number of null rows for each column are:\n{df.isna().sum()}') #number of rows that contain null values (incomplete)
# Identify numeric columns
num_columns = df.select_dtypes(exclude='object').columns #identifying numerical columns

for c in num_columns: #drawing box plots to identify and list outliers
    plt.figure()
    sns.boxplot(y=c,x='BMI Category',data=df);
    plt.show()
##There is no data needs reformatting to another format, all data is in the appropriate dtTypes (Munging and Wrangling concept)

##To fix the inconsistencies, we will apply the following temp-functions
df["Age"] = df["Age"].apply(lambda x : x if x > 0 else abs(x))
