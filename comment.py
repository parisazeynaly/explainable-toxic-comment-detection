import pandas as pd

train_df = pd.read_csv("Data/train.csv")
print(train_df.head())

test_df=pd.read_csv("Data/test.csv")
print(test_df.head())
print(train_df['toxic'].value_counts())
print("Shape:", train_df.shape)
print("\nInfo:")
print(train_df.info())
display(train_df.head())
