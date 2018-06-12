from aiohttp import web
import aiohttp_jinja2
import jinja2
import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

import controllers.index_controller

app = web.Application()
aiohttp_session.setup(app,
        EncryptedCookieStorage(b'Thirty  two  length  bytes  key.'))
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('views/templates/'))
app.router.add_static('/static/', path='views/static/', name='static')
app.add_routes([web.get('/', controllers.index_controller.handle),
                web.get('/{name}', controllers.index_controller.handle)])

web.run_app(app)