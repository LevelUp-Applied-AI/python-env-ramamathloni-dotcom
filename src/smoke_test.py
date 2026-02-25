import pandas as pd
import pathlib

# الكود الموصى به للمسارات
path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"
df = pd.read_csv(path)

print("Shape:", df.shape)
print(df.head())
print(df.describe())