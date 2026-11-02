from dash import Dash, html



app = Dash()

app.layout = html.Div(
        html.H1("Harness Chat")
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False)