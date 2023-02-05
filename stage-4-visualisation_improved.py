from dash import Dash, dcc, html, Input, Output

import plotly.express as px
import pandas as pd
import datetime 

#too doo
#add pinkmorsel tesselation background
#https://color.adobe.com/create/color-wheel (use split coomplimentary) and figure out colours, main font and 
#plot_bgcolor, paper_bgcolour, paper_bgcolor, font_color




#constants change these if you want to switch the input source, colour of the line or the date the price changed
CONST_PRICE_CHANGE_DATE = datetime.datetime(2021, 1, 15)
CONST_INPUT_FILE = 'https://raw.githubusercontent.com/arshdixit/quantium-starter-repo/main/STAGE_2_OUTPUT_DATA.csv'
CONST_LINE_COLOUR = "yellow"
HEADER_ID_NAME = "top"
RADIO_ID_NAME = "radio_text"


GRAPH_COLOUR_LIST = {'font': "#0CF0DA",'main' : '#F024DB'  ,'background' : "#10A395"  }
OUTSIDE_COLOUR_LIST = {'font': "#F024DB",'main' : '#A30894'  ,'background' : "#F0CD3C" }

app = Dash(__name__)


title = " "* 68 + "("+ CONST_LINE_COLOUR + " line represents when the price changed)"



#reads the pdf and inputs it to the data frame
raw_data_frame = pd.read_csv(CONST_INPUT_FILE)
data_frame = raw_data_frame



#adds the vertical line

top = html.H1(
    "pink morsels sales - time graph",
    id=HEADER_ID_NAME,
)
radio_text = html.H4(
    "Please select the region",
    id=RADIO_ID_NAME,
 
) 

#html layout of the app
app.layout = html.Div([
    top,
    radio_text,
    dcc.RadioItems(['north', 'east', 'south','west', 'all'], 'all', id="dataset_radio", style= {}),
    dcc.Graph(
            id='sales_time_graph',
    )
],
    #
    style={
        "textAlign": "center",
        "background-color": OUTSIDE_COLOUR_LIST["background"],
         "color": OUTSIDE_COLOUR_LIST["font"],
    }

)

@app.callback(
    Output(component_id = 'sales_time_graph', component_property='figure'),
    Input(component_id = 'dataset_radio', component_property = "value")
)
def update_data_set(region):
    data_frame = raw_data_frame
     #would use match case if it was available on this version
    if region != 'all':
        data_frame = raw_data_frame[raw_data_frame['region'] == region]
    else:
        data_frame = raw_data_frame.sort_values(by= "date")
    
    fig = px.line(data_frame, y = "sales", x = "date", title = title)
    fig.add_vline(x =  CONST_PRICE_CHANGE_DATE, line_dash="dash", line_color=CONST_LINE_COLOUR)
    fig.update_layout(paper_bgcolor = GRAPH_COLOUR_LIST['background'],
            plot_bgcolor = GRAPH_COLOUR_LIST['main'],
            font_color = GRAPH_COLOUR_LIST['font']
        
    )
    return fig
    


if __name__ == '__main__':
    app.run_server(debug=True)
