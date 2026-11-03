from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import requests



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

API_URL = "http://127.0.0.1:8000/chat"

def render_messages(history: list):
    if not history:
        return html.Div("Начните диалог...", style={"color": "#999"})

    items = []
    for msg in history:
        role = msg.get("role", "user")
        content = msg.get("content", "")

        if role == "user":
            items.append(
                html.Div(
                    [html.B("Вы: "), content],
                    style={"marginBottom": "8px", "color": "#1a5490"},
                )
            )
        else:
            items.append(
                html.Div(
                    [html.B("Ассистент: "), content],
                    style={"marginBottom": "8px"},
                )
            )

    return items

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

@callback(Output("history", "data"), Output("messages", "children"), Output("user-input", "value"), Input("send-btn", "n_clicks"), State("user-input", "value"), State("history", "data"), prevent_initial_call=True)
def send_message(n_clicks, user_text, history):
    if not user_text or not user_text.strip():
        return (history or [], render_messages(history or []), "")

    history = history or []

    new_history = history + [{"role": "user", "content": user_text}]

    try:
        r = requests.post(API_URL, json={"message": user_text}, timeout=180)
        data = r.json()

        reply = data.get("reply") or f"[Ошибка: {data.get('error', 'неизвестно')}]"
    except Exception as exc:
        reply = f"[Ошибка соединения: {exc}]"

    new_history.append({"role":"assistant", "content":reply})

    return new_history, render_messages(new_history), ""




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=False)