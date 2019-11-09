import pandas as pd
import os

data=os.path.join("Resources", "project1_dataset.csv")

datacsv=pd.read_csv(data)

data_df=pd.DataFrame(datacsv)

data_df.to_html('data_table.html')


