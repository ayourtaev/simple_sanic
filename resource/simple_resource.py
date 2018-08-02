from sanic.views import HTTPMethodView
from sanic.response import json
from random import choice
from config import logger


class EchoResource(HTTPMethodView):
    async def post(self, request):
        headers = request.headers
        body = request.json

        # list = [400, 400, 400, 400, 400, 400]
        list = [200, 400]
        status = choice(list)
        if status == 200:
            print('\nHEADERS:\n {headers}\n{split}\nBODY: \n{body}'.format(
                headers=headers, split='---' * 30, body=body))
        else:
            print(status)
        return json(body='OK' if status == 200 else 'NOT OK', status=status)

