import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv("marksVSpresent.csv")
data1 = df["Marks In Percentage"].tolist()
data2 = df["Days Present"].tolist()

fig = px.scatter(df, y="Marks In Percentage", x="Days Present")
fig.show()

correlation=np.corrcoef(data2,data1)
print(correlation)