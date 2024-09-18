import  pandas as pd
from sklearn.preprocessing import  LabelEncoder,OneHotEncoder

# Convert categorical data into numerical data using One-Hot Encoding

df=pd.read_csv("file.csv")
encoding=OneHotEncoder(sparse_output=False)
new_encoding=encoding.fit_transform(df[["Name"]])
new_encoding_df=pd.DataFrame(new_encoding,columns=encoding.get_feature_names_out(["Name"]))
print(new_encoding_df.to_string())

df=pd.read_csv("file.csv")
encoding=OneHotEncoder()
new_encoding=pd.get_dummies(df["Name"])
print(new_encoding)

# Implement label encoding on a dataset with categorical features

df=pd.read_csv('file.csv')
encoding=LabelEncoder()
df["new_encoding"]=encoding.fit_transform(df["Name"])
df["new_encounder"]=encoding.inverse_transform(df["new_encoding"])
print(df.to_string())