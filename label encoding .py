import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Encoding-Categorical-Data\file.csv'

df=pd.read_csv(file_path)
encoding=LabelEncoder()
df["new_name"]=encoding.fit_transform(df["Name"])
print(df)

# inverse_transform
df["original name"]=encoding.inverse_transform(df["new_name"])
print(df)