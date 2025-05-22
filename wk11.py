# command to create a new venv = python -m venv .venv
#! source .venv/Scripts/activate
#! pip install -r requirements.txt
# ctrl shift p
# python interpreter
# VENV!!!!

#! Pandas with matplotlib .plot()
import pandas as pd
import matplotlib.pyplot as plt

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
# # #! You, the student will create lesson11_b.py
# import plotly.express as px
# import plotly.data as pldata

# df = pldata.iris(return_type='pandas') # Returns a DataFrame.  plotly.data has a number of sample datasets included.
# fig = px.scatter(df, x='sepal_length', y='petal_length', color='species',
#                  title="Iris Data, Sepal vs. Petal Length", hover_data=["petal_length"])
# fig.write_html("iris.html", auto_open=True)


# #! Do not try fig.show()!  This sometimes works, but usually it just hangs.


#? Dash o clock
# from dash import Dash, dcc, html, Input, Output # Dash components you need
# import plotly.express as px # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
# import plotly.data as pldata # This is only needed to give access to the Plotly built in datasets.

# df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True) # This loads one of the datasets


# # Initialize Dash app
# app = Dash(__name__) # This creates the app object, to which various things are added below. 
# # __name__ is the name of the running Python module, which is your main module in this case

# # Layout: This section creates the HTML components
# app.layout = html.Div([ # This div is for the dropdown you see at the top, and also for the graph itself
#     dcc.Dropdown( # This creates the dropdown
#         id="stock-dropdown", # and it needs an id
#         options=[{"label": symbol, "value": symbol} for symbol in df.columns], # This populates the dropdown with the list of stocks
#         value="GOOG" # This is the initial value
#     ),
#     dcc.Graph(id="stock-price") # And the graph itself has to have an ID
# ])

# # Callback for dynamic updates
# @app.callback( # OK, now this is a decorator.  Hmm, we haven't talked about decorators in Python.  This decorator is decorating the update_graph() function.
#     # Because of the decorator, the update_graph() will be called when the stock-dropdown changes, passing the value selected in the dropdown.
#     Output("stock-price", "figure"),  # And ... you get the graph back
#     [Input("stock-dropdown", "value")] # When you pass in the value of the dropdown.
# )
# #? Decorators take another function as an argument. 
# #? Callbacks are functions passed to another function(our decorator) and is executed after the function has finished its task, usually async. 
# #! decorators link to the function immediately below them in dash. 
# def update_graph(symbol): # This function is what actually does the plot, by calling Plotly, in this case a line chart of date (which is the index) vs. the chosen stock price.
#     fig = px.line(df, df.index, y=symbol, title=f"{symbol} Price")
#     #! dan added line
#     fig.write_html("output.html")  # Save the figure to an HTML file
#     return fig

# # Run the app
# if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
#     app.run(debug=True) # start the Flask web server


#! Data Table - display dataframes
import pandas as pd
from dash import dash_table, Dash, html

app = Dash(__name__)

df = pd.read_csv("some_csv.csv")

app.layout = html.Div([  
    dash_table.DataTable(
        df.to_dict('records'),  # Convert dataframe to dictionary format
        [{"name": i, "id": i} for i in df.columns],  # Create column headers dynamically -> list comprehension.
        id='tbl'
    )
])

if __name__ == "__main__": 
    app.run(debug=True)