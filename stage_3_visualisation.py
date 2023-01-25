from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import datetime 





#constants change these if you want to switch the input source, colour of the line or the date the price changed
CONST_PRICE_CHANGE_DATE = datetime.datetime(2021, 1, 15)
CONST_INPUT_FILE = 'https://raw.githubusercontent.com/arshdixit/quantium-starter-repo/main/STAGE_2_OUTPUT_DATA.csv'
CONST_LINE_COLOUR = "yellow"

app = Dash(__name__)


title = " "* 68 + "("+ CONST_LINE_COLOUR + " line represents when the price changed)"



#reads the pdf and inputs it to the data frame
data_frame = pd.read_csv(CONST_INPUT_FILE)

#merges all adds together the sales of all the different region
data_frame["sales"] = data_frame.groupby("date")["sales"].transform(sum)

#graphs a line chart with the data frame
fig = px.line(data_frame, y = "sales", x = "date", title = title)

#adds the vertical line
fig.add_vline(x =  CONST_PRICE_CHANGE_DATE, line_dash="dash", line_color=CONST_LINE_COLOUR)


#html layout of the app
app.layout = html.Div(children = [html.H1(children = 'Pink Morsel sales - time graph'),
    dcc.Graph(
            id='sales time graph',
            figure=fig
        )
]
)

if __name__ == '__main__':
    app.run_server(debug=True)
