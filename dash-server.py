from dash import Dash, html, dcc, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
  html.H1("Prototype: Dash App in AWS App Runner")
])

if __name__ == '__main__':
    app.run_server()
