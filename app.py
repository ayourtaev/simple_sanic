from sanic import Sanic, Blueprint
from route import routes
from config import config

routes = [r for r in routes]

bp = Blueprint('v1', url_prefix='/api/v1')
bp.add_route(routes[0], routes[1], routes[2])

app = Sanic('simple_server', strict_slashes=False)
app.blueprint(blueprint=bp)

app.run(host=config.host, port=config.port, debug=True)
