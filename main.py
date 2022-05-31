# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
csv_file = pd.DataFrame(pd.read_csv("C:\\Users\\hyj58\\Downloads\\top20.csv", sep=",", header=0, index_col=False))
csv_file.to_json("C:\\Users\\hyj58\\Downloads\\file.json", orient="records", date_format="epoch", double_precision=10,
                     force_ascii=False, date_unit="ms", default_handler=None)
df=pd.read_json("C:\\Users\\hyj58\\Downloads\\file.json")
data = pd.DataFrame(df)

print(data[['licenseOrgan']])