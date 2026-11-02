from dash import Dash, html



app = Dash()

app.layout(
    html.Div(
        html.H1("Harness Chat")
    )
)

app.run(debug=True, port=8050)