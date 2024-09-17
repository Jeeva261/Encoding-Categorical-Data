import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Encoding-Categorical-Data\file.csv'

df=pd.read_csv(file_path)
encoding=OneHotEncoder(sparse_output=False)
df=encoding.fit_transform(df[["Name"]])
print(df)

df=pd.read_csv(file_path)
encoding=OneHotEncoder(sparse_output=False)
new_encoding=encoding.fit_transform(df[["Name"]])
new_encoding_df=pd.DataFrame(new_encoding,columns=encoding.get_feature_names_out(["Name"]))
print(new_encoding_df)

# dummy encoding

df=pd.read_csv(file_path)
df=pd.get_dummies(df["Name"])
print(df)
