from dash import Dash, html, dcc
import dash_bootstrap_components as dbc




app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H2("Harness Chat", className="my-3"),
    dcc.Store(id="history", data=[]),
    html.Div(id="messages", style={"height":"60vh", 
                                   "overflowY": "auto", 
                                   "border": "1px solid #ddd", 
                                   "borderRadius": "8px", 
                                   "padding" : "12px", 
                                   "background": "#fafafa"}),
    dbc.InputGroup([
        dbc.Input(id="user-input", placeholder="Введите сообщение", type="text"),
        dbc.Button("Отправить", id="send-btn", color="primary", n_clicks=0)
    ])
], fluid=True, style={"maxWidth": "900px"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False)