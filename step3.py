#To find the summary of the numrical data
display(df[Numerical_Columns].describe())
#To find the summary of categorical data
display(df[Categorical_Columns].describe())



#For Numrical data using hist plot
df.hist(bins=10, figsize=(15, 10))
plt.show()
#For cat data using count plot
fig, axes = plt.subplots(2, 2, figsize=(25, 25))
for ind,col in enumerate(Categorical_Columns):
    sns.countplot(y=col,data=df,ax=axes.flatten()[ind])
plt.show()

# using boxplot to differ between a cat data and numrical data 
num_cols = 3
num_rows = len(Numerical_Columns)//num_cols+1 
fig, axes = plt.subplots(num_rows, num_cols, figsize=(25, 25))
for i, c in enumerate(Numerical_Columns):
    row = i // num_cols
    col = i % num_cols
    sns.boxplot(y=c, x='Gender', data=df, ax=axes[row, col])
    axes[row, col].set_title(c)   
# to delete3 the emphty box   
for j in range(i + 1, num_rows * num_cols):
    fig.delaxes(axes.[j])
    
    
