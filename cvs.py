import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv("cofeeVSsleep.csv")
data1 = df["Coffee in ml"].tolist()
data2 = df["sleep in hours "].tolist()

fig = px.scatter(df, x="Coffee in ml", y="sleep in hours ", color="week")
fig.show()

correlation=np.corrcoef(data1,data2)
print(correlation)