import dash
import pytest
import visualisation_improved as visualisation
import pytest_dash 



def test(element_id,dash_duo):
    dash_duo.start_server(visualisation.app)
    dash_duo.wait_for_element_by_id(element_id,11)


def test_header(dash_duo):
    test(visualisation.HEADER_ID_NAME, dash_duo)

def test_radio(dash_duo):
    test(visualisation.RADIO_ID_NAME,dash_duo)

def test_graph(dash_duo):
    test(visualisation.GRAPH_ID_NAME,dash_duo)
    
