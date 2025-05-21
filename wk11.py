# command to create a new venv = python -m venv .venv
#! source .venv/Scripts/activate
#! pip install -r requirements.txt
# ctrl shift p
# python interpreter
# VENV!!!!

#! PAndas with matplotlib .plot()
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load a dataset
# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#     "Sales": [100, 150, 200, 250, 300, 350],
#     "Expenses": [80, 120, 180, 200, 220, 300]
# }
# df = pd.DataFrame(data)

# # Line Plot pandas .plot() method internally uses matplotlib behind the scenes.
# df.plot(x="Month", y=["Sales", "Expenses"], kind="line", title="Sales vs. Expenses")
# plt.show()

# # Bar Plot
# df.plot(x="Month", y="Sales", kind="bar", color="skyblue", title="Monthly Sales")
# plt.show()

#? Plotly!! 
#! You, the student will create lesson11_b.py
import plotly.express as px
import plotly.data as pldata


df = pldata.iris(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
fig = px.scatter(df, x='sepal_length', y='petal_length', color='species',
                 title="Iris Data, Sepal vs. Petal Length", hover_data=["petal_length"])
fig.write_html("iris.html", auto_open=True)

#! Do not try fig.show()!  This sometimes works, but usually it just hangs.

