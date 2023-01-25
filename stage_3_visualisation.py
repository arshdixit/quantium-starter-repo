from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import datetime 


CONST_PRICE_CHANGE_DATE = datetime.datetime(2021, 1, 15)
CONST_INPUT_FILE = 'https://raw.githubusercontent.com/arshdixit/quantium-starter-repo/main/STAGE_2_OUTPUT_DATA.csv'
CONST_LINE_COLOUR = "yellow"


title = "Pink Morsel sales" + " "* 52 + "("+ CONST_LINE_COLOUR + " line represents when the price changed)"



data_frame = pd.read_csv(CONST_INPUT_FILE)
data_frame["sales"] = data_frame.groupby("date")["sales"].transform(sum)



fig = px.line(data_frame, y = "sales", x = "date", title = title)
fig.add_vline(x =  CONST_PRICE_CHANGE_DATE, line_dash="dash", line_color=CONST_LINE_COLOUR)
fig.show()



