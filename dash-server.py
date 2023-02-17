from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
from dash import Dash, html, dcc, Input, Output, State

dash_app = Dash(__name__)

dash_app.layout = html.Div([
    html.H1("Prototype: Dash App in AWS App Runner")
])

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('dash', '/')
        config.add_view(dash_app.run_server(), route_name='dash')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
    
